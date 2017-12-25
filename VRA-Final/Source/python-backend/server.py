from flask import Flask, render_template, request, Response
from flask_cors import CORS, cross_origin
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_jsonpify import jsonify
from werkzeug import secure_filename
import os
import urllib
import search
from config import Config

app = Flask(__name__,
            static_url_path = "",
            static_folder = Config.Resources["STATIC_FOLDER"],
            template_folder = Config.Resources["TEMPLATE_FOLDER"])

CORS(app, support_credentials=True)      
app.jinja_env.add_extension("pypugjs.ext.jinja.PyPugJSExtension")

def getImage(protocol, host, imgSrc):
    rootIndex = imgSrc.find(Config.Resources["STATIC_FOLDER"])
    if rootIndex != -1:
        imgSrc = imgSrc[rootIndex + len(Config.Resources["STATIC_FOLDER"]):]
    return "{}://{}/{}".format(protocol, host, imgSrc)


@app.route("/file-upload", methods=["POST"])
@cross_origin() # allow all origins all methods.
def upload():
    f = request.files["file"]
    filename = secure_filename(f.filename)
    f.save(os.path.join(Config.Resources["UPLOAD_FOLDER"], filename))

    httpHost = request.environ["HTTP_HOST"]
    httpProtocol = request.environ["SERVER_PROTOCOL"].lower()
    if httpProtocol.find('/') != -1:
        httpProtocol = httpProtocol[:httpProtocol.find("/")]

    data = {
        "fileSrc": getImage(httpProtocol, httpHost, Config.Resources["IMAGE_PATH"] + filename),
        "fileName": filename
    }
    return jsonify(data)


@app.route("/search", methods=["GET", "POST"])
@cross_origin() # allow all origins all methods.
def searchImage():
    q = request.values.get("q", type = str)
    cx = request.values.get("cx", default = 0, type = int)
    cy = request.values.get("cy", default = 0, type = int)
    cw = request.values.get("cw", default = 0, type = int)
    ch = request.values.get("ch", default = 0, type = int)
    feature = request.values.get("feature", type = str)
    q = urllib.unquote(q).decode("utf8")
    
    print "Search images with query is '{}'".format(q)     
    result = search.searchImage(q, feature, cx, cy, cw, ch)

    if result == None:
        return jsonify({ "error": "No images are found" })

    httpHost = request.environ["HTTP_HOST"]
    httpProtocol = request.environ["SERVER_PROTOCOL"].lower()
    if httpProtocol.find('/') != -1:
        httpProtocol = httpProtocol[:httpProtocol.find("/")]

    for item in result:
        item["image"] = getImage(httpProtocol, httpHost, item["image"])

    return jsonify({ "data": result })


if __name__ == "__main__":
    app.run(port=5000)
     