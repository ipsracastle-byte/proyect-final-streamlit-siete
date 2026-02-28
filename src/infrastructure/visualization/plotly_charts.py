"""
Generador de gráficos con Plotly.

Centraliza la creación de visualizaciones usando Plotly.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import List
from src.domain.entities.vehicle import Vehicle


class PlotlyChartGenerator:
    """
    Generador de gráficos con Plotly.
    
    Esta clase encapsula la lógica de creación de gráficos,
    separándola de la lógica de negocio y la UI.
    """
    
    @staticmethod
    def create_odometer_histogram(vehicles: List[Vehicle], nbins: int = 50) -> go.Figure:
        """
        Crea un histograma de la distribución del odómetro.
        
        Args:
            vehicles: Lista de vehículos
            nbins: Número de bins para el histograma
        
        Returns:
            Figura de Plotly con el histograma
        
        Example:
            >>> chart_gen = PlotlyChartGenerator()
            >>> fig = chart_gen.create_odometer_histogram(vehicles)
            >>> fig.show()
        """
        # Extraer datos de odómetro
        odometer_data = [v.odometer for v in vehicles if v.odometer is not None]
        
        # Crear histograma
        fig = go.Figure(data=[go.Histogram(
            x=odometer_data,
            nbinsx=nbins,
            marker_color='steelblue',
            opacity=0.8
        )])
        
        # Personalizar layout
        fig.update_layout(
            title_text='Distribución del Odómetro',
            xaxis_title='Odómetro (millas)',
            yaxis_title='Frecuencia',
            template='plotly_white',
            hovermode='x unified',
            showlegend=False
        )
        
        return fig
    
    @staticmethod
    def create_price_histogram(vehicles: List[Vehicle], nbins: int = 50) -> go.Figure:
        """
        Crea un histograma de la distribución de precios.
        
        Args:
            vehicles: Lista de vehículos
            nbins: Número de bins
        
        Returns:
            Figura de Plotly
        """
        prices = [v.price for v in vehicles]
        
        fig = go.Figure(data=[go.Histogram(
            x=prices,
            nbinsx=nbins,
            marker_color='green',
            opacity=0.8
        )])
        
        fig.update_layout(
            title_text='Distribución de Precios',
            xaxis_title='Precio (USD)',
            yaxis_title='Frecuencia',
            template='plotly_white',
            hovermode='x unified'
        )
        
        return fig
    
    @staticmethod
    def create_price_vs_year_scatter(vehicles: List[Vehicle]) -> go.Figure:
        """
        Crea un gráfico de dispersión de precio vs año.
        
        Args:
            vehicles: Lista de vehículos
        
        Returns:
            Figura de Plotly
        """
        years = [v.model_year for v in vehicles]
        prices = [v.price for v in vehicles]
        
        fig = go.Figure(data=[go.Scatter(
            x=years,
            y=prices,
            mode='markers',
            marker=dict(
                size=5,
                color=prices,
                colorscale='Viridis',
                showscale=True,
                opacity=0.6
            )
        )])
        
        fig.update_layout(
            title_text='Precio vs Año del Modelo',
            xaxis_title='Año del Modelo',
            yaxis_title='Precio (USD)',
            template='plotly_white',
            hovermode='closest'
        )
        
        return fig
    
    @staticmethod
    def create_condition_boxplot(vehicles: List[Vehicle]) -> go.Figure:
        """
        Crea un boxplot de precios por condición.
        
        Args:
            vehicles: Lista de vehículos
        
        Returns:
            Figura de Plotly
        """
        # Preparar datos
        data_dict = {}
        for vehicle in vehicles:
            if vehicle.condition not in data_dict:
                data_dict[vehicle.condition] = []
            data_dict[vehicle.condition].append(vehicle.price)
        
        # Crear boxplot
        fig = go.Figure()
        
        for condition, prices in data_dict.items():
            fig.add_trace(go.Box(
                y=prices,
                name=condition,
                boxmean='sd'
            ))
        
        fig.update_layout(
            title_text='Distribución de Precios por Condición',
            xaxis_title='Condición',
            yaxis_title='Precio (USD)',
            template='plotly_white',
            showlegend=True
        )
        
        return fig
    
    @staticmethod
    def create_price_vs_odometer_scatter(vehicles: List[Vehicle]) -> go.Figure:
        """
        Crea un gráfico de dispersión de precio vs odómetro.
        
        Muestra la relación entre el kilometraje y el precio de los vehículos.
        Útil para identificar tendencias y outliers.
        
        Args:
            vehicles: Lista de vehículos
        
        Returns:
            Figura de Plotly con el gráfico de dispersión
        
        Example:
            >>> chart_gen = PlotlyChartGenerator()
            >>> fig = chart_gen.create_price_vs_odometer_scatter(vehicles)
            >>> fig.show()
        """
        # Filtrar vehículos con datos completos
        valid_vehicles = [
            v for v in vehicles 
            if v.odometer is not None and v.price is not None
        ]
        
        # Extraer datos
        odometer_data = [v.odometer for v in valid_vehicles]
        price_data = [v.price for v in valid_vehicles]
        
        # Preparar texto para hover (información adicional)
        hover_text = [
            f"Modelo: {v.model}<br>"
            f"Año: {v.model_year}<br>"
            f"Precio: ${v.price:,.0f}<br>"
            f"Odómetro: {v.odometer:,.0f} millas<br>"
            f"Condición: {v.condition}"
            for v in valid_vehicles
        ]
        
        # Crear gráfico de dispersión
        fig = go.Figure(data=[go.Scatter(
            x=odometer_data,
            y=price_data,
            mode='markers',
            marker=dict(
                size=6,
                color=price_data,  # Color basado en precio
                colorscale='Viridis',  # Escala de colores
                showscale=True,
                colorbar=dict(title="Precio (USD)"),
                opacity=0.6,
                line=dict(width=0.5, color='white')
            ),
            text=hover_text,
            hovertemplate='%{text}<extra></extra>'
        )])
        
        # Personalizar layout
        fig.update_layout(
            title_text='Relación entre Precio y Kilometraje',
            xaxis_title='Odómetro (millas)',
            yaxis_title='Precio (USD)',
            template='plotly_white',
            hovermode='closest',
            showlegend=False,
            height=600
        )
        
        # Agregar formato a los ejes
        fig.update_xaxes(
            tickformat=',',  # Formato con comas para miles
            gridcolor='lightgray'
        )
        fig.update_yaxes(
            tickformat='$,',  # Formato de moneda
            gridcolor='lightgray'
        )
        
        return fig