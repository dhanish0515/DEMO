from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from feedback_app.forms import FeedbackForm
from feedback_app.models import Feedback


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})


def show_feedback(request):
    form = Feedback.objects.all()
    context = {
        'form': form
    }
    return render(request, 'data_all.html', context)


def edit_feedback(request, pk):
    edits = Feedback.objects.get(pk=pk)
    form = FeedbackForm(instance=edits)
    return render(request, 'feedback_form.html', {'form': form})


def delete_feedback(request, pk):
    remove = Feedback.objects.get(pk=pk)
    remove.delete()
    form = Feedback.objects.all()
    return render(request, 'data_all.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feedback')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('feedback')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})





