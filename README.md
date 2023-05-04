### Repository Description
### Developement mode

Prerequisites:
- npm
- python
- vue
- [MySQL](https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html)
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)

### DB

Open MySQL Workbench and create an sql script. Add the following code

~~~~mysql
create schema if not exists activities;
~~~~

After creating the database schema you have to set two environmental variables, being the credentials of the database (i.e. username, password).

```
setx DB_USER your_username
setx DB_PASSWORD your_password
```

After installing the requirements for the rep-backend and creating the activities database tables using applications.py, as mentioning below we add data to the database using the following commands:

```
cd db/py-scripts
python3 addInfoDb.py
```

### rep-backend

```
# check that the password defined if file "Activities-Repository/rep-backend/surveyapi/config.py" is the same with the mysql user you use to connect to mysql
cd rep-backend
python3 -m venv venv
cd venv/Scripts
activate.bat
cd ../..
pip3 install -r requirements.txt
cd surveyapi
python3 applications.py
```
### rep-frontend

```
cd rep-frontend
npm install  # only the first time for installing dependencies
npm i quasar # only the first time to install quasar
npm i @quasar/cli # only the first time to install quasar
quasar dev
```


