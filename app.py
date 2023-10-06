from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from text_summarizer import summarizer,punctuator



app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    text=""
    speechSummary=""
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            text = punctuator(transcript)
            speechSummary = summarizer(text)

    return render_template('index.html', transcript=transcript,speechSummary=speechSummary)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    
# from flask import Flask,render_template,request
# from text_summarizer import summarizer

# app = Flask(__name__)
# @app.route("/")
# def index():
#     return render_template("index.html")

# # @app.route("/summarize",methods=['GET'])
# # def summary():
# #     summary = summarizer()
# #     return render_template("summary.html",summary=summary)

# if __name__=="__main__":
#     app.run(debug=True)
    