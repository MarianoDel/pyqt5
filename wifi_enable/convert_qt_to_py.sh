#!/bin/bash

#resources for uis
pyrcc5 wifi_res.qrc > wifi_res_rc.py

#python uis
pyuic5 wifi_dlg.ui > ui_wifi_dlg.py
pyuic5 wifi_keyboard_dlg.ui > ui_wifi_keyboard_dlg.py
pyuic5 wifi_test_thread.ui > ui_wifi_test_thread_dlg.py




