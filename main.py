from flask import Flask, render_template , request
import uuid # provide uniques id to all different folders
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    print(f"Unique ID for this session: {myid}")

    if request.method == "POST":
        print(request.files.keys())
        rec_id = request.form.get("uuid")   # received unique id
        desc = request.form.get("text")      # Description
        for key,value in request.files.items():
            print(f"Key: {key}, Value: {value}")
            # upload the file
            # key is file1, file2 etc   and value is the file name like image name

    return render_template("create.html", myid=myid)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

if __name__ == "__main__":
    app.run(debug=True)
    