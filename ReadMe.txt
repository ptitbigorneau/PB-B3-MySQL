PB_B3MySQL v b2.0 (PtitBigorneau www.ptitbigorneau.fr)
##############################################################
BigBrotherBot(b3) www.bigbrotherbot.net 

Permet de créer votre base de donnée mysql pour b3

pb_b3mysql a besoin de MySQL pour fonctionner

sous Linux (Debian)

Installer mysql-server et pymysql:

apt-get install mysql-server
mysql_secure_installation

apt-get install python-dev python-pip
pip install pymysql

Sous Windows

Télécharger et installer MySQL:

 -> http://dev.mysql.com/downloads/mysql/
 
Installer pymysql:
python -m pip install pymysql

et rajouter la variable Path dans les variables d'environnement

   Exemple:
   --------
   Variable: PATH
   Valeur : C:\Program Files\MySQL\MySQL Server 5.6\bin
  
