# Installs the database packages
python -m pip install mysql-connector
python -m pip install pymongo

echo 'Creating SQLDatabase'
python ./SQLSetup.py
echo 'Finished creating SQLDatabase'