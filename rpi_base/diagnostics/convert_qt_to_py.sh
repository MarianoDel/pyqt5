#!/bin/bash

#resources for uis
pyrcc5 diagnostics_res.qrc > diagnostics_res_rc.py

#python uis
pyuic5 diagnostics.ui > ui_diagnostics.py
pyuic5 rtc.ui > ui_rtc.py
pyuic5 power_control.ui > ui_power_control.py





