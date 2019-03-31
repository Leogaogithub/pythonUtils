# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook

class ExcelWriter:
    def __init__(self, fileName, sheetName):
        self.fileName = fileName
        self.sheetName = sheetName
        self.wb = Workbook()
        self.sheet = self.wb.add_sheet(sheetName)

    def save(self):
        self.wb.save(self.fileName)

    def write(self, colum, list):
        i = 0
        for str in list:
           self.sheet.write(i,colum, str)
           i = i+1


