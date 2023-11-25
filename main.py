from flask import Flask, render_template, url_for
app = Flask(__name__,static_url_path='/static') 

@app.route("/", methods=['GET','POST'])
def home(): # Run the function
	return render_template("index.html") #render index.html

@app.route("/Download")
def Download():
	return render_template("Download.html") 

@app.route("/About", methods=['GET','POST'])
def About():
	return render_template("About.html") 

@app.route("/Feedback", methods=['GET','POST'])
def Feedback():
	return render_template("Feedback.html") 


if  __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True) #does what it says

'''
TODO LIST:
Add more content
Clean up navbar code(might use chatgpt because its a nightmare to read and probally not worth the effort) or replace navbar code entirely
'''