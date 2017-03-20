from django.utils import timezone

def blog(request):
    return {
        'current_datetime': timezone.now(),
    }

