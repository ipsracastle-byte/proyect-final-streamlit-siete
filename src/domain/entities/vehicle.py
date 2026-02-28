"""
Entidad Vehicle - Representa un vehículo en el dominio.

Esta es la entidad principal del dominio que encapsula
toda la lógica de negocio relacionada con vehículos.
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Vehicle:
    """
    Entidad Vehicle del dominio.
    
    Representa un vehículo con todas sus características y
    contiene la lógica de negocio pura relacionada con vehículos.
    
    Attributes:
        price: Precio del vehículo en USD
        model_year: Año del modelo
        model: Nombre del modelo
        condition: Condición del vehículo
        cylinders: Número de cilindros (opcional)
        fuel: Tipo de combustible
        odometer: Kilometraje en millas (opcional)
        transmission: Tipo de transmisión
        vehicle_type: Tipo de vehículo
        paint_color: Color de pintura (opcional)
        is_4wd: Si tiene tracción 4WD
        date_posted: Fecha de publicación
        days_listed: Días listado
    
    Example:
        >>> vehicle = Vehicle(
        ...     price=25000.0,
        ...     model_year=2020,
        ...     model="Camry",
        ...     condition="excellent",
        ...     fuel="gas",
        ...     transmission="automatic",
        ...     vehicle_type="sedan",
        ...     is_4wd=False,
        ...     date_posted=datetime.now(),
        ...     days_listed=10
        ... )
        >>> vehicle.is_recent()
        True
    """
    
    price: float
    model_year: int
    model: str
    condition: str
    fuel: str
    transmission: str
    vehicle_type: str
    is_4wd: bool
    date_posted: datetime
    days_listed: int
    cylinders: Optional[int] = None
    odometer: Optional[float] = None
    paint_color: Optional[str] = None
    
    def __post_init__(self):
        """Valida los datos después de la inicialización."""
        self._validate()
    
    def _validate(self) -> None:
        """
        Valida que los datos del vehículo sean correctos.
        
        Raises:
            ValueError: Si algún dato es inválido
        """
        # Validar precio
        if self.price <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        
        if self.price > 1_000_000:
            raise ValueError("El precio no puede exceder $1,000,000")
        
        # Validar año
        current_year = datetime.now().year
        if self.model_year < 1900 or self.model_year > current_year + 1:
            raise ValueError(f"Año del modelo inválido: {self.model_year}")
        
        # Validar odómetro
        if self.odometer is not None and self.odometer < 0:
            raise ValueError("El odómetro no puede ser negativo")
        
        # Validar cilindros
        if self.cylinders is not None and (self.cylinders < 1 or self.cylinders > 16):
            raise ValueError("Número de cilindros inválido")
        
        # Validar días listado
        if self.days_listed < 0:
            raise ValueError("Los días listados no pueden ser negativos")
    
    def is_recent(self, max_age_years: int = 5) -> bool:
        """
        Determina si el vehículo es reciente.
        
        Un vehículo se considera reciente si tiene menos de
        max_age_years años de antigüedad.
        
        Args:
            max_age_years: Edad máxima en años para considerar reciente
        
        Returns:
            True si el vehículo es reciente, False en caso contrario
        
        Example:
            >>> vehicle = Vehicle(model_year=2023, ...)
            >>> vehicle.is_recent()
            True
            >>> vehicle.is_recent(max_age_years=2)
            True
        """
        current_year = datetime.now().year
        age = current_year - self.model_year
        return age <= max_age_years
    
    def is_low_mileage(self, threshold: float = 50000) -> bool:
        """
        Determina si el vehículo tiene bajo kilometraje.
        
        Args:
            threshold: Umbral de millas para considerar bajo kilometraje
        
        Returns:
            True si tiene bajo kilometraje, False en caso contrario
        
        Example:
            >>> vehicle = Vehicle(odometer=30000, ...)
            >>> vehicle.is_low_mileage()
            True
        """
        if self.odometer is None:
            return False
        return self.odometer < threshold
    
    def calculate_age(self) -> int:
        """
        Calcula la edad del vehículo en años.
        
        Returns:
            Edad del vehículo en años
        
        Example:
            >>> vehicle = Vehicle(model_year=2020, ...)
            >>> vehicle.calculate_age()
            4  # Si estamos en 2024
        """
        current_year = datetime.now().year
        return current_year - self.model_year
    
    def is_excellent_condition(self) -> bool:
        """
        Verifica si el vehículo está en excelente condición.
        
        Returns:
            True si la condición es 'excellent', False en caso contrario
        """
        return self.condition.lower() == 'excellent'
    
    def get_price_per_year(self) -> float:
        """
        Calcula el precio por año de antigüedad.
        
        Returns:
            Precio dividido por la edad del vehículo
        
        Example:
            >>> vehicle = Vehicle(price=20000, model_year=2020, ...)
            >>> vehicle.get_price_per_year()
            5000.0  # Si el vehículo tiene 4 años
        """
        age = self.calculate_age()
        if age == 0:
            return self.price
        return self.price / age
    
    def __str__(self) -> str:
        """Representación en string del vehículo."""
        return (
            f"{self.model_year} {self.model} - "
            f"${self.price:,.2f} - "
            f"{self.condition} - "
            f"{self.odometer or 'N/A'} mi"
        )
    
    def __repr__(self) -> str:
        """Representación técnica del vehículo."""
        return (
            f"Vehicle(model_year={self.model_year}, "
            f"model='{self.model}', "
            f"price={self.price}, "
            f"condition='{self.condition}')"
        )
