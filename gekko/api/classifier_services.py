from .classifier import Classifier
from langchain.agents import Tool
from gekko.memory.memory_writer import write_to_json
from gekko.api.file_watcher import watch_file

class ClassifierManager: 
    def __init__ (self):
        self.has_classifier = False;
        self.tools = [
            Tool(
                name = "Store",
                func = write_to_json,
                description="Use to store important memories"
            )
        ]  
        self.classifier = self.create_classifier()

    def create_classifier(self):
        # Initialize the CustomAgent with any necessary tools
        try:   
            classifier = Classifier(self.tools)
            self.has_classifier = True
            return classifier
        
        except Exception as e:
            return e

    def start_classifier(self):
        watch_file()

    #def stop_classifier(self):

    def get_classifier(self):
        return self.classifier

    def restart_classifier(self):
        self.classifier.restart()

    def intake(self, conversation):
        return self.classifier.intake(conversation)
