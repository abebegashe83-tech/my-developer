from datetime import datetime, timezone

from django.http import JsonResponse

from .data import PORTFOLIO_PROJECTS


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
