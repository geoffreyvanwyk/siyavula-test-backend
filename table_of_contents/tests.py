import unittest
from pyramid import testing


class TOCViewTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home

        request = testing.DummyRequest()
        response = home(request)
        self.assertEqual({}, response)

    def test_toc_with_valid_url(self):
        from .views import table_of_contents

        page_name = 'Chess'
        url = 'https://en.wikipedia.org/wiki/' + page_name

        request = testing.DummyRequest()
        request.params['page_url'] = url
        response = table_of_contents(request)

        self.assertEqual('Table Of Contents', response['title'])
        self.assertEqual(page_name, response['page_name'])
        self.assertEqual(url, response['page_url'])
        self.assertIn('<div class="toc" id="toc">', str(response['table_of_contents']))


class TOCFunctionalTests(unittest.TestCase):

    def setUp(self):
        from table_of_contents import main
        from webtest import TestApp

        app = main({})
        self.testapp = TestApp(app)

    def test_home(self):
        response = self.testapp.get('/', status=200)
        self.assertIn(b'<input type="url"', response.body)
        self.assertIn(b'<button type="submit"', response.body)

    def test_toc_with_valid_url(self):
        response = self.testapp.post(
            '/table-of-contents',
            {'page_url': 'https://en.wikipedia.org/wiki/Chess'},
            status=200
        )

        self.assertIn(
            b'<b>Requested Page:</b> <a href="https://en.wikipedia.org/wiki/Chess">Chess</a>',
            response.body
        )

        self.assertIn(
            b'<button onclick="go_home()">Reset</button>',
            response.body
        )

        self.assertIn(b'<div class="toc" id="toc">', response.body)

    def test_toc_with_invalid_domain(self):
        response = self.testapp.post(
            '/table-of-contents',
            {'page_url': 'https://en.mikipedia.org/wiki/Chess'},
            status=200
        )

        self.assertIn(b'<p>Error: The URL does not contain a Wikipedia domain.</p>', response.body)
        self.assertIn(b'<input type="url"', response.body)
        self.assertIn(b'<button type="submit"', response.body)

    def test_toc_with_invalid_path(self):
        response = self.testapp.post(
            '/table-of-contents',
            {'page_url': 'https://en.wikipedia.org/wiki/Chess/Openings'},
            status=200
        )

        self.assertIn(b'<p>Error: The path to the page is not correct.</p>', response.body)
        self.assertIn(b'<input type="url"', response.body)
        self.assertIn(b'<button type="submit"', response.body)
