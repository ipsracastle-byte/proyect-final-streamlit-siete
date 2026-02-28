"""
Configuración global de la aplicación.

Implementa el patrón Singleton para la configuración.
"""

from pathlib import Path
from typing import Optional


class Settings:
    """
    Configuración global de la aplicación (Singleton).
    
    Centraliza toda la configuración de la aplicación.
    """
    
    _instance: Optional['Settings'] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self._initialized = True
        self._configure()
    
    def _configure(self):
        """Configura los valores por defecto."""
        # Rutas del proyecto
        self.project_root = Path(__file__).parent.parent.parent.parent
        self.data_path = self.project_root / 'data' / 'raw' / 'vehicles_us.csv'
        
        # Configuración de caché
        self.cache_enabled = True
        
        # Configuración de visualización
        self.default_plot_template = 'plotly_white'
        self.default_nbins = 50
        
        # Configuración de la aplicación
        self.app_title = "🚗 Análisis de Vehículos"
        self.page_icon = "🚗"
        self.layout = "wide"
