from django.shortcuts import render
import random
from twilio.rest import Client
from django.conf import settings

# Create your views here.


def index(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')  # Assuming you have a form with a phone_number field
        verification_code = str(random.randint(100000, 999999))
        print(request.POST.get('phone_number'))
        # Save the verification code in your database or cache for later verification
        #request.session['verification_code'] = verification_code

        # Send the code via Twilio call
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f'Your verification code is: {verification_code}',
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        print(f"HTTP Response Status: {message.status}")
        return render(request, 'verification.html')
    
    return render(request, 'index.html')


def verification_sent(request):
    
    return render(request, 'verification.html')
    