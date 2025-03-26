#!/bin/bash

#resources for uis
pyrcc5 stretcher4_res.qrc > stretcher4_res_rc.py

#python uis
pyuic5 stretcher_ver_4_0.ui > ui_stretcher40.py
pyuic5 stretcher_treatment_dlg.ui > ui_treatment_dlg.py
pyuic5 stretcher_memory_dlg.ui > ui_memory_dlg.py
pyuic5 stretcher_stages_dlg.ui > ui_stages_dlg.py
pyuic5 stretcher_mem_manager_dlg.ui > ui_mem_manager_dlg.py




