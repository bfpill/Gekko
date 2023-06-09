from datetime import datetime
from flask import Flask, jsonify, request
from api.classifier_services import ClassifierManager
from whisper_wrap.live_transcribe import main
from memory.memory_writer import add_to_todo_stack
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
    
    return jsonify({"response": "yeah classifier created"})
        
@app.route('/classifier/create', methods=['POST'])
def get_new_classifier():
    response = classifier_manager.create_classifier()
    if response is Exception:
        return jsonify({"error": str(response)}), 500
    else:
        return jsonify({"message": "it worked"})
    
@app.route('/classifier/start', methods=['POST'])
def start_classifier():
    try:
        print("Transcriber started")
        classifier_manager.start_classifier()
        return jsonify({"message": "Worked!!"})
    except Exception as e:
        return jsonify({"error": "Error" + str(e)}), 500
    
@app.route('/gekko/start', methods=['POST'])
def start_gekko():
    try:
        classifier_manager.create_classifier()
        print("classifier started")
        start_transcriber()
        print("Transcriber started")
        return jsonify({"message": "Gekko Started!!"})
    except Exception as e:
        return jsonify({"error": "Error"}), 500

@app.route('/whisper/start', methods=['POST'])
def start_transcriber():
    model = "tiny"
    non_english = False
    energy_threshold = 1000
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
    app.run(port=8000, debug=True)
