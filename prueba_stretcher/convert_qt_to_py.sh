#!/bin/bash

#resources for uis
pyrcc5 stretcher_res.qrc > stretcher_res_rc.py

#python uis
pyuic5 stretcher_ver_2_0.ui > ui_stretcher.py
pyuic5 stretcher_diags.ui > ui_stretcher_diag.py

