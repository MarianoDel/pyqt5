#!/bin/bash

#resources for uis
pyrcc5 stretcher3_res.qrc > stretcher3_res_rc.py

#python uis
pyuic5 stretcher_ver_3_1.ui > ui_stretcher.py
# pyuic5 stretcher_diags.ui > ui_stretcher_diag.py
# pyuic5 stretcher_rtc.ui > ui_stretcher_rtc.py


