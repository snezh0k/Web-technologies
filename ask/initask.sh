sudo rm /etc/nginx/nginx.conf
sudo rm /etc/gunicorn.d/qa.py
sudo ln -s /home/box/web/etc/qa.py /etc/gunicorn.d/qa.py
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart
sudo gunicorn -c ../etc/qa.py ask.wsgi
