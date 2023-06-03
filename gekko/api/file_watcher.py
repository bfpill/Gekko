import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import threading
import queue

class FileWatcher:
    class MyHandler(FileSystemEventHandler):
        def __init__(self, filename, queue):
            self.filename = filename
            self.queue = queue

        def on_modified(self, event):
            if event.src_path.endswith(self.filename):
                self.queue.put(event.src_path)  # put the file path in the queue

    class WorkerThread(threading.Thread):
        def __init__(self, queue, callback):
            super().__init__()
            self.queue = queue
            self.callback = callback

        def run(self):
            while True:
                file_path = self.queue.get()  # block until an item is available
                with open(file_path, 'r+') as file:
                    content = file.read()
                self.callback(content)
                with open(file_path, 'r') as file:
                    entire_file = file.read()
                entire_file = entire_file.replace(content, '')
                with open(file_path, 'w') as file:
                    file.write(entire_file)
                self.queue.task_done()

    def __init__(self, callback):
        self.callback = callback
        self.queue = queue.Queue()
        self.worker = self.WorkerThread(self.queue, callback)
        self.worker.start()

    def watch_file(self):
        dir_path = '/Volumes/T7/Gekko/gekko/memory/'
        file_path = '/Volumes/T7/Gekko/gekko/memory/todo_stack.txt'

        event_handler = self.MyHandler(file_path, self.queue)
        observer = Observer()
        observer.schedule(event_handler, path=dir_path)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
