"""
Aplicación Streamlit para análisis de vehículos.

Esta es la aplicación principal que sigue los principios de Clean Architecture.
Todas las dependencias se inyectan mediante el DIContainer.
"""

import streamlit as st
import sys
from pathlib import Path

# Agregar src al path para imports
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from src.infrastructure.di.container import DIContainer
from src.infrastructure.config.settings import Settings
from src.interfaces.streamlit_app.components.histogram_component import HistogramComponent
from src.interfaces.streamlit_app.components.scatter_plot_component import ScatterPlotComponent


def configure_page():
    """Configura la página de Streamlit."""
    settings = Settings()
    
    st.set_page_config(
        page_title=settings.app_title,
        page_icon=settings.page_icon,
        layout=settings.layout,
        initial_sidebar_state="expanded"
    )


def render_header():
    """Renderiza el encabezado de la aplicación."""
    st.title('🚗 Análisis de Vehículos')
    st.markdown("""
    Esta aplicación permite explorar datos de vehículos usados en Estados Unidos
    utilizando **Clean Architecture** y mejores prácticas de desarrollo.
    
    **Características:**
    - 🏛️ Clean Architecture
    - 🎨 Patrones de Diseño
    - 📊 Visualizaciones Interactivas
    - 🧪 Código Testeable
    """)


def render_sidebar(container: DIContainer):
    """
    Renderiza el sidebar con información del dataset.
    
    Args:
        container: Contenedor de dependencias
    """
    with st.sidebar:
        st.header('📊 Información del Dataset')
        
        # Obtener estadísticas
        try:
            stats_use_case = container.get('get_vehicle_statistics_use_case')
            stats = stats_use_case.execute()
            
            # Métricas principales
            st.metric('Total de vehículos', f'{stats["total_vehicles"]:,}')
            st.metric('Precio Promedio', f'${stats["average_price"]:,.2f}')
            st.metric('Odómetro Promedio', f'{stats["average_odometer"]:,.0f} mi')
            
            # Información adicional
            st.subheader('📈 Estadísticas Adicionales')
            st.metric('Vehículos Recientes', f'{stats["recent_vehicles"]:,}')
            st.metric('Bajo Kilometraje', f'{stats["low_mileage_vehicles"]:,}')
            
            # Rango de años
            year_min, year_max = stats['year_range']
            st.metric('Rango de Años', f'{year_min} - {year_max}')
            
        except Exception as e:
            st.error(f'❌ Error al cargar estadísticas: {e}')


def render_main_content(container: DIContainer):
    """
    Renderiza el contenido principal.
    
    Args:
        container: Contenedor de dependencias
    """
    # Obtener dependencias del container
    get_statistics_use_case = container.get('get_vehicle_statistics_use_case')
    filter_vehicles_use_case = container.get('filter_vehicles_use_case')
    chart_generator = container.get('chart_generator')
    repository = container.get('vehicle_repository')
    
    # Componente de histograma
    histogram_component = HistogramComponent(
        get_statistics_use_case,
        filter_vehicles_use_case,
        chart_generator
    )
    
    # Componente de gráfico de dispersión
    scatter_component = ScatterPlotComponent(repository)
    
    # Renderizar componentes
    histogram_component.render()
    
    st.markdown('---')  # Separador visual
    
    scatter_component.render()


def render_footer():
    """Renderiza el footer de la aplicación."""
    st.markdown('---')
    st.markdown("""
    **Proyecto Sprint Final 7** | Clean Architecture | Israel Castillo
    
    📚 Arquitectura:
    - Domain: Lógica de negocio pura
    - Use Cases: Orquestación de lógica
    - Adapters: Conversión de datos
    - Infrastructure: Detalles técnicos
    - Interfaces: UI (Streamlit)
    """)


def main():
    """
    Función principal de la aplicación.
    
    Sigue el principio de Dependency Injection:
    - Crea el contenedor de dependencias
    - Inyecta dependencias en los componentes
    - Renderiza la UI
    """
    # Configurar página
    configure_page()
    
    # Crear contenedor de dependencias
    container = DIContainer()
    
    try:
        # Renderizar componentes
        render_header()
        render_sidebar(container)
        render_main_content(container)
        render_footer()
        
    except Exception as e:
        st.error(f'❌ Error en la aplicación: {e}')
        st.exception(e)


if __name__ == '__main__':
    main()
