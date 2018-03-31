from timers_module import ContinuousCB

def MyCallback():
    print ("Hi!")

ctimer = ContinuousCB(3, MyCallback)

while (True):
    pass
