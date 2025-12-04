@echo off
pushd "%~dp0"
echo ========================================
echo  Iniciando Microservicio de PEDIDOS
echo ========================================
echo.
echo Servicio disponible en: http://localhost:8000
echo Documentacion en: http://localhost:8000/docs
echo.
py -m uvicorn services.pedidos.app:app --host 0.0.0.0 --port 8000 --reload

popd
