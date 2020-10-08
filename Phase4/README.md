# Requirements

* MySQL >=5.5
* Python3 >=3.5
* PyMySQL
```
pip install PyMySQL
```
* prettytable
```
pip install prettytable
```

# Instructions

1. Make sure you are in the folder.
2. Run your MySQL server. Now run the following to import the database.
```sql
source Dump.sql;
```
3. Exit MySQL.
4. The python file is configured for the Docker setup as instructed to us. 
Due to this, you may have to make changes in the host and/or port arguments.
```python
con = pymysql.connect(
            host="localhost",  # OR set appropriate host
            user=username,
            password=password,
            db="Restaurant_Ratings",  # Name of our Database
            cursorclass=pymysql.cursors.DictCursor,
            port=5005,  # Since our docker container hosts mysql server at this port
        )
```
5. Now you are all set to run the file! Run in terminal:
```
python ui.py
```
