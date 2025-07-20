import random 
import networkx as nx
import matplotlib.pyplot as plt

class networkSimulation:

    '''
    Clase para simular y visualizar una red bipartita entre usuarios y servidores.

    Esta clase genera una cantidad aleatoria de nodos en un rango [a,b] para usuarios y servidores
    y crea conexiones aleatorias entre ellos simulando una red. 
    Se pueden visualizar tanto el grafo bipartito como las estadísticas de conexiones por nodo.

    Nota: para representar los nodos y sus grados, se usaron diccionarios dado
    que es sencillo rastrear un elemento del mismo y actualizar un valor al cual referencia. 
    En este caso, el elemento es la llave (key) y el valor es la referencia (value) tieniendo 
    la siguiente forma:

    key : value    <-->    nodo : grado
    '''

    def __init__(self) -> None:
        '''
        user : dict
        Diccionario que contiene los nodos de usuario. Las claves son identificadores
        de usuario (como 'u0', 'u1', ...) y los valores representan la cantidad de
        conexiones (grado) que tiene cada uno.

        server : dict
        Diccionario que contiene los nodos de servidor. Las claves son identificadores
        de servidor (como 's0', 's1', ...) y los valores son su grado de conexión.

        relation : dict
        Diccionario con las relaciones entre usuarios y servidores. Las claves son
        tuplas (usuario, servidor) y los valores representan cuántas veces ocurrió
        esa conexión.
        '''
        self.user={}
        self.server={}
        self.relation={}
        pass

    def _generar_diccionario_nodos(self, name:str, a:int, b:int):
        '''
        Método privado para generar un diccionario de nodos con identificadores únicos
        dentro de un rango aleatorio [a, b].
        '''
        conjunto_nodos={}
        cantidad_ips=random.randint(a,b)

        for ip in range(cantidad_ips):
            conjunto_nodos.setdefault(f"{name}{ip}", 0)

        return conjunto_nodos

    def construir_diccionarios(self, a:int ,b:int):
        '''
        Inicializa los diccionarios de usuarios y servidores con cantidad aleatoria de nodos, 
        dentro de un rango aleatorio [a,b], haciendo uso del método privado _generar_diccionario_nodos.
        '''
        self.user=self._generar_diccionario_nodos("u", a, b)
        self.server=self._generar_diccionario_nodos("s", a, b)

    

    def construir_red(self, total_conexiones):
        '''
        Genera conexiones aleatorias entre usuarios y servidores, actualizando el
        diccionario de relaciones y los grados de los nodos, recordando que, en cada diccionario:

        key : value    <-->    nodo : grado

        Por lo tanto se siguen estos pasos:
        1.) Se selecciona un elemento aleatorio de U que pertenece a self.user y uno de S 
        que pertenece a self.server. 
        2.) Se aumentan los grados de U y S en self.user y self.server
        3.) Se relacionan U y S en una tupla de tal forma que:
            U --> S. Por lo tanto, (U,S) pertenece a self.relation.
        4.) Se aumenta el grado de la relación formada en self.relation 

        '''
        user=list(self.user.keys())
        server=list(self.server.keys())

        cardinal_user=len(user)
        cardinal_server=len(server)

        for conexion in range(total_conexiones):
            random_number1=random.randint(0,cardinal_user-1)
            random_number2=random.randint(0,cardinal_server-1)

            random_user=user[random_number1]
            random_server=server[random_number2]

            conexion_usuario_servidor=(random_user, random_server)

            self.user[random_user]+=1
            self.server[random_server]+=1

            self.relation.setdefault(conexion_usuario_servidor,0)
            self.relation[conexion_usuario_servidor]+=1

            print(conexion_usuario_servidor,end="  --> ")
            print((random_number1, random_number2))



    def graficar_grafo_bipartito(self):
        '''
        Dibuja un grafo bipartito con los usuarios y servidores, donde las aristas
        indican relaciones. Se muestra el peso (frecuencia) de cada conexión.

        '''
        GRAFO=nx.Graph()

        user=list(self.user.keys())
        server=list(self.server.keys())

        GRAFO.add_nodes_from(user, bipartite=0)
        GRAFO.add_nodes_from(server, bipartite=1)

        for conexion in self.relation:
            current_user=conexion[0]
            current_server=conexion[1]
            grado=self.relation[conexion]
            GRAFO.add_edge(current_user, current_server, weight=grado)

        pos = nx.bipartite_layout(GRAFO, user)

        for node in pos:
            x, y = pos[node]
            pos[node] = (x * 3.0, y * 4.0) 

        plt.figure(figsize=(14, 8))  

        nx.draw_networkx_nodes(GRAFO, pos, nodelist=user, node_color='skyblue', label='Usuarios')
        nx.draw_networkx_nodes(GRAFO, pos, nodelist=server, node_color='lightgreen', label='Servidores')
        nx.draw_networkx_edges(GRAFO, pos)
        nx.draw_networkx_labels(GRAFO, pos, font_size=9)

        etiquetas = nx.get_edge_attributes(GRAFO, 'weight')

        nx.draw_networkx_edge_labels(GRAFO, pos, edge_labels=etiquetas)
        plt.title("Red Usuario - Servidor (Bipartita)")
        plt.axis("off")
        plt.legend()
        plt.tight_layout()
        plt.show()


    def imprimir_valores_y_grados(diccionario):
        for i, key in enumerate(diccionario):
            print(f"IP {i}: {key}   -->  {diccionario[key]}")
        print()






