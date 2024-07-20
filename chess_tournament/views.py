from django.http import JsonResponse

def index(request):
    return JsonResponse({
        'message': 'Welcome to the Chess Tournament Management System API. Please use /api/ to access the API endpoints.'
    })
