from requests import request

pages = ['login', 'register']


def test_api_sanity():
    for page in pages:
        url = f"https://demowebshop.tricentis.com/{page}"
        response = request("GET", url)
        if response.status_code == 200:
            print(f"PASS : {url}")
        else:
            print(f"FAIL : {url}")


# pytest test_api_sanity.py --html = "sanity.html"
