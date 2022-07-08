import wntr 
import plotly.express as px
import pandas as pd

wn = wntr.network.WaterNetworkModel('networks/Net3.inp') 
ax = wntr.graphics.plot_network(wn, node_attribute='elevation',
node_colorbar_label='Elevacion (m)')

pop = wntr.metrics.population(wn)
wntr.graphics.plot_interactive_network(wn, node_attribute=pop,
                                       node_range=[0,500], filename='population.html', auto_open=False)
#Define el mapa en un archivo llamado mapacarelmapu.html Lake define el lago definito en epanet y 219 se refiere a un nodo
#se debe escalar nuevo mapa y hacer recorrido asociado.
longlat_map = {'Lake':(-73.70948, -41.7496873), '219': (-73.07848, -41.5718873)}
wn2 = wntr.morph.convert_node_coordinates_to_longlat(wn, longlat_map)
length = wn2.query_link_attribute('length')
wntr.graphics.plot_leaflet_network(wn2, link_attribute=length, link_width=3,
link_range=[0,1000], filename='mapacarelmapu.html')
#
#


wn.options.quality.parameter = 'AGE'
sim = wntr.sim.EpanetSimulator(wn)
results = sim.run_sim()
water_age = results.node['quality']/3600 # convert seconds to hours
anim = wntr.graphics.network_animation(wn, node_attribute=water_age, node_range=[0,24]) 

pressure_at_node123 = results.node['pressure'].loc[:,'157']
ax = pressure_at_node123.plot()
text = ax.set_xlabel('Time (s)')
text = ax.set_ylabel('Pressure (m)')





tankH = results.node['pressure'].loc[:,wn.tank_name_list]
tankH = tankH * 3.28084 # Convert tank head to ft
tankH.index /= 3600 # convierte el tiempo en horas
fig = px.line(tankH)
fig = fig.update_layout(xaxis_title='Time (hr)', yaxis_title='Head (ft)',
                  template='simple_white', width=650, height=400)
fig.write_html('tank_head.html')

pump = wn.get_link('10')
ax = wntr.graphics.plot_pump_curve(pump)

wn.add_curve('Curve', 'VOLUME', [
  (1,  0),
   (2,  60),
   (3,  188),
   (4,  372),
   (5,  596),
   (6,  848),
  (7,  1114),
  (8,  1379),
    (9,  1631),
    (10, 1856),
    (11, 2039),
    (12, 2168),
    (13, 2228)])
tank = wn.get_node('2')
tank.vol_curve_name = 'Curve'
ax = wntr.graphics.plot_tank_volume_curve(tank)
