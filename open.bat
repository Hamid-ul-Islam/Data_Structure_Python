@echo off


rem Specify the path to the directory you want to open
set DirectoryPath="D:\Development\PYTHON\DSA Python - Coding Ninja"

rem Change to the directory
cd /d %DirectoryPath%

rem Open Visual Studio Code in the current directory and start it in a new window
start code .

endlocal
