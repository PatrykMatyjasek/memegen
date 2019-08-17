import json

from backend.main import app


def describe_templates():
    def describe_GET():
        def it_returns_all_templates(expect):
            request, response = app.test_client.get("/api/templates")
            expect(response.status) == 200


def describe_images():
    def describe_GET():
        def it_returns_sample_image_urls(expect):
            request, response = app.test_client.get("/api/images")
            expect(response.status) == 200
            expect(response.json).contains(
                {
                    "url": "http://localhost:8000/api/images/iw/tests_code/in_production.jpg"
                }
            )

    def describe_POST():
        def it_returns_an_image_url(expect):
            data = {"key": "iw", "lines": ["foo", "bar"]}
            request, response = app.test_client.post(
                "/api/images", data=json.dumps(data)
            )
            expect(response.status) == 201
            expect(response.json) == {
                "url": "http://localhost:8000/api/images/iw/foo/bar.jpg"
            }