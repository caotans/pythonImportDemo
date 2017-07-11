#!usr/bin/python3.06
#coding:utf-8
class constant:
 TABLEL_MODULE="[AnalysisPlatform].[dbo].[Ref_CommodityModuleDetail]"
 TABLEL_TAB="[AnalysisPlatform].[dbo].[Ref_CommodityTab]"
 TABLEL_PRICEPOINT="[AnalysisPlatform].[dbo].[Ref_TabPricePointDetail]"
 JG="价格"
 GX="供需"
 ZZCQ="装置/船期"
 LRTL="利润/套利"
 SY="上游"
 XY="下游"
 TDP="替代品"
 HGSJ="宏观数据"
 HYSJ="行业指数"
 AXSZS="安讯思指数"

 GNJG="国内价格"
 QQJG="全球价格"
 QYBJ="企业报价"
 CNCLKGL="产能产量开工率"
 BGXQ="表观需求"
 JCK="进出口"
 XYXQ="下游需求"
 KC="库存"
 GXYC="供需预测"
 TCJX="停车检修"
 CQ="船期"
 KJGT="扩建/关停"
 XYJG="下游价格"
 KGL="开工率"
 XYLR="下游利润"
 HL="汇率"
 YJ="油价"
 GDP="GDP"
 CPI="CPI"
 PMI="PMI"
 PPI="PPI"
 M2="M2"
 LR="利润"
 TL="套利"
 FDCY="房地产业"
 FZHY="纺织行业"
 GYHY="工业行业"
 JDHY="家电行业"
 QCHY="汽车行业"
 YSHCCY="运输和存储业"
 SYHHXGY="石油和化学工业"
 NYHY="能源行业"
 JXHY="机械行业"
 JRSC="金融市场"
 HGZS="化工指数"
 NYZS="能源指数"
 TRQ="天然气"
 JGDB="价格对比"
 SYJCK="进出口"
 WPBJ="外盘报价"
 DAY="日"
 WEEK="周"
 MONTH="月"
 YEAR="年"
 QUARTER="季"

 def matchDate(self,time):
     return time.replace(self.DAY,"day").replace(self.WEEK,"week").replace(self.MONTH,"month").replace(self.YEAR,"year").replace(self.QUARTER,"quarter")
 def matchDic(self,name):
     if name==self.JG:
         return "101"
     elif name==self.GX:
         return "102"
     elif name==self.ZZCQ:
         return "103"
     elif name==self.LR:
         return "104"
     elif name==self.SY:
         return "105"
     elif name==self.XY:
         return "106"
     elif name==self.TDP:
         return "110"
     elif name==self.HGSJ:
         return "107"
     elif name==self.HYSJ:
         return "108"
     elif name==self.AXSZS:
         return "109"
     elif name==self.GNJG:
         return "1"
     elif name==self.QQJG:
         return "2"
     elif name==self.QYBJ:
         return "3"
     elif name==self.CNCLKGL:
         return "4"
     elif name==self.BGXQ:
         return "5"
     elif name==self.JCK:
         return "6"
     elif name==self.XYXQ:
         return "7"
     elif name==self.KC:
         return "8"
     elif name==self.GXYC:
         return "9"
     elif name==self.TCJX:
         return "10"
     elif name==self.CQ:
         return "11"
     elif name==self.KJGT:
         return "12"
     elif name==self.XYJG:
         return "13"
     elif name==self.KGL:
         return "14"
     elif name==self.XYLR:
         return "15"
     elif name==self.HL:
         return "16"
     elif name==self.YJ:
         return "17"
     elif name==self.GDP:
         return "18"
     elif name==self.CPI:
         return "19"
     elif name==self.PMI:
         return "20"
     elif name==self.PPI:
         return "21"
     elif name==self.M2:
         return "22"
     elif name==self.LR:
         return "23"
     elif name==self.TL:
         return "24"
     elif name==self.FDCY:
         return "25"
     elif name==self.FZHY:
         return "26"
     elif name==self.GYHY:
         return "27"
     elif name==self.JDHY:
         return "28"
     elif name==self.QCHY:
         return "29"
     elif name==self.YSHCCY:
         return "30"
     elif name==self.SYHHXGY:
         return "31"
     elif name==self.NYHY:
         return "32"
     elif name==self.JXHY:
         return "33"
     elif name==self.JRSC:
         return "34"
     elif name==self.HGZS:
         return "35"
     elif name==self.NYZS:
         return "36"
     elif name==self.TRQ:
         return "37"
     elif name==self.JGDB:
         return "38"
     elif name==self.SYJCK:
         return "39"
     elif name==self.WPBJ:
         return "40"

