#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة وصف الأفلام

python pwb.py des/filmnew

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import time
import pywikibot
import codecs
from API.maindir import main_dir #used in logfiles, unicoded strings
if main_dir == "I:/core/master/": main_dir = "I:/core/core-yemen/"
import datetime
import json
#---

from API import printe
import sys
#---
import urllib
import urllib.request
import urllib.parse
#---
from API import himoBOT
#---
wikidatasite = pywikibot.Site('wikidata', 'wikidata')
repo = wikidatasite.data_repository()
#---
AskSave = {}
#---
def logme(q , label):
    verbose = False
    filename = main_dir + "name/name.log.csv"
    with codecs.open(filename, "a", encoding="utf-8") as logfile:
        formattedstring = ( '%s\t%s\n' % ( q , label) )
        try:   
            logfile.write(formattedstring)
        except Exception as e:
            pywikibot.output( '<<lightred>> Traceback (most recent call last):' )
            pywikibot.output("Error writing to file: %s " % filename )
            pywikibot.output( "<<lightred>> Exception:%s." % e )
            pywikibot.output( 'CRITICAL:' )
            verbose = True    #now I want to see what!   
    logfile.close()
    if verbose:
        printe.output(formattedstring)  
#---
AskSave[1] = True
#---
#def AddDes( item , pa , lang , Qid , keys):
def action_one_item( Qid, pa , lang , keys):
    item = getwditem( pa['item'] )
    if item:
        #desc = MakeDesc(Qid, auth, lang)
        #Summary= 'Bot: - Add descriptions: '+ lang
        keys = list(keys)
        keys.sort()
        #---
        if 'en' in keys:
            keys.append('en-gb')
            keys.append('en-ca')
        printe.output('keys:' + str(keys))
        #---
        descriptions = item.descriptions
        NewDesc = {}
        addedlangs = []
        #---
        for lang in keys:
            if lang not in descriptions.keys():
                #---
                lang2 = lang
                if lang in ('en-ca' , 'en-gb'):
                    lang2 = 'en'
                #---
                if MakeDesc(Qid, pa, lang2):
                    des = MakeDesc(Qid, pa, lang2)
                    NewDesc[lang] = {"language":lang,"value": des }
                    dns = ''
                    if 'endes' in pa:
                        dns = pa['endes']
                    printe.output('newar:%s,en:%s' % (des , dns) )
                    addedlangs.append(lang)
                else:
                    printe.output('*no desc for "%s"' % lang)
        #---
        if addedlangs:
            qitem = item.title(as_link=False)
            if AskSave[1]:
                printe.output('================== + '  + str(addedlangs))
                for lan in NewDesc.keys():
                    printe.output( 'lang:%s, value: "%s"'  % (lan , NewDesc[lan]['value'] ) )
                saaa = pywikibot.input(' Add as descriptions? ' )
                if saaa == 'y' or saaa == 'a' or saaa == '':
                    if saaa == 'a':
                        AskSave[1] = False
                    himoBOT.work_api_desc( NewDesc , qitem)
                else:
                    printe.output('* rong answer' )
            else:
                himoBOT.work_api_desc( NewDesc , qitem)
#---
def getwditem(qitem):
    try:
        item = pywikibot.ItemPage( repo, qitem )
        #---
        item.get()
        return item
    except:
        return False
#---
Comma = {
        "an": " y ", 
        "ar": "، و" ,
        "ast": " y ", 
        "ca": " i ", 
        "de": " und ", 
        "es": " y ", 
        "ext": " y ", 
        "fr": " et ",  
        "he": " ו",
        "gl": " e ", 
        "it": " e ", 
        "nl": " en ", 
        "oc": " e ", 
        "pt": " e ", 
        "ro": " și ", 
        "sv": " och ", 
        'en' : ", ",

    }
Comma2 = {
        'ar' : "، و" ,
        'en' : ", ",
        'de' : ", ",
        'fr' : ", ",
        'nl' : ", "
    }
