from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from flask_cors import CORS, cross_origin
import os

cred = credentials.Certificate("/Users/christie/Documents/GitHub/TritonOneStop_Frontend/back-end/tostest1-5e30d-firebase-adminsdk-0d1va-bf403ad302.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
resource_ref = db.collection('resources')

app = Flask(__name__)
CORS(app)

@app.route('/getResources', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        resource : Return document that matches query ID.
        all_resources : Return all documents.
    """
    try:
        resource_id = request.args.get('id')
        if resource_id:
            resource = resource_ref.document(resource_id).get()
            return jsonify(resource.to_dict()), 200
        else:
            all_resources = [doc.to_dict() for doc in resource_ref.get()]
            return jsonify(all_resources), 200
    except Exception as e:
        return f"An Error Occured: {e}"


port = int(os.environ.get('PORT', 8080))

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='127.0.0.0', port=port)
