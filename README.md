# SFL_takehome

This is a takehome assignment from SFL Scientific, where I was tasked to populate a database of my choice with a given csv file.

## Dependencies

This repo uses SQLalchemy and ipadress (a standard library after python 3.3). A python virtual environment is set up for this repo, see Python Virtual Environment.

## Approach

I decided to use SQLite, a database I have never used before. I created the sfl_db.db via the sqlite3 command line, then used db_init.py to initiate the database with tables needed, as well as initializing SQLalchemy engine and metadata. Lastly, I populate the database with populate_data.py, with proper transaction and duplicate prevention in place. The populate python file also uses utility functions from the util.py.

## Check

For a quick check of the result generated, run scratch.py for diplaying all user information in the db.

## Python Virtual Environment

### Python Virtual Environment

Python has a built-in virtual environment(venv) that this repo supports. To get started with venv, while at the repo's directory, run
```
python -m venv venv
```

This will generate a directory called venv containing necessary components to initiate the venv. To initiate the venv, run

Windows

```
venv\scripts\activate.bat
```
Linux

```
source venv/bin/activate.bat
```

The venv prefix indicates that you have entered python venv. To install all the dependencies while in the venv, while at the repo's directory, run

```
pip install -r requirements.txt
```

After installing the required dependencies you should be able to run scripts in this repo.