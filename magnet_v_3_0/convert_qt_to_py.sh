#!/bin/bash

#resources for uis
pyrcc5 magnet3_res.qrc > magnet3_res_rc.py

#python uis
pyuic5 magnet_ver_3_1.ui > ui_magnet31.py
pyuic5 magnet_first_dlg.ui > ui_first_dlg.py
pyuic5 magnet_treatment_dlg.ui > ui_treatment_dlg.py
pyuic5 magnet_diags_dlg.ui > ui_diagnostics_dlg.py
pyuic5 magnet_rtc_dlg.ui > ui_rtc_dlg.py
pyuic5 magnet_pwr_ctrl_dlg.ui > ui_pwr_ctrl_dlg.py
pyuic5 magnet_memory_dlg.ui > ui_memory_dlg.py
pyuic5 magnet_screen_saver_dlg.ui > ui_screen_saver_dlg.py




