"""
Script de prueba para verificar la instalación de plotly y nbformat.

Este script verifica que las librerías están correctamente instaladas
y pueden ser importadas sin errores.
"""

import sys


def test_plotly():
    """Prueba la instalación de Plotly."""
    try:
        import plotly
        import plotly.express as px
        import plotly.graph_objects as go
        
        print("✅ Plotly instalado correctamente")
        print(f"   Versión: {plotly.__version__}")
        
        # Crear un gráfico simple de prueba
        fig = px.scatter(x=[1, 2, 3], y=[4, 5, 6], title="Test Plotly")
        print("   ✓ Gráfico de prueba creado exitosamente")
        
        return True
    except ImportError as e:
        print(f"❌ Error al importar Plotly: {e}")
        return False
    except Exception as e:
        print(f"❌ Error al usar Plotly: {e}")
        return False


def test_nbformat():
    """Prueba la instalación de nbformat."""
    try:
        import nbformat
        from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
        
        print("\n✅ nbformat instalado correctamente")
        print(f"   Versión: {nbformat.__version__}")
        
        # Crear un notebook simple de prueba
        nb = new_notebook()
        nb.cells.append(new_markdown_cell('# Test Notebook'))
        nb.cells.append(new_code_cell('print("Hello, World!")'))
        print("   ✓ Notebook de prueba creado exitosamente")
        
        return True
    except ImportError as e:
        print(f"❌ Error al importar nbformat: {e}")
        return False
    except Exception as e:
        print(f"❌ Error al usar nbformat: {e}")
        return False


def test_other_libraries():
    """Prueba otras librerías importantes del proyecto."""
    libraries = {
        'pandas': 'pd',
        'numpy': 'np',
        'matplotlib.pyplot': 'plt',
        'scipy': 'scipy',
        'requests': 'requests',
        'streamlit': 'st'
    }
    
    print("\n📦 Verificando otras librerías:")
    all_ok = True
    
    for lib_name, alias in libraries.items():
        try:
            lib = __import__(lib_name.split('.')[0])
            version = getattr(lib, '__version__', 'N/A')
            print(f"   ✅ {lib_name:25} v{version}")
        except ImportError:
            print(f"   ❌ {lib_name:25} NO INSTALADO")
            all_ok = False
    
    return all_ok


def main():
    """Función principal que ejecuta todas las pruebas."""
    print("=" * 70)
    print("🧪 VERIFICACIÓN DE LIBRERÍAS - vehicles_env")
    print("=" * 70)
    
    # Mostrar información del entorno
    print(f"\n🐍 Python: {sys.version}")
    print(f"📍 Ejecutable: {sys.executable}")
    
    print("\n" + "-" * 70)
    print("PRUEBAS DE LIBRERÍAS NUEVAS")
    print("-" * 70)
    
    # Probar las librerías nuevas
    plotly_ok = test_plotly()
    nbformat_ok = test_nbformat()
    
    print("\n" + "-" * 70)
    print("VERIFICACIÓN DE LIBRERÍAS EXISTENTES")
    print("-" * 70)
    
    # Probar otras librerías
    others_ok = test_other_libraries()
    
    # Resumen final
    print("\n" + "=" * 70)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 70)
    
    results = {
        'Plotly': plotly_ok,
        'nbformat': nbformat_ok,
        'Otras librerías': others_ok
    }
    
    for name, status in results.items():
        icon = "✅" if status else "❌"
        print(f"{icon} {name}: {'OK' if status else 'FALLÓ'}")
    
    all_passed = all(results.values())
    
    if all_passed:
        print("\n🎉 ¡Todas las pruebas pasaron exitosamente!")
        print("✅ El entorno está listo para usar")
    else:
        print("\n⚠️  Algunas pruebas fallaron")
        print("❌ Revisa los errores arriba")
        sys.exit(1)
    
    print("=" * 70)


if __name__ == '__main__':
    main()
