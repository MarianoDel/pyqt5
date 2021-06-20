import configparser



class Treatment():
    """ Clase para guardar valores de tratamiento """

    def __init__(self):
        ## Parametros por Default
        self.power_red = 70
        self.power_ired = 70
        self.max_power_red = 100
        self.max_power_ired = 100        
        self.min_power = 10
        self.signal = 'None'

        self.treatment_timer = 20

        self.pulse_max = 2000
        self.pulse_min = 10
        self.pulse_duration = 2000
        
        self.pannel_a = True
        self.pannel_b = True
        self.pannel_c = True
        self.pannel_d = True
        self.pannel_e = True

        self.steps_in_treatment = 1
        self.steps_pause_in_treatment = False

        self.treatment_state = 'STOP'

        #contadores internos
        self.remaining_minutes = 0
        self.remaining_seconds = 0

        # version actual de soft
        self.current_version = 'Stretcher_ver_1_0'

        # tipo de OS donde corre
        self.current_system = ''

        # donde se ejecuta el programa - Date & Time -
        self.localization = ''

        # how much wait before launch the screensaver
        # self.timeout_screensaver = 60 * 10
        self.timeout_screensaver = 30      
        
        self.ReadConfigFile()


    def SetCurrentSystem (self, system):
        self.current_system = system

    def GetCurrentSystem (self):
        return self.current_system

    def SetLocalization (self, locali):
        self.localization = locali

    def GetLocalization (self):
        return self.localization
    
    def SetCurrentVersion (self, version):
        self.current_version = version
        
    def SetCurrentVersion (self, version):
        self.current_version = version

    def SetSignal (self, snl):
        self.signal = snl
        
    def GetSignal (self):
        return self.signal
            
    def SetPowerRed (self, pwr):
        self.power_red = pwr

    def GetPowerRed (self):
        return self.power_red

    def SetPowerIRed (self, pwr):
        self.power_ired = pwr

    def GetPowerIRed (self):
        return self.power_ired

    def SetPulseDuration (self, pulse_time):
        self.pulse_duration = pulse_time

    def GetPulseDuration (self):
        return self.pulse_duration
    
    def GetPowerLimit (self, signal):
        if signal == 'triangular':
            return self.triangular_power_limit
        elif signal == 'square':
            return self.square_power_limit
        else:
            return self.sinusoidal_power_limit
    
    def SetFrequency(self, fq):
        self.frequency = fq

    def GetFrequency(self):
        return self.frequency
    
    def SetTreatmentTimer (self, new_time):
        self.treatment_timer = new_time

    def GetTreatmentTimer (self):
        return self.treatment_timer

    def EnablePannelsInTreatment (self, pannel):
        if (pannel == 'pannel_a'):
            self.pannel_a = True
        if (pannel == 'pannel_b'):
            self.pannel_b = True
        if (pannel == 'pannel_c'):
            self.pannel_c = True
        if (pannel == 'pannel_d'):
            self.pannel_d = True
        if (pannel == 'pannel_e'):
            self.pannel_e = True

    def DisablePannelsInTreatment (self, pannel):
        if (pannel == 'pannel_a'):
            self.pannel_a = False
        if (pannel == 'pannel_b'):
            self.pannel_b = False
        if (pannel == 'pannel_c'):
            self.pannel_c = False
        if (pannel == 'pannel_d'):
            self.pannel_d = False
        if (pannel == 'pannel_e'):
            self.pannel_e = False

    def GetPannelsInTreatment (self, pannel):
        if (pannel == 'pannel_a'):
            return self.pannel_a
        if (pannel == 'pannel_b'):
            return self.pannel_b
        if (pannel == 'pannel_c'):
            return self.pannel_c
        if (pannel == 'pannel_d'):
            return self.pannel_d
        if (pannel == 'pannel_e'):
            return self.pannel_e
        
    def SetSteps (self, how_many):
        self.steps_in_treatment = how_many
        
    def GetSteps (self):
        return self.steps_in_treatment
        

    def ReadConfigFile (self):
        config = configparser.RawConfigParser()
        config.read('config.txt')
        t_pwr = config.get('power_limits', 'triangular', fallback = '100')
        sq_pwr = config.get('power_limits', 'square', fallback = '100')
        sin_pwr = config.get('power_limits', 'sinusoidal', fallback = '100')
        self.triangular_power_limit = int(t_pwr)
        self.square_power_limit = int(sq_pwr)
        self.sinusoidal_power_limit = int(sin_pwr)

        p_curr = config.get('static_params', 'peak_current', fallback = '3.6')
        r065 = config.get('static_params', 'resistance065', fallback = '47')
        r080 = config.get('static_params', 'resistance080', fallback = '23.5')
        t065 = config.get('static_params', 'tempcoef065', fallback = '0.2627')
        t080 = config.get('static_params', 'tempcoef080', fallback = '0.2627')
        ta = config.get('static_params', 'tempamb', fallback = '25')        
        self.peak_current = float(p_curr)        
        self.resistance065 = float(r065)
        self.resistance080 = float(r080)
        self.tempcoef065 = float(t065)
        self.tempcoef080 = float(t080)
        self.tempamb = float(ta)

        self.mem1_signal = config.get('mem1', 'signal', fallback = 'None')
        self.mem1_treat_time = config.get('mem1', 'time', fallback = 'None')
        self.mem1_power_red = config.get('mem1', 'power_red', fallback = 'None')
        self.mem1_power_ired = config.get('mem1', 'power_ired', fallback = 'None')
        self.mem1_pannels = config.get('mem1', 'pannels', fallback = 'None')
        self.mem1_steps = config.get('mem1', 'steps', fallback = 'None')
        self.mem1_pulse_duration = config.get('mem1', 'pulse_duration', fallback = 'None')

        self.mem2_signal = config.get('mem2', 'signal', fallback = 'None')
        self.mem2_treat_time = config.get('mem2', 'time', fallback = 'None')
        self.mem2_power_red = config.get('mem2', 'power_red', fallback = 'None')
        self.mem2_power_ired = config.get('mem2', 'power_ired', fallback = 'None')
        self.mem2_pannels = config.get('mem2', 'pannels', fallback = 'None')        
        self.mem2_steps = config.get('mem2', 'steps', fallback = 'None')
        self.mem2_pulse_duration = config.get('mem2', 'pulse_duration', fallback = 'None')

        self.mem3_signal = config.get('mem3', 'signal', fallback = 'None')
        self.mem3_treat_time = config.get('mem3', 'time', fallback = 'None')
        self.mem3_power_red = config.get('mem3', 'power_red', fallback = 'None')
        self.mem3_power_ired = config.get('mem3', 'power_ired', fallback = 'None')
        self.mem3_pannels = config.get('mem3', 'pannels', fallback = 'None')        
        self.mem3_steps = config.get('mem3', 'steps', fallback = 'None')
        self.mem3_pulse_duration = config.get('mem3', 'pulse_duration', fallback = 'None')
        

    def SaveConfigFile (self):
        config = configparser.RawConfigParser()

        config.add_section('power_limits')
        config.set('power_limits', 'triangular', str(self.triangular_power_limit))
        config.set('power_limits', 'square', str(self.square_power_limit))
        config.set('power_limits', 'sinusoidal', str(self.sinusoidal_power_limit))

        config.add_section('static_params')
        config.set('static_params', 'peak_current', str(self.peak_current))
        config.set('static_params', 'resistance065', str(self.resistance065))
        config.set('static_params', 'resistance080', str(self.resistance080))
        config.set('static_params', 'tempcoef065', str(self.tempcoef065))
        config.set('static_params', 'tempcoef080', str(self.tempcoef080))
        config.set('static_params', 'tempamb', str(self.tempamb))

        config.add_section('mem1')
        config.set('mem1', 'signal', self.mem1_signal)
        config.set('mem1', 'time', self.mem1_treat_time)
        config.set('mem1', 'power_red', self.mem1_power_red)
        config.set('mem1', 'power_ired', self.mem1_power_ired)
        config.set('mem1', 'pannels', self.mem1_pannels)
        config.set('mem1', 'steps', self.mem1_steps)
        config.set('mem1', 'pulse_duration', self.mem1_pulse_duration)        

        config.add_section('mem2')
        config.set('mem2', 'signal', self.mem2_signal)
        config.set('mem2', 'time', self.mem2_treat_time)
        config.set('mem2', 'power_red', self.mem2_power_red)
        config.set('mem2', 'power_ired', self.mem2_power_ired)
        config.set('mem2', 'pannels', self.mem2_pannels)
        config.set('mem2', 'steps', self.mem2_steps)
        config.set('mem2', 'pulse_duration', self.mem2_pulse_duration)        

        config.add_section('mem3')
        config.set('mem3', 'signal', self.mem3_signal)
        config.set('mem3', 'time', self.mem3_treat_time)
        config.set('mem3', 'power_red', self.mem3_power_red)
        config.set('mem3', 'power_ired', self.mem3_power_ired)
        config.set('mem3', 'pannels', self.mem3_pannels)
        config.set('mem3', 'steps', self.mem3_steps)
        config.set('mem3', 'pulse_duration', self.mem3_pulse_duration)        
        
        # Writing our configuration file to 'example.cfg'
        with open('config.txt', 'w') as configfile:
            config.write(configfile)
            

    def MoveCurrentConfToMem (self, which_mem):
        if which_mem == 'mem1':
            self.mem1_signal = self.signal
            self.mem1_treat_time = str(self.treatment_timer)
            self.mem1_power_red = str(self.power_red)
            self.mem1_power_ired = str(self.power_ired)
            self.mem1_pannels = self.Parse_Pannels()
            self.mem1_steps = self.Parse_Steps()
            self.mem1_pulse_duration = str(self.pulse_duration)

        if which_mem == 'mem2':
            self.mem2_signal = self.signal
            self.mem2_treat_time = str(self.treatment_timer)
            self.mem2_power_red = str(self.power_red)
            self.mem2_power_ired = str(self.power_ired)            
            self.mem2_pannels = self.Parse_Pannels()
            self.mem2_steps = self.Parse_Steps()
            self.mem2_pulse_duration = str(self.pulse_duration)

        if which_mem == 'mem3':
            self.mem3_signal = self.signal
            self.mem3_treat_time = str(self.treatment_timer)
            self.mem3_power_red = str(self.power_red)
            self.mem3_power_ired = str(self.power_ired)            
            self.mem3_pannels = self.Parse_Pannels()
            self.mem3_steps = self.Parse_Steps()
            self.mem3_pulse_duration = str(self.pulse_duration)


    def EmptyMem (self, which_mem):
        if which_mem == 'mem1':
            self.mem1_signal = 'None'
            self.mem1_treat_time = 'None'
            self.mem1_power_red = 'None'
            self.mem1_power_ired = 'None'
            self.mem1_pannels = 'None'
            self.mem1_steps = 'None'
            self.mem1_pulse_duration = 'None'

        if which_mem == 'mem2':
            self.mem2_signal = 'None'
            self.mem2_treat_time = 'None'
            self.mem2_power_red = 'None'
            self.mem2_power_ired = 'None'            
            self.mem2_pannels = 'None'
            self.mem2_steps = 'None'
            self.mem2_pulse_duration = 'None'

        if which_mem == 'mem3':
            self.mem3_signal = 'None'
            self.mem3_treat_time = 'None'
            self.mem3_power_red = 'None'
            self.mem3_power_ired = 'None'            
            self.mem3_pannels = 'None'
            self.mem3_steps = 'None'
            self.mem3_pulse_duration = 'None'
            

    def Parse_Pannels (self):
        pannels_str = ''
        if self.GetPannelsInTreatment('pannel_a') == True:
            pannels_str += 'A'
        if self.GetPannelsInTreatment('pannel_b') == True:
            pannels_str += 'B'
        if self.GetPannelsInTreatment('pannel_c') == True:
            pannels_str += 'C'
        if self.GetPannelsInTreatment('pannel_d') == True:
            pannels_str += 'D'
        if self.GetPannelsInTreatment('pannel_e') == True:
            pannels_str += 'E'

        return pannels_str


    def Parse_Steps (self):
        steps_str = str(self.steps_in_treatment)
        if self.steps_pause_in_treatment == True:
            steps_str += 'P'

        return steps_str

        
        
            

### end of file ###
