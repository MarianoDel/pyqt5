from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer, QThread
# from time import time
from threading import Timer
import os
import subprocess
import platform



###########################
# WiFiThreadManager Class #
###########################
class WiFiThreadManager (QThread):

    def __init__(self):
        QThread.__init__(self)

        self.status = 'NO CONN'


    def __del__(self):
        self.wait()

        
    def run (self):
        while True:
            if self.status == 'NO CONN':
                if self.GetInterfases() == 'IP':
                    self.status = 'IP'
                
            elif self.status == 'IP':
                if self.GetPing() == 'PING':
                    self.status = 'PING'
                elif self.GetInterfases() != 'IP':
                    self.status = 'NO CONN'

            elif self.status == 'PING':
                if self.GetTunnel() == 'TUNNEL':
                    self.status = 'TUNNEL'
                elif self.GetPing() != 'PING':
                    self.status = 'IP'

            self.sleep(4)

    
    def GetStatus (self):
        return self.status
        

    def GetInterfases (self):
        output = ""
        try:
            output = subprocess.check_output(['python3','scan_interfase.py'])
        except subprocess.CalledProcessError as err:
            print(err)
            return
 
        output_str = output.decode('utf-8')
        lines = output_str.split('\n')

        for line in lines:
            wired_index = line.find('eth')
            wireless_index = line.find('wlan')
            if wired_index > 0:
                ether_str = 'Net: eth' + line[wired_index + 3]

                ip_index = line.find('ip')
                gw_index = line.find('gw')                
                if ip_index > 0 and gw_index > 0:
                    ip_str = 'Ip: ' + line[ip_index + 3:gw_index]
                    gw_str = 'Gw: ' + line[gw_index + 3:]
                    
            if wireless_index > 0:
                ether_str = 'Net: wlan' + line[wireless_index + 4]
                ip_index = line.find('ip')
                gw_index = line.find('gw')                
                if ip_index > 0 and gw_index > 0:
                    ip_str = 'Ip: ' + line[ip_index + 3:gw_index]
                    gw_str = 'Gw: ' + line[gw_index + 3:]

                    # 'Ip: 0.0.0.0' 'Gw: 0.0.0.0'
                    if len(ip_str) > 11 and len(gw_str) > 11:
                        return 'IP'
                    

    def GetPing (self):
        output = ""
        try:
            output = subprocess.check_output(['ping','-c', '1', '-i', '2', '8.8.8.8'])
        except subprocess.CalledProcessError as err:
            print(err)
            return

        output_str = output.decode('utf-8')
        lines = output_str.split('\n')

        for line in lines:
            if line.startswith('1 packets transmitted, 1 received, 0% packet loss'):
                return 'PING'


    def GetTunnel (self):
        output = ""
        try:
            output = subprocess.check_output(['python3','scan_pitunnel.py'])
        except subprocess.CalledProcessError as err:
            print(err)
            return

        output_str = output.decode('utf-8')
        if 'ESTABLISHED' in output_str:
            return 'TUNNEL'

        

            
        
        
### end of file ###
