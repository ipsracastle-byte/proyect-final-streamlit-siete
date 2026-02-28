#!/bin/bash

# -----------------------------
# Configuración
# -----------------------------
ENV_NAME="vehicles_env"
PYTHON_BIN="python3"

echo "🚀 Creando entorno virtual..."

# Crear entorno virtual
$PYTHON_BIN -m venv $ENV_NAME

# Activar entorno virtual (solo dentro del script)
source $ENV_NAME/bin/activate

echo "✅ Entorno virtual creado"

# -----------------------------
# Actualizar pip
# -----------------------------
python -m pip install --upgrade pip

# -----------------------------
# Instalar dependencias base
# -----------------------------
pip install pandas numpy matplotlib scipy


# -----------------------------
# para hacer peticiones a la API
# -----------------------------
pip install requests 


# -----------------------------
# para crear aplicaciones web
# -----------------------------
pip install streamlit

# -----------------------------
# para visualizaciones interactivas
# -----------------------------
pip install plotly

# -----------------------------
# para trabajar con notebooks (formato .ipynb)
# -----------------------------
pip install nbformat

# -----------------------------
# para notebooks Jupyter interactivos
# -----------------------------
pip install jupyter ipykernel

# Registrar kernel
python -m ipykernel install --user --name=$ENV_NAME --display-name="Python ($ENV_NAME)"

echo "📓 Jupyter instalado y kernel registrado"

# -----------------------------
# Crear estructura del proyecto
# -----------------------------
echo "📁 Creando estructura del proyecto..."

# Código fuente
mkdir -p src/{models,processing,visualization,utils}

# Datos
mkdir -p data/{raw,processed}

# Otros
mkdir -p notebooks
mkdir -p tests
mkdir -p reports/figures

# -----------------------------
# Archivos base Python
# -----------------------------
touch src/__init__.py
touch src/main.py

touch src/models/__init__.py
touch src/processing/__init__.py
touch src/visualization/__init__.py
touch src/utils/__init__.py

# -----------------------------
# Archivos de proyecto
# -----------------------------
touch README.md
touch requirements.txt
touch .gitignore

# -----------------------------
# Guardar dependencias
# -----------------------------
pip freeze > requirements.txt

# -----------------------------
# .gitignore básico
# -----------------------------
cat <<EOL > .gitignore
# Entorno virtual
venv/

# Python
__pycache__/
*.pyc

# Jupyter
.ipynb_checkpoints/

# Datos crudos
data/raw/
EOL

echo "🎉 Proyecto inicializado correctamente."
echo "👉 Ejecuta: source venv/bin/activate para empezar a trabajar"
