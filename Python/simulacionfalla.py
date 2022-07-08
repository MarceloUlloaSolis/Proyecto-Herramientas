""
El siguiente ejemplo ejecuta mÃºltiples realizaciones de escenarios de fugas de
tuberÃ­as donde a cada tuberÃ­a se le asigna una falla de probabilidad 
relacionada con el diÃ¡metro de la tuberÃ­a y las ubicaciones de las fugas y las
 duraciones se extraen de las distribuciones de probabilidad. Se grafica la 
 disponibilidad del servicio de agua y el nivel de agua del tanque para cada
 realizaciÃ³n.
"""
import numpy as np
import matplotlib.pyplot as plt
import pickle
import wntr

# Crea un modelo de red de agua
inp_file = 'networks/Net3.inp'
wn = wntr.network.WaterNetworkModel(inp_file)

# Modifica el modelo de red de agua
wn.options.time.duration = 48*3600
wn.options.time.hydraulic_timestep = 1800
wn.options.time.report_timestep = 1800
wn.options.hydraulic.required_pressure = 15
wn.options.hydraulic.minimum_pressure = 0


# Defina la probabilidad de falla para cada tuberÃ­a, segÃºn el diÃ¡metro de la
# tuberÃ­a. La probabilidad de falla debe sumar 1. Net3 tiene algunas tuberÃ­as 
# con un diÃ¡metro = 99 pulgadas, para excluirlas del conjunto de ubicaciones 
# de fugas factibles, use query_link_attribute

pipe_diameters = wn.query_link_attribute('diameter', np.less_equal,
                                         0.9144,  # 36 inches = 0.9144 m
                                         link_type=wntr.network.Pipe)
failure_probability = pipe_diameters/pipe_diameters.sum()

# Pickle el modelo de red y recargarlo para cada realizaciÃ³n
f=open('wn.pickle','wb')
pickle.dump(wn,f)
f.close()

# Ejecutar 5 realizaciones
results = {} # Inicializar diccionario para almacenar resultados
np.random.seed(67823) # Establece semilla aleatoria
for i in range(5):

    # Seleccione el nÃºmero de fugas, valor aleatorio entre 1 y 5
    N = np.random.randint(1,5+1)

    # Seleccione N tuberÃ­as Ãºnicas en funciÃ³n de la probabilidad de falla
    pipes_to_fail = np.random.choice(failure_probability.index, 5,
                                     replace=False,
                                     p=failure_probability.values)

    # Seleccione tiempo de falla, dist uniforme, entre 1 y 10 horas
    time_of_failure = np.round(np.random.uniform(1,10,1)[0], 2)

    #Seleccione la duraciÃ³n de la falla, dist uniforme, entre 12 y 24 horas
    duration_of_failure = np.round(np.random.uniform(12,24,1)[0], 2)
    
    # Agregar fugas al modelo
    for pipe_to_fail in pipes_to_fail:
        pipe = wn.get_link(pipe_to_fail)
        leak_diameter = pipe.diameter*0.3
        leak_area=3.14159*(leak_diameter/2)**2
        wn = wntr.morph.split_pipe(wn, pipe_to_fail, pipe_to_fail + '_B', pipe_to_fail+'leak_node')
        leak_node = wn.get_node(pipe_to_fail+'leak_node')
        leak_node.add_leak(wn, area=leak_area,
                          start_time=time_of_failure*3600,
                          end_time=(time_of_failure + duration_of_failure)*3600)

    # Simule la hidrÃ¡ulica y almacene los resultados
    wn.options.hydraulic.demand_model = 'PDD'
    sim = wntr.sim.WNTRSimulator(wn)
    print('Pipe Breaks: ' + str(pipes_to_fail) + ', Start Time: ' + \
                str(time_of_failure) + ', End Time: ' + \
                str(time_of_failure+duration_of_failure))
    results[i] = sim.run_sim()
    
    # Recargar el modelo de red de agua
    f=open('wn.pickle','rb')
    wn = pickle.load(f)
    f.close()

# Disponibilidad de servicio de agua y nivel de agua del tanque
# para cada realizaciÃ³n
for i in results.keys():
    
    # Disponibilidad del servicio de agua en cada empalme y horario
    expected_demand = wntr.metrics.expected_demand(wn)
    demand = results[i].node['demand'].loc[:,wn.junction_name_list]
    wsa_nt = wntr.metrics.water_service_availability(expected_demand, demand)
    
    # Disponibilidad media del servicio de agua en cada momento
    wsa_t = wntr.metrics.water_service_availability(expected_demand.sum(axis=1), 
                                                  demand.sum(axis=1))
                               
    # Nivel de agua del tanque
    tank_level = results[i].node['pressure'].loc[:,wn.tank_name_list]
    
    # Trazar resultados
    plt.figure()
    
    plt.subplot(2,1,1)
    wsa_nt.plot(ax=plt.gca(), legend=False)
    wsa_t.plot(ax=plt.gca(), label='Average', color='k', linewidth=3.0, legend=False)
    plt.ylim( (-0.05, 1.05) )
    plt.ylabel('Disponibilidad de servicio')
    
    plt.subplot(2,1,2)
    tank_level.plot(ax=plt.gca())
    plt.ylim(ymin=0, ymax=12)
    plt.legend()
    plt.ylabel('Nivel del tanque (m)')
