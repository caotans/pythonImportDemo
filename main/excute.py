#!usr/bin/python3.60
#cording:utf-8
import xlrd
import os
from main.constant import constant
print("--------开始----------")
root=os.path.dirname(os.getcwd())
data=xlrd.open_workbook(root+"/template.xlsx")
sheetNames=data.sheet_names()
outPath=root+"/export"
if not os.path.exists(outPath):
    os.mkdir(outPath)
else:
    #循环删除里面的文件
    fileArray=os.listdir(outPath)
    for file in fileArray:
        os.remove(outPath+"/"+file)
for name in sheetNames:
    sheet=data.sheet_by_name(name)
    try:
      rows =sheet.cell(2,4) #行数
    except:
      break
    min=int(rows.value.split("-")[0])
    max=int(rows.value.split("-")[1])
    moduleIndex=min
    moduleSort=1
    tabIndex=min
    tabSort=1
    pricePointIndex=min
    pricePointSort=1
    cols =4 #列数
    productName=sheet.cell(1,0)
    f=open(outPath+"/"+productName.value+".sql","w")
    productCode=sheet.cell(1,4)
    fileContent=""#tab的内容
    diffModule=""#模块名称
    moduleContent=""#模块的内容
    pricePointContent=""#价格点内容
    for rownum in range(0,max-min+4):
        try:
          row=sheet.row_values(rownum)
        except:
          row=""
        if row!="":
                if rownum>3:
                 tabName=row[1]
                 cycleStr=row[2]
                 parentCode=row[3]
                 pricePoint=row[4]
                 moduleName=row[0]
                 moduleName=moduleName.strip().lstrip()
                 if moduleName=="":
                     continue
                 fileContent="--tab配置\n"
                 fileContent=fileContent+"insert into  "+constant.TABLEL_TAB+" values( "+str(moduleIndex)+","+constant.matchDic(constant,tabName)+","+str(moduleSort)+",'"+constant.matchDate(constant,cycleStr)+"',"+constant.matchDic(constant,moduleName)+",'"+cycleStr+"')\n"
                 if moduleSort>1:
                     fileContent=",( "+str(moduleIndex)+","+constant.matchDic(constant,tabName)+","+str(moduleSort)+",'"+constant.matchDate(constant,cycleStr)+"',"+constant.matchDic(constant,moduleName)+",'"+cycleStr+"')\n"
                 moduleIndex=moduleIndex+1
                 moduleSort=moduleSort+1
                 print(fileContent)
                 f.write(fileContent)
                 if parentCode!="":
                    moduleContent=moduleContent+","+parentCode
                 if diffModule=="":
                     moduleContent="--module配置\n"
                     moduleContent=moduleContent+"insert into  "+constant.TABLEL_MODULE+" values( "+str(tabIndex)+",'"+productCode.value+"','"+productName.value+"',"+str(tabSort)+",1,0)\n"
                 else:
                     if moduleName!=diffModule:
                         tabIndex=tabIndex+1
                         tabSort=tabSort+1
                         moduleContent=moduleContent+",( "+str(tabIndex)+","+constant.matchDic(constant,tabName)+",'"+productCode.value+"','"+productName.value+"',"+str(tabSort)+",1,0)\n"
                 diffModule=moduleName
                 #价格点配置
                 #解析价格点
                 pricePointArray=pricePoint.strip().split("\n")
                 for pricePointObject in pricePointArray:
                     pricePointId=pricePointIndex
                     tabId=str(moduleIndex)
                     pricePointDisabled="0"
                     cnCode=pricePointObject.split("-")[1]
                     cnCodeName=pricePointObject.split("-")[0]
                     currentCycleStr=pricePointObject.split("-")[2]
                     if pricePointSort==1:
                      pricePointContent="--价格点配置\n"
                      pricePointContent=pricePointContent+"insert into "+constant.TABLEL_PRICEPOINT+" values("+str(pricePointId)+",'"+cnCode+"','"+cnCodeName+"',"+tabId+",'"+constant.matchDate(constant,currentCycleStr)+"',"+pricePointDisabled+")\n"
                     else:
                      pricePointContent=pricePointContent+",("+str(pricePointId)+",'"+cnCode+"','"+cnCodeName+"',"+tabId+",'"+constant.matchDate(constant,currentCycleStr)+"',"+pricePointDisabled+")\n"
                     pricePointIndex=pricePointIndex+1
                     pricePointSort=pricePointSort+1

        else:
            break

    #生成每个品目的脚本到指定的目录下边
    if productCode and productName:
     f.write(moduleContent)
     f.write(pricePointContent)
     print(moduleContent)
     print(pricePointContent)
     print("---------结束-------")
f.close()
