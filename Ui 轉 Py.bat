@echo off
:: �ˬd�O�_���ѤF���
if "%~1"=="" (
    echo �бN�n�ഫ�� .ui �����즹 BAT ���C
    pause
    exit /b 1
)

:: ���������|�M���W
set "filepath=%~1"
set "filename=%~n1"
set "extension=%~x1"

:: �ˬd����X�i�W�O�_�� .ui
if /i not "%extension%"==".ui" (
    echo �д��Ѥ@�� .ui ���C
    pause
    exit /b 1
)

:: �ϥ� pyuic6 �i���ഫ
pyuic6 -x "%filepath%" -o "%filename%.py"

echo ���w�ഫ�G%filename%.py
