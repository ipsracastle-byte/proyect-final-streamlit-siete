# 🚗 Proyecto Final Sprint 7 - Análisis de Vehículos

## 📋 Descripción del Proyecto

Proyecto de análisis de datos de vehículos utilizando Python, con visualizaciones interactivas y aplicaciones web.

**Este proyecto sigue principios de Clean Architecture y está diseñado como proyecto de portafolio profesional.**

## ✨ Funcionalidades

### 📊 Visualizaciones Disponibles

1. **Histograma del Odómetro** 🔍
   - Distribución del kilometraje de los vehículos
   - Estadísticas descriptivas (media, mediana, desviación estándar)
   - Filtros por rango de kilometraje
   - Análisis de vehículos con bajo kilometraje

2. **Gráfico de Dispersión Precio vs Odómetro** 📈 ✨ **NUEVO**
   - Análisis de correlación entre precio y kilometraje
   - Visualización interactiva con Plotly
   - Escala de colores basada en precio
   - Hover con información detallada (modelo, año, precio, kilometraje, condición)
   - Cálculo automático de correlación de Pearson
   - Interpretación inteligente de resultados
   - Identificación de outliers
   - Insights y recomendaciones automáticas

### 🎯 Características Técnicas

- 🏛️ **Clean Architecture** - Separación de responsabilidades en 5 capas
- 🎨 **Design Patterns** - Repository, Factory, Dependency Injection, Singleton
- 📊 **Análisis Estadístico** - Correlación, estadísticas descriptivas, percentiles
- 🔍 **Filtrado Dinámico** - Filtros interactivos por rango de valores
- 💡 **Insights Automáticos** - Interpretación inteligente de datos
- ✅ **Código Testeable** - Arquitectura que facilita testing
- 📝 **Documentación Completa** - Guías, referencias y estándares

## 📚 Documentación del Proyecto

| Documento | Descripción |
|-----------|-------------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | 🏛️ Arquitectura completa del proyecto (Clean Architecture) |
| [DESIGN_PATTERNS.md](DESIGN_PATTERNS.md) | 🎨 Patrones de diseño implementados |
| [CODING_STANDARDS.md](CODING_STANDARDS.md) | 📝 Estándares de código y mejores prácticas |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | ⚡ Referencia rápida para consulta diaria |
| [README.md](README.md) | 📖 Este archivo - Guía general |

### 🎯 Por Dónde Empezar

