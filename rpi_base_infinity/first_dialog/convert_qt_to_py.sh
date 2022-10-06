#!/bin/bash

#resources for uis
pyrcc5 first_dialog_res.qrc > first_dialog_res_rc.py

#python uis
pyuic5 first_dialog.ui > first_dialog_ui.py





