# SAE23_Sujet2
Le script SQL permet de créer automatiquement les tables dont on a besoin pour la base de donnée. (exepté les tables crées automatiquement par django






## **Toutes les commandes se font en su -**

apt install -y python3-venv

**//Transférer le repo github au niveau de /home/votreuser/(placer ici)**


**//Dans notre cas**

cd /home/servusr/SAE23_Sujet2

python -m venv django_env

source django_env/bin/activate

apt-get install python3-dev default-libmysqlclient-dev build-essential

**Installer depuis le requirement.txt**

pip install -r requirements.txt


**//Dans votre setting.py ajouter l'IP de votre machine serveur comme ceci: ALLOWED_HOSTS = ['X.X.X.X']
//config gunicorn**

mkdir conf

nano conf/gunicorn_config.py

**//entrer les lignes suivantes**

command = '/home/votreuser/django_env/bin/gunicorn'

pythonpath = '/home/votreuser/SAE23_Sujet2'

bind = 'X.X.X.X:port' *(l'ip de votre machine server, et le port sur lequel vous souhaiter écouter, ici 8000)*

workers = 3

**//Fermer nano**



**//Passons à la config de nginx
//Vérifier que dans votre settings.py le chemin de STATIC soit bien relatif, et qu'il fonctionnait lors de vos tests en local.**

nano /etc/nginx/sites-available/SAE23_Sujet2

server{
	listen 80;
	server_name X.X.X.X;

location /static/ {
	root emplacement_de_votre_dossier_static_en_absolu;
}

location / {
	proxy_pass http://X.X.X.X:port_de_la_config_gunicorn *(ici 8000)*;
	}
}

**//Fermer nano**



cd /etc/nginx/sites-enabled

ln -s /etc/nginx/sites-available/SAE23_Sujet2

systemctl restart nginx

**//enfin on peut lancer le serveur**

cd /home/servusr/SAE23_Sujet2
gunicorn -c conf/gunicorn_config.py SAE23_Sujet2.wsgi

**//Dans votre navigateur tapez http://X.X.X.X:80/filmographie**
