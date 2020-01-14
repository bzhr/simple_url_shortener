from rest_framework.views import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError, NotFound

from .serializers import CreateShortUrlSerializer, RetreiveUrlSerializer
from .utils import find_index
from .models import Url as UrlModel


@api_view(['POST'])
def create_short_url(request):
    data = request.data
    serializer = CreateShortUrlSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def retreive_long_url(request):
    code = request.data['short_code']
    try:
        obj_index = find_index(code)
    except ValueError:
        raise ValidationError("Code is invalid", code=400)
    try:
        obj = UrlModel.objects.get(id=obj_index)
    except UrlModel.DoesNotExist:
        raise NotFound("Code not found in DB")
    serializer = RetreiveUrlSerializer(obj)
    return Response(serializer.data, status=201)
