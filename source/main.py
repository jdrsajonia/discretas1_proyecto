import networkSimulation as nw
import utils as u

simular_red=nw.networkSimulation()
simular_red.construir_diccionarios(5,10)

simular_red.construir_red(10)   # posible relacion: entre más grande sea la cantidad de conexiones y más pequeñas sean las listas de los nodos, cada IP tendrá más aristas (conexiones), por lo que habrán altos grados

print(simular_red.user)
print(simular_red.server)
print(simular_red.relation)

simular_red.graficar_grafo_bipartito()

red=simular_red.relation
botnet=simular_red.user

u.graficar_diccionario_barras(
    "Conexiones Usuario - Servidor",
    "Usuario - Servidor",
    "Número de conexiones",
    red
)

u.graficar_diccionario_barras(
    "Conexiones por Usuario",
    "Usuario",
    "Número de conexiones",
    botnet
)
