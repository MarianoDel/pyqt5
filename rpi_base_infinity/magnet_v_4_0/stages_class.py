

class Stages():
    """ Class for save stages data """

    def __init__(self):
        ## Default Parameters
        self.timer = 0
        self.power = 0
        self.signal = 'None'
        self.frequency = 'None'
        self.status = 'disable'


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
        return self.StageDataToStr()

    
    def __str__(self):
        return self.StageDataToStr()        

    
    def StageDataToStr (self):
        if self.signal == 'sinusoidal':
            signal_conv = 'S'
        elif self.signal == 'triangular':
            signal_conv = 'T'
        elif self.signal == 'square':
            signal_conv = 'R'
        else:
            signal_conv = 'N'

        freq_conv = self.StageFreqIndexToValue(self.frequency)
            
        return str(self.time) + "' " + signal_conv + ' ' + str(self.power) + '% ' + freq_conv

    
    def StageFreqIndexToValue (self, freq_index_str):
        freq_value_str = 'None'
        
        if freq_index_str == 'freq1':
            freq_value_str = '0.98Hz'
        elif freq_index_str == 'freq2':
            freq_value_str = '1.96Hz'
        elif freq_index_str == 'freq3':
            freq_value_str = '3.92Hz'
        elif freq_index_str == 'freq4':
            freq_value_str = '7.83Hz'
        elif freq_index_str == 'freq5':
            freq_value_str = '11.79Hz'
        elif freq_index_str == 'freq6':
            freq_value_str = '16.67Hz'
        elif freq_index_str == 'freq7':
            freq_value_str = '23.58Hz'
        elif freq_index_str == 'freq8':
            freq_value_str = '30.80Hz'
        elif freq_index_str == 'freq9':
            freq_value_str = '62.64Hz'
        elif freq_index_str == 'freq10':
            freq_value_str = '86.22Hz'

        return freq_value_str
    

### end of file ###
