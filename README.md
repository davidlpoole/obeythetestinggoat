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

- Install Firefox (as per book)
- Install Git (as per book)
- Install Python 3.11 from [Python.org](https://www.python.org/downloads/)
- Install pipenv (`pip3 install pipenv`) (_instead of using virtualenv_)
- `pipenv install django selenium` (latest versions which are django 4.2.1, selenium 4.9.1)
- Download [Geckodriver](https://github.com/mozilla/geckodriver/releases) and move to /usr/local/bin/

## [Chapter 01: Getting Django Set Up Using a Functional Test](https://www.obeythetestinggoat.com/book/chapter_01.html)

### [Obey the Testing Goat! Do Nothing Until You Have a Test](https://www.obeythetestinggoat.com/book/chapter_01.html#_obey_the_testing_goat_do_nothing_until_you_have_a_test)

*functional_tests.py*  
~~`assert 'Django' in browser.title`~~  
`assert 'The install worked successfully' in browser.title`

### [Getting Django Up and Running](https://www.obeythetestinggoat.com/book/chapter_01.html#_getting_django_up_and_running)

$~~`django-admin.py startproject superlists .`~~  
$`django-admin startproject superlists .`

## [Chapter 02: Extending Our Functional Test Using the unittest Module](https://www.obeythetestinggoat.com/book/chapter_02_unittest.html)

No code changes required.

## [Chapter 03: Testing a Simple Home Page with Unit Tests](https://www.obeythetestinggoat.com/book/chapter_unit_test_first_view.html)

### [urls.py](https://www.obeythetestinggoat.com/book/chapter_unit_test_first_view.html#_urls_py)

The way the URL dispatcher works in the book examples compared to Django 4.2 has changed, see
the [Django 4.2 URL dispatcher docs](https://docs.djangoproject.com/en/4.2/topics/http/urls/#url-dispatcher)

*superlists/urls.py:*  
~~`url(r'^$', views.home_page, name='home'),`~~  
`path('', views.home_page, name='home')`

## [Chapter 04: What Are We Doing with All These Tests? (And, Refactoring)](https://www.obeythetestinggoat.com/book/chapter_philosophy_and_refactoring.html)

### [Using Selenium to Test User Interactions](https://www.obeythetestinggoat.com/book/chapter_philosophy_and_refactoring.html#_using_selenium_to_test_user_interactions)

The `.find_element_by_id()` and `.find_element_by_tag_name()` methods need to be replaced with:  
`.find_element(by=['id'|'tag name'], value='id|name')` as follows.

*/lists/tests.py:*  
~~`header_text = self.browser.find_element_by_tag_name('h1').text`~~   
`header_text = self.browser.find_element(by='tag name', value='h1').text`

~~`inputbox = self.browser.find_element_by_id('id_new_item')`~~  
`input_box = self.browser.find_element(by='id', value='id_new_item')`

~~`table = self.browser.find_element_by_id('id_list_table')`~~  
`table = self.browser.find_element(by='id', value='id_list_table')`

~~`rows = table.find_elements_by_tag_name('tr')`~~  
`rows = table.find_elements(by='tag name', value='tr')`

Note, I named the `inputbox` variable with an underscore `input_box` to keep it consistent with the
previous `header_text`
variable.  
Also, there's a `.find_elements()` method, not used here, which can be used in place of `.find_elements_by_id()` and
`.find_elements_by_tag_name()`

## [Chapter 05: Saving User Input: Testing the Database](https://www.obeythetestinggoat.com/book/chapter_post_and_database.html)

No code changes required, except for `.find_elements_by_id()` as per chapter 04 above

## [Chapter 06: Improving Functional Tests: Ensuring Isolation and Removing Voodoo Sleeps](https://www.obeythetestinggoat.com/book/chapter_explicit_waits_1.html)

No code changes required.

## [Chapter 07: Working Incrementally](https://www.obeythetestinggoat.com/book/chapter_working_incrementally.html)

### [Taking a First, Self-Contained Step: One New URL](https://www.obeythetestinggoat.com/book/chapter_working_incrementally.html#_taking_a_first_self_contained_step_one_new_url)

#### A New URL

*/superlists/urls.py:*  
~~`url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list'),`~~  
`path('lists/the-only-list-in-the-world/', views.view_list, name='view_list'),`

### [Biting the Bullet: Adjusting Our Models](https://www.obeythetestinggoat.com/book/chapter_working_incrementally.html#_biting_the_bullet_adjusting_our_models)

#### A Foreign Key Relationship

`on_delete` is now a required named parameter to `models.ForeignKey()`

*/lists/models.py:*  
~~`list = models.ForeignKey(List, default=None)`~~  
`list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)`

I've used `models.CASCADE` which will delete the `item` when it's `list` is deleted.  
See the other available options in
the [Django 4.2 docs: ForeignKey.on_delete](https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ForeignKey.on_delete)

### [Each List Should Have Its Own URL](https://www.obeythetestinggoat.com/book/chapter_working_incrementally.html#_each_list_should_have_its_own_url)

#### Capturing Parameters from URLs

The url dispatcher code has changed since the book example was written (as noted in Chapter 03)

*/superlists/urls.py:*  
~~`url(r'^lists/(.+)/$', views.view_list, name='view_list'),`~~  
`path("lists/<int:id>/", views.view_list, name='view_list'),`

### [One More View to Handle Adding Items to an Existing List](https://www.obeythetestinggoat.com/book/chapter_working_incrementally.html#_one_more_view_to_handle_adding_items_to_an_existing_list)

#### Beware of Greedy Regular Expressions!

Because the URL dispatcher is different now, the last change to */superlists/urls.py* doesn't use the same regular
expressions, and is not susceptible to this problem, so we can skip this section as we receive the error 404 already.

#### The Last New URL

*/superlists/urls.py:*  
~~`url(r'^lists/(\d+)/add_item$', views.add_item, name='add_item'),`~~  
`path("lists/<int:list_id>/add_item", views.add_item, name='add_item'),`

## [Chapter 08: Prettification: Layout and Styling, and What to Test About It](https://www.obeythetestinggoat.com/book/chapter_prettification.html)

No code changes required.

## Chapters 09, 10, 11: Staging site, Production-Ready Deployment, Automating Deployment with Fabric

I skimmed through these chapters, and ended up [deploying my app](http://davidpoole.pythonanywhere.com/)
on [PythonAnywhere](https://www.pythonanywhere.com), which was probably a lot simpler - I just started with
PythonAnywhere's Django template and replaced the code with the code from this repo. There was a slightly different
process for getting the environment variables set up, but I followed the instructions in PA's help, and got it working.

## [Chapter 12: Splitting Our Tests into Multiple Files, and a Generic Wait Helper](https://www.obeythetestinggoat.com/book/chapter_organising_test_files.html)

> #### Set of supported locator strategies (for `find_element()` and `find_elements()`):
> - "id"
> - "xpath"
> - "link text"
> - "partial link text"
> - "name"
> - "tag name"
> - "class name"
> - "css selector"

*functional_tests/test_list_item_validation.py:*  
~~`self.browser.find_element_by_css_selector('.has-error').text,`~~  
`self.browser.find_element(by='css selector', value='.has-error'),`

## [Chapter 13: Validation at the Database Layer](https://www.obeythetestinggoat.com/book/chapter_database_layer_validation.html)

No code changes required.

## [Chapter 14: A Simple Form](https://www.obeythetestinggoat.com/book/chapter_simple_form.html)

No code changes required.