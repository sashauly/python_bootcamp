from flask import Flask, render_template, request
from flask import redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['SFX_FOLDER'] = 'sfx/'
app.config['ALLOWED_EXTENSIONS'] = {'wav', 'mp3', 'ogg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['SFX_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    files = [f for f in os.listdir(
        app.config['SFX_FOLDER']) if allowed_file(f)]
    return render_template('index.html', files=files)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['SFX_FOLDER'], filename)


@app.route('/all', methods=['GET'])
def get_all_sounds():
    return "\n".join([str(x) for x in os.listdir(app.config['SFX_FOLDER'])])


if __name__ == '__main__':
    app.run(port=8888)
