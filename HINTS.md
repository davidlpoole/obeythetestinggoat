# Useful Commands and Concepts

*Some of these are from the book, others are my own notes.*

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

## Chapter 12: Tips on Organising Tests and Refactoring

Just as you use multiple files to hold your application code, you should split your tests out into multiple files.

- For functional tests, group them into tests for a particular feature or user story.
- For unit tests, use a folder called tests, with an `__init__.py`
- You probably want a separate test file for each tested source code file. For Django, that’s
  typically `test_models.py`, `test_views.py`, and `test_forms.py`.
- Have at least a placeholder test for every function and class.

## Chapter 14

For more complex forms:

- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [django-floppyforms](https://django-floppyforms.readthedocs.io/en/latest/)

## Chapter 21

### [Setting up SSH key for GitHub on server](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac)

`ssh-keygen -t ed25519 -C "your_email@example.com"`  
`eval "$(ssh-agent -s)"`
`nano ~/.ssh/config`

Add this to the config file:

```
Host github.com
  AddKeysToAgent yes
  IdentityFile ~/.ssh/id_ed25519
```

`ssh-add ~/.ssh/id_ed25519`  
`cat ~/.ssh/id_ed25519.pub`  
copy this to GitHub settings.

### Running the functional tests against the staging server

`STAGING_SERVER=davidpoole.pythonanywhere.com python manage.py test functional_tests`