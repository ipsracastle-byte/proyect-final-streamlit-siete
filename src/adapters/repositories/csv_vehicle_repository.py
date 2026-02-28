"""
Implementación del repositorio de vehículos usando CSV.

Esta implementación concreta del VehicleRepository lee datos
desde archivos CSV.
"""

import pandas as pd
from typing import List, Dict, Any, Optional
from src.domain.entities.vehicle import Vehicle
from src.domain.repositories.vehicle_repository import VehicleRepository
from src.domain.factories.vehicle_factory import VehicleFactory
from src.infrastructure.data_sources.csv_reader import CSVReader
from src.shared.exceptions import RepositoryError


class CSVVehicleRepository(VehicleRepository):
    """
    Implementación de VehicleRepository usando CSV.
    
    Esta clase adapta los datos del CSV al dominio de la aplicación,
    convirtiendo DataFrames en entidades Vehicle.
    """
    
    def __init__(self, csv_reader: CSVReader):
        """
        Inicializa el repositorio.
        
        Args:
            csv_reader: Lector de archivos CSV
        """
        self._csv_reader = csv_reader
        self._data: Optional[pd.DataFrame] = None
        self._cache: Optional[List[Vehicle]] = None
    
    def _load_data(self) -> pd.DataFrame:
        """
        Carga los datos del CSV (con caché).
        
        Returns:
            DataFrame con los datos
        """
        if self._data is None:
            try:
                self._data = self._csv_reader.read()
            except Exception as e:
                raise RepositoryError(f"Error al cargar datos: {e}")
        return self._data
    
    def _dataframe_to_entities(self, df: pd.DataFrame) -> List[Vehicle]:
        """
        Convierte un DataFrame a lista de entidades Vehicle.
        
        Args:
            df: DataFrame con datos de vehículos
        
        Returns:
            Lista de entidades Vehicle
        """
        vehicles = []
        for _, row in df.iterrows():
            try:
                vehicle = VehicleFactory.create_from_dict(row.to_dict())
                vehicles.append(vehicle)
            except Exception as e:
                # Log error pero continúa con otros registros
                # En producción, usaríamos un logger apropiado
                continue
        
        return vehicles
    
    def find_all(self) -> List[Vehicle]:
        """
        Obtiene todos los vehículos.
        
        Returns:
            Lista de todos los vehículos
        
        Raises:
            RepositoryError: Si hay un error al obtener los datos
        """
        if self._cache is None:
            df = self._load_data()
            self._cache = self._dataframe_to_entities(df)
        
        return self._cache
    
    def find_by_filters(self, filters: Dict[str, Any]) -> List[Vehicle]:
        """
        Filtra vehículos según criterios.
        
        Args:
            filters: Diccionario con filtros
        
        Returns:
            Lista de vehículos filtrados
        
        Example:
            >>> filters = {'model_year': 2020, 'price_max': 50000}
            >>> vehicles = repository.find_by_filters(filters)
        """
        df = self._load_data().copy()
        
        # Aplicar filtros
        if 'model_year' in filters:
            df = df[df['model_year'] == filters['model_year']]
        
        if 'price_min' in filters:
            df = df[df['price'] >= filters['price_min']]
        
        if 'price_max' in filters:
            df = df[df['price'] <= filters['price_max']]
        
        if 'condition' in filters:
            df = df[df['condition'] == filters['condition']]
        
        if 'vehicle_type' in filters:
            df = df[df['type'] == filters['vehicle_type']]
        
        if 'is_4wd' in filters:
            df = df[df['is_4wd'] == filters['is_4wd']]
        
        if 'odometer_max' in filters:
            df = df[df['odometer'] <= filters['odometer_max']]
        
        return self._dataframe_to_entities(df)
    
    def count(self) -> int:
        """
        Cuenta el total de vehículos.
        
        Returns:
            Número total de vehículos
        """
        df = self._load_data()
        return len(df)
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Obtiene estadísticas generales.
        
        Returns:
            Diccionario con estadísticas
        """
        df = self._load_data()
        
        return {
            'total_vehicles': len(df),
            'average_price': float(df['price'].mean()),
            'median_price': float(df['price'].median()),
            'average_odometer': float(df['odometer'].mean()),
            'median_odometer': float(df['odometer'].median()),
            'year_range': (int(df['model_year'].min()), int(df['model_year'].max())),
            'conditions': df['condition'].value_counts().to_dict(),
            'vehicle_types': df['type'].value_counts().to_dict()
        }
