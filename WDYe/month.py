#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  
#---
import re
import time
import codecs
import pywikibot
import json
import unicodedata
#---
import sys
#---
quuu = {} 
quuu['month'] = ''' 
SELECT DISTINCT ?item
WHERE { 
?item schema:description "%s"@en  .
FILTER NOT EXISTS {?item schema:description ?ar.
             FILTER((LANG(?ar)) = "ar" ) }
} 
limit 3000 
'''
#---
from API import  newdesc
# newdesc.work22(q , topic, translations) 
# newdesc.main_from_file(file , topic , translations) 
# newdesc.mainfromQuarry2( topic , Quarry, translations) 
#--- ----------------------
translations = {
    'month': { 
        'ar': 'شهر',
        },
    }
translations["island in Indonesia"] = {"ar" : "جزيرة في إندونيسيا" }
#---
def mainfromQuarry(topic):
    pywikibot.output( '*<<lightyellow>> mainfromQuarry:' )
    Quarry = quuu["month"] % topic
    if sys.argv and "OFFSET" in sys.argv : 
        Quarry = Quarry + " OFFSET 100000"
    newdesc.mainfromQuarry2( topic , Quarry, translations)
#---
if __name__ == "__main__" : 
    mainfromQuarry("island in Indonesia")
    mainfromQuarry('month')
#---