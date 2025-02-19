# AVL Priority Management System

Este proyecto implementa un sistema de gestión de prioridades utilizando un Árbol AVL.

## 📁 Estructura del Proyecto
- `src/avl_tree.py`: Implementación del Árbol AVL.
- `src/main.py`: Punto de entrada del sistema con una interfaz simple.
- `src/priority_manager.py`: Módulo para manejar la gestión de prioridades.
- `tests/test_avl.py`: Pruebas unitarias para validar el funcionamiento del AVL.
- `docs/report.pdf`: Informe técnico del proyecto.
- `requirements.txt`: Dependencias del proyecto.

## 🚀 Instalación

Clonar el repositorio y navegar al directorio:
```bash
git clone https://github.com/fredyuide/Estructura_Datos/new/main/avl_priority_system.git
cd avl_priority_system



---

### 🔎 **Explicación del Trabajo**
El objetivo de este proyecto es desarrollar un sistema de gestión de prioridades utilizando **árboles AVL**. Se trata de una estructura de datos eficiente para la inserción, eliminación y búsqueda de elementos, lo que lo hace ideal para aplicaciones donde el equilibrio y el rendimiento son esenciales.

#### 📌 **Caso de Uso: Gestión de Prioridades**
El sistema simula una cola de prioridades donde los elementos (tareas, procesos o paquetes) se insertan y organizan automáticamente en un **árbol AVL**, garantizando que las operaciones sean óptimas en términos de eficiencia.

#### ⚡ **Por qué usar un Árbol AVL en lugar de otras estructuras**
- **Listas Ordenadas**: Aunque permiten acceso rápido a elementos de alta prioridad, la inserción es costosa \(O(n)\).
- **Montículos (Heaps)**: Son eficientes en operaciones de inserción y extracción de mínimos, pero no permiten búsquedas rápidas de elementos específicos.
- **Árboles AVL**: Mantienen el equilibrio y garantizan que todas las operaciones básicas sean **O(log n)**, ofreciendo un excelente balance entre rendimiento y flexibilidad.

#### 🔄 **Funcionalidad del Sistema**
1. **Agregar tareas con prioridad**: Se insertan en el árbol AVL, garantizando un equilibrio automático.
2. **Visualizar tareas ordenadas por prioridad**: Se imprimen en forma de árbol, mostrando claramente la jerarquía de prioridades.
3. **Comparación con otras estructuras**: Se analiza su rendimiento frente a listas ordenadas y montículos.

#### 📌 **Conclusión**
El uso de un **árbol AVL** en un sistema de gestión de prioridades garantiza un rendimiento eficiente y predecible, lo que lo hace ideal para aplicaciones como:
- Asignación de turnos en hospitales.
- Priorización de paquetes en logística.
- Planificación de procesos en sistemas operativos.

Este proyecto ofrece una **implementación práctica y funcional** de este concepto, junto con análisis de rendimiento y pruebas unitarias para validar su eficacia. 🚀