1. **Si eres nuevo:** Lee este README completo
2. **Para entender la arquitectura:** [ARCHITECTURE.md](ARCHITECTURE.md)
3. **Para escribir código:** [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
4. **Para code review:** [CODING_STANDARDS.md](CODING_STANDARDS.md)
5. **Para patrones:** [DESIGN_PATTERNS.md](DESIGN_PATTERNS.md)

---

## 🛠️ Configuración del Entorno

### 1. Instalación Automática (Recomendado)

El proyecto incluye un script de configuración automática que:
- Crea el entorno virtual `vehicles_env`
- Instala todas las dependencias necesarias
- Configura la estructura del proyecto

```bash
# Dar permisos de ejecución
chmod +x setup_env.sh

# Ejecutar el script
./setup_env.sh
```

### 2. Activar el Entorno Virtual

```bash
source vehicles_env/bin/activate
```

Deberías ver `(vehicles_env)` al inicio de tu línea de comandos:
```bash
(vehicles_env) israelcastillo@MacBook-Ipsra proyect_sprint_final_7 %
```

### 3. Desactivar el Entorno Virtual

```bash
deactivate
```

---

## 📦 Dependencias Instaladas

### Librerías de Análisis de Datos
| Librería | Versión | Uso |
|----------|---------|-----|
| `pandas` | 2.3.3 | Manipulación y análisis de datos |
| `numpy` | 2.0.2 | Cálculos numéricos |
| `scipy` | 1.13.1 | Análisis estadístico |

### Librerías de Visualización
| Librería | Versión | Uso |
|----------|---------|-----|
| `matplotlib` | 3.9.4 | Gráficos estáticos |
| `plotly` | 6.5.2 | **Visualizaciones interactivas** |

### Librerías Web y APIs
| Librería | Versión | Uso |
|----------|---------|-----|
| `streamlit` | 1.50.0 | Aplicaciones web interactivas |
| `requests` | 2.32.5 | Peticiones HTTP a APIs |

### Librerías de Notebooks
| Librería | Versión | Uso |
|----------|---------|-----|
| `nbformat` | 5.10.4 | **Trabajo con notebooks Jupyter (.ipynb)** |

---

## 🆕 Librerías Adicionales Instaladas

### 📊 Plotly
**Instalación:**
```bash
pip install plotly
```

**Uso:**
```python
import plotly.express as px
import plotly.graph_objects as go

# Ejemplo: Gráfico de dispersión interactivo
fig = px.scatter(df, x='precio', y='kilometraje', color='marca')
fig.show()
```

**Características:**
- Gráficos interactivos (zoom, hover, pan)
- Exportación a HTML
- Integración con Streamlit
- Soporte para 3D y mapas

### 📓 nbformat
**Instalación:**
```bash
pip install nbformat
```

**Uso:**
```python
import nbformat

# Leer un notebook
with open('notebook.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

# Acceder a las celdas
for cell in nb.cells:
    print(cell.source)
```

**Características:**
- Leer/escribir archivos `.ipynb`
- Manipular celdas de código y markdown
- Validar estructura de notebooks
- Conversión entre versiones

---

## 📁 Estructura del Proyecto

```
proyect-final-streamlit-siete/
├── 📱 app.py                          # Punto de entrada principal de Streamlit
│
├── 🔧 Configuración
│   ├── setup_env.sh                   # Script de configuración automática
│   ├── requirements.txt               # Dependencias del proyecto
│   └── .gitignore                     # Archivos ignorados por Git
│
├── 📚 Documentación
│   ├── README.md                      # Este archivo - Guía general
│   ├── ARCHITECTURE.md                # Arquitectura Clean completa
│   └── CHANGELOG.md                   # Historial de cambios
│
├── 🏗️  src/                           # Código fuente (Clean Architecture)
│   ├── __init__.py
│   │
│   ├── 🎯 domain/                     # CAPA 1: Lógica de negocio pura
│   │   ├── entities/                  # Entidades del dominio
│   │   │   ├── __init__.py
│   │   │   └── vehicle.py             # Entidad Vehicle con validaciones
│   │   ├── repositories/              # Interfaces de repositorios
│   │   │   ├── __init__.py
│   │   │   └── vehicle_repository.py  # Abstract base class
│   │   ├── factories/                 # Factory Pattern
│   │   │   ├── __init__.py
│   │   │   └── vehicle_factory.py     # Creación de entidades
│   │   └── value_objects/             # Value Objects (futuro)
│   │
│   ├── 🎬 use_cases/                  # CAPA 2: Casos de uso
│   │   ├── __init__.py
│   │   ├── get_vehicle_statistics.py  # Obtener estadísticas
│   │   └── filter_vehicles.py         # Filtrar vehículos
│   │
│   ├── 🔌 adapters/                   # CAPA 3: Adaptadores
│   │   ├── __init__.py
│   │   ├── repositories/              # Implementaciones de repositorios
│   │   │   ├── __init__.py
│   │   │   └── csv_vehicle_repository.py  # Repositorio CSV
│   │   └── presenters/                # Presentadores (futuro)
│   │
│   ├── 🏭 infrastructure/             # CAPA 4: Infraestructura
│   │   ├── __init__.py
│   │   ├── config/                    # Configuración
│   │   │   ├── __init__.py
│   │   │   └── settings.py            # Settings (Singleton Pattern)
│   │   ├── data_sources/              # Fuentes de datos
│   │   │   ├── __init__.py
│   │   │   └── csv_reader.py          # Lector de CSV
│   │   ├── visualization/             # Generación de gráficos
│   │   │   ├── __init__.py
│   │   │   └── plotly_charts.py       # Gráficos con Plotly
│   │   └── di/                        # Dependency Injection
│   │       ├── __init__.py
│   │       └── container.py           # DI Container
│   │
│   ├── 🖥️  interfaces/                # CAPA 5: Interfaces de usuario
│   │   ├── __init__.py
│   │   └── streamlit_app/             # Aplicación Streamlit
│   │       ├── __init__.py
│   │       ├── app.py                 # App principal
│   │       ├── components/            # Componentes UI
│   │       │   ├── __init__.py
│   │       │   ├── histogram_component.py      # Histograma
│   │       │   └── scatter_plot_component.py   # Gráfico dispersión ✨
│   │       └── pages/                 # Páginas adicionales (futuro)
│   │
│   ├── 🔗 shared/                     # Código compartido
│   │   ├── __init__.py
│   │   └── exceptions.py              # Excepciones personalizadas
│   │
│   ├── models/                        # (Legacy - migrar a domain)
│   ├── processing/                    # (Legacy - migrar a use_cases)
│   ├── utils/                         # Utilidades generales
│   └── visualization/                 # (Legacy - migrar a infrastructure)
│
├── 📊 data/                           # Datos del proyecto
│   ├── raw/                           # Datos crudos (no se sube a Git)
│   │   └── vehicles_us.csv            # Dataset principal (4.3 MB)
│   ├── processed/                     # Datos procesados
│   └── external/                      # Datos externos
│
├── 📓 notebooks/                      # Jupyter notebooks
│   └── exploratory/                   # Análisis exploratorio
│       └── EDA.ipynb                  # Notebook de EDA
│
├── 🧪 tests/                          # Pruebas unitarias (pendiente)
│   ├── unit/                          # Tests unitarios
│   ├── integration/                   # Tests de integración
│   └── e2e/                           # Tests end-to-end
│
├── 📈 reports/                        # Reportes generados
│   └── figures/                       # Gráficos exportados
│
└── 🐍 vehicles_env/                   # Entorno virtual (no se sube a Git)
    ├── bin/                           # Ejecutables
    ├── lib/                           # Librerías instaladas
    └── pyvenv.cfg                     # Configuración del venv
```

### 🏛️ Arquitectura Clean - 5 Capas

```
┌─────────────────────────────────────────────────────────────┐
│                    🖥️  INTERFACES (UI)                      │
│              Streamlit App, Components, Pages               │
│                  (Capa más externa)                         │
└─────────────────────────────────────────────────────────────┘
                            ↓ depende de
┌─────────────────────────────────────────────────────────────┐
│                  🏭 INFRASTRUCTURE                           │
│        Config, Data Sources, Visualization, DI              │
│              (Detalles técnicos)                            │
└─────────────────────────────────────────────────────────────┘
                            ↓ depende de
┌─────────────────────────────────────────────────────────────┐
│                    🔌 ADAPTERS                               │
│          Repositories, Presenters, Controllers              │
│            (Conversión de datos)                            │
└─────────────────────────────────────────────────────────────┘
                            ↓ depende de
┌─────────────────────────────────────────────────────────────┐
│                   🎬 USE CASES                               │
│        Lógica de aplicación, Orquestación                   │
│          (Casos de uso del negocio)                         │
└─────────────────────────────────────────────────────────────┘
                            ↓ depende de
┌─────────────────────────────────────────────────────────────┐
│                    🎯 DOMAIN                                 │
│        Entities, Value Objects, Repositories (interfaces)   │
│              (Lógica de negocio pura)                       │
│                  (Capa más interna)                         │
└─────────────────────────────────────────────────────────────┘
```

### 📦 Componentes Clave

| Componente | Ubicación | Descripción |
|------------|-----------|-------------|
| **Vehicle** | `domain/entities/` | Entidad principal con validaciones |
| **VehicleRepository** | `domain/repositories/` | Interface del repositorio |
| **CSVVehicleRepository** | `adapters/repositories/` | Implementación CSV |
| **GetVehicleStatistics** | `use_cases/` | Caso de uso: estadísticas |
| **FilterVehicles** | `use_cases/` | Caso de uso: filtrado |
| **PlotlyChartGenerator** | `infrastructure/visualization/` | Generador de gráficos |
| **Settings** | `infrastructure/config/` | Configuración (Singleton) |
| **DIContainer** | `infrastructure/di/` | Inyección de dependencias |
| **HistogramComponent** | `interfaces/streamlit_app/components/` | Componente histograma |
| **ScatterPlotComponent** | `interfaces/streamlit_app/components/` | Componente dispersión ✨ |

---

## 🚀 Comandos Útiles

### Verificar Entorno Virtual
```bash
# Ver qué Python estás usando
which python

# Resultado esperado (dentro del venv):
# /Users/israelcastillo/Documents/Cursor_IA/Python_IA/proyect_sprint_final_7/vehicles_env/bin/python

# Ver paquetes instalados
pip list

# Buscar un paquete específico
pip list | grep plotly
```

### Actualizar Dependencias
```bash
# Después de instalar nuevos paquetes
pip freeze > requirements.txt
```

### Instalar desde requirements.txt
```bash
pip install -r requirements.txt
```

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Análisis con Pandas y Plotly
```python
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv('data/raw/vehicles.csv')

# Análisis exploratorio
print(df.describe())

# Visualización interactiva
fig = px.histogram(df, x='precio', nbins=50, title='Distribución de Precios')
fig.show()
```

### Ejemplo 2: Aplicación Streamlit con Plotly
```python
import streamlit as st
import plotly.express as px
import pandas as pd

st.title('🚗 Dashboard de Vehículos')

# Cargar datos
df = pd.read_csv('data/raw/vehicles.csv')

# Sidebar
marca = st.sidebar.selectbox('Selecciona marca:', df['marca'].unique())

# Filtrar datos
df_filtrado = df[df['marca'] == marca]

# Gráfico interactivo
fig = px.scatter(df_filtrado, x='año', y='precio', 
                 hover_data=['modelo', 'kilometraje'])
st.plotly_chart(fig)
```

### Ejemplo 3: Trabajar con Notebooks
```python
import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

# Crear un nuevo notebook
nb = new_notebook()

# Agregar celdas
nb.cells.append(new_markdown_cell('# Análisis de Vehículos'))
nb.cells.append(new_code_cell('import pandas as pd\nimport plotly.express as px'))

# Guardar
with open('notebooks/analisis.ipynb', 'w') as f:
    nbformat.write(nb, f)
```

---

## 🔧 Solución de Problemas

### Error: `ModuleNotFoundError: No module named 'plotly'`

**Solución:**
```bash
# 1. Verificar que estás en el venv
which python

# 2. Activar el venv si no lo estás
source vehicles_env/bin/activate

# 3. Instalar plotly
pip install plotly
```

### Error: `ModuleNotFoundError: No module named 'nbformat'`

**Solución:**
```bash
# Activar venv e instalar
source vehicles_env/bin/activate
pip install nbformat
```

### El entorno virtual no se activa

**Solución:**
```bash
# Usar ruta completa
source /Users/israelcastillo/Documents/Cursor_IA/Python_IA/proyect_sprint_final_7/vehicles_env/bin/activate
```

### Recrear el entorno virtual

Si todo falla:
```bash
# Eliminar el entorno actual
rm -rf vehicles_env

# Ejecutar el script de configuración
./setup_env.sh

# O hacerlo manualmente:
python3 -m venv vehicles_env
source vehicles_env/bin/activate
pip install -r requirements.txt
```

---

## 📊 Comparación: Matplotlib vs Plotly

| Característica | Matplotlib | Plotly |
|----------------|------------|--------|
| **Tipo** | Estático | Interactivo |
| **Zoom** | ❌ | ✅ |
| **Hover info** | ❌ | ✅ |
| **Exportar HTML** | ❌ | ✅ |
| **Velocidad** | Rápido | Más lento |
| **Tamaño archivo** | Pequeño | Grande |
| **Uso típico** | Reportes PDF | Dashboards web |

### Cuándo usar cada uno:

**Matplotlib:**
- Reportes estáticos
- Publicaciones científicas
- Gráficos simples y rápidos

**Plotly:**
- Dashboards interactivos
- Aplicaciones web (Streamlit)
- Exploración de datos
- Presentaciones interactivas


# 1. Ir al proyecto
cd /Users/israelcastillo/Documents/Cursor_IA/Python_IA/proyect_sprint_final_7

# 2. Activar entorno
source vehicles_env/bin/activate

# 3. Verificar instalación
python test_libraries.py

# 4. Ver librerías instaladas
pip list | grep -E "(plotly|nbformat)"

---

## 🎯 Próximos Pasos

1. **Cargar datos de vehículos** en `data/raw/`
2. **Explorar datos** usando notebooks en `notebooks/`
3. **Crear visualizaciones** con Plotly
4. **Desarrollar dashboard** con Streamlit
5. **Documentar hallazgos** en `reports/`

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [Pandas](https://pandas.pydata.org/docs/)
- [Plotly](https://plotly.com/python/)
- [Streamlit](https://docs.streamlit.io/)
- [nbformat](https://nbformat.readthedocs.io/)

### Tutoriales
- [Plotly Express Tutorial](https://plotly.com/python/plotly-express/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Jupyter Notebook Best Practices](https://jupyter-notebook.readthedocs.io/)

---

## 👤 Autor

**Israel Castillo (Isra)**
- Especialidad: Desarrollo Full-Stack (Java, Python)
- Servicios: AWS, Auth0

---

## 📝 Notas de Versión

### v1.0.0 (2026-02-26)
- ✅ Configuración inicial del proyecto
- ✅ Instalación de dependencias base
- ✅ Agregado Plotly para visualizaciones interactivas
- ✅ Agregado nbformat para trabajo con notebooks
- ✅ Documentación completa

---

**Última actualización:** 2026-02-26
