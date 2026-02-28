"""
Interface del repositorio de vehículos.

Define el contrato que deben cumplir todas las implementaciones
de repositorios de vehículos, independientemente de la fuente de datos.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from src.domain.entities.vehicle import Vehicle


class VehicleRepository(ABC):
    """
    Interface para repositorio de vehículos.
    
    Esta es una abstracción que define las operaciones que se pueden
    realizar sobre vehículos, sin especificar cómo se implementan.
    
    Siguiendo el principio de Dependency Inversion (SOLID), las capas
    superiores dependen de esta abstracción, no de implementaciones concretas.
    """
    
    @abstractmethod
    def find_all(self) -> List[Vehicle]:
        """
        Obtiene todos los vehículos.
        
        Returns:
            Lista de todos los vehículos disponibles
        
        Raises:
            RepositoryError: Si hay un error al acceder a los datos
        """
        pass
    
    @abstractmethod
    def find_by_filters(self, filters: Dict[str, Any]) -> List[Vehicle]:
        """
        Filtra vehículos según criterios específicos.
        
        Args:
            filters: Diccionario con los filtros a aplicar
                Ejemplos de filtros:
                - model_year: int
                - price_min: float
                - price_max: float
                - condition: str
                - vehicle_type: str
                - is_4wd: bool
        
        Returns:
            Lista de vehículos que cumplen con los filtros
        
        Raises:
            RepositoryError: Si hay un error al filtrar los datos
        
        Example:
            >>> filters = {'model_year': 2020, 'price_max': 50000}
            >>> vehicles = repository.find_by_filters(filters)
        """
        pass
    
    @abstractmethod
    def count(self) -> int:
        """
        Cuenta el total de vehículos.
        
        Returns:
            Número total de vehículos
        
        Raises:
            RepositoryError: Si hay un error al contar
        """
        pass
    
    @abstractmethod
    def get_statistics(self) -> Dict[str, Any]:
        """
        Obtiene estadísticas generales de los vehículos.
        
        Returns:
            Diccionario con estadísticas como:
            - total_vehicles: int
            - average_price: float
            - average_odometer: float
            - year_range: tuple
        
        Raises:
            RepositoryError: Si hay un error al calcular estadísticas
        """
        pass
