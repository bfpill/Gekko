import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from gekko.api.classifier import intake
import os

class MyHandler(FileSystemEventHandler):
    def __init__(self, filename):
        self.filename = filename
    
    def on_modified(self, event):
        if event.src_path.endswith(self.filename):
            with open(event.src_path, 'r+') as file:
                content = file.read()
            intake(content)  # or do whatever you want with the content

def watch_file():
    dir_path = '/Volumes/T7/Gekko/gekko/memory/'
    file_path = '/Volumes/T7/Gekko/gekko/memory/todo_stack.txt'

    event_handler = MyHandler(file_path)
    observer = Observer()
    observer.schedule(event_handler, path=dir_path)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

