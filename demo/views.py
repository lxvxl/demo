from django.http import JsonResponse

def report(request):
    print(request)
    print(111)
    return JsonResponse({'message': 'Hello, this is an API endpoint!'})
