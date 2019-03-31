# This Python file uses the following encoding: utf-8
import os, sys
from lxml import html
import csv, os, json
import requests
from exceptions import ValueError
from time import sleep
from lxml import html
from lxml import etree

# https://www.python.org/dev/peps/pep-0263/

from FileReader import FileReader
from ExcelWriter import ExcelWriter

class ConvertHtmlToExecl1point3acre:

    def __init__(self, fileName):
        self.fileName = fileName

    def getField(self, xpathString):
        reader = FileReader(self.fileName)
        content = reader.read()
        tree = etree.HTML(content)
        # https://www.w3schools.com/xml/xpath_syntax.asp
        #
        titles = tree.xpath(xpathString)

        return titles

    def getAllFields(self):
        #  http://www.tizag.com/xmlTutorial/xpathattribute.php
        titlePath = '//div[@class="Thread__verticalLine___3WYd8 col-md-10 col-sm-12 col-xs-12"]//h4//a[contains(@href,"https://instant.1point3acres.com/thread/")]//text()'
        linkPath ='//div[@class="Thread__verticalLine___3WYd8 col-md-10 col-sm-12 col-xs-12"]//h4//a[contains(@href,"https://instant.1point3acres.com/thread/")]//@href'
        titles = self.getField(titlePath)
        links = self.getField(linkPath)

        i = 0
        for title in titles:
            i += 1
            #print(str(i) + "    " + title)

        for link in links:
            i += 1
            #print(str(i) + "    " + link)

        return titles, links

if __name__ == "__main__":
    fileName = '/home/leo/Desktop/houzz.html'
    excelFileName = './data/data.xls'
    sheetName = 'test'
    parser = ConvertHtmlToExecl1point3acre(fileName)
    titles, links = parser.getAllFields()
    excelWriter = ExcelWriter(excelFileName, sheetName)
    excelWriter.write(0, titles)
    excelWriter.write(1, links)
    excelWriter.save()

