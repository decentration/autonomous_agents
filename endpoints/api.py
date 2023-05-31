from flask import Flask, request, jsonify
from api_logic import APILogic

app = Flask(__name__)
api_logic = APILogic()

@app.route('/api/instances/<instance_id>', methods=['GET'])
def get_instance_data(instance_id):
    return jsonify(api_logic.get_instance_data(instance_id))

@app.route('/api/conversations/<instance_id>', methods=['GET'])
def get_conversation_history(instance_id):
    return jsonify(api_logic.get_conversation_history(instance_id))

if __name__ == '__main__':
    app.run()
