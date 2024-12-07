from django.shortcuts import render, redirect
from .forms import ApplicationForm  # the . implies we are importing from the directory
from .models import Form
from django.contrib import messages


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # connecting database
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            messages.success(request, "Form submitted successfully")

            # Redirect to the same page after form submission to prevent duplicate submission
            return redirect('index')  # Replace 'index' with the appropriate URL name if needed
    return render(request, "index.html")
