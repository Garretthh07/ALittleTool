#!usr/bin/python
# Description: Advanced Usage of apihelper.py

from apihelper import info
import odbchelper

info(odbchelper)

info(odbchelper, 12)

info(odbchelper, collapse=0)

info(spacing=15, object=odbchelper)
