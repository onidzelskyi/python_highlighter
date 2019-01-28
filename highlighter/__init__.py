"""Flask module
file: __init__.py
date: 12.12.2012
author smith@example.com
license: MIT"""

from flask import Flask, render_template, request, Markup


def create_app():
    """Create flask app for binding."""
    app = Flask(__name__)

    template_file_name = 'index.html'

    @app.route('/', methods=['GET'])
    def index():
        return render_template(template_file_name)

    @app.route('/', methods=['POST'])
    def process():
        search_text = request.form['search']
        text = request.form['text']
        highlighted_text = highlight_text(text, search_text)
        result = {'text': text,
                  'highlighted_text': Markup(highlighted_text),
                  }
        return render_template(template_file_name, **result)

    def markup_text(text):
        """Markup given text.
        @:param text - string text to be marked
        @:return marked text, e.g., <mark>highlighted text</mark>."""
        result = text

        # TODO: add an implementation

        return result

    def highlight_text(text, expr):
        """Markup searched string in given text.
        @:param text - string text to be processed
        @:return marked text, e.g., "sample text <mark>highlighted part</mark> rest of the text"."""
        result = text

        # TODO: add an implementation

        return result

    return app
