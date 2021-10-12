from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET'])
def root():
    return jsonify({'messagem' : 'teste API Python'})