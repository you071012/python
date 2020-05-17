# !/usr/bin/python
# -*- coding:utf8 -*-
import xmltodict


def trans_dict_to_xml(jsdict):
    xml = ''
    try:
        xml = xmltodict.unparse(jsdict, encoding='utf-8')
    except:
        xml = xmltodict.unparse({'request': jsdict}, encoding='utf-8')
    finally:
        return xml

tmp = {"rgnList":["01","02"]}
print(trans_dict_to_xml(tmp))