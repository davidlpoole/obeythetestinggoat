# Useful Commands and Concepts

## Chapter 1

### Initialise a Django project

`django-admin.py startproject projectname .`

### Running the Django dev server

`python manage.py runserver`

## Chapter 2

### View changes since last commit

`git diff`

### View commit history

`git log --all --decorate --oneline --graph`

### Undo the last commit

`git reset HEAD~`

## Chapter 3

### Create an app in the Django project

`python manage.py startapp appname`

### Running the functional tests

`python functional_tests.py`

### Running the unit tests

`python manage.py test`

### The unit-test/code cycle

    Run the unit tests in the terminal.
    Make a minimal code change in the editor.
    Repeat!
