@echo off
c:
cd C:\REPOS\DistribuidoraShalom
copy lastlog.txt previouslog.txt /y
date /t > lastlog.txt
time /t >> lastlog.txt
echo Ejecuto python milista.py >> lastlog.txt
python milista.py >> lastlog.txt
echo Ejecuto git pull >> lastlog.txt
echo Escribir "zapato" 
git pull >> lastlog.txt
echo Ejecuto git add .
git add . >> lastlog.txt
echo Ejecuto git commit >> lastlog.txt
git commit -m "test" >> lastlog.txt
echo Ejecuto git push >> lastlog.txt
echo Escribir "zapato" 
git push >> lastlog.txt 
echo Listo  >> lastlog.txt
time /t >> lastlog.txt