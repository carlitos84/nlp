from flask import Flask, request, Response, jsonify
from flask_restful import reqparse
import nltkserver
from nltkserver.stemming import stemmer, lemmatize
from nltkserver.stanfordner import tagger
application = app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return nltkserver.helpers.ret_failure(404), 404


@app.route('/test', methods=['GET'])
def test():
    return 'Testing test()'


@app.route('/word_tokenize', methods=['POST'])
def word_tokenize():
    return nltkserver.word_tokenize(request.data)


@app.route('/sent_tokenize', methods=['POST'])
def sent_tokenize():
    return nltkserver.sent_tokenize(request.data)


@app.route('/pos_tag', methods=['POST'])
def pos_tag():
    return nltkserver.pos_tag(request.data)


@app.route('/stem/<method>', methods=['POST'])
def stem(method):
    return stemmer(method,request.data)


@app.route('/lemmatize/<method>', methods=['POST'])
def lem(method):
    return lemmatize(method, request.data)


@app.route('/stanfordNER', methods=['POST'])
def nertagger():
    return tagger(request.data)


@app.route('/stantest', methods=['GET'])
def stanTest():
    parser = reqparse.RequestParser()
    parser.add_argument('a')
    return tagger(parser.parse_args().get('a'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
