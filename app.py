from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/about")
def about2():
	return render_template("about.html")
@app.route("/smlogin")
def smlogin():
	return render_template("smlogin.html")

@app.route("/sologin")
def sologin():
	return render_template("sologin.html")

@app.route("/custlogin")
def custlogin():
	return render_template("custlogin.html")

@app.route("/custregister")
def custregister():
	return render_template("custregister.html")

if __name__=='__main__':
	app.run(debug=True)