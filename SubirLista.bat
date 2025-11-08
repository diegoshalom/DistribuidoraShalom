c:
cd C:\REPOS\DistribuidoraShalom
copy c:\qb45\TEXTO.TXT . /y
date /t > lastlog.txt
time /t >> lastlog.txt
echo Ejecuto python milista.py >> lastlog.txt
path = C:\Users\Elias y Pochi\AppData\Local\Programs\Python\Python313-32\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\Git\cmd;C:\Users\Elias y Pochi\AppData\Local\Programs\Python\Launcher\;C:\Users\Elias y Pochi\AppData\Local\Microsoft\WindowsApps;
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