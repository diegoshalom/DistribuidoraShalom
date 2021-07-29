@echo off
c:
cd C:\REPOS\DistribuidoraShalom
copy lastlog.txt previouslog.txt /y
date /t > lastlog.txt 2>&1
time /t >> lastlog.txt 2>&1
echo "Ejecuto python milista.py" >> lastlog.txt 2>&1
python milista.py >> lastlog.txt 2>&1
echo "Ejecuto git pull" >> lastlog.txt 2>&1
echo Escribí "zapato" >con
git pull >> lastlog.txt 2>&1
echo "Ejecuto git pull" >> lastlog.txt 2>&1
echo "Ejecuto git add ."
git add . >> lastlog.txt 2>&1
echo "Ejecuto git commit" >> lastlog.txt 2>&1
git commit -m "test" >> lastlog.txt 2>&1
echo "Ejecuto git push" >> lastlog.txt 2>&1
echo Escribí "zapato" >con 
git push >> lastlog.txt 2>&1
echo "Listo"  >> lastlog.txt  2>&1
time /t >> lastlog.txt 2>&1