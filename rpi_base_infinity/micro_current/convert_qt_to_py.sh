#!/bin/bash

#resources for uis
pyrcc5 microc_res.qrc > microc_res_rc.py

#python uis
pyuic5 micro.ui > ui_micro.py