#---
def GetQuery(Qid , lang , keys):
    #---
    P50 = 'P57'
    #---
    #sa = ('?item wdt:P31 wd:%s .\n' % Qid )
    ur = 'SELECT ?item ?%s '% lang 
    head = '?' + ' ?'.join([ x for x in keys if x != lang])
    ur = ur + head
    #ur = ur + ('\n(GROUP_CONCAT(DISTINCT(?date); separator=",") as ?dates) ?endes ' )
    ur = ur + ' ?endes  ?dates \n' 
    ur = ur  + 'WHERE { \n?item wdt:%s ?auths . \n?item wdt:%s ?auths2 .\n' % (P50 , P50)
    #---
    sa = ' ?item wdt:P31 wd:Q11424 .\n?item wdt:P577 ?date2.\nBIND(year(?date2) AS ?dates). \n'
    sa = sa + 'OPTIONAL { ?item schema:description ?endes. FILTER((LANG(?endes)) = "en") }\n'
    ur = ur  + sa
    #---
    row = 'OPTIONAL {?auths rdfs:label ?%s filter (lang(?%s) = "%s")} .'
    OPTIONAL = '\n'.join([(row % (x,x,x)) for x in keys if x != lang])
    '''for lan in keys:
        if lan != lang:
            ur = ur + 'OPTIONAL {?auths rdfs:label ?%s filter (lang(?%s) = "%s")} .\n' % (lan, lan, lan) '''
    ur = ur + OPTIONAL
    #---
    ur = ur + ' \n{?auths2 rdfs:label ?%s2 filter (lang(?%s2) = "%s")} .' % (lang, lang, lang) 
    ur = ur + '\nOPTIONAL {?item schema:description ?itemDes filter(lang(?itemDes) = "%s")}' % lang 
    ur = ur + 'FILTER(!BOUND(?itemDes))\n'# GROUP BY ?item '
    ur = ur + 'SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en". ?auths rdfs:label ?%s }}\n'  % lang 
    #printe.output(ur)
    #---
    return ur
#---
def Gquery2(json1):
    table = {}
    #table = []
    #for head in json1['head']['vars']:
    for result in json1['results']['bindings']:
        q = 'item' in result and result['item']['value'].split('/entity/')[1] or ''
        s = {}
        for se in result:
            s[se] = result[se]['value']
        s['item'] = q
        table[q] = s
    return table
#---
filmform = {}
xsxsx = {
        'an': 'cinta de ~YEAR~ dirichita por ~AUTHOR~', 
        'ar': 'فيلم أُصدر سنة ~YEAR~، من إخراج ~AUTHOR~', 
        'ast': 'película de ~YEAR~ dirixida por ~AUTHOR~', 
        'ca': 'pel·lícula de ~YEAR~ dirigida per ~AUTHOR~', 
        'de': 'Film von ~AUTHOR~ (~YEAR~)', 
        'es': 'película de ~YEAR~ dirigida por ~AUTHOR~', 
        'ext': 'pinicla de ~YEAR~ dirigía por ~AUTHOR~', 
        'fr': 'film de ~AUTHOR~, sorti en ~YEAR~', 
        'gl': 'filme de ~YEAR~ dirixido por ~AUTHOR~', 
        #'he': 'סרט של ~AUTHOR~ משנת ~YEAR~', #warning, avoid mix Latin and Hebrew chars for directors name
        'he': 'סרט משנת ~YEAR~', 
        'it': 'film del ~YEAR~ diretto da ~AUTHOR~', 
        'nl': 'film uit ~YEAR~ van ~AUTHOR~', 
        'oc': 'filme de ~YEAR~ dirigit per ~AUTHOR~', 
        'pt': 'filme de ~YEAR~ dirigido por ~AUTHOR~', 
        'ro': 'film din ~YEAR~ regizat de ~AUTHOR~', 
        'sv': 'film från ~YEAR~ regisserad av ~AUTHOR~', 
    }
filmform['film'] = {#
        'ar': 'فيلم أُصدر سنة ~YEAR~، من إخراج ~AUTHOR~', 
        'en': '~YEAR~ film by ~AUTHOR~', 
        'nl': 'film uit ~YEAR~ van ~AUTHOR~', 

    }

