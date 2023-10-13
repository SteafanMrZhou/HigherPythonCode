class CustomEventLoop:

    def __init__(self):
        self.listen_events_ary = []
        self.callbacks = {}
        self.timeout = None

    def register_event(self, event, callback):
        self.listen_events_ary.append(event)
        self.callbacks[event] = callback


def process_events(self, events):
    for event in events:
        self.callbacks[event](event)


def unregister_event(self, event):
    self.listen_events_ary.remove(event)
    del self.callbacks[event]


# def start_listen_loop(self):
#     while True:
#         events_happend = poll_events(listen_events_ary, timeout)
#         self.process_events(events_happend)
#
#
# loop = CustomEventLoop()
# loop.register_event(tmepEventObj, callback)
# loop.start_listen_loop()
