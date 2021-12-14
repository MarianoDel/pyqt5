#!/bin/bash

#resources for uis
pyrcc5 diagnostics_res.qrc > diagnostics_res_rc.py

#python uis
pyuic5 diagnostics.ui > diagnostics_ui.py
pyuic5 rtc.ui > rtc_ui.py
pyuic5 power_control.ui > power_control_ui.py
pyuic5 display_mode.ui > display_mode_ui.py





