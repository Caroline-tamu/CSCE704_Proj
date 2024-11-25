import pandas as pd
from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
from defender.models.attribute_extractor import PEAttributeExtractor


def create_app(model):
    app = Flask(__name__)
    app.config['model'] = model
    model = load_model(app.config['model'], compile=False)

    # analyse a sample
    @app.route('/', methods=['POST'])
    def post():
        # curl -XPOST --data-binary @somePEfile http://127.0.0.1:8080/ -H "Content-Type: application/octet-stream"
        if request.headers['Content-Type'] != 'application/octet-stream':
            resp = jsonify({'error': 'expecting application/octet-stream'})
            resp.status_code = 400  # Bad Request
            return resp

        bytez = request.data

        try:
            pe_att_ext = PEAttributeExtractor(bytez)
            atts = pe_att_ext.extract()
            prediction = model.predict(atts, verbose=0)
            print(prediction)
            result = 1 if prediction[0][0] > 0.89 else 0
            print('LABEL = ', result)
        except Exception as e:
            result = 1
            print('LABEL = ', result)
            print("Errror: ", e)


        if not isinstance(result, int) or result not in {0, 1}:
            resp = jsonify({'error': 'unexpected model result (not in [0,1])'})
            resp.status_code = 500  # Internal Server Error
            return resp

        resp = jsonify({'result': result})
        resp.status_code = 200
        return resp

    # get the model info
    @app.route('/model', methods=['GET'])
    def get_model():
        # curl -XGET http://127.0.0.1:8080/model
        resp = jsonify(app.config['model'].model_info())
        resp.status_code = 200
        return resp

    return app
