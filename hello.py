from flask import Flask
from flask import request, send_from_directory
from OpenSSL import SSL

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('spark.pri')
context.use_certificate_file('spark.cer')
context  = ('spark.cer','spark.pri')
app = Flask(__name__)

@app.route("/")
def hello():
    page = open("index.html").read()
    return page

@app.route("/client.js")
def js():
    page = open("client.js").read()
    return page

def processjscontent(post_id):
    fh = open("tmp.js","w")
    fh.write(post_id)
    fh.close()
    cmd1 = "python ./exe/run_showfeature.py tmp.js"
    import commands
    fv = commands.getstatusoutput(cmd1)[1]
    return fv

@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        print "handle user", user_id
        data = request.form # a multidict containing POST data
        print type(data), len(data)
        print dir(data)
        print data["data"]
        fv = processjscontent(data["data"])
        return fv

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)#,debug=False, ssl_context=context)
