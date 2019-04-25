




class Treatment():
    """ Clase para guardar valores de tratamiento """

    def __init__(self):
        self.general_power = 0
        
        self.ch1_laser_power = 0
        self.ch2_laser_power = 0
        self.ch3_laser_power = 0
        self.ch4_laser_power = 0
        self.ch5_laser_power = 0
        self.ch6_laser_power = 0
        self.ch7_laser_power = 0
        self.ch8_laser_power = 0

        self.ch1_led_power = 0
        self.ch2_led_power = 0
        self.ch3_led_power = 0
        self.ch4_led_power = 0
        self.ch5_led_power = 0
        self.ch6_led_power = 0
        self.ch7_led_power = 0
        self.ch8_led_power = 0

        self.alarms = 0
        self.signal = 'cwave'
        self.frequency = 0

        self.treatment_timer = 0
        self.treatment_alarms = 0

        self.treatment_state = 'STOPED'

        #contadores internos
        self.remaining_minutes = 0
        self.remaining_seconds = 0

    """ si setean el power general modifico todos los canales """
    def SetGeneralPower(self, power):
        self.general_power = power
        
        self.ch1_laser_power = power
        self.ch2_laser_power = power
        self.ch3_laser_power = power
        self.ch4_laser_power = power
        self.ch5_laser_power = power
        self.ch6_laser_power = power
        self.ch7_laser_power = power
        self.ch8_laser_power = power
        
        self.ch1_led_power = power
        self.ch2_led_power = power
        self.ch3_led_power = power
        self.ch4_led_power = power
        self.ch5_led_power = power
        self.ch6_led_power = power
        self.ch7_led_power = power
        self.ch8_led_power = power
        

    def GetGeneralPower(self):
        return self.general_power
        
            
    def SetLaserPower(self, channel, power):
        if channel == 'ch1' or channel == 'CH1':
            self.ch1_laser_power = power
        if channel == 'ch2' or channel == 'CH2':
            self.ch2_laser_power = power
        if channel == 'ch3' or channel == 'CH3':
            self.ch3_laser_power = power
        if channel == 'ch4' or channel == 'CH4':
            self.ch4_laser_power = power

        if channel == 'ch5' or channel == 'CH5':
            self.ch5_laser_power = power
        if channel == 'ch6' or channel == 'CH6':
            self.ch6_laser_power = power
        if channel == 'ch7' or channel == 'CH7':
            self.ch7_laser_power = power
        if channel == 'ch8' or channel == 'CH8':
            self.ch8_laser_power = power

            
    def SetLedPower(self, channel, power):
        if channel == 'ch1' or channel == 'CH1':
            self.ch1_led_power = power
        if channel == 'ch2' or channel == 'CH2':
            self.ch2_led_power = power
        if channel == 'ch3' or channel == 'CH3':
            self.ch3_led_power = power
        if channel == 'ch4' or channel == 'CH4':
            self.ch4_led_power = power

        if channel == 'ch5' or channel == 'CH5':
            self.ch5_led_power = power
        if channel == 'ch6' or channel == 'CH6':
            self.ch6_led_power = power
        if channel == 'ch7' or channel == 'CH7':
            self.ch7_led_power = power
        if channel == 'ch8' or channel == 'CH8':
            self.ch8_led_power = power

            
    def GetLaserPower(self, channel):
        if channel == 'ch1' or channel == 'CH1':
            local = self.ch1_laser_power
        if channel == 'ch2' or channel == 'CH2':
            local = self.ch2_laser_power
        if channel == 'ch3' or channel == 'CH3':
            local = self.ch3_laser_power
        if channel == 'ch4' or channel == 'CH4':
            local = self.ch4_laser_power

        if channel == 'ch5' or channel == 'CH5':
            local = self.ch5_laser_power
        if channel == 'ch6' or channel == 'CH6':
            local = self.ch6_laser_power
        if channel == 'ch7' or channel == 'CH7':
            local = self.ch7_laser_power
        if channel == 'ch8' or channel == 'CH8':
            local = self.ch8_laser_power
            
        return local

    def GetLedPower(self, channel):
        if channel == 'ch1' or channel == 'CH1':
            local = self.ch1_led_power
        if channel == 'ch2' or channel == 'CH2':
            local = self.ch2_led_power
        if channel == 'ch3' or channel == 'CH3':
            local = self.ch3_led_power
        if channel == 'ch4' or channel == 'CH4':
            local = self.ch4_led_power

        if channel == 'ch5' or channel == 'CH5':
            local = self.ch5_led_power
        if channel == 'ch6' or channel == 'CH6':
            local = self.ch6_led_power
        if channel == 'ch7' or channel == 'CH7':
            local = self.ch7_led_power
        if channel == 'ch8' or channel == 'CH8':
            local = self.ch8_led_power
            
        return local

    
    def SetSignal (self, new_signal):
        if (new_signal == 'CWAVE') or (new_signal == 'PULSED') or (new_signal == 'MODULATED'):
            self.signal = new_signal

    def GetSignal (self):
        return self.signal

    def ConvertPower (self, power):
        """ power me llega de 0 a 100, tipo %, lo convierto a 255 """
        dummy = power * 255 / 100
        return int(dummy)

    def SetTreatmentTimer (self, new_time):
        self.treatment_timer = new_time

    def SetTreatmentAlarms (self, new_alarms):
        self.treatment_alarms = new_alarms

    def GetTreatmentTimer (self):
        return self.treatment_timer

    def GetTreatmentAlarms (self):
        return self.treatment_alarms

    
