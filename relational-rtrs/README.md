# Realtime Recommendation System based on relational databases

This folder contains mysql based real time recommendation system implementation
using python as the programming language.


## Setup

First install mysql:

```bash
sudo apt install mysql-server
```

Follow the instructions and remember the password you set for root. Then secure the installation by
running

```bash
sudo mysql_secure_installation
```

Make sure mysql is running

```bash
sudo service mysql start
```

Then login into mysql using admin (root)

```bash
sudo mysql -u root -p
```

When asked for password, give password for root that you provided during mysql installation.
After that you're logged into MySQL CLI, create database and user here.

```sql
create database movies_db;
grant all privileges on movies_db.* to anum@localhost identified by 'pakistan';
```

Then press Ctrl+D to exit mysql prompt and confirm that you can login using the new user:

```bash
mysql movies_db -u anum -ppakistan
```

Then press Ctrl+D again to exit

Now create tables in the DB by executing the db_setup.sql file against the database.

```bash
mysql movies_db -u anum -ppakistan < db_setup.sql
```

