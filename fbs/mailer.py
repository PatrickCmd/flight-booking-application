from django.core.mail import EmailMessage
from django.shortcuts import redirect


def sendEmailVerification(request, user, user_data):
        username = user.get('first_name')
        subject = "FBS Account Verification"
        body = f"Hello {username}, Thank you for registering on our system with us, kindly \
                click the link below to activate your account! \
                http://{request.get_host()}/fbs-api/users/verify_account/{user_data.get('token')}"
        to_email = [user.get('email')]
        email = EmailMessage(subject, body, to=to_email)
        email.send()
        user_data.update(
            {'message': 'A verification link has been sent to your email, please visit your email '
                        'and activate your account.'}
        )