#!/bin/bash

#resources for uis
pyrcc5 stretcher3_res.qrc > stretcher3_res_rc.py

#python uis
pyuic5 stretcher_ver_3_1.ui > ui_stretcher.py
pyuic5 stretcher_first_dlg.ui > ui_first_dlg.py
pyuic5 stretcher_treatment_dlg.ui > ui_treatment_dlg.py
pyuic5 stretcher_diags_dlg.ui > ui_diagnostics_dlg.py
pyuic5 stretcher_rtc_dlg.ui > ui_rtc_dlg.py
pyuic5 stretcher_pwr_ctrl_dlg.ui > ui_pwr_ctrl_dlg.py



