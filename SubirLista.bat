c:
cd C:\REPOS\DistribuidoraShalom
copy lastlog.txt previouslog.txt /y
copy \\WIN32VIRTUAL\qb45\TEXTO.TXT . /y
date /t > lastlog.txt
time /t >> lastlog.txt
echo Ejecuto python milista.py >> lastlog.txt
python milista.py >> lastlog.txt
echo Ejecuto git pull >> lastlog.txt
git pull >> lastlog.txt
echo Ejecuto git add .
git add . >> lastlog.txt
echo Ejecuto git commit >> lastlog.txt
git commit -m "test" >> lastlog.txt
echo Ejecuto git push >> lastlog.txt
git push >> lastlog.txt 
echo Listo  >> lastlog.txt
time /t >> lastlog.txt