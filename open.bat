@echo off
setlocal

rem Specify the path to the directory you want to open
set DirectoryPath="D:\Development\PYTHON\DSA Python - Coding Ninja"

rem Change to the directory
cd %DirectoryPath%

rem Open Visual Studio Code in the current directory
code .

endlocal
