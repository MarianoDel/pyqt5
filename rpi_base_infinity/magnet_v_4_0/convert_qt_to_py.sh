#!/bin/bash

#resources for uis
pyrcc5 magnet4_res.qrc > magnet4_res_rc.py

#python uis
pyuic5 magnet_ver_4_0.ui > ui_magnet40.py
pyuic5 magnet_treatment_dlg.ui > ui_treatment_dlg.py
pyuic5 magnet_memory_dlg.ui > ui_memory_dlg.py
pyuic5 magnet_stages_dlg.ui > ui_stages_dlg.py

## for Magnet_ver_3_1
# cp main.py main31.py
# sed -i 's/^RUN_VER_3_1 =.*/RUN_VER_3_1 = 1/g' main31.py
# sed -i 's/^RUN_VER_3_2 =.*/RUN_VER_3_2 = 0/g' main31.py
## for Magnet_ver_3_2
# cp main.py main32.py
# sed -i 's/^RUN_VER_3_1 =.*/RUN_VER_3_1 = 0/g' main32.py
# sed -i 's/^RUN_VER_3_2 =.*/RUN_VER_3_2 = 1/g' main32.py




