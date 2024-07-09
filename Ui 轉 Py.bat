@echo off
:: 檢查是否提供了文件
if "%~1"=="" (
    echo 請將要轉換的 .ui 文件拖放到此 BAT 文件。
    pause
    exit /b 1
)

:: 提取文件路徑和文件名
set "filepath=%~1"
set "filename=%~n1"
set "extension=%~x1"

:: 檢查文件擴展名是否為 .ui
if /i not "%extension%"==".ui" (
    echo 請提供一個 .ui 文件。
    pause
    exit /b 1
)

:: 使用 pyuic6 進行轉換
pyuic6 -x "%filepath%" -o "%filename%.py"

echo 文件已轉換：%filename%.py
