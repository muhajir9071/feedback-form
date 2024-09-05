
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_confirmation')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback_form.html', {'form': form})

def feedback_confirmation(request):
    feedback_entries = Feedback.objects.all()
    return render(request, 'feedback_confirmation.html', {'feedback_entries': feedback_entries})

def home(request):
    return render(request,"home.html")