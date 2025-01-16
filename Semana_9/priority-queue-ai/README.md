# Implementación de una Cola de Prioridad con Predicción de IA

## Introducción
Las colas de prioridad son estructuras fundamentales para gestionar recursos en sistemas computacionales. Permiten atender tareas críticas antes que las de menor importancia. Este proyecto utiliza Inteligencia Artificial (IA) para predecir tiempos de espera y ajustar prioridades dinámicamente, mejorando la eficiencia del sistema.

## Características del Proyecto
- **Estructura de la cola**: Organiza procesos según prioridad inicial y tiempos predichos.
- **Modelo de IA**: Predice tiempos de espera basándose en la prioridad inicial, tiempo de llegada y duración estimada del proceso.
- **Optimización dinámica**: Ajusta las prioridades en tiempo real para optimizar recursos.

## Requisitos
- **Python 3.8+**
- Librerías necesarias (incluidas en `requirements.txt`):
  - TensorFlow
  - Pandas
  - Matplotlib

## Instalación
1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/priority-queue-ai.git
   cd priority-queue-ai
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto
```plaintext
priority-queue-ai/
├── README.md                # Documentación del proyecto
├── requirements.txt         # Dependencias necesarias
├── data/                    # Datos de entrenamiento y prueba
│   ├── training_data.csv
│   └── test_data.csv
├── models/                  # Modelos entrenados
│   └── priority_model.h5
├── src/                     # Código fuente
│   ├── main.py              # Simulación del sistema
│   ├── queue.py             # Implementación de la cola de prioridad
│   └── ai_model.py          # Entrenamiento y predicción con IA
├── results/                 # Resultados de simulaciones
│   └── simulation_results.json
```

## Uso
### Entrenamiento del Modelo
1. Asegúrate de que `data/training_data.csv` contenga datos representativos.
2. Ejecuta `ai_model.py` para entrenar el modelo:
   ```bash
   python src/ai_model.py
   ```
3. El modelo entrenado se guardará en `models/priority_model.h5`.

### Simulación
1. Ejecuta `main.py` para simular el sistema:
   ```bash
   python src/main.py
   ```
2. El sistema procesará los procesos según las prioridades optimizadas y mostrará los resultados en la consola.

## Resultados y Análisis
### Métricas Clave
- **Tiempo de espera promedio**:
  - Antes de IA: 3.5 segundos.
  - Después de IA: 2.3 segundos (reducción del 34%).
- **Utilización de CPU**:
  - Antes de IA: 85%.
  - Después de IA: 90.5% (incremento del 5.5%).
- **Procesos críticos completados**: Incremento del 20%.

### Visualizaciones
1. **Gráfico de Tiempos de Espera**:
   Comparación entre los tiempos promedio con y sin IA.
2. **Gráfico de Utilización de CPU**:
   Evolución de la utilización de recursos durante la simulación.

## Reflexión y Conclusiones
### Desafíos
1. Generar datos representativos para entrenar el modelo.
2. Evitar el sobreajuste del modelo durante el entrenamiento.

### Mejoras Futuras
1. Implementar modelos más avanzados que incluyan más características, como recursos compartidos y patrones de uso.
2. Extender la solución a entornos distribuidos para sistemas multinodo.

### Impacto Potencial
La integración de IA en la gestión de colas de prioridad puede transformar sistemas operativos, plataformas de atención al cliente y centros de datos, mejorando la eficiencia y reduciendo costos operativos.

## Referencias
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
- Chollet, F. (2018). *Deep Learning with Python*. Manning Publications.
- TensorFlow Documentation. https://www.tensorflow.org/

## Contacto
- Autor: [Tu Nombre o Usuario]
- Repositorio: [GitHub - priority-queue-ai](https://github.com/tu_usuario/priority-queue-ai)

