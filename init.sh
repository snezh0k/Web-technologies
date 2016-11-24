sudo rm /etc/nginx/nginx.conf
sudo rm /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart
sudo gunicorn hello:app -c /etc/gunicorn.d/hello.py
