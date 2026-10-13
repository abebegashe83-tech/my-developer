import json
import logging
from datetime import datetime, timezone

from django.conf import settings
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .data import PORTFOLIO_PROJECTS
from .models import ContactMessage

logger = logging.getLogger(__name__)


def health_check(request):
    return JsonResponse(
        {
            'status': 'ok',
            'message': 'Portfolio API is running.',
            'timestamp': datetime.now(timezone.utc).isoformat(),
        }
    )


def project_list(request):
    return JsonResponse({'projects': PORTFOLIO_PROJECTS})


@csrf_exempt
def contact_message(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are supported.'}, status=405)

    try:
        payload = json.loads(request.body.decode('utf-8')) if request.body else {}
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Request body must be valid JSON.'}, status=400)

    name = str(payload.get('name', '')).strip()
    email = str(payload.get('email', '')).strip()
    message = str(payload.get('message', '')).strip()

    if not name or not email or not message:
        return JsonResponse({'error': 'Name, email, and message are required.'}, status=400)

    if '@' not in email:
        return JsonResponse({'error': 'Please provide a valid email address.'}, status=400)

    contact = ContactMessage.objects.create(name=name, email=email, message=message)
    recipient_email = getattr(settings, 'EMAIL_TO', settings.DEFAULT_FROM_EMAIL)

    try:
        EmailMessage(
            subject=f'Portfolio message from {name}',
            body=(
                f'Name: {name}\n'
                f'Email: {email}\n\n'
                f'{message}'
            ),
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com'),
            to=[recipient_email],
            reply_to=[email],
        ).send()
        success_message = 'Your message was sent successfully.'
    except Exception:
        logger.exception('Failed to send portfolio contact email via configured SMTP backend')
        success_message = (
            'Your message was saved successfully, but live email delivery is unavailable. '
            'The SMTP credentials appear invalid or not configured. '
            'Add a valid Gmail app password or another working SMTP configuration to enable delivery.'
        )

    return JsonResponse(
        {
            'status': 'success',
            'message': success_message,
            'saved_id': contact.id,
        },
        status=201,
    )
