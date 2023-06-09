from django.contrib import auth, messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import Token


def send_login_email(request):
    email = request.POST["email"]
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(reverse("login") + "?token=" + str(token.uid))
    message_body = (
        f"Here's your personal login link:\n{url}\n"
        # f"Use this link whenever you want to sign in, "
        # f"maybe add it to your browser's bookmarks."
    )
    send_mail(
        "Your login link for Superlists",
        message_body,
        "noreply@superlists",
        [email],
    )
    messages.success(
        request, "Check your email, we've sent you a link you can use to log in."
    )
    return redirect("/")


def login(request):
    user = auth.authenticate(uid=request.GET.get("token"))
    if user:
        auth.login(request, user)
    return redirect("/")
