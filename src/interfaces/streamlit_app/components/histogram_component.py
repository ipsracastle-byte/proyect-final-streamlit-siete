"""
Componente de histograma para Streamlit.

Encapsula la lógica de renderizado del histograma de odómetro.
"""

import streamlit as st
from src.use_cases.get_vehicle_statistics import GetVehicleStatisticsUseCase
from src.use_cases.filter_vehicles import FilterVehiclesUseCase
from src.infrastructure.visualization.plotly_charts import PlotlyChartGenerator


class HistogramComponent:
    """
    Componente para mostrar histograma de odómetro.
    
    Este componente encapsula la lógica de UI para mostrar
    el histograma del odómetro de vehículos.
    """
    
    def __init__(
        self,
        get_statistics_use_case: GetVehicleStatisticsUseCase,
        filter_vehicles_use_case: FilterVehiclesUseCase,
        chart_generator: PlotlyChartGenerator
    ):
        """
        Inicializa el componente.
        
        Args:
            get_statistics_use_case: Caso de uso para obtener estadísticas
            filter_vehicles_use_case: Caso de uso para filtrar vehículos
            chart_generator: Generador de gráficos
        """
        self._get_statistics = get_statistics_use_case
        self._filter_vehicles = filter_vehicles_use_case
        self._chart_generator = chart_generator
    
    def render(self):
        """Renderiza el componente en Streamlit."""
        st.header('📈 Visualizaciones')
        
        # Botón para mostrar histograma
        if st.button('🔍 Construir Histograma', type='primary'):
            self._render_histogram()
    
    @staticmethod
    @st.cache_data(ttl=600)  # Caché por 10 minutos
    def _get_cached_vehicles(_filter_use_case):
        """
        Obtiene vehículos con caché para mejorar rendimiento.
        
        Args:
            _filter_use_case: Caso de uso de filtrado
        
        Returns:
            Lista de vehículos
        """
        return _filter_use_case.execute({})
    
    def _render_histogram(self):
        """Renderiza el histograma y estadísticas."""
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        
        # Obtener vehículos (con caché)
        with st.spinner('Cargando datos...'):
            vehicles = self._get_cached_vehicles(self._filter_vehicles)
        
        # Crear y mostrar histograma
        fig = self._chart_generator.create_odometer_histogram(vehicles)
        st.plotly_chart(fig, use_container_width=True)
        
        # Mostrar estadísticas adicionales
        self._render_statistics(vehicles)
    
    def _render_statistics(self, vehicles):
        """
        Renderiza estadísticas adicionales.
        
        Args:
            vehicles: Lista de vehículos
        """
        with st.expander('📊 Ver estadísticas detalladas del odómetro'):
            # Calcular estadísticas
            odometers = [v.odometer for v in vehicles if v.odometer is not None]
            
            if odometers:
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric('Mínimo', f'{min(odometers):,.0f} mi')
                
                with col2:
                    st.metric('Máximo', f'{max(odometers):,.0f} mi')
                
                with col3:
                    avg = sum(odometers) / len(odometers)
                    st.metric('Promedio', f'{avg:,.0f} mi')
                
                with col4:
                    # Desviación estándar
                    mean = sum(odometers) / len(odometers)
                    variance = sum((x - mean) ** 2 for x in odometers) / len(odometers)
                    std_dev = variance ** 0.5
                    st.metric('Desv. Estándar', f'{std_dev:,.0f} mi')
