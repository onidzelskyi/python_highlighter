import unittest
import sys
sys.path.append('.')
from app import app


class HighlightTest(unittest.TestCase):

    def setUp(self):
        """This method is called each time the test routine run"""
        # TODO: add the test data in this routine
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.text = 'Sample text to be highlighted'
        self.search_text = 'text'
        self.highlighted_text = 'Sample <mark>text</mark> to be highlighted'

    def tearDown(self):
        """This method is called after the test routine is finished 
        to clear out the data created in setUp method."""
        # TODO: add an implementation
        pass

    def test_markup_text(self):
        response = self.app.post('/', follow_redirects=True,
                                      data={'search': self.search_text,
                                            'text': self.text})
        import pdb; pdb.set_trace()
        self.assertEqual(response.content['highlighted_text'], self.highlighted_text)
