#!/bin/bash

#resources for uis
pyrcc5 wifi_res.qrc > wifi_res_rc.py

#python uis
pyuic5 wifi_dlg.ui > wifi_enable_ui.py
pyuic5 wifi_keyboard_dlg.ui > wifi_keyboard_ui.py
pyuic5 wifi_test_thread.ui > wifi_test_thread_dlg_ui.py




