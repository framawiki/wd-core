#!/usr/bin/python
# -*- coding: utf-8  -*-
#
"""

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import taxoo
	
arabic  = {
     'Q11937877' : {'ar' : 'من القشريات المتعددة' }
    , 'Q83483' : {'ar' : 'من القنفذ البحري' }
    , 'Q13389544' : {'ar' : 'من الكببيانية' }
    , 'Q811147' : {'ar' : 'من الكرات النافحة' }
    , 'Q190090' : {'ar' : 'من الكيسيات' }
    , 'Q17156' : {'ar' : 'من اللافصيميات' }
    , 'Q133571' : {'ar' : 'من اللقنورانية' }
    , 'Q2563582' : {'ar' : 'من المتكيسات الرئوية' }
    , 'Q207547' : {'ar' : 'من المثقوبات' }
    , 'Q3178797' : {'ar' : 'من المخروطانيات' }
    , 'Q135200' : {'ar' : 'من المخندقانيات' }
    , 'Q147868' : {'ar' : 'من المرشانتاناوت' }
    , 'Q1953103' : {'ar' : 'من المستحراوات المتقلبة' }
    , 'Q1135978' : {'ar' : 'من المستحراوات المكورة' }
    , 'Q132809' : {'ar' : 'من المطثيات' }
    , 'Q273179' : {'ar' : 'من المكعبيات' }
    , 'Q133551' : {'ar' : 'من الملاسانيات' }
    , 'Q20635347' : {'ar' : 'من الملتوياوات' }
    , 'Q1054206' : {'ar' : 'من الملحاوات العصوية' }
    , 'Q212798' : {'ar' : 'من المهتزات' }
    , 'Q244147' : {'ar' : 'من المؤتلفات' }
    , 'Q1051432' : {'ar' : 'من الميثاناوات الجرثومية' }
    , 'Q867927' : {'ar' : 'من الميثاناوات النارية' }
    , 'Q22933896' : {'ar' : 'من الميدوزات الفنجانية' }
    , 'Q28960' : {'ar' : 'من اليرقانيات' }
    , 'Q1137709' : {'ar' : 'من أصيصيانية' }
    , 'Q167367' : {'ar' : 'من ألفية الأرجل' }
    , 'Q43447' : {'ar' : 'من أم أربعة وأربعين' }
    , 'Q271631' : {'ar' : 'من أوليات الذنب' }
    , 'Q4867740' : {'ar' : 'من بطنيات القدم' }
    , 'Q221563' : {'ar' : 'من ثنائيات الذنب' }
    , 'Q8316' : {'ar' : 'من ثنائيات الفلقة' }
    , 'Q1096274' : {'ar' : 'من حزازيات إسويطية' }
    , 'Q831482' : {'ar' : 'من حزازيات حقيقية' }
    , 'Q1149748' : {'ar' : 'من حزازيات ذئبية' }
    , 'Q1422487' : {'ar' : 'من حزازيات سبخية' }
    , 'Q12207651' : {'ar' : 'من حزازيات قرناء' }
    , 'Q642852' : {'ar' : 'من حزازيات يشعورية' }
    , 'Q138088' : {'ar' : 'من حلميات الأسنان' }
    , 'Q127470' : {'ar' : 'من خيار البحر' }
    , 'Q623286' : {'ar' : 'من داخليات الفك' }
    , 'Q589697' : {'ar' : 'من دودة البلوط' }
    , 'Q25368' : {'ar' : 'من ذوات الصدفتين' }
    , 'Q131630' : {'ar' : 'من ذوات منشأ الحركة' }
    , 'Q132649' : {'ar' : 'من رأسيات الدرقة' }
    , 'Q128257' : {'ar' : 'من رأسيات القدم' }
    , 'Q19430' : {'ar' : 'من سيفيات الذيل' }
    , 'Q127282' : {'ar' : 'من شعاعيات الزعانف' }
    , 'Q132006' : {'ar' : 'من شقرانانية' }
    , 'Q194257' : {'ar' : 'من صفيحيات الخياشيم الغضروفية' }
    , 'Q188906' : {'ar' : 'من عديدة الأصداف' }
    , 'Q19436' : {'ar' : 'من عريضات الأجنحة' }
    , 'Q19106' : {'ar' : 'من عناكب البحر' }
    , 'Q188360' : {'ar' : 'من غلصميات الأرجل' }
    , 'Q132662' : {'ar' : 'من فكيات الأرجل' }
    , 'Q843232' : {'ar' : 'من فنجانيانيات' }
    , 'Q190701' : {'ar' : 'من قافزات الذيل' }
    , 'Q193006' : {'ar' : 'من قليلات الأشواك' }
    , 'Q18952' : {'ar' : 'من كثيرات الأشعار' }
    , 'Q160830' : {'ar' : 'من لحميات الزعانف' }
    , 'Q182978' : {'ar' : 'من لينات الدرقة' }
    , 'Q490800' : {'ar' : 'من متشعبات الأرجل' }
    , 'Q136797' : {'ar' : 'من متقلبات إيبسيلونية' }
    , 'Q306579' : {'ar' : 'من متقلبات ألفا' }
    , 'Q136674' : {'ar' : 'من متقلبات بيتا' }
    , 'Q307535' : {'ar' : 'من متقلبات دلتا' }
    , 'Q3329480' : {'ar' : 'من متقلبات زيتا' }
    , 'Q134668' : {'ar' : 'من متقلبات غاما' }
    , 'Q275657' : {'ar' : 'من مخاطيات الأبواغ' }
    , 'Q586245' : {'ar' : 'من مخروطيات الأسنان' }
    , 'Q488032' : {'ar' : 'من مخفيات النبت' }
    , 'Q189069' : {'ar' : 'من مندمجات الأقواس' }
    , 'Q25349' : {'ar' : 'من نجوم البحر' }
    }    
if __name__ == "__main__":
    taxoo.main(arabic)