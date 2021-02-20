try:
    import sys, os
    sys.path.append(os.path.abspath(os.path.join('..', 'url-shortener')))
    from url_shortener import create_app, db
    from url_shortener.models import Url
    from flask_testing import TestCase
    import unittest

except Exception as e:
    print(e)

class AppTest(TestCase):
    def create_app(self):
        return create_app("test_config.py")

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Test Response (200)
    def test_index(self):
        tester = self.client
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_add_url(self):
        tester = self.client
        response = tester.post("/add_url", data = dict( original_url= "https://leetcode.com/problemset/all/"))
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_redirect(self):
        tester = self.client
        response = tester.get("/15EKbU6e")
        print(response.data)
        status_code = response.status_code
        self.assertEqual(status_code, 302)

    def test_views(self):
        tester = self.client
        response = tester.get("/views")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # Test Content Type
    def test_index_content_type(self):
        tester = self.client
        response = tester.get("/")
        content_type = response.content_type
        self.assertEqual(content_type, "text/html; charset=utf-8")

    def test_views_content_type(self):
        tester = self.client
        response = tester.get("/views")
        content_type = response.content_type
        self.assertEqual(content_type, "text/html; charset=utf-8")


if __name__ == "__main__":
    unittest.main()