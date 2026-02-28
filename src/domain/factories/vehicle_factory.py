"""
Factory para crear entidades Vehicle.

Centraliza la lógica de creación de vehículos desde diferentes fuentes de datos.
"""

from typing import Dict, Any
from datetime import datetime
import pandas as pd
from src.domain.entities.vehicle import Vehicle
from src.shared.exceptions import ValidationError


class VehicleFactory:
    """
    Factory para crear entidades Vehicle.
    
    Implementa el patrón Factory para centralizar y simplificar
    la creación de objetos Vehicle desde diferentes formatos.
    """
    
    @staticmethod
    def create_from_dict(data: Dict[str, Any]) -> Vehicle:
        """
        Crea un Vehicle desde un diccionario.
        
        Args:
            data: Diccionario con datos del vehículo
        
        Returns:
            Instancia de Vehicle
        
        Raises:
            ValidationError: Si los datos son inválidos
        
        Example:
            >>> data = {
            ...     'price': 25000,
            ...     'model_year': 2020,
            ...     'model': 'Camry',
            ...     'condition': 'excellent',
            ...     'fuel': 'gas',
            ...     'transmission': 'automatic',
            ...     'type': 'sedan',
            ...     'is_4wd': False,
            ...     'date_posted': '2024-01-01',
            ...     'days_listed': 10
            ... }
            >>> vehicle = VehicleFactory.create_from_dict(data)
        """
        try:
            return Vehicle(
                price=float(data['price']),
                model_year=int(data['model_year']),
                model=str(data['model']),
                condition=str(data['condition']),
                fuel=str(data['fuel']),
                transmission=str(data['transmission']),
                vehicle_type=str(data.get('type', data.get('vehicle_type', 'unknown'))),
                is_4wd=bool(data.get('is_4wd', False)),
                date_posted=VehicleFactory._parse_date(data.get('date_posted')),
                days_listed=int(data.get('days_listed', 0)),
                cylinders=int(data['cylinders']) if pd.notna(data.get('cylinders')) else None,
                odometer=float(data['odometer']) if pd.notna(data.get('odometer')) else None,
                paint_color=str(data['paint_color']) if pd.notna(data.get('paint_color')) else None
            )
        except (KeyError, ValueError, TypeError) as e:
            raise ValidationError(f"Error al crear Vehicle desde diccionario: {e}")
    
    @staticmethod
    def _parse_date(date_value: Any) -> datetime:
        """
        Parsea una fecha de diferentes formatos.
        
        Args:
            date_value: Valor de fecha en diferentes formatos
        
        Returns:
            Objeto datetime
        """
        if isinstance(date_value, datetime):
            return date_value
        
        if isinstance(date_value, str):
            try:
                return pd.to_datetime(date_value)
            except Exception:
                return datetime.now()
        
        if pd.isna(date_value):
            return datetime.now()
        
        return datetime.now()
