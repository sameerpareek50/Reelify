# from flask import Flask, render_template , request
# import uuid # provide uniques id to all different folders
# from werkzeug.utils import secure_filename
# import os 

# UPLOAD_FOLDER = 'user_uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




# @app.route("/")
# def home():
#     return render_template("index.html") 


# # The button of "create reel" on create page will send POST request to our flask
# # end point and this end point will upload all the files to a folder and saving
# # the description to a text file in that folder
# # The folder will be named with a unique id so that we can use it later for AI

# @app.route("/create", methods=["GET", "POST"])
# def create():
#     myid = uuid.uuid1()
#     print(f"Unique ID for this session: {myid}")

#     if request.method == "POST":
#         print(request.files.keys())
#         rec_id = request.form.get("uuid")   # received unique id
#         desc = request.form.get("text")      # Description
#         input_files = []
#         for key,value in request.files.items():
#             print(f"Key: {key}, Value: {value}")
#             # key is file1, file2 etc   and value is the file name like image name
            
#             # upload the file
#             file = request.files[key]
#             if file:
#                 filename = secure_filename(file.filename)
#                 if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id)))):
#                     # if the folder does not exist, create it
#                     os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'],rec_id,  filename))
#    # joining the upload folder with the unique id and the file 
   
#                 input_files.append(file.filename)
#                 print(file.filename)
#         # Now we will create a text file called input.txt inside the folder
            
#             # Capture the description and save it to a file
#             with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.txt"), "w") as f:
#                 f.write(desc)        
#  # I am taking the upload folder and rec_id with it and then writing the description to a file called desc.txt which user has typed     
#  # so that we can use it later for the AI model to generate the voiceover

#         for fl in input_files:
#             with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,  "input.txt"), "a") as f:
#                 f.write(f"file '{fl}'\nduration 1\n")


#     return render_template("create.html", myid=myid)







# app.run(debug=True)
    
from flask import Flask, render_template, request, redirect, url_for, flash
import uuid
from werkzeug.utils import secure_filename
import os
import subprocess

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "supersecretkey"  # Needed for flashing messages

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    error = None

    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text", "").strip()
        input_files = []
        files_uploaded = False

        # Check for at least one image file
        for key in request.files:
            file = request.files[key]
            if file and allowed_file(file.filename):
                files_uploaded = True
                break

        # Validation: at least one image or text
        if not files_uploaded and not desc:
            error = "Please upload at least one image or enter text for audio."
            return render_template("create.html", myid=myid, error=error)

        # Save files and text
        for key in request.files:
            file = request.files[key]
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                file.save(os.path.join(folder_path, filename))
                input_files.append(filename)

        # Save description
        if desc:
            folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            with open(os.path.join(folder_path, "desc.txt"), "w") as f:
                f.write(desc)

        # Save input.txt for images
        for fl in input_files:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"), "a") as f:
                f.write(f"file '{fl}'\nduration 1\n")

        # --- AUTOMATICALLY RUN GENERATE PROCESS ---
        # If generate_process.py is a script, run it with subprocess
        try:
            subprocess.run(
                ["python", "generate_process.py", str(rec_id)],
                check=True
            )
        except Exception as e:
            error = f"Error generating reel: {e}"
            return render_template("create.html", myid=myid, error=error)

        # Redirect or show success message
        flash("Reel is being generated! Check the gallery soon.", "success")
        return redirect(url_for("gallery"))

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

# This would add the reels to the static folder so that we can access them later in gallery of website

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)