from django.http import JsonResponse, HttpRequest
def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON data
    print(body)
    return JsonResponse({"message":"Hi there, this is your Django API response"})