from flask import Flask, render_template, flash, request, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER='static/images'
app.secret_key = "123"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def browse_file():
    return render_template('Uploadimages.html')

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if request.method=='POST':
        if 'files[]' not in request.files:
            flash("No File",'danger')
            return redirect(request.url)
        files=request.files.getlist('files[]')
        for file in files:
            if file and allowed_file(file.filename):
                filename=secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        flash("Files Upload Successfully","success")
        imageList = os.listdir('static/images')
        imagelist = ['images/' + image for image in imageList]
        return render_template('Uploadimages.html', data=imagelist)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
