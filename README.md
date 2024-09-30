# Tasks

## Follow the installation steps

1. Clone the repository:

```bash
git clone https://github.com/pankajsajekar/CatalystMediaTask.git
```

## A. Setup Django Server
1. change dir
```
cd CatalystMediaTask
```

2. Create a virtual environment
```
python -m venv venv

```
3. Activate virtual environment
```
command - .\venv\Scripts\activate
```
4. Install packages from requirements file
```
pip install -r requirements.txt
```

6. Create Database 
```
python manage.py makemigrations
python manage.py migrate
```
7. Run server
```
python manage.py runserver
```

8. Createsuper user
```
python manage.py createsuperuser
```


## B. Setup Celery 
#### Open new terminal & run this command

```bash
celery -A CatalystMediaTask worker -l INFO
```

Need venv activated


## C. Setup WebSocket 
#### Open new terminal & run this command
```bash
python ws_server.py
```

Requirements for executing tasks:
- RAM: minimum of 16 GB
- Processor: Intel Core i5