#---
quaua = '''SELECT #DISTINCT 
?item ?ar ?nl ?en ?endes  ?dates ?auths
WHERE {
?item wdt:P57 ?auths .
#?item wdt:P57 ?auths2 .
?item wdt:P31 wd:Q11424 .
?item wdt:P577 ?date2.
BIND(year(?date2) AS ?dates).
OPTIONAL { ?item schema:description ?endes. FILTER((LANG(?endes)) = "en") }
OPTIONAL {?auths rdfs:label ?nl filter (lang(?nl) = "nl")} .
OPTIONAL {?auths rdfs:label ?en filter (lang(?en) = "en")} .
#{?auths2 rdfs:label ?ar2 filter (lang(?ar2) = "ar")} .
#OPTIONAL {?item schema:description ?itemDes filter(lang(?itemDes) = "ar")} FILTER(!BOUND(?itemDes))
MINUS {?item schema:description ?itemDes filter(lang(?itemDes) = "ar")}# FILTER(!BOUND(?itemDes))
SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en". ?auths rdfs:label ?ar }}

'''
def WorkWithOneLang( Qid , lang , keys ):
    printe.output( '*<<lightyellow>> WorkWithOneLang: ')
    limit = 200
    #limit = '10000'
    #lang = 'de'
    #keys = 
    #try:
    #---
    quary = quaua
    #quary = GetQuery(Qid , lang, keys)
    quary = quary + '\n limit %d' % limit
    printe.output(quary)
    #---
    PageList = himoBOT.sparql_generator_url(quary , key='item')
    #---
    total = len(PageList)
    num = 0
    #---
    printe.output('* PageList: ')
    for pa in PageList.keys():
        printe.output(pa)
        PageList[pa]['item'] = pa.split('/entity/')[1]
        num += 1
        SAO = filmform[Qid][lang]
        printe.output('<<lightblue>>> %s "%s" :%s/%d : %s'  % ( lang , SAO , num , total , PageList[pa]['item'] ) )
        #---
        action_one_item( Qid, PageList[pa] , lang , keys)
#---
by_list = {
          'ar' : "من تأليف"
        , 'en' : "by"
        , 'fr' : "de"
        , 'de' : "von"
        , 'nl' : "van"
        , 'ca' : "per"
        , 'cs' : "od"
        , 'la' : "ab"
        , 'it' : "da"
        , 'io' : "da"
        , 'eo' : "de"
        , 'da' : "af"
        , 'pl' : "przez"
        , 'ro' : "de"
        , 'es' : "por"
        , 'sv' : "av"
        }
#---
def MakeDesc(Qid, pa, lang):
    #for lang in language:
    #auth
    description = False
    english = ['en-gb' , 'en-ca' ]
    if lang in english:
        lang = 'en'
    #---
    if not lang in by_list:
        printe.output('<<lightblue>>> cant find "by" in by_list for lang: "%s"'  % lang )
        return False
    #---
    co = by_list[lang] + ' '
    if (Qid == 'Q482994') and (lang == 'ar'):
        #co = 'ل'
        co = 'من أداء '
    #---
    if (lang in pa) and (pa[lang] != ''):
        auth = pa[lang]
        if auth:
            if lang in filmform[Qid]:
                des = filmform[Qid][lang]
                YEAR = pa['dates']
                YEARS = YEAR#.split(',')
                endes = pa['endes'][0]
                #---
                true_year = ''
                if len(YEARS) > 1:
                    for ye in YEARS:
                        if endes != re.sub( ye  , '' , endes):
                            true_year = ye
                else:
                    true_year = pa['dates'][0]
                auth2 = Comma[lang].join(auth)
                #---
                #d = d + ' '                        # الرابط by 
                d = re.sub( '~AUTHOR~'  , auth2 , des)
                d = re.sub( '~YEAR~'  , true_year, d)
                #printe.output( 'd' )
                #printe.output( d )
                description = d
    #else:
        #description = False
    if lang == 'ar':
        if description and description != re.sub( '[abcdefghijklmnobqrstuvwxyz]'  , '' , description):
            printe.output( '<<lightred>> arabic description test failed "%s".' % description )
            description = False
    return description
#---
def films():
        printe.output("films: ")
        Q = 'film'  
        #for lang in language:
        keys = filmform[Q].keys()
        #printe.output( 'lang: "%s" with value: ' % 'fr' )
        WorkWithOneLang( Q , 'ar' , keys)
#---
if __name__ == "__main__":  
     films()
#---