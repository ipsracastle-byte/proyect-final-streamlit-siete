"""
Contenedor de Inyección de Dependencias.

Centraliza la creación y gestión de dependencias de la aplicación.
"""

from typing import Dict, Any, Callable
from src.infrastructure.config.settings import Settings
from src.infrastructure.data_sources.csv_reader import CSVReader
from src.adapters.repositories.csv_vehicle_repository import CSVVehicleRepository
from src.use_cases.get_vehicle_statistics import GetVehicleStatisticsUseCase
from src.use_cases.filter_vehicles import FilterVehiclesUseCase
from src.infrastructure.visualization.plotly_charts import PlotlyChartGenerator


class DIContainer:
    """
    Contenedor de Inyección de Dependencias.
    
    Implementa el patrón Dependency Injection para gestionar
    la creación y ciclo de vida de las dependencias.
    
    Example:
        >>> container = DIContainer()
        >>> use_case = container.get('get_vehicle_statistics_use_case')
        >>> stats = use_case.execute()
    """
    
    def __init__(self):
        """Inicializa el contenedor."""
        self._services: Dict[str, Any] = {}
        self._factories: Dict[str, Callable] = {}
        self._configure()
    
    def _configure(self):
        """Configura las dependencias y sus factories."""
        
        # Configuración
        self._factories['settings'] = lambda: Settings()
        
        # Data Sources
        self._factories['csv_reader'] = lambda: CSVReader(
            str(self.get('settings').data_path)
        )
        
        # Repositories
        self._factories['vehicle_repository'] = lambda: CSVVehicleRepository(
            self.get('csv_reader')
        )
        
        # Use Cases
        self._factories['get_vehicle_statistics_use_case'] = lambda: GetVehicleStatisticsUseCase(
            self.get('vehicle_repository')
        )
        
        self._factories['filter_vehicles_use_case'] = lambda: FilterVehiclesUseCase(
            self.get('vehicle_repository')
        )
        
        # Visualization
        self._factories['chart_generator'] = lambda: PlotlyChartGenerator()
    
    def get(self, service_name: str) -> Any:
        """
        Obtiene una instancia del servicio.
        
        Args:
            service_name: Nombre del servicio
        
        Returns:
            Instancia del servicio
        
        Raises:
            ValueError: Si el servicio no está registrado
        
        Example:
            >>> container = DIContainer()
            >>> repository = container.get('vehicle_repository')
        """
        # Si ya existe la instancia, retornarla
        if service_name not in self._services:
            if service_name not in self._factories:
                raise ValueError(f"Servicio no registrado: {service_name}")
            
            # Crear la instancia usando el factory
            self._services[service_name] = self._factories[service_name]()
        
        return self._services[service_name]
    
    def reset(self):
        """Resetea todas las instancias (útil para testing)."""
        self._services.clear()
