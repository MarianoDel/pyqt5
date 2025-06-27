#!/bin/bash

#resources for uis
pyrcc5 microc_res.qrc > microc_res_rc.py

#python uis
pyuic5 micro.ui > ui_micro.py
pyuic5 micro2.ui > ui_micro2.py
pyuic5 micro3.ui > ui_micro3.py
pyuic5 micro3_hamb.ui > ui_menu3.py
pyuic5 micro3_rtf.ui > ui_rtf3.py




