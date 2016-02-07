# Flask-Skeleton
Adds basic JWT based user auth and sessions to Flask

## Production

### Requirements
* Python 3.4+
* VirtualEnv 12.1+

### Install
```
./install.sh
```

### Run
```
./run.sh
```

## Development

### Requirements
* Python 3.4+
* VirtualEnv 12.1+
* NPM 2.8+
* Node 0.12+
* Grunt-CLI 0.1.13+
* Ruby 2.2+
* Nginx (optional)

### Install
```
./install-dev.sh
```
Nginx config:
```
user www-data; # Nginx will be ran by this user, should NOT be root
worker_processes 4; # Number of core on the machine
pid /run/nginx.pid;

events {
    worker_connections 8096;
    multi_accept on;
    use epoll;
}

worker_rlimit_nofile 40000;

http {
    sendfile           on;
    tcp_nopush         on;
    tcp_nodelay        on;
    keepalive_timeout  15;

    server {
        listen 80;
        server_name test.flaskskeleton.com;

        location / {
            proxy_pass http://127.0.0.1:8333; 
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}

``` 

Nginx is used to better simulate the production environment, completely optional of course.

### Run
```
./run-dev.sh
```

### Assets compilation

Watches for modifications in assets:
```
grunt
```


### Creating Database

```
env/bin/python manage.py shell

# From the Flask shell

from app.config.config import *
db.create_all()
```