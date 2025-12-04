@echo off
pushd "%~dp0"
echo ========================================
echo   Sistema de Pizzeria - Microservicios
echo ========================================
echo.
echo Iniciando ambos microservicios...
echo.

start "Pedidos" cmd /k "py -m uvicorn services.pedidos.app:app --host 0.0.0.0 --port 8000 --reload"
timeout /t 2 /nobreak >nul

start "Entregas" cmd /k "py -m uvicorn services.entregas.app:app --host 0.0.0.0 --port 8001 --reload"

echo.
echo ========================================
echo  Servicios iniciados:
echo  - Pedidos:  http://localhost:8000
echo  - Entregas: http://localhost:8001
echo.
echo  Documentacion:
echo  - Pedidos:  http://localhost:8000/docs
echo  - Entregas: http://localhost:8001/docs
echo ========================================
echo.
echo Presione cualquier tecla para cerrar los servicios...
pause >nul

taskkill /FI "WindowTitle eq Pedidos*" /T /F >nul 2>&1
taskkill /FI "WindowTitle eq Entregas*" /T /F >nul 2>&1

popd
