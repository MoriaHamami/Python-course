import threading
from queue import Queue

class Stream:
    def __init__(self):
        self.items = Queue()
        self.next_streams = []
        self.is_running = True
        self.funcs_to_run = []
        self.thread = threading.Thread(target=self.run)
        # Open thread once Stream is created
        self.thread.start()

    def run(self):
        while self.is_running:
            # Fetch an item
            item = self.items.get()
            if item is None:
                break
            # Don't let other threads run funcs simultaneously
            with threading.Lock():
                # Run all functions
                for func in self.funcs_to_run:
                    func(item)
            # Indicate that a formerly enqueued item is used
            self.items.task_done()

    def add(self, item):
        self.items.put(item)

    def apply(self, func):
        new_stream = Stream()
        # When running this func, add relevant result to new stream
        def run_func(x):
            y = func(x)
            if y:
                if y is True:
                    new_stream.add(x)
                else:
                    new_stream.add(y)
        self.next_streams.append(new_stream)
        # Run this task on each item in queue when possible
        self.forEach(run_func)
        return new_stream

    def forEach(self, consumer_func):
        # When possible, run this func on each item in queue
        self.funcs_to_run.append(consumer_func)

    def stop(self):
        self.is_running = False
        self.items.put(None)
        self.thread.join()
        for stream in self.next_streams:
            stream.stop()
