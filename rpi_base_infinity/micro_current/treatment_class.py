import configparser


class Treatment():
    """ Config Params Class """

    def __init__(self):
        ## Parametros por Default
        # actual soft version
        self.current_version = 'Micro Current ver 3.0'

        # OS running
        self.current_system = ''

        # - Date & Time - localization
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
        

    def ReadConfigFile (self):
        config = configparser.RawConfigParser()
        config.read('config.txt')

        self.audio_selected = config.get('static_config', 'audio_selected', fallback = 'full')

        # tsaver = config.get('static_config', 'timeout_screensaver', fallback = '300')
        # self.timeout_screensaver = int(tsaver)

        self.localization = config.get('static_config', 'localization', fallback='usa')
        

    def SaveConfigFile (self):
        config = configparser.RawConfigParser()

        config.add_section('static_config')
        config.set('static_config', 'localization', self.localization)
        config.set('static_config', 'audio_selected', self.audio_selected)        
        
        # Writing our configuration file to 'example.cfg'
        with open('config.txt', 'w') as configfile:
            config.write(configfile)
            


### end of file ###
