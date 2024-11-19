@echo off
IF EXIST ".\env" (
    CALL .\env\Scripts\activate.bat
    ECHO Dependencies already installed
) ELSE (
    ECHO Installing Dependencies this may take a few minutes...
    CALL python -m venv env
    CALL .\env\Scripts\activate.bat
    CALL pip install -r requirements.txt
    ECHO Dependencies successfully installed
)