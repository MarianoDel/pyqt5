


class AntennaInTreatment():
    """ Class to save the know values for the antennas """

    def __init__(self):
        self.antenna_ch1 = False
        self.antenna_ch2 = False
        self.antenna_ch3 = False
        self.antenna_ch4 = False

        self.antenna_ch1_L = 0.0
        self.antenna_ch2_L = 0.0
        self.antenna_ch3_L = 0.0
        self.antenna_ch4_L = 0.0

        self.antenna_ch1_R = 0.0
        self.antenna_ch2_R = 0.0
        self.antenna_ch3_R = 0.0
        self.antenna_ch4_R = 0.0

        self.antenna_ch1_I = 0.0
        self.antenna_ch2_I = 0.0
        self.antenna_ch3_I = 0.0
        self.antenna_ch4_I = 0.0

        self.antenna_ch1_T = 0.0
        self.antenna_ch2_T = 0.0
        self.antenna_ch3_T = 0.0
        self.antenna_ch4_T = 0.0

        self.name_ch1 = 'unknow'
        self.name_ch2 = 'unknow'
        self.name_ch3 = 'unknow'
        self.name_ch4 = 'unknow'


    # Externals
    def GetLString (self, channel):
        if channel == 'ch1':
            return str(self.antenna_ch1_L)

        if channel == 'ch2':
            return str(self.antenna_ch2_L)

        if channel == 'ch3':
            return str(self.antenna_ch3_L)            

        if channel == 'ch4':
            return str(self.antenna_ch4_L)            

    def GetRString (self, channel):
        if channel == 'ch1':
            return str(self.antenna_ch1_R)

        if channel == 'ch2':
            return str(self.antenna_ch2_R)

        if channel == 'ch3':
            return str(self.antenna_ch3_R)            

        if channel == 'ch4':
            return str(self.antenna_ch4_R)            

    def GetIString (self, channel):
        if channel == 'ch1':
            return str(self.antenna_ch1_I)

        if channel == 'ch2':
            return str(self.antenna_ch2_I)

        if channel == 'ch3':
            return str(self.antenna_ch3_I)            

        if channel == 'ch4':
            return str(self.antenna_ch4_I)            

    def GetTString (self, channel):
        if channel == 'ch1':
            return str(self.antenna_ch1_T)

        if channel == 'ch2':
            return str(self.antenna_ch2_T)

        if channel == 'ch3':
            return str(self.antenna_ch3_T)            

        if channel == 'ch4':
            return str(self.antenna_ch4_T)            
        

    ## Internals
    def setL (self, channel, s_l):
        try:
            new_L = float(s_l)
            if channel == 'ch1':
                self.antenna_ch1_L = new_L

            if channel == 'ch2':
                self.antenna_ch2_L = new_L

            if channel == 'ch3':
                self.antenna_ch3_L = new_L

            if channel == 'ch4':
                self.antenna_ch4_L = new_L
                
        except:
            print ('Noisy Line on antenna float params!')


    def setR (self, channel, s_r):
        try:
            new_R = float(s_r)
            if channel == 'ch1':
                self.antenna_ch1_R = new_R

            if channel == 'ch2':
                self.antenna_ch2_R = new_R

            if channel == 'ch3':
                self.antenna_ch3_R = new_R

            if channel == 'ch4':
                self.antenna_ch4_R = new_R
                
        except:
            print ('Noisy Line on antenna float params!')

    def setI (self, channel, s_i):
        try:
            new_I = float(s_i)
            if channel == 'ch1':
                self.antenna_ch1_I = new_I

            if channel == 'ch2':
                self.antenna_ch2_I = new_I

            if channel == 'ch3':
                self.antenna_ch3_I = new_I

            if channel == 'ch4':
                self.antenna_ch4_I = new_I
                
        except:
            print ('Noisy Line on antenna float params!')

    def setT (self, channel, s_t):
        try:
            new_T = float(s_t)
            if channel == 'ch1':
                self.antenna_ch1_T = new_T

            if channel == 'ch2':
                self.antenna_ch2_T = new_T

            if channel == 'ch3':
                self.antenna_ch3_T = new_T

            if channel == 'ch4':
                self.antenna_ch4_T = new_T
                
        except:
            print ('Noisy Line on antenna float params!')

            
    def setActive (self, channel):
        if channel == 'ch1':
            self.antenna_ch1 = True

        if channel == 'ch2':
            self.antenna_ch2 = True

        if channel == 'ch3':
            self.antenna_ch3 = True

        if channel == 'ch4':
            self.antenna_ch4 = True
            
    
    def SetName (self, channel, new_name):
        if channel == 'ch1':
            self.name_ch1 = new_name

        if channel == 'ch2':
            self.name_ch2 = new_name            

        if channel == 'ch3':
            self.name_ch3 = new_name            

        if channel == 'ch4':
            self.name_ch4 = new_name
        

    def GetActive (self, channel):
        if channel == 'ch1':
            return self.antenna_ch1

        if channel == 'ch2':
            return self.antenna_ch2

        if channel == 'ch3':
            return self.antenna_ch3

        if channel == 'ch4':
            return self.antenna_ch4

    def SetActiveStatus (self, channel, status):
        if channel == 'ch1':
            self.antenna_ch1 = status

        if channel == 'ch2':
            self.antenna_ch2 = status

        if channel == 'ch3':
            self.antenna_ch3 = status

        if channel == 'ch4':
            self.antenna_ch4 = status
        
            
    def Flush (self):
        self.antenna_ch1 = False
        self.antenna_ch2 = False
        self.antenna_ch3 = False
        self.antenna_ch4 = False

        self.name_ch1 = 'unknow'
        self.name_ch2 = 'unknow'
        self.name_ch3 = 'unknow'
        self.name_ch4 = 'unknow'


    def ProcessStringList (self, slist):
        # first check the channel
        ch_list = slist[5].rsplit('\r')
        ch_str = ch_list[0]
        if ch_str == '1':
            channel = 'ch1'

        elif ch_str == '2':
            channel = 'ch2'

        elif ch_str == '3':
            channel = 'ch3'

        elif ch_str == '4':            
            channel = 'ch4'

        else:
            print ("error in antenna parser")
            return

        if slist[0].startswith('ch'):
            print ("no named antenna")
        else:
            print ("antenna name: " + slist[0])
            self.SetName(channel, slist[0])

        self.setL(channel, slist[1])
        self.setR(channel, slist[2])
        self.setI(channel, slist[3])
        self.setT(channel, slist[4])
        self.setActive(channel)

            
            
            
        
        


### end of file ###
