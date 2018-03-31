from threading import Timer
from time import time
from datetime import datetime

class TimeoutCB():

    def __init__(self, new_time, callback):
        self.t = Timer(new_time, callback)
        self.t.start()
        # self.t.join()

class ContinuousCB():

    def __init__(self, lapse, callback):
        #print (datetime.now())
        self.next_call = time() + lapse
        Timer(self.next_call - time(), self.foo, kwargs=dict(la=lapse,cb=callback)).start()

    def foo (self, la, cb):
        #print (datetime.now())
        self.next_call = self.next_call + la
        #ahora llamo al callback
        cb()
        #ahora activo de nuevo
        Timer(self.next_call - time(), self.foo, kwargs=dict(la=la,cb=cb)).start()
        
        
