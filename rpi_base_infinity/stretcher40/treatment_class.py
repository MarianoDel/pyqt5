import configparser


class Treatment():
    """ Clase para guardar valores de tratamiento """

    def __init__(self):
        ## Parametros por Default
        # no current stages info in treatment
        # self.stage1_info = 'None'
        # self.stage2_info = 'None'
        # self.stage3_info = 'None'

        # no current stages info in treatment
        # self.stage_current_dict = {
        #     'stage1' : "15' S 35% 7.83Hz",
        #     'stage2' : "15' S 35% 7.83Hz",
        #     'stage3' : "15' S 35% 7.83Hz"
        #     }

        ## this two will be overrided by ReadConfigFile()
        self.mem_instant_dict = {
            'mema' : ['Arm and Leg Inflammatory', "15' S 35% 7.83Hz", '', ''],
            'memb' : ['Arm and Leg Inflammatory', "15' S 35% 7.83Hz", '', ''],
            'memc' : ['Arm and Leg Inflammatory', "15' S 35% 7.83Hz", '', ''],
            'memd' : ['', '', '', '']
            }

        self.mem_all_dict = {
            'mema' : ['Arm and Leg Inflammatory', "15' S 35% 7.83Hz", '', ''],
            'memb' : ['Arm and Leg Inflammatory', "15' S 35% 7.83Hz", '', ''],
            'memc' : ['Arm and Leg Inflammatory', "15' S 35% 7.83Hz", '', ''],
            'memd' : ['', '', '', ''],
            'mem5' : ['', '', '', ''],
            'mem6' : ['', '', '', ''],
            'mem7' : ['', '', '', ''],
            'mem8' : ['', '', '', ''],
            'mem9' : ['', '', '', ''],
            'mem10' : ['', '', '', ''],
            'mem11' : ['', '', '', ''],
            'mem12' : ['', '', '', ''],
            'mem13' : ['', '', '', ''],
            'mem14' : ['', '', '', ''],
            'mem15' : ['', '', '', ''],
            'mem16' : ['', '', '', ''],
            'mem17' : ['', '', '', ''],
            'mem18' : ['', '', '', ''],
            'mem19' : ['', '', '', ''],
            'mem20' : ['', '', '', '']
            }
            
        self.max_power = 100
        self.min_power = 10
        self.max_treatment_timer = 120
        self.min_treatment_timer = 1

        self.ch1 = True
        self.ch2 = True
        self.ch3 = True
        self.updwn = True
        self.treatment_state = 'STOP'

        #contadores internos
        self.remaining_minutes = 0
        self.remaining_seconds = 0

        # version actual de soft
        self.current_version = 'Magnet_ver_4_0'

        # tipo de OS donde corre
        self.current_system = ''

        # donde se ejecuta el programa - Date & Time -
        self.localization = ''

        # how much wait before launch the screensaver
        # self.timeout_screensaver = 60 * 10
        self.timeout_screensaver = 60 * 5
        
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
        
    def GetCurrentVersion (self):
        return self.current_version

    def SetSignal (self, snl):
        self.signal = snl
        
    def GetSignal (self):
        return self.signal
            
    def SetPower(self, pwr):
        self.power = pwr

    def GetPower(self):
        return self.power

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

    def SetUpDwnStretcher(self, updwn_mode):
        if updwn_mode:
            self.updwn = True
        else:
            self.updwn = False

    def GetUpDwnStretcher(self):
        return self.updwn
    
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
        treat = "signal,"

        if self.signal == 'triangular':
            new_power = int(self.triangular_power_limit * self.power / 100)
            if new_power < 10:
                new_power = 10
                
            treat += "{:03d},{:03d},0000,".format(new_power, new_power)

            # rising edge, maintenance, falling edge, stop time 
            if self.frequency == '7.83Hz':
                treat += '0061,0001,0001,0064,0000,0000,1'
            if self.frequency == '11.79Hz':
                treat += '0040,0001,0001,0043,0000,0000,1'
            if self.frequency == '16.67Hz':
                treat += '0028,0001,0001,0030,0000,0000,1'
            if self.frequency == '23.58Hz':
                treat += '0019,0001,0001,0021,0000,0000,1'
            if self.frequency == '30.80Hz':
                treat += '0014,0001,0001,0016,0000,0000,1'
            if self.frequency == '62.64Hz':
                treat += '0006,0001,0001,0008,0000,0000,1'

        if self.signal == 'sinusoidal':
            new_power = int(self.sinusoidal_power_limit * self.power / 100)
            if new_power < 10:
                new_power = 10
                
            treat += "{:03d},{:03d},0000,".format(new_power, new_power)

            # rising edge, maintenance, falling edge, stop time 
            if self.frequency == '7.83Hz':
                treat += '0021,0021,0021,0064,0000,0000,1'
            if self.frequency == '11.79Hz':
                treat += '0014,0014,0014,0043,0000,0000,1'
            if self.frequency == '16.67Hz':
                treat += '0010,0010,0010,0030,0000,0000,1'
            if self.frequency == '23.58Hz':
                treat += '0007,0007,0007,0021,0000,0000,1'
            if self.frequency == '30.80Hz':
                treat += '0005,0006,0005,0016,0000,0000,1'
            if self.frequency == '62.64Hz':
                treat += '0003,0002,0003,0008,0000,0000,1'

        if self.signal == 'square':
            new_power = int(self.square_power_limit * self.power / 100)
            if new_power < 10:
                new_power = 10
                
            treat += "{:03d},{:03d},0000,".format(new_power, new_power)

            # rising edge, maintenance, falling edge, stop time 
            if self.frequency == '7.83Hz':
                treat += '0001,0061,0001,0064,0000,0000,1'
            if self.frequency == '11.79Hz':
                treat += '0001,0040,0001,0043,0000,0000,1'
            if self.frequency == '16.67Hz':
                treat += '0001,0028,0001,0030,0000,0000,1'
            if self.frequency == '23.58Hz':
                treat += '0001,0019,0001,0021,0000,0000,1'
            if self.frequency == '30.80Hz':
                treat += '0001,0014,0001,0016,0000,0000,1'
            if self.frequency == '62.64Hz':
                treat += '0001,0006,0001,0008,0000,0000,1'        

        return treat

    
    def GetMagnetoDurationString (self):
        treat_time = 'duration,00,{:02d},00,1'.format(self.treatment_timer)
        return treat_time
        

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

        ## get all memories config or defaults
        mem_all_dict_index = self.mem_all_dict
        for mem_index in mem_all_dict_index:
            to_save_lst = ['','','','']
            to_save_lst[0] = config.get(mem_index, 'desc', fallback = '')
            to_save_lst[1] = config.get(mem_index, 'one', fallback = '')
            to_save_lst[2] = config.get(mem_index, 'two', fallback = '')
            to_save_lst[3] = config.get(mem_index, 'three', fallback = '')
            self.mem_all_dict[mem_index] = to_save_lst
            print('in ' + mem_index)
            print(self.mem_all_dict[mem_index])

        ## get instant access memory config from all
        mem_instant_index = self.mem_instant_dict
        for mem_index in mem_instant_index:
            self.mem_instant_dict[mem_index] = self.mem_all_dict[mem_index]

        print(self.mem_instant_dict)
        # self.mem1_frequency = config.get('mem1', 'frequency', fallback = 'None')
        # self.mem1_signal = config.get('mem1', 'signal', fallback = 'None')
        # self.mem1_treat_time = config.get('mem1', 'time', fallback = 'None')
        # self.mem1_power = config.get('mem1', 'power', fallback = 'None')

        # self.mem2_frequency = config.get('mem2', 'frequency', fallback = 'None')
        # self.mem2_signal = config.get('mem2', 'signal', fallback = 'None')
        # self.mem2_treat_time = config.get('mem2', 'time', fallback = 'None')
        # self.mem2_power = config.get('mem2', 'power', fallback = 'None')

        # self.mem3_frequency = config.get('mem3', 'frequency', fallback = 'None')
        # self.mem3_signal = config.get('mem3', 'signal', fallback = 'None')
        # self.mem3_treat_time = config.get('mem3', 'time', fallback = 'None')
        # self.mem3_power = config.get('mem3', 'power', fallback = 'None')

        self.localization = config.get('static_config', 'localization', fallback='usa')

        
        

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

        ## save all memory dict
        for mem_index in self.mem_all_dict:
            config.add_section(mem_index)
            to_save_lst = self.mem_all_dict[mem_index]
            config.set(mem_index, 'desc', to_save_lst[0])
            config.set(mem_index, 'one', to_save_lst[1])
            config.set(mem_index, 'two', to_save_lst[2])
            config.set(mem_index, 'three', to_save_lst[3])

        # config.add_section('mem2')
        # config.set('mem2', 'frequency', self.mem2_frequency)
        # config.set('mem2', 'signal', self.mem2_signal)
        # config.set('mem2', 'time', self.mem2_treat_time)
        # config.set('mem2', 'power', self.mem2_power)

        # config.add_section('mem3')
        # config.set('mem3', 'frequency', self.mem3_frequency)
        # config.set('mem3', 'signal', self.mem3_signal)
        # config.set('mem3', 'time', self.mem3_treat_time)
        # config.set('mem3', 'power', self.mem3_power)

        config.add_section('static_config')
        config.set('static_config', 'localization', self.localization)
        
        # Writing our configuration file to 'example.cfg'
        with open('config.txt', 'w') as configfile:
            config.write(configfile)
            

    def MoveCurrentConfToMem (self, which_mem):
        if which_mem == 'mem1':
            self.mem1_frequency = self.frequency
            self.mem1_signal = self.signal
            self.mem1_treat_time = str(self.treatment_timer)
            self.mem1_power = str(self.power)

        if which_mem == 'mem2':
            self.mem2_frequency = self.frequency
            self.mem2_signal = self.signal
            self.mem2_treat_time = str(self.treatment_timer)
            self.mem2_power = str(self.power)

        if which_mem == 'mem3':
            self.mem3_frequency = self.frequency
            self.mem3_signal = self.signal
            self.mem3_treat_time = str(self.treatment_timer)
            self.mem3_power = str(self.power)


    def EmptyMem (self, which_mem):
        if which_mem == 'mem1':
            self.mem1_frequency = 'None'
            self.mem1_signal = 'None'
            self.mem1_treat_time = 'None'
            self.mem1_power = 'None'

        if which_mem == 'mem2':
            self.mem2_frequency = 'None'
            self.mem2_signal = 'None'
            self.mem2_treat_time = 'None'
            self.mem2_power = 'None'

        if which_mem == 'mem3':
            self.mem3_frequency = 'None'
            self.mem3_signal = 'None'
            self.mem3_treat_time = 'None'
            self.mem3_power = 'None'
            

    # def StageInfoToString (self, stage_obj):
    #     stage_obj.

### end of file ###
