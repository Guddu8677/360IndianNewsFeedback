from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FeedbackForm
from .models import Feedback
from stories.models import NewsStory

@login_required
def feedback_form(request, story_id):
    story = get_object_or_404(NewsStory, pk=story_id)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.story = story
            feedback.user = request.user
            feedback.ip_address = request.META.get('REMOTE_ADDR')
            feedback.language = 'en'
            feedback.save()
            
            messages.success(request, 'Thank you! Your feedback has been submitted successfully!')
            return redirect('stories:story_detail', story_id=story.id)
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback/feedback_form.html', {
        'form': form,
        'story': story
    })