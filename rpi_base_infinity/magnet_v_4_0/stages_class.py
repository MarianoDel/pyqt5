

class Stages():
    """ Class for save stages data """

    def __init__(self):
        ## Default Parameters
        self.timer = 0
        self.power = 0
        self.signal = 'None'
        self.frequency = 'None'
        self.status = 'Clear'


    def SetStageTimer (self, new_time):
        self.timer = new_time

    def GetStageTimer (self):
        return self.timer

    def SetStagePower(self, pwr):
        self.power = pwr

    def GetStagePower(self):
        return self.power

    def SetStageSignal (self, snl):
        self.signal = snl
        
    def GetStageSignal (self):
        return self.signal
            
    def SetStageFrequency(self, fq):
        self.frequency = fq

    def GetStageFrequency(self):
        return self.frequency

    def SetStageStatus(self, st):
        self.status = st

    def GetStageStatus(self):
        return self.status

    def __repr__(self): 
        return "Time: " + str(self.timer) + " Power: " + str(self.power) + \
            " Signal: " + self.signal + " Freq: " + self.frequency + " Status: " + self.status
    
    def __str__(self):
        return "Time: " + str(self.timer) + " Power: " + str(self.power) + \
            " Signal: " + self.signal + " Freq: " + self.frequency + " Status: " + self.status


### end of file ###
