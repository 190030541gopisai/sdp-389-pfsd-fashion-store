# Fashion Shopping System



#### if you use linux use below command to activate virtual environment
```
source venv2/bin/activate
```
#### For windows you can activate the virtual enviroment using below command 
```
venv\Scripts\activate
```

To list the all available packages in your virtual environment
pip list


## Installing packages
```
 pip3 install django==2.1.0  &&
 pip install django-crispy-forms &&
 pip install pillow &&
 pip install mysqlclient 
```

## Migrate Before Running server
```
python manage.py makemigrations &&
python manage.py migrate
```

## Running Server
```
python manage.py runserver
```

## If you want to deploy to the server Like Amazon - EC2
below command makes the server not to go into sleep even if you close the server and keep it running
```
screen -d -m python manage.py runserver 0.0.0.0:8000
```
