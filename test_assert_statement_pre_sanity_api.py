from requests import request
from pytest import mark

headers = "page"
pages = [('login'), ('register'), ('cart')]
@mark.parametrize("page", pages)
def test_api_sanity(page):
    url = f"http://demowebshop.tricentis.com/{page[0]}"

