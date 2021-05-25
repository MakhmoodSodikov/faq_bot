from flask import Flask, request, jsonify, abort, redirect, url_for, flash
from model import load, infer
app = Flask(__name__)

model = load()


@app.route('/')
def check_is_running():
    return 'Application is running'


@app.route('/badrequest400')
def bad_request():
    return abort(400)


def run_prediction(model, query):
    if query is None:
        print('ERROR: GET-query is empty')

    try:
        pred, proba = infer(model, query)
        return pred, proba
    except Exception as e:
        print(e)
        print('Model error')


@app.route('/model/test_api_external', methods=['POST'])
def hello_world():
    print('request received')
    query = None

    try:
        content = request.get_json()
        query = content['query']
        print('Data OK')
    except Exception as e:
        print(e)
        print('Data error')

    pred, proba = run_prediction(model, query)
    output = {'answer': pred, 'proba': proba}
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)

