import pytest

from .. import settings


def describe_index():
    def it_contains_the_api_root(expect, client):
        request, response = client.get("/")
        expect(response.status) == 200
        expect(response.json).contains("_docs")


def describe_examples():
    @pytest.mark.slow
    def it_displays_images(expect, client):
        request, response = client.get("/examples")
        expect(response.status) == 200
        expect(response.text.count("img")) > 100
        expect(response.text).excludes("setInterval")

    @pytest.mark.slow
    def it_can_enable_automatic_refresh(expect, client, monkeypatch):
        monkeypatch.setattr(settings, "DEBUG", True)
        request, response = client.get("/examples?debug=true")
        expect(response.status) == 200
        expect(response.text.count("img")) > 100
        expect(response.text).includes("setInterval")


def describe_test():
    def it_redirects_to_the_index(expect, client):
        request, response = client.get("/test", allow_redirects=False)
        expect(response.status) == 302
        expect(response.headers["Location"]) == "/"

    def it_displays_test_images_when_debug(expect, client, monkeypatch):
        monkeypatch.setattr(settings, "DEBUG", True)
        request, response = client.get("/test", allow_redirects=False)
        expect(response.status) == 200
        expect(response.text.count("img")) > 5
        expect(response.text.count("img")) < 100
