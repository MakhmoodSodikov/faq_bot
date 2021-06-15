from flask import Flask, request, jsonify, abort, redirect, url_for, flash
from model import load, infer
app = Flask(__name__)

prediction_model, intent_model = load()


@app.route('/')
def check_is_running():
    return 'Application is running'


@app.route('/badrequest400')
def bad_request():
    return abort(400)


@app.route('/update')
def bad_request():
    return abort(400)


def run_prediction(prediction_model, intent_model, query):
    if query is None:
        print('ERROR: GET-query is empty')

    try:
        pred, proba, intent = infer(prediction_model, intent_model, query)
        return pred, proba, intent
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

    pred, proba, intent = run_prediction(prediction_model,
                                         intent_model,
                                         query)
    output = {'answer': pred, 'proba': proba, 'intent': intent}
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)

