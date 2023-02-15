from cel.forms import ReminderForm
from cel.task import send_mail_task

from django.shortcuts import redirect, render
from django.urls import reverse


def send_mail(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.clean()
            send_mail_task.apply_async(args=[form.cleaned_data['email'], form.cleaned_data['message']],
                                       eta=form.cleaned_data['date_time'])
            return redirect(reverse('send_mail'))
    else:
        form = ReminderForm()
    return render(request, 'mail_form.html', {'form': form})
