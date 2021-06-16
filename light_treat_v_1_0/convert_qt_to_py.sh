#!/bin/bash

#resources for uis
pyrcc5 light1_res.qrc > light1_res_rc.py

#python uis
pyuic5 light_ver_1_0.ui > ui_light1.py
pyuic5 light_first_dlg.ui > ui_first_dlg.py
pyuic5 light_treatment_dlg.ui > ui_treatment_dlg.py
pyuic5 light_diags_dlg.ui > ui_diagnostics_dlg.py
pyuic5 light_rtc_dlg.ui > ui_rtc_dlg.py
pyuic5 light_pwr_ctrl_dlg.ui > ui_pwr_ctrl_dlg.py
pyuic5 light_memory_dlg.ui > ui_memory_dlg.py
pyuic5 light_screen_saver_dlg.ui > ui_screen_saver_dlg.py




