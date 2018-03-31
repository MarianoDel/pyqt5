import datetime, threading, time

next_call = time.time()

def foo(elapsed):
  global next_call
  print (datetime.datetime.now())
  next_call = next_call+elapsed
  threading.Timer( next_call - time.time(), foo, [elapsed] ).start()

foo(10)
