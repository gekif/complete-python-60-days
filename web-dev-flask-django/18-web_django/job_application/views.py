from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == "POST":

        form = ApplicationForm(request.POST or None)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation,
            )

            messages.success(request, "Application submitted successfully!")

            message_body = f"New job application received:\n\nName: {first_name} {last_name}\nEmail: {email}\nDate: {date}\nOccupation: {occupation}"
            email_message = EmailMessage(
                subject="New Job Application",
                body=message_body,
                to=[email]
            )
            email_message.send()
            return redirect("/")

    else:
        form = ApplicationForm()

    return render(request, "index.html", {"form": form})