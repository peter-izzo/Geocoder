from flask import Flask, render_template, request, send_file, send_from_directory, url_for, redirect
from werkzeug import secure_filename
import folium

app=Flask(__name__)

#UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
ALLOWED_EXTENSIONS = {"csv", "xls", "xlsx"}
#app.uploads.file_type(extensions=('csv', 'xls', 'xlsx'))

def allowed_file(filename):
    return '.' in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=="POST":
        file=request.files["file"]
        file.save(secure_filename(file.filename))
        if 'file' not in request.files:
            return render_template("index.html",
            text="No file attached!")
        #if file and allowed_file(file.filename):
        #    filename = secure_filename(file.fiename)
    #    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #        process_filename(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
        #else:
        #    return render_template("invalid.html")
        return render_template("index.html", btn="download.html")

@app.route("/download")
def download():
    return send_file(file.filename, attachment_filename="yourfile"+file.filename, as_attachment=True)

@app.route("/invalid")
def invalid():
    if file_type not in file:
        return render_template("invalid.html")


if __name__ == '__main__':
    app.debug=True
    app.run()
