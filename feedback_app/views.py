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





