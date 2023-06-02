from flask import Flask, jsonify, request
from gekko.api.classifier_services import ClassifierManager
from gekko.whisper.live_transcribe import main
from gekko.memory.memory_writer import add_to_todo_stack
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
    
@app.route('/whisper/start', methods=['POST'])
def start_transcriber():
    model = "tiny"
    non_english = False
    energy_threshold = 700
    record_timeout = 2
    phrase_timeout = 5

    main(model, non_english, energy_threshold, record_timeout, phrase_timeout)
    return jsonify({"message": "Started Transcriber"})

@app.route('/memory/write', methods=['POST'])
def write_to_todo_stack():
    try: 
        add_to_todo_stack("TEST TEXT")
        return jsonify({"message": "Wrote to file"})
    except Exception as e: 
        return jsonify({"Error:": e})

if __name__ == '__main__':
    app.run(debug=True)
