from flask import Flask, render_template , request
import uuid # provide uniques id to all different folders
from werkzeug.utils import secure_filename
import os 

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route("/")
def home():
    return render_template("index.html") 


# The button of "create reel" on create page will send POST request to our flask
# end point and this end point will upload all the files to a folder and saving
# the description to a text file in that folder
# The folder will be named with a unique id so that we can use it later for AI

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
            # key is file1, file2 etc   and value is the file name like image name
            
            # upload the file
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id)))):
                    # if the folder does not exist, create it
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],rec_id,  filename))
   # joining the upload folder with the unique id and the file name
            
            # Capture the description and save it to a file
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.txt"), "w") as f:
                f.write(desc)
 # I am taking the upload folder and rec_id with it and then writing the description to a file called desc.txt which user has typed     
 # so that we can use it later for the AI model to generate the voiceover

    return render_template("create.html", myid=myid)





@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

if __name__ == "__main__":
    app.run(debug=True)
    