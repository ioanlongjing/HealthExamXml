#!/usr/bin/env python
#coding: utf-8
import glob
from lxml import etree

for name in glob.glob('un/*.xml'):
	print( name )
        try:
            page = etree.parse( name )
            for nodeOffice in page.xpath('//Check[@Name="Office Security Updates"]/Advice'):
                    print(" The Office Security Updata is %s "  % nodeOffice.text )

            for nodeWindows in page.xpath('//Check[@Name="Windows Security Updates"]/Advice'):
                    print(" The Windows Seucrity Update is %s " %nodeOffice.text )

        except:
            print( " The File context is null." )
            print( name )
            continue
