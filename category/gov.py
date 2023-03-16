#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
#---
import other
import pywikibot
#---
mha = [
    "محافظة البيضاء (اليمن)",
    "محافظة البيضاء",
    "محافظة الجوف",
    "محافظة الحديدة",
    "محافظة الضالع",
    "محافظة المحويت",
    "محافظة المهرة",
    "محافظة إب",
    "محافظة أبين",
    "محافظة أمانة العاصمة",
    "محافظة تعز",
    "محافظة حجة",
    "محافظة حضرموت",
    "محافظة ذمار",
    "محافظة ريمة",
    "محافظة سقطرى",
    "محافظة شبوة",
    "محافظة صعدة",
    "محافظة صنعاء",
    "محافظة عمران",
    "محافظة لحج",
    "محافظة مأرب",
    "محافظة أرخبيل سقطرى",
    "محافظة سقطرى",
    ]
#---
from islahvillage import islahvillage
def yemen():
    num = 0
    #mha = islahvillage
    #keys = [ 'مديريات' , 'عزل' , 'قرى', 'تقسيمات' , 'أماكن مأهولة في']
    keys = [ 'جغرافيا' ]
    #keys = ['قرى']
    for key in keys:
        for title in mha:
            num = num + 1
            title = 'تصنيف:'+ key + ' '  + title
            pywikibot.output( '<<lightyellow>>\n----------\n>> %d >> %s << <<' % ( num , title) )
            other.GetType2(title)
#---
if __name__ == "__main__":
    yemen()
#---