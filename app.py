from flask import Flask, request, render_template, jsonify
from transformers import pipeline

app = Flask(__name__, static_folder="static")
summarizer = pipeline("summarization")

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    summarised_text = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return render_template('index.html', summarised=summarised_text[0]["summary_text"])

if __name__ == '__main__':
    app.run()
