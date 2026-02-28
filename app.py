"""
Punto de entrada principal para la aplicación Streamlit.

Este archivo es un wrapper que ejecuta la aplicación principal
ubicada en src/interfaces/streamlit_app/app.py

Para ejecutar:
    streamlit run app.py
"""

import sys
from pathlib import Path

# Agregar src al path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Importar y ejecutar la aplicación principal
from src.interfaces.streamlit_app.app import main

if __name__ == '__main__':
    main()
