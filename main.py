from flask import Flask, render_template , request
import uuid # provide uniques id to all different folders

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    print(f"Unique ID for this session: {myid}")

    if request.method == "POST":
        print(request.files.keys())
        for key,value in request.files.items():
            print(f"Key: {key}, Value: {value}")

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

if __name__ == "__main__":
    app.run(debug=True)
    