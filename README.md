# Tasks

## Follow the installation steps

1. Clone the repository:

```bash
git clone https://github.com/pankajsajekar/CatalystMediaTask.git
```

## A. Setup Project
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