




class Treatment():
    """ Clase para guardar valores de tratamiento """

    def __init__(self):
        self.power = 70

        self.signal = 'triangular'

        self.frequency = '10Hz'

        self.treatment_timer = 30
        self.treatment_alarms = 0

        self.treatment_state = 'STOP'

        self.ch1 = True
        self.ch2 = True
        self.ch3 = True

        #contadores internos
        self.remaining_minutes = 0
        self.remaining_seconds = 0


    def SetSignal (self, snl):
        self.signal = snl

    def GetSignal (self):
        return self.signal
            
    def SetPower(self, pwr):
        self.power = pwr

    def GetPower(self):
        return self.power

    def SetFrequency(self, fq):
        self.frequency = fq

    def GetFrequency(self):
        return self.frequency
                
    def SetTreatmentTimer (self, new_time):
        self.treatment_timer = new_time

    def GetTreatmentTimer (self):
        return self.treatment_timer

    def EnableChannelsInTreatment (self, ch):
        if (ch == 'ch1'):
            self.ch1 = True
        if (ch == 'ch2'):
            self.ch2 = True
        if (ch == 'ch3'):
            self.ch3 = True

    def DisableChannelsInTreatment (self, ch):
        if (ch == 'ch1'):
            self.ch1 = False
        if (ch == 'ch2'):
            self.ch2 = False
        if (ch == 'ch3'):
            self.ch3 = False

    def GetChannelInTreatment (self, ch):
        if (ch == 'ch1'):
            return self.ch1
        if (ch == 'ch2'):
            return self.ch2
        if (ch == 'ch3'):
            return self.ch3
            
        
