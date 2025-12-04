@echo off
pushd "%~dp0"
echo ========================================
echo  Iniciando Microservicio de ENTREGAS
echo ========================================
echo.
echo Servicio disponible en: http://localhost:8001
echo Documentacion en: http://localhost:8001/docs
echo.
py -m uvicorn services.entregas.app:app --host 0.0.0.0 --port 8001 --reload

popd
