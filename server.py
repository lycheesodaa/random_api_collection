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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
