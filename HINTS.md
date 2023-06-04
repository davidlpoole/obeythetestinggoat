# Useful Commands and Concepts

## Chapter 01

### Initialise a Django project

$`django-admin.py startproject projectname .`

### Running the Django dev server

$`python manage.py runserver`

## Chapter 02

### View changes since last commit

$`git diff`

### View commit history

$`git log --all --decorate --oneline --graph`

### Undo the last commit

$`git reset HEAD~`

## Chapter 03

### Create an app in the Django project

$`python manage.py startapp appname`

### Running the functional tests

$`python functional_tests.py`

### Running the unit tests

$`python manage.py test`

### The unit-test/code cycle

    Run the unit tests in the terminal.
    Make a minimal code change in the editor.
    Repeat!

## Chapter 05

### build the database migrations based on models

$`python manage.py makemigrations`

### apply migrations to db

$`python manage.py migrate`

## Chapter 06

### To run all tests

$`python manage.py test`

### To run the functional tests

$`python manage.py test functional_tests`

### To run the unit tests

$`python manage.py test lists`

## Chapter 07

### Undo last git commit but keep changes (changes become un-staged)

$`git reset HEAD^`

### Use grep to summarise a file to classes and functions

$`grep -E "class|def" lists/tests.py`