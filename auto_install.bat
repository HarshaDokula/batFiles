@echo off

Title SemiAutoInstaller


echo *******************
echo Semi Auto installer.
echo *******************
echo


for /f  %%i in ('dir /b *exe') do (

call %%i
echo completed %%i

)

pause
exit

