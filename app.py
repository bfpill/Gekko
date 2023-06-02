from flask import Flask, jsonify, request
from src.api.classifier_services import ClassifierManager

app = Flask(__name__)

classifier_manager = ClassifierManager()
classifier_manager.create_classifier()

@app.route('/classifier', methods=['GET'])
def intake():
    if not classifier_manager.has_classifier:
        try: 
            response = classifier_manager.create_classifier()         
        except Exception as e: 
            return jsonify({e: response[0]}), 500
        
    response = classifier_manager.intake("How much money should milk cost? Answer concisely")
    
    return jsonify({"response": response})
        

@app.route('/classifier/create', methods=['POST'])
def get_new_classifier():
    response = classifier_manager.create_classifier()
    if "Error" in response[0]:
        return jsonify({"error": response[0]}), 500
    else:
        return jsonify({"message": response[0]})

if __name__ == '__main__':
    app.run(debug=True)
