from flask import render_template, request, Markup
import sys
sys.path.append('..')
from app import app

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
    result = '<mark>{}</mark>'.format(text)

    return result


def highlight_text(text, expr):
    """Markup searched string in given text.
    @:param text - string text to be processed
    @:return marked text, e.g., "sample text <mark>highlighted part</mark> rest of the text"."""
    result = text

    # TODO: add an implementation
    result = ''
    offset = 0
    text_length = len(text)
    expr_length = len(expr)
    while offset < text_length:
        if text[offset: offset + expr_length] == expr:
            result += markup_text(text[offset: offset + expr_length])
            offset += expr_length
        else:
            result += text[offset]
            offset += 1

    return result


if __name__ == '__main__':
    app.run(debug=True)