# Simple URL Shortener API with Django and Django Rest Framework

## Set Up

To create a virtual env and install dependencies run:

`pipenv shell`

To run the server:

`./manage.py runserver`

## API Endpoints

There are two endpoints, one to create a short URL and another to retreive the original link from a short URL.

### Create short URL

- Make a POST request to `/shorten-url`
- POST data format: `{"url": "https://www.django-rest-framework.org/tutorial/quickstart/"}`
- Example response:

```
{
    "url": "https://www.django-rest-framework.org/tutorial/quickstart/",
    "short_code": "MjY="
}
```

## Retreive the original URL

- Make a POST request to `/retreive-original-url`
- POST data format: `{"short_code": "MjM="}`
- Example response:

```
{
    "url": "https://www.django-rest-framework.org/tutorial/quickstart/"
}
```

## Testing

To run tests:

`./manage.py`
