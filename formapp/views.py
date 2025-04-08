from django.shortcuts import render
from django.http import HttpResponse
from .models import Submission
from .forms import SubmissionForm
from django.core.mail import send_mail
from django.conf import settings

def upload_form(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save()

            # Σύνθεση email περιεχομένου
            subject = 'Νέα Καταχώρηση Έργου'
            message = f"""
ΝΕΑ ΥΠΟΒΟΛΗ:

Όνομα: {submission.name}
Email: {submission.email}
Τηλέφωνο: {submission.phone}
Περιγραφή: {submission.description}

Το αρχείο έχει ανέβει στον server.
"""
            recipient = ['dhspapa@zohomail.eu']
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient)

            return HttpResponse("Η αποστολή ολοκληρώθηκε.")
    else:
        form = SubmissionForm()
    return render(request, 'upload.html', {'form': form})
