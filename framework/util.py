import xlrd
import os
from framework.logger import Logger
logger = Logger("logger=Util").getlog()
class Util(object):
    @classmethod
    def get_execl(self,excel_path,name="Sheet1"):
        excel=xlrd.open_workbook(excel_path)
        sheet=excel.sheet_by_name(name)
        keys=sheet.row_values(0)
        h=sheet.nrows
        l=sheet.ncols
        if h<=1:
            logger.info("Excel表中数据总行数少于一行")
        else:
            self.r=[]
            for i in range(1,h):
                sheet_data={}
                values=sheet.row_values(i)
                for j in range(l):
                    sheet_data[keys[j]]=values[j]
                self.r.append(sheet_data)
        return self.r
if __name__=="__main__":
    excel_path=os.path.dirname(os.path.abspath("."))+"/data/"+"user.xlsx"
    print(Util.get_execl(excel_path,"Sheet1"))




