# Django imports
import random
import string

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Local imports
from applications.users.models import User


def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def send_email_verify_code(id=None):
    user = get_object_or_404(User, id=id)
    subject = _('Verification Code') + '  ' + _('ForEmail') + '  ' + user.first_name
    message = (
        f'{_("Verification Code")}:  {user.code_verification} \n{_("ForEmail")} {user.first_name}\n'
        f'{_("Link")} {settings.LINK_BASE_URL}verification-user/{user.id}'
    )
    email_sender = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_sender, [user.email, ])


def send_again_email_verify_code(id=None):
    user = get_object_or_404(User, id=id)
    user.code_verification = code_generator()
    user.save()
    send_email_verify_code(id)
