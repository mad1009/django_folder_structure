from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def greeting(request):
    return Response("Hello world!")
