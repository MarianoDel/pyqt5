




class Treatment():
    """ Clase para guardar valores de tratamiento """

    def __init__(self):
        ## Parametros por Default
        self.power = 70
        self.max_power = 100
        self.min_power = 10
        self.signal = 'None'
        self.frequency = 'None'
        self.treatment_timer = 60
        self.max_treatment_timer = 120
        self.min_treatment_timer = 1
        self.ch1 = True
        self.ch2 = True
        self.ch3 = True
        self.treatment_state = 'STOP'

        #contadores internos
        self.remaining_minutes = 0
        self.remaining_seconds = 0

        # version actual de soft
        self.current_version = 'Stretcher_ver_1_0'


    def SetCurrentVersion (self, version):
        self.current_version = version

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

    def GetMagnetoFreqSignalPowerString (self):
        """ 
            Devuelve un string con toda la info combinada para el Magneto viejo 
            "signal,%03d,%03d,0%x%x%d,%04d,%04d,%04d,%04d,%04d,%04d,1\r\n"
            example. signal,100,100,0000,0003,0003,0003,0006,0000,0000,1
        """
        treat = "signal,{:03d},{:03d},0000,".format(self.power,self.power)

        if self.signal == 'triangular':
            # rising edge, maintenance, falling edge, stop time 
            if self.frequency == '7.83Hz':
                treat += '0061,0001,0001,0064,0000,0000,1'
            if self.frequency == '14.3Hz':
                treat += '0033,0001,0001,0035,0000,0000,1'
            if self.frequency == '20.8Hz':
                treat += '0022,0001,0001,0024,0000,0000,1'
            if self.frequency == '27.3Hz':
                treat += '0016,0001,0001,0019,0000,0000,1'
            if self.frequency == '33.8Hz':
                treat += '0012,0001,0001,0015,0000,0000,1'
            if self.frequency == '62.6Hz':
                treat += '0006,0001,0001,0008,0000,0000,1'

        if self.signal == 'sinusoidal':
            # rising edge, maintenance, falling edge, stop time 
            if self.frequency == '7.83Hz':
                treat += '0021,0021,0021,0064,0000,0000,1'
            if self.frequency == '14.3Hz':
                treat += '0012,0011,0012,0035,0000,0000,1'
            if self.frequency == '20.8Hz':
                treat += '0008,0008,0008,0024,0000,0000,1'
            if self.frequency == '27.3Hz':
                treat += '0006,0006,0006,0019,0000,0000,1'
            if self.frequency == '33.8Hz':
                treat += '0005,0004,0005,0015,0000,0000,1'
            if self.frequency == '62.6Hz':
                treat += '0003,0002,0003,0008,0000,0000,1'

        if self.signal == 'square':
            # rising edge, maintenance, falling edge, stop time 
            if self.frequency == '7.83Hz':
                treat += '0001,0061,0001,0064,0000,0000,1'
            if self.frequency == '14.3Hz':
                treat += '0001,0033,0001,0035,0000,0000,1'
            if self.frequency == '20.8Hz':
                treat += '0001,0022,0001,0024,0000,0000,1'
            if self.frequency == '27.3Hz':
                treat += '0001,0016,0001,0019,0000,0000,1'
            if self.frequency == '33.8Hz':
                treat += '0001,0012,0001,0015,0000,0000,1'
            if self.frequency == '62.6Hz':
                treat += '0001,0006,0001,0008,0000,0000,1'        

        return treat

    def GetMagnetoDurationString (self):
        treat_time = 'duration,00,{:02d},00,1'.format(self.treatment_timer)
        return treat_time
        

        
