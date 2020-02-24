#!/usr/bin/python
# -*- coding: utf-8
# ОПИСАНИЕ БОТА: Бот помогает мне управлять процесом
# АВТОР БОТА   : Купинов Вадим ильич
# ТЕЛЕГРАММ АВТОРА : @Izofen
# Доработки: Подъведение под общий шаблон

import requests
import xmltodict
import json


f = open('/home/izofen/Studiya/mail.txt')
for line in f:
    line = line.strip()    
    nm = line.find (':')
    mailT = line[0:nm]
    passT = line[nm+1:]
    nm = mailT.find('@')
    domen = mailT[nm+1:]

    r = requests.get("https://autoconfig.thunderbird.net/v1.1/{}".format(domen))
    
    body = r.text 
    if body.find('<title>404 Not Found</title>') != -1:
    	print ('--------------------')
    else:	
        #print (r.text)
        xpars = xmltodict.parse(r.text)
        #jsonl = json.dumps(xpars)
        #print (xpars) 
        print ('')  
        clientConfig = xpars['clientConfig']
        jsonl = json.dumps(clientConfig)
        d = json.loads(jsonl)
        print (d['@version'])
        #for line in jsonl:
        #    print ('[+]',line)

    #nsat.jp
    print ('=====================================================================')
    print ('[+]',line,mailT,passT,domen)
    print ('=====================================================================')