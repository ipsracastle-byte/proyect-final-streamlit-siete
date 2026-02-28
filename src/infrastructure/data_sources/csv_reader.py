"""
Lector de archivos CSV.

Maneja la lectura de archivos CSV y retorna DataFrames.
"""

import pandas as pd
from pathlib import Path
from typing import Optional
from src.shared.exceptions import DataSourceError


class CSVReader:
    """
    Lee archivos CSV y retorna DataFrames.
    
    Esta clase encapsula la lógica de lectura de archivos CSV,
    incluyendo validación y manejo de errores.
    """
    
    def __init__(self, file_path: str):
        """
        Inicializa el lector CSV.
        
        Args:
            file_path: Ruta al archivo CSV
        
        Raises:
            DataSourceError: Si el archivo no existe
        """
        self._file_path = Path(file_path)
        self._validate_file()
    
    def _validate_file(self) -> None:
        """
        Valida que el archivo existe y es accesible.
        
        Raises:
            DataSourceError: Si el archivo no existe o no es accesible
        """
        if not self._file_path.exists():
            raise DataSourceError(f"Archivo no encontrado: {self._file_path}")
        
        if not self._file_path.is_file():
            raise DataSourceError(f"La ruta no es un archivo: {self._file_path}")
        
        if self._file_path.suffix.lower() != '.csv':
            raise DataSourceError(f"El archivo no es un CSV: {self._file_path}")
    
    def read(self, **kwargs) -> pd.DataFrame:
        """
        Lee el archivo CSV.
        
        Args:
            **kwargs: Argumentos adicionales para pd.read_csv
        
        Returns:
            DataFrame con los datos del CSV
        
        Raises:
            DataSourceError: Si hay un error al leer el archivo
        
        Example:
            >>> reader = CSVReader('data/vehicles.csv')
            >>> df = reader.read()
            >>> print(len(df))
            51525
        """
        try:
            df = pd.read_csv(self._file_path, **kwargs)
            return df
        except Exception as e:
            raise DataSourceError(f"Error al leer CSV: {e}")
    
    def get_file_info(self) -> dict:
        """
        Obtiene información sobre el archivo.
        
        Returns:
            Diccionario con información del archivo
        """
        return {
            'path': str(self._file_path),
            'size_mb': self._file_path.stat().st_size / (1024 * 1024),
            'exists': self._file_path.exists()
        }
