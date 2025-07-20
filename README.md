
# 🛡️ DDoS: Detrás del Grafo

Proyecto final de **Matemáticas Discretas I** – Universidad Nacional de Colombia  
Autores: María Catalina Rodríguez, Juan Diego Rozo, Omar Alejandro Blanco  
Julio de 2025

---

## 📌 Descripción

Este proyecto simula un entorno de red donde usuarios y servidores se modelan mediante un **grafo bipartito no dirigido**. El objetivo es estudiar el comportamiento de un ataque de **Denegación de Servicio Distribuido (DDoS)** desde un enfoque teórico y práctico, empleando conceptos fundamentales de **matemáticas discretas**, como la teoría de grafos y la lógica proposicional.

La simulación busca detectar patrones sospechosos de tráfico que podrían indicar un ataque DDoS, analizando:

- El grado de los vértices (usuarios y servidores)
- La frecuencia de conexiones
- Condiciones lógicas aplicadas a patrones anómalos

---

## 🧠 Fundamento Matemático

El grafo G está definido como:

```
G = {V, E, W}
```

- V = {U, S}: conjunto de nodos, donde U = usuarios, S = servidores
- E: conjunto de aristas entre U y S
- W: pesos asociados a las aristas, representando el número de conexiones

Se emplea una función f: E → W que mapea cada conexión a su peso (frecuencia).

---

## 🧮 Lógica Proposicional Aplicada

Además de la representación gráfica, se incorporan **proposiciones lógicas** para identificar comportamientos sospechosos:

- `p`: El servidor está siendo sobrecargado.
- `q`: El usuario `u_i` está involucrado en el ataque.

Se utilizan reglas de inferencia como **Modus Ponens** y **Modus Tollens** para establecer relaciones entre proposiciones y deducciones sobre la red simulada.

---

## 🧰 Estructura del Proyecto

```
📁 discretas1_proyecto
├── 📁 documents
│   ├── Desarrollo_Teórico_Proyecto_Final_Matemáticas_Discretas.pdf
│   └── proyecto_matematicas_discretas1.ipynb
│
├── 📁 source
│   ├── main.py
│   ├── networkSimulation.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

## 📈 Ejemplo de Salida Gráfica

El proyecto genera gráficos como:

- 📊 Barras de conexiones usuario-servidor
- 🌐 Grafo bipartito etiquetado
- 🔍 Análisis de los nodos más activos o sospechosos

---

## ▶️ Ejecución

Para correr la simulación desde `main.py`:

```bash
cd source
python main.py
```

Requisitos:

- Python 3.7+
- `matplotlib`
- `networkx`

Puedes instalar dependencias con:

```bash
pip install -r requirements.txt
```

---

## 🔍 Análisis de Resultados

- Servidores con alto grado ⇒ Potencial blanco del ataque
- Usuarios con conexiones excesivas ⇒ Posible bot o atacante
- Conjunción lógica de condiciones ⇒ Disparadores de alerta

---




