"""
Caso de uso: Obtener estadísticas de vehículos.

Este caso de uso orquesta la lógica para obtener estadísticas
generales de los vehículos almacenados.
"""

from typing import Dict, Any
from src.domain.repositories.vehicle_repository import VehicleRepository


class GetVehicleStatisticsUseCase:
    """
    Caso de uso para obtener estadísticas de vehículos.
    
    Este caso de uso coordina la obtención de estadísticas
    generales de vehículos desde el repositorio.
    """
    
    def __init__(self, vehicle_repository: VehicleRepository):
        """
        Inicializa el caso de uso.
        
        Args:
            vehicle_repository: Repositorio de vehículos
        """
        self._repository = vehicle_repository
    
    def execute(self) -> Dict[str, Any]:
        """
        Ejecuta el caso de uso.
        
        Returns:
            Diccionario con estadísticas de vehículos:
            - total_vehicles: Total de vehículos
            - average_price: Precio promedio
            - average_odometer: Odómetro promedio
            - year_range: Rango de años (min, max)
            - recent_vehicles: Cantidad de vehículos recientes
            - low_mileage_vehicles: Cantidad con bajo kilometraje
        
        Example:
            >>> use_case = GetVehicleStatisticsUseCase(repository)
            >>> stats = use_case.execute()
            >>> print(stats['total_vehicles'])
            51525
        """
        # Obtener estadísticas básicas del repositorio
        basic_stats = self._repository.get_statistics()
        
        # Obtener todos los vehículos para cálculos adicionales
        vehicles = self._repository.find_all()
        
        # Calcular estadísticas adicionales usando lógica de dominio
        recent_count = sum(1 for v in vehicles if v.is_recent())
        low_mileage_count = sum(1 for v in vehicles if v.is_low_mileage())
        excellent_condition_count = sum(1 for v in vehicles if v.is_excellent_condition())
        
        # Combinar estadísticas
        return {
            **basic_stats,
            'recent_vehicles': recent_count,
            'low_mileage_vehicles': low_mileage_count,
            'excellent_condition_count': excellent_condition_count,
            'recent_percentage': (recent_count / len(vehicles) * 100) if vehicles else 0,
            'low_mileage_percentage': (low_mileage_count / len(vehicles) * 100) if vehicles else 0
        }
