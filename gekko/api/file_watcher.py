import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class FileWatcher:
    class MyHandler(FileSystemEventHandler):
        def __init__(self, filename, callback):
            self.filename = filename
            self.callback = callback
        
        def on_modified(self, event):
            if event.src_path.endswith(self.filename):
                with open(event.src_path, 'r+') as file:
                    content = file.read()
                self.callback(content)  # or do whatever you want with the content

    def __init__(self, callback):
        self.callback = callback
    
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
