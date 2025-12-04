@echo off
echo ========================================
echo   Pruebas del Sistema de Pizzeria
echo ========================================
echo.

echo Instalando dependencias...

py -m pip install -r requirements.txt
echo.

echo Ejecutando pruebas del microservicio de PEDIDOS...
py -m pytest tests/test_main.py -v
echo.

echo Ejecutando pruebas del microservicio de ENTREGAS...
py -m pytest tests/test_entregas.py -v
echo.

echo Ejecutando TODAS las pruebas...
py -m pytest -v
echo.

echo ========================================
echo   Pruebas completadas
echo ========================================
pause

