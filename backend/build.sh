echo "Building the project..."
python3.9 -m pip install -r requirements.txt

echo "Making Migrations..."
#python3.9 manage.py makemigrations --noinput
#python3.9 manage.py migrate --noinput
python3.9 manage.py makemigrations
python3.9 manage.py migrate

echo "Collecting Static..."
#python3.9 manage.py collectstatic --noinput --clear
python3.9 manage.py collectstatic
