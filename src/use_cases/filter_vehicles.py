"""
Caso de uso: Filtrar vehículos.

Este caso de uso orquesta la lógica para filtrar vehículos
según criterios específicos.
"""

from typing import List, Dict, Any
from src.domain.entities.vehicle import Vehicle
from src.domain.repositories.vehicle_repository import VehicleRepository


class FilterVehiclesUseCase:
    """
    Caso de uso para filtrar vehículos.
    
    Coordina el filtrado de vehículos según criterios específicos
    y aplica lógica de negocio adicional si es necesario.
    """
    
    def __init__(self, vehicle_repository: VehicleRepository):
        """
        Inicializa el caso de uso.
        
        Args:
            vehicle_repository: Repositorio de vehículos
        """
        self._repository = vehicle_repository
    
    def execute(self, filters: Dict[str, Any]) -> List[Vehicle]:
        """
        Ejecuta el filtrado de vehículos.
        
        Args:
            filters: Diccionario con filtros a aplicar
        
        Returns:
            Lista de vehículos que cumplen los criterios
        
        Example:
            >>> filters = {'model_year': 2020, 'price_max': 50000}
            >>> use_case = FilterVehiclesUseCase(repository)
            >>> vehicles = use_case.execute(filters)
        """
        # Obtener vehículos filtrados del repositorio
        vehicles = self._repository.find_by_filters(filters)
        
        # Aplicar lógica de negocio adicional si es necesario
        # Por ejemplo, ordenar por precio
        if filters.get('sort_by') == 'price':
            vehicles = sorted(vehicles, key=lambda v: v.price)
        elif filters.get('sort_by') == 'year':
            vehicles = sorted(vehicles, key=lambda v: v.model_year, reverse=True)
        
        return vehicles
