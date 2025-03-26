#!/bin/bash

#resources for uis
pyrcc5 microc_res.qrc > microc_res_rc.py

#python uis
pyuic5 micro.ui > ui_micro.py
pyuic5 micro2.ui > ui_micro2.py




