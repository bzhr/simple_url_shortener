from rest_framework.serializers import (
    ModelSerializer, URLField, SerializerMethodField, CharField
)

from .utils import shorten_id
from .models import Url


class CreateShortUrlSerializer(ModelSerializer):
    url = URLField(required=True)
    short_code = SerializerMethodField(read_only=True)

    class Meta:
        model = Url
        fields = ["url", "short_code"]

    def get_short_code(self, obj):
        short_code = shorten_id(obj.id)
        return short_code


class RetreiveUrlSerializer(CreateShortUrlSerializer):
    url = URLField(read_only=True)
    short_code = CharField(required=True)

    class Meta:
        model = Url
        fields = ["url"]
