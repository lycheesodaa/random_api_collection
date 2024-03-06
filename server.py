from flask import Flask, request
app = Flask(__name__)

from dialog_tag import DialogTag

model = DialogTag('distilbert-base-uncased')

@app.route('/dialogtag', methods= ['POST'])
def dialog_tag():
    dialog_tag = model.predict_tag(request.json['text'])
    return {
        "dialog_tag": dialog_tag
    }