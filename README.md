# Obeying The Testing Goat in 2023... with the latest versions of Python (3.11), Django (4.2), and Selenium (4.9)

## About this project

The goal of this project is to follow along with the tutorials in the book:
"Test-Driven Development with Python, 2nd Edition" by Harry Percival, which is available for free online
at  [www.obeythetestinggoat.com](https://www.obeythetestinggoat.com/pages/book.html#toc), however the example code uses
old versions of python, django and selenium, and the book discourages trying to use newer versions. But because I don't
do what I'm told, I've decided to document the changes required to bring run the code with the latest versions as of
June 2023. This readme file will describe just the amendments, and the code will be available in full in the repository,
with branches for each Chapter.

## [Prerequisites and Assumptions](https://www.obeythetestinggoat.com/book/pre-requisite-installations.html)

- Install Firefox
- Install Git
- Install Python 3.11 from [Python.org](https://www.python.org/downloads/)
- Install pipenv (`pip3 install pipenv`)
- `pipenv install django selenium` (latest versions which are django 4.2.1, selenium 4.9.1)
- Download [Geckodriver](https://github.com/mozilla/geckodriver/releases) and move to /usr/local/bin/

## [Chapter 01: Getting Django Set Up Using a Functional Test](https://www.obeythetestinggoat.com/book/chapter_01.html)

### [Obey the Testing Goat! Do Nothing Until You Have a Test](https://www.obeythetestinggoat.com/book/chapter_01.html#_obey_the_testing_goat_do_nothing_until_you_have_a_test)

*functional_tests.py*  
~~`assert 'Django' in browser.title`~~  
`assert 'The install worked successfully' in browser.title`

### [Getting Django Up and Running](https://www.obeythetestinggoat.com/book/chapter_01.html#_getting_django_up_and_running)

~~`django-admin.py startproject superlists .`~~  
`django-admin startproject superlists .`

## [Chapter 02: Extending Our Functional Test Using the unittest Module](https://www.obeythetestinggoat.com/book/chapter_02_unittest.html)

No code changes required.

## [Chapter 03: Testing a Simple Home Page with Unit Tests](https://www.obeythetestinggoat.com/book/chapter_unit_test_first_view.html)
