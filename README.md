# Proyecto-Herramientas
Analisis de simulacion de red hidraulica a traves de Epanet y Python. En Chile, según el informe de gestión de la Super Intendencia de Servicios Sanitarios 2020 (SISS.2020), las aguas no facturadas (ANF), se han mantenido en niveles altos llegando a un 33,4%. Donde la ciudadanía exige un uso más eficiente de este recurso debido al escenario de menor disponibilidad de agua. Se realizara un analisis hidraulico y se simularan fallas dentro del sistema.


# Epanet
Epanet es un software libre, desarrollado por la EPA (Agencia de protección Ambiental de Estados Unidos), que realiza simulaciones del comportamiento hidráulico y de calidad de agua en redes de tuberías a presión. Está diseñado para el uso con sistemas de distribución de agua potable, aunque en general puede ser utilizado para el análisis de cualquier fluido no compresible con flujo a presión [4].
En general, una red consta de tuberías, nodos (Conexión de tuberías), bombas, válvulas y tanques de almacenamiento o depósitos. Epanet determina el caudal que circula por cada una de las conducciones, la presión en cada uno de los nodos, el nivel de agua en cada estanque y la concentración de diferentes químicos a través de la red durante un determinado periodo de simulación analizando diferentes intervalos de tiempo. La información necesaria para diseñar un modelo de red de distribución debe por lo menos la siguiente:
•	Dimensiones de tuberías.
•	Materialidad de tuberías.
•	Ubicación de nodos.
•	Ubicación de elementos de red como válvulas, estanques, tuberías, controladores de flujos, entre otros.
•	Demandas.

	Epanet proporciona un entorno integrado bajo Windows, para la edición de los datos de entrada a la red, la realización de simulaciones hidráulicas y de la calidad del agua, y la visualización de resultados en una amplia variedad de formatos. Entre éstos se incluyen mapas de la red codificados por colores, tablas numéricas, gráficas de evolución y mapas de isolíneas.
	Dos de los requisitos fundamentales para poder construir con garantías un modelo de la calidad del agua son la potencia de cálculo y la precisión del modelo hidráulico utilizado. Epanet contiene un simulador hidráulico muy avanzado que ofrece las siguientes prestaciones [5]:

•	No existe límite en cuanto al tamaño de la red que puede procesarse. 
•	 Las pérdidas de carga pueden calcularse mediante las fórmulas de Hazen-Williams, de DarcyWeisbach o de Chezy-Manning. 
•	Contempla pérdidas menores en codos, accesorios, etc.
•	Admite bombas de velocidad fija o variable. 
•	 Determina el consumo energético y sus costes. 
•	Permite considerar varios tipos de válvulas, tales como válvulas de corte, de retención, y reguladoras de presión o caudal. 
•	 Admite depósitos de geometría variable (esto es, cuyo diámetro varíe con el nivel). 
•	Permite considerar diferentes tipos de demanda en los nudos, cada uno con su propia curva de modulación en el tiempo.
•	Permite modelar tomas de agua cuyo caudal dependa de la presión. 
•	Admite leyes de control simples, basadas en el valor del nivel en los depósitos o en la hora prefijada por un temporizador, y leyes de control más complejas basadas en reglas lógicas.


# LeakDB

LeakDB (Leakage Diagnosis Benchmark) es un conjunto de datos de fugas realistas para redes de distribución de agua. El conjunto de datos se compone de una gran cantidad de escenarios de fuga creados artificialmente pero realistas, en diferentes redes de distribución de agua, en condiciones variables. Se proporciona un algoritmo de puntuación en código MATLAB para evaluar los resultados de diferentes algoritmos.


# Descarga de base de datos
Se utilizara una base de datos actualizada de simulacion en Epanet y Matbal, ademas se realizara una comparativa con algoritmos de deteccion y funciones obtenidas a traves del siguiente enlace: https://goo.gl/zLJpuD

# Citas

Vrachimis, S. G., Kyriakou, M. S., Eliades, D. G. y Polycarpou, M. M. (2018). LeakDB: un conjunto de datos de referencia para el diagnóstico de fugas en las redes de distribución de agua. En Proc. de la Conferencia Conjunta WDSA/CCWI (Vol. 1).



