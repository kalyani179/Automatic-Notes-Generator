from flask import Flask,render_template,request
from text_summarizer import summarizer

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize",methods=['GET'])
def summary():
    summary = summarizer()
    return render_template("summary.html",summary=summary)

if __name__=="__main__":
    app.run(debug=True)
    