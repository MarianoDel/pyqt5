#!/bin/bash

#resources for uis
pyrcc5 screen_saver_res.qrc > screen_saver_res_rc.py

#python uis
pyuic5 screen_saver.ui > ui_screen_saver.py





