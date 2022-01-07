# encoding: utf-8
import re


class CleanUtil:

    @staticmethod
    def clean_content(text:str):
        comp = re.compile('[^A-Z^a-z^0-9^ ]')
        return comp.sub('', text)

    @staticmethod
    def clean_location(text:str):
        return True if re.findall('[cC]hina',text) else False

    @staticmethod
    def clean_lang_zh(text:str):
        return True if re.findall("zh",text) else False
