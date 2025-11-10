from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'bias', 'accuracy_flag', 'tags', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Rate 1-5'
            }),
            'bias': forms.Select(attrs={'class': 'form-select'}),
            'accuracy_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your thoughts...'
            }),
        }
        labels = {
            'rating': 'Rating (1-5)',
            'bias': 'Perceived Bias',
            'accuracy_flag': 'Flag as potentially inaccurate',
            'comment': 'Your Comment',
        }

    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., sensational, incomplete'
        }),
        help_text='Separate multiple tags with commas'
    )

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating and (rating < 1 or rating > 5):
            raise forms.ValidationError('Rating must be between 1 and 5.')
        return rating

    def clean_tags(self):
        tags_str = self.cleaned_data.get('tags', '')
        if tags_str:
            return [tag.strip() for tag in tags_str.split(',') if tag.strip()]
        return []