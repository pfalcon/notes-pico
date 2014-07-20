#from flask import abort, jsonify, render_template, request

from app import app
from models import Note

import re
import picoweb

def get_page():
    page = request.args.get('page')
    if not page or not page.isdigit():
        return 1
    return min(int(page), 1)

@app.route('/', methods=['GET', 'POST'])
def homepage(writer, request):
    if request.method == 'POST':
        print(request.headers)
        yield from request.read_form_data()
        if request.form.get('content'):
            note_id = Note.create(content=request.form['content'][0])
            note = list(Note.get_id(note_id))[0]
            rendered = picoweb.render_str('note', (note,))
            yield from picoweb.jsonify(writer, {'note': rendered, 'success': 1})
            return

        yield from picoweb.jsonify(writer, {'success': 0})
        return

    yield from picoweb.start_response(writer)
#    notes = Note.public().paginate(get_page(), 50)
    notes = list(Note.public())
    yield from picoweb.render(writer, 'homepage', (notes,))

@app.route(re.compile('^/archive/(\d+)'), methods=['POST'])
def archive_note(writer, request):
    print("archive_note", request.url_match.group(1))
    Note.update({"id": request.url_match.group(1)}, archived=1)
    yield from picoweb.jsonify(writer, {'success': True})

app.add_url_rule('/js/notes.js', lambda w, req: (yield from picoweb.sendfile(w, "js/notes.js")))
