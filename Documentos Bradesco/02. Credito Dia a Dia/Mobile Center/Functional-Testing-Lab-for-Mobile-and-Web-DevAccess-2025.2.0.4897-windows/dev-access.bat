@echo off
SET PWD=%~dp0
IF "%PWD:~-1%"=="\" SET PWD=%PWD:~0,-1%
"%PWD%"\jre\bin\java %DEBUG_OPT% %LOCAL_OPT% -Ddevplay.home="%PWD%" -jar "%PWD%"\dev-access.jar
