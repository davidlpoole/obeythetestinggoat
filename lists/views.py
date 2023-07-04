from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect, render

from lists.forms import ExistingListItemForm, ItemForm, NewListForm
from lists.models import List

User = get_user_model()


def home_page(request):
    return render(request, "home.html", {"form": ItemForm()})


def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, "home.html", {"form": form})


def view_list(request, list_id):
    try:
        list_ = List.objects.get(id=list_id)
    except List.DoesNotExist:
        return HttpResponseNotFound(f"Error: Can't find list {list_id}...")
    if list_.owner is not None and list_.owner != request.user:
        return HttpResponseForbidden(
            "Error: That's not your list, or you're not logged in."
        )
    form = ExistingListItemForm(for_list=list_)
    if request.method == "POST":
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, "list.html", {"list": list_, "form": form})


def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, "my_lists.html", {"owner": owner})


def public_lists(request):
    lists = List.objects.filter(owner=None)
    return render(request, "public_lists.html", {"lists": lists})
