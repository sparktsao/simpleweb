from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    page = open("index.html").read()
    return page

@app.route("/js")
def js():
    page = open("client.js").read()
    return page

@app.route('/hello/<string:post_id>')
def fun1(post_id):
    fh = open("tmp.js","w")
    fh.write(post_id)
    fh.close()
    cmd1 = "python ./exe/run_showfeature.py tmp.js"
    import commands
    fv = commands.getstatusoutput(cmd1)[1]
    return fv
