"""
Excepciones personalizadas para el dominio de vehículos.

Este módulo define todas las excepciones específicas del dominio
que pueden ser lanzadas durante la ejecución de la aplicación.
"""


class VehicleException(Exception):
    """Excepción base para errores relacionados con vehículos."""
    pass


class VehicleNotFoundError(VehicleException):
    """Se lanza cuando no se encuentra un vehículo."""
    
    def __init__(self, vehicle_id: str):
        self.vehicle_id = vehicle_id
        super().__init__(f"Vehículo con ID '{vehicle_id}' no encontrado")


class ValidationError(VehicleException):
    """Se lanza cuando la validación de datos falla."""
    pass


class RepositoryError(VehicleException):
    """Se lanza cuando hay un error en el repositorio."""
    pass


class DataSourceError(VehicleException):
    """Se lanza cuando hay un error al acceder a la fuente de datos."""
    pass
