#!/bin/bash

#resources for uis
pyrcc5 screen_saver_res.qrc > screen_saver_res_rc.py

#python uis
pyuic5 screen_saver.ui > screen_saver_ui.py





