Help on function send_mail in module django.core.mail:

sseenndd__mmaaiill(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
    Easy wrapper for sending a single message to a recipient list. All members
    of the recipient list will see the other recipients in the 'To' field.
    
    If auth_user is None, use the EMAIL_HOST_USER setting.
    If auth_password is None, use the EMAIL_HOST_PASSWORD setting.
    
    Note: The API for this method is frozen. New code wanting to extend the
    functionality should use the EmailMessage class directly.
