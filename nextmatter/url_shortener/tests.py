import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .utils import shorten_id


class CreateShortUrlTest(APITestCase):
    def test_create_invalid_url(self):
        url = reverse('shorten')
        data = {"url": "I Am Not An URL"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_url(self):
        url = reverse('shorten')
        data = {"url": "https://nextmatter.com/how-it-works/"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RetreiveOriginalUrlTest(APITestCase):
    def test_valid_response(self):
        create_url = reverse('shorten')
        post_url = "https://nextmatter.com/about/"
        data = {"url": post_url}
        response = self.client.post(create_url, data, format='json')
        content_json = json.loads(response.content)
        short_code = content_json['short_code']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        retreive_url = reverse('retreive-original')
        data = {"short_code": short_code}
        response = self.client.post(retreive_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_response(self):
        retreive_url = reverse('retreive-original')
        invalid_short_code = "kognondoinboisnb"
        data = {"short_code": invalid_short_code}
        response = self.client.post(retreive_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_found_response(self):
        retreive_url = reverse('retreive-original')
        unexisting_index = 50000
        short_code = shorten_id(unexisting_index)
        data = {"short_code": short_code}
        response = self.client.post(retreive_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
