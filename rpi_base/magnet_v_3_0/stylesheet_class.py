




class ButtonStyles():
    """ Stylesheet Class for Buttons """
    """ static properties """

    def __init__(self):
        ## Signal buttons StyleSheet
        self.triangular_disable = "background-image: url(:/buttons/resources/Triangular.png);\
                                   background-color: rgb(245, 245, 245);\
                                   border-radius: 10px;\
                                   border:2px solid rgb(55, 52, 53);"


        self.square_disable = "background-image: url(:/buttons/resources/Cuadrada.png);\
                               background-color:  rgb(245, 245, 245);\
                               border-radius: 10px;\
                               border:2px solid rgb(55, 52, 53);"


        self.sinusoidal_disable = "background-image: url(:/buttons/resources/Sinus.png);\
                                   background-color:  rgb(245, 245, 245);\
                                   border-radius: 10px;\
                                   border:2px solid rgb(55, 52, 53);"

        self.triangular_enable = "background-image: url(:/buttons/resources/Triangular.png);\
                                  background-color: rgb(248, 247, 190);\
                                  border-radius: 10px;\
                                  border:2px solid rgb(55, 52, 53);"

        self.square_enable = "background-image: url(:/buttons/resources/Cuadrada.png);\
                              background-color:  rgb(244, 243, 158);\
                              border-radius: 10px;\
                              border:2px solid rgb(55, 52, 53);"

        self.sinusoidal_enable = "background-image: url(:/buttons/resources/Sinus.png);\
                                  background-color: rgb(240, 238, 126);\
                                  border-radius: 10px;\
                                  border:2px solid rgb(55, 52, 53);"

        ## Frequency buttons StyleSheet
        self.freq1_enable = "background-image: url(:/frequencies/resources/7_83Hz.png);\
                             background-color: rgb(221, 202, 222);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq2_enable = "background-image: url(:/frequencies/resources/11_79Hz.png);\
                             background-color: rgb(211, 187, 213);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq3_enable = "background-image: url(:/frequencies/resources/16_67Hz.png);\
                             background-color: rgb(202, 173, 204);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq4_enable = "background-image: url(:/frequencies/resources/23_58Hz.png);\
                             background-color: rgb(196, 161, 203);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq5_enable = "background-image: url(:/frequencies/resources/30_80Hz.png);\
                             background-color: rgb(169, 121, 179);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq6_enable = "background-image: url(:/frequencies/resources/62_64Hz.png);\
                             background-color: rgb(137, 84, 148);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq1_disable = "background-image: url(:/frequencies/resources/7_83Hz.png);\
                             background-color: rgb(245, 245, 245);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq2_disable = "background-image: url(:/frequencies/resources/11_79Hz.png);\
                             background-color: rgb(245, 245, 245);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq3_disable = "background-image: url(:/frequencies/resources/16_67Hz.png);\
                             background-color: rgb(245, 245, 245);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq4_disable = "background-image: url(:/frequencies/resources/23_58Hz.png);\
                             background-color: rgb(245, 245, 245);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq5_disable = "background-image: url(:/frequencies/resources/30_80Hz.png);\
                             background-color: rgb(245, 245, 245);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.freq6_disable = "background-image: url(:/frequencies/resources/62_64Hz.png);\
                             background-color: rgb(245, 245, 245);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"
        

        self.ch_getting = "color: rgb(55, 52, 53);\
                           background-color: rgb(191, 218, 231);\
                           border-radius: 10px;\
                           text-align:top;\
                           border:2px solid rgb(55, 52, 53);"

        self.ch_old_ant = "color: rgb(55, 52, 53);\
                           background-color: rgb(246, 172, 172);\
                           border-radius: 10px;\
                           text-align:top;\
                           border:2px solid rgb(55, 52, 53);"

        self.ch_enable = "color: rgb(55, 52, 53);\
                          background-color: rgb(157, 211, 175);\
                          border-radius: 10px;\
                          text-align:top;\
                          border:2px solid rgb(55, 52, 53);"
        
        self.ch_disable = "color: rgb(55, 52, 53);\
                          background-color: rgb(245, 245, 245);\
                          border-radius: 10px;\
                          text-align:top;\
                          border:2px solid rgb(55, 52, 53);"

        self.start_enable = "background-image: url(:/buttons/resources/Play.png);\
                             color: rgb(55, 52, 53);\
                             background-color: rgb(157, 211, 175);\
                             border-radius: 10px;\
                             border:2px solid rgb(55, 52, 53);"

        self.start_disable = "background-image: url(:/buttons/resources/Play.png);\
                              color: rgb(55, 52, 53);\
                              background-color: rgb(245, 245, 245);\
                              border-radius: 10px;\
                              border:2px solid rgb(55, 52, 53);"

        self.stop_rsm_enable = "background-image: url(:/buttons/resources/Stop-Pause.png);\
                                background-color: rgb(237, 50, 55);\
                                border-radius: 10px;\
                                border:2px solid rgb(55, 52, 53);"

        self.stop_rsm_disable = "background-color: rgb(230, 245, 253);\
                                 border: 0px;"

        self.stop_rsm_rewind = "background-image: url(:/buttons/resources/rewind.png);\
                                background-color: rgb(157, 211, 175);\
                                border-radius: 10px;\
                                border:2px solid rgb(55, 52, 53);"
        
        self.label_green = "color: rgb(0, 163, 86);"
        self.label_red = "color: rgb(237, 50, 55);"
        self.label_blue = "color: rgb(65, 105, 128);"

        self.ended_label_enable = "background-color: rgb(230, 245, 253);\
                                  border: 0px;\
                                  color: rgb(55, 52, 53);"

        self.ended_label_disable = "background-color: rgb(230, 245, 253);\
                                   border: 0px;\
                                   color: rgb(230, 245, 253);"

        self.mem1_button_enable = "color: rgb(55, 52, 53);\
                                   background-color: rgb(255, 244, 230);\
                                   border-radius: 10px;\
                                   border:2px solid rgb(55, 52, 53);"

        self.mem2_button_enable = "color: rgb(55, 52, 53);\
                                   background-color: rgb(255, 232, 204);\
                                   border-radius: 10px;\
                                   border:2px solid rgb(55, 52, 53);"

        self.mem3_button_enable = "color: rgb(55, 52, 53);\
                                   background-color: rgb(255, 221, 179);\
                                   border-radius: 10px;\
                                   border:2px solid rgb(55, 52, 53);"
        
        
        
### end of file ###
