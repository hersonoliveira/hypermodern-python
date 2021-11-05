import click
import desert
import marshmallow
import requests

from hypermodern_python.models import Page

API_URL: str = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"
schema = desert.schema(Page, meta={"unknown": marshmallow.EXCLUDE})


def random_page(language: str = "en") -> Page:
    url = API_URL.format(language=language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            data = response.json()
            return schema.load(data)
    except (requests.RequestException, marshmallow.ValidationError) as e:
        message = str(e)
        raise click.ClickException(message) from e
