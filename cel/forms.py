from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class ReminderForm(forms.Form):
    email = forms.EmailField(label="Email", initial='hillel@example.com')
    message = forms.CharField(label='Reminder text', max_length=255, widget=forms.Textarea(attrs={"rows": 3}))
    date_time = forms.DateTimeField(label='Reminder time YYYY-MM-DD HH:MM:SS', initial=timezone.now())

    def clean_date_time(self):
        date_time = self.cleaned_data['date_time']
        if date_time < timezone.now():
            raise ValidationError('Sorry, but we can go past....yet')
        elif date_time > timezone.now() + timezone.timedelta(days=2):
            raise ValidationError('Only +2 days in future')
        else:
            return date_time
