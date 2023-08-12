#!/bin/bash

#resources for uis
pyrcc5 magnet4_res.qrc > magnet4_res_rc.py

#python uis
pyuic5 magnet_ver_4_1.ui > ui_magnet41.py
pyuic5 magnet_treatment_dlg.ui > ui_treatment_dlg.py
pyuic5 magnet_memory_dlg.ui > ui_memory_dlg.py
pyuic5 magnet_stages_dlg.ui > ui_stages_dlg.py
pyuic5 magnet_mem_manager_dlg.ui > ui_mem_manager_dlg.py




