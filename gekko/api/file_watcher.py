import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from classifier.classifier import Classifier
class FileWatcher:
    class MyHandler(FileSystemEventHandler):
        def __init__(self, filename, callback):
            self.filename = filename
            self.callback = callback
            self.process_events = True;
        
        def on_modified(self, event):
            if event.src_path.endswith(self.filename) and self.process_events:
                with open(event.src_path, 'r+') as file:
                    content = file.read()
            
            if content.strip() and content.strip() != "Thank you." and content.strip() != "Thanks for watching.":
                with open(event.src_path, 'w') as file:
                    file.write('')

                print("calling AI with: " + content)
                self.callback(content)  # call the passed in function with the content

            else: 
                with open(event.src_path, 'w') as file:
                    file.write('')
            #self.process_events = False
            #self.process_events = True     -> use these when you inevitably need to change how this works. 

    def __init__(self, classifier):
        self.callback = classifier.intake

    def watch_file(self):
        dir_path = '/Volumes/T7/Gekko/gekko/memory/'
        file_path = '/Volumes/T7/Gekko/gekko/memory/todo_stack.txt'

        event_handler = self.MyHandler(file_path, self.callback)
        observer = Observer()
        observer.schedule(event_handler, path=dir_path)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
