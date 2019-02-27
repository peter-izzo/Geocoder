from flask import Flask, render_template, request, send_file, send_from_directory, url_for, redirect
from werkzeug import secure_filename
import folium
import csv
import pandas

app=Flask(__name__)

#UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
ALLOWED_EXTENSIONS = {"csv", "xls", "xlsx"}
#app.uploads.file_type(extensions=('csv', 'xls', 'xlsx'))

def allowed_file(filename):
    return '.' in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

#read uploaded csv and add new Latitude & Longitude columns
fields = ["Latitude", "Longitude"]
with open(file, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

map = folium.Map(location=[] , zoom_start=6)

#way to add markers and location to folium...fill this in with real data later
fg = folium.FeatureGroup(name="My Map")
for coordinates in addresses
fg.add_child(folium.marker(location=[], popup="This is one of your addresses", icon=folium.Icon(color='green')))
map.add_child(fg)

#use pandas to open csv, then save addresses as a variable. Use this variable to add content to lat/long columns
data = pandas.read_csv(file)
def readcsv(path, column_names):
    with open(path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            record = {address}

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=="POST":
        file=request.files["file"]
        file.read()
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
