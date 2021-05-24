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
    try:
        content = infer(model, query)
        return content
    except:
        print('Model error')


@app.route('/model/test_api_external', methods=['GET'])
def hello_world():
    print('request received')

    try:
        content = request.get_json()
        query = content['query']
        print('Data OK')
    except:
        print('Data error')

    output = run_prediction(model, query)
    output = {'answer': output}
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)

