

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
        signal_conv = self.StageSignalToChar(self.signal)
        freq_conv = self.StageFreqIndexToValue(self.frequency)
            
        return str(self.timer) + "' " + signal_conv + ' ' + str(self.power) + '% ' + freq_conv

    
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

    
    def StageFreqValueToIndex (self, freq_value_str):
        freq_index_str = 'None'
        
        if freq_value_str == '0.98Hz':
            freq_index_str = 'freq1'
        elif freq_value_str == '1.96Hz':
            freq_index_str = 'freq2'
        elif freq_value_str == '3.92Hz':
            freq_index_str = 'freq3'
        elif freq_value_str == '7.83Hz':
            freq_index_str = 'freq4'
        elif freq_value_str == '11.79Hz':
            freq_index_str = 'freq5'
        elif freq_value_str == '16.67Hz':
            freq_index_str = 'freq6'
        elif freq_value_str == '23.58Hz':
            freq_index_str = 'freq7'
        elif freq_value_str == '30.80Hz':
            freq_index_str = 'freq8'
        elif freq_value_str == '62.64Hz':
            freq_index_str = 'freq9'
        elif freq_value_str == '86.22Hz':
            freq_index_str = 'freq10'

        return freq_index_str


    def StageCharToSignal (self, symbol_char):
        if symbol_char == 'S':
            signal_str = 'sinusoidal'
        elif symbol_char == 'T':
            signal_str = 'triangular'
        elif symbol_char == 'R':
            signal_str = 'square'
        else:
            signal_str = 'None'

        return signal_str

    
    def StageSignalToChar (self, signal_str):
        if signal_str == 'sinusoidal':
            signal_char = 'S'
        elif signal_str == 'triangular':
            signal_char = 'T'
        elif signal_str == 'square':
            signal_char = 'R'
        else:
            signal_char = 'N'

        return signal_char

### end of file ###
