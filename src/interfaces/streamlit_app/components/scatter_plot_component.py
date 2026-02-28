"""
Componente de Streamlit para gráfico de dispersión.

Este componente maneja la visualización del gráfico de dispersión
precio vs odómetro, siguiendo los principios de Clean Architecture.

Optimizaciones implementadas:
- Caché de datos con @st.cache_data
- Muestreo de datos para mejorar rendimiento
- Opción de usar todos los datos o muestra
"""

import streamlit as st
import random
from typing import List
from src.use_cases.get_vehicle_statistics import GetVehicleStatisticsUseCase
from src.infrastructure.visualization.plotly_charts import PlotlyChartGenerator
from src.adapters.repositories.csv_vehicle_repository import CSVVehicleRepository
from src.domain.entities.vehicle import Vehicle


class ScatterPlotComponent:
    """
    Componente para renderizar el gráfico de dispersión en Streamlit.
    
    Responsabilidades:
    - Renderizar el botón de acción
    - Obtener datos a través de casos de uso
    - Mostrar el gráfico de dispersión
    - Mostrar estadísticas relacionadas
    """
    
    def __init__(self, repository: CSVVehicleRepository):
        """
        Inicializa el componente.
        
        Args:
            repository: Repositorio de vehículos
        """
        self.repository = repository
        self.stats_use_case = GetVehicleStatisticsUseCase(repository)
        self.chart_generator = PlotlyChartGenerator()
    
    def render(self):
        """Renderiza el componente en Streamlit."""
        st.header('📊 Análisis de Correlación')
        
        # Opciones de rendimiento
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Botón para mostrar gráfico de dispersión
            show_plot = st.button('🔍 Construir Gráfico de Dispersión', type='secondary')
        
        with col2:
            # Opción de muestreo
            use_sample = st.checkbox('Muestra rápida', value=True, 
                                    help='Usa 5,000 registros aleatorios para mayor velocidad')
        
        if show_plot:
            self._render_scatter_plot(use_sample=use_sample)
    
    @staticmethod
    @st.cache_data(ttl=600)  # Caché por 10 minutos
    def _get_cached_vehicles(_repository) -> List[Vehicle]:
        """
        Obtiene vehículos con caché para mejorar rendimiento.
        
        Args:
            _repository: Repositorio (el _ evita que Streamlit lo hashee)
        
        Returns:
            Lista de vehículos
        """
        return _repository.find_all()
    
    def _sample_vehicles(self, vehicles: List[Vehicle], sample_size: int = 5000) -> List[Vehicle]:
        """
        Toma una muestra aleatoria de vehículos.
        
        Args:
            vehicles: Lista completa de vehículos
            sample_size: Tamaño de la muestra
        
        Returns:
            Muestra aleatoria de vehículos
        """
        if len(vehicles) <= sample_size:
            return vehicles
        return random.sample(vehicles, sample_size)
    
    def _render_scatter_plot(self, use_sample: bool = True):
        """
        Renderiza el gráfico de dispersión y estadísticas.
        
        Args:
            use_sample: Si True, usa muestra de 5000 registros para mayor velocidad
        """
        try:
            # Mostrar mensaje informativo
            st.write('Creación de un gráfico de dispersión para analizar la relación entre precio y kilometraje')
            
            # Obtener vehículos (con caché)
            with st.spinner('Cargando datos...'):
                all_vehicles = self._get_cached_vehicles(self.repository)
            
            if not all_vehicles:
                st.warning('⚠️ No hay datos disponibles')
                return
            
            # Aplicar muestreo si está habilitado
            if use_sample and len(all_vehicles) > 5000:
                vehicles = self._sample_vehicles(all_vehicles, sample_size=5000)
                st.info(f'📊 Mostrando muestra de {len(vehicles):,} vehículos de {len(all_vehicles):,} totales para mayor velocidad')
            else:
                vehicles = all_vehicles
                if len(all_vehicles) > 5000:
                    st.info(f'📊 Mostrando todos los {len(vehicles):,} vehículos (puede tardar unos segundos)')
            
            # Crear y mostrar el gráfico
            with st.spinner('Generando gráfico de dispersión...'):
                fig = self.chart_generator.create_price_vs_odometer_scatter(vehicles)
                st.plotly_chart(fig, use_container_width=True)
            
            # Mostrar estadísticas relacionadas
            self._show_correlation_stats(vehicles)
            
            # Mostrar insights
            self._show_insights(vehicles)
            
            st.success('✅ Gráfico generado exitosamente')
            
        except Exception as e:
            st.error(f'❌ Error al generar el gráfico: {str(e)}')
    
    def _show_correlation_stats(self, vehicles):
        """
        Muestra estadísticas de correlación.
        
        Args:
            vehicles: Lista de vehículos
        """
        st.subheader('📈 Estadísticas de Correlación')
        
        # Filtrar vehículos con datos completos
        valid_vehicles = [
            v for v in vehicles 
            if v.odometer is not None and v.price is not None
        ]
        
        if not valid_vehicles:
            st.warning('No hay suficientes datos para calcular correlación')
            return
        
        # Calcular correlación simple
        import numpy as np
        odometers = [v.odometer for v in valid_vehicles]
        prices = [v.price for v in valid_vehicles]
        
        correlation = np.corrcoef(odometers, prices)[0, 1]
        
        # Mostrar en columnas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="Correlación",
                value=f"{correlation:.3f}",
                help="Correlación de Pearson entre odómetro y precio"
            )
        
        with col2:
            avg_price = np.mean(prices)
            st.metric(
                label="Precio Promedio",
                value=f"${avg_price:,.0f}",
                help="Precio promedio de los vehículos"
            )
        
        with col3:
            avg_odometer = np.mean(odometers)
            st.metric(
                label="Kilometraje Promedio",
                value=f"{avg_odometer:,.0f} mi",
                help="Kilometraje promedio de los vehículos"
            )
        
        # Interpretación de la correlación
        st.markdown("---")
        st.markdown("**💡 Interpretación de la Correlación:**")
        
        if correlation < -0.7:
            interpretation = "🔴 **Correlación negativa fuerte**: A mayor kilometraje, menor precio"
        elif correlation < -0.3:
            interpretation = "🟠 **Correlación negativa moderada**: Tendencia a menor precio con mayor kilometraje"
        elif correlation < 0.3:
            interpretation = "🟡 **Correlación débil**: Poca relación entre kilometraje y precio"
        elif correlation < 0.7:
            interpretation = "🟢 **Correlación positiva moderada**: A mayor kilometraje, mayor precio"
        else:
            interpretation = "🔵 **Correlación positiva fuerte**: A mayor kilometraje, mayor precio"
        
        st.info(interpretation)
    
    def _show_insights(self, vehicles):
        """
        Muestra insights adicionales.
        
        Args:
            vehicles: Lista de vehículos
        """
        st.subheader('🔍 Insights Adicionales')
        
        # Filtrar vehículos válidos
        valid_vehicles = [
            v for v in vehicles 
            if v.odometer is not None and v.price is not None
        ]
        
        if not valid_vehicles:
            return
        
        # Encontrar outliers (vehículos caros con alto kilometraje)
        import numpy as np
        prices = [v.price for v in valid_vehicles]
        odometers = [v.odometer for v in valid_vehicles]
        
        price_75 = np.percentile(prices, 75)
        odometer_75 = np.percentile(odometers, 75)
        
        high_price_high_mileage = [
            v for v in valid_vehicles
            if v.price > price_75 and v.odometer > odometer_75
        ]
        
        with st.expander("📌 Ver Insights Detallados"):
            st.markdown(f"""
            - **Total de vehículos analizados:** {len(valid_vehicles):,}
            - **Vehículos con alto precio y alto kilometraje:** {len(high_price_high_mileage):,}
            - **Rango de precios:** ${min(prices):,.0f} - ${max(prices):,.0f}
            - **Rango de kilometraje:** {min(odometers):,.0f} - {max(odometers):,.0f} millas
            
            **💡 Recomendación:**
            - Los vehículos con bajo kilometraje tienden a tener precios más altos
            - Considera el kilometraje como factor importante en la valoración
            - Los outliers pueden representar vehículos de lujo o casos especiales
            """)
