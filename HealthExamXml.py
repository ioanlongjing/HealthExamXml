#!/usr/bin/env python
#coding: utf-8
import glob
from lxml import etree

for name in glob.glob('un/*.xml'):
        print(" \n ")
        print( name )
        try:
                page = etree.parse( name )
                Windows_Sec_update = '//Check[(@Name="Windows Security Updates" and @ID="500")]'

                Windows_Sec_Update = page.xpath( Windows_Sec_update )
                for Window_Check in Windows_Sec_Update:
                        print '========'
                        advices = Window_Check.findall("./Advice")
                        for advice in advices:
                                print '[ Advice ] : '+advice.text
                        updatedDatas = Window_Check.findall("./Detail/UpdateData[@IsInstalled=\"false\"]")
                        for update in updatedDatas:
                                titles = update.findall("./Title")
                                for title in titles:
                                        print '[ title ] : '+ title.text
                                details = update.findall("./References/InformationURL")
                                for detail in details:
                                        print '[ Detail ] : '+ detail.text
                        print '========'
        except Exception as e:
                print e
                print( " The File context is null." )
                print( name )
                continue
