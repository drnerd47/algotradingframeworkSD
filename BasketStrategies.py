import datetime
import atomic as atom
import definitions as defs
from pathlib import Path
import pandas as pd
import strategies
import reporting as rep
import positionconfigs as posconfig
import generalconfigs as genconfig
import TIconfigs
import directional as direc
import os
import utils
import numpy as np

import warnings
warnings.filterwarnings("ignore")

# Logic to define path
user = "SD"

if user == "SD":
  Root = "D:/Work/Sykes and Ray/"
  Result_path = "D:/Work/Sykes and Ray/NIFTYOptionsData/OptionsData/Results/"
  parent_dir = "D:/Work/Sykes and Ray/NIFTYOptionsData/OptionsData/Results/BasketStrategies/"
elif user == "RI":
  Root = "../"
  Result_path = "Results/"
  parent_dir = "BasketStrategies/"
elif user == "MS":
  Root = "Moulik's File path"
  Result_path = " Moulik's result path"
  parent_dir = " "

Banknifty_Path = Root + "NIFTYOptionsData/OptionsData/PickleFiles/Banknifty/"
Nifty_Path = Root + "NIFTYOptionsData/OptionsData/PickleFiles/Nifty/"


# strategytypes = [ "IntraDayN", "IntraDayBN", "IntradayNRE", "IntradayBNRE", "ExpiryBN", "ExpiryN", "NextDayBNMW", "NextDayNMW", "NextDayBNF", "NextDayNF", "IntradaySA", "ExpirySA", "NextDaySA",
# strategytypes = ["RSI-ADXNb", "RSIDualNb", "BB1Nb", "BB2Nb", "RSI-ADXBNb", "RSIDualBNb", "BB1BNb", "BB2BNb", "RSI-ADXNs", "RSIDualNs", "BB1Ns", "BB2Ns", "SupertrendNs", "RSI-ADXBNs", "RSIDualBNs", "BB1BNs", "BB2BNs", "SupertrendBNs"]

   

# strategytypes = [ "IntraDayN", "IntraDayBN", "IntradayNRE", "IntradayBNRE", "ExpiryBN", "ExpiryN", "NextDayBNMW", "NextDayNMW", "NextDayBNF", "NextDayNF", "IntradaySA", "ExpirySA", "NextDaySA",
strategytypes =[ "RSI-ADXNb", "RSIDualNb", "RSI_2Nb", "BB1Nb",  "BB2Nb", "RSI-ADXBNb", "RSIDualBNb", "RSI_2BNb", "BB1BNb", "BB2BNb",
                 "EMABNb","EMANb",
                 "RSI-ADXNs", "RSIDualNs", "RSI_2Ns", "BB1Ns", "BB2Ns", "RSI-ADXBNs", "RSIDualBNs", "RSI_2BNs", "BB1BNs", "BB2BNs",
                 "EMABNs", "EMANs"]

   

def RunStrategy(strattypes, start, end, yearpath):
  if (strattypes == "IntraDayN"):
      generalconfig = genconfig.generalconfigIntradayN
      positionconfig = posconfig.positionconfigShortStraddle
      intraday = True
      Arb = False
      directional = False
      buystrategy = False
      margin = 110000
  elif (strattypes == "IntraDayBN"):
      generalconfig = genconfig.generalconfigIntradayBN
      positionconfig = posconfig.positionconfigShortStraddle
      intraday = True
      Arb = False
      directional = False
      buystrategy = False
      margin = 180000
  elif (strattypes == "IntradayNRE"):
      generalconfig = genconfig.generalconfigIntradayREN
      positionconfig = posconfig.positionconfigShortStraddle
      intraday = True
      Arb = False
      directional = False
      buystrategy = False
      margin = 110000
  elif (strattypes == "IntradayBNRE"):
      generalconfig = genconfig.generalconfigIntradayREBN
      positionconfig = posconfig.positionconfigShortStraddle
      intraday = True
      Arb = False
      directional = False
      buystrategy = False
      margin = 180000
  elif (strattypes == "ExpiryBN"):
      generalconfig = genconfig.generalconfigExpiryBN
      positionconfig = posconfig.positionconfigShortStraddle
      intraday = False
      Arb = False
      directional = False
      buystrategy = False
      margin = 180000
  elif (strattypes == "ExpiryN"):
      generalconfig = genconfig.generalconfigExpiryN
      positionconfig = posconfig.positionconfigShortStraddle
      intraday = False
      Arb = False
      directional = False
      buystrategy = False
      margin = 110000
  elif (strattypes == "NextDayBNMW"):
      generalconfig = genconfig.generalconfigNextDayBNMW
      positionconfig = posconfig.positionconfigShortStraddle
      intraday = False
      Arb = False
      directional = False
      buystrategy = False
      margin = 180000
  elif (strattypes == "NextDayNMW"):
      generalconfig = genconfig.generalconfigNextDayNMW
      positionconfig = posconfig.positionconfigShortStraddle
      intraday = False
      Arb = False
      directional = False
      buystrategy = False
      margin = 110000
  elif (strattypes == "NextDayBNF"):
      generalconfig = genconfig.generalconfigNextDayBNF
      positionconfig = posconfig.positionconfigLongStraddle
      intraday = False
      Arb = False
      directional = False
      buystrategy = True
  elif (strattypes == "NextDayNF"):
      generalconfig = genconfig.generalconfigNextDayNF
      positionconfig = posconfig.positionconfigLongStraddle
      intraday = False
      Arb = False
      directional = False
      buystrategy = True
  elif (strattypes == "IntradaySA"):
      generalconfig = [genconfig.generalconfigIntradayBN, genconfig.generalconfigIntradayN]
      positionconfig = posconfig.positionconfigStatArbStraddle
      intraday = True
      Arb = True
      directional = False
      buystrategy = False
      margin = 210000
  elif (strattypes == "ExpirySA"):
      generalconfig = [genconfig.generalconfigExpiryBN, genconfig.generalconfigExpiryN]
      positionconfig = posconfig.positionconfigStatArbStraddle
      intraday = False
      Arb = True
      directional = False
      buystrategy = False
      margin = 210000
  elif (strattypes == "NextDaySA"):
      generalconfig = [genconfig.generalconfigNextDayBNMW, genconfig.generalconfigNextDayNMW]
      positionconfig = posconfig.positionconfigStatArbStraddle
      intraday = False
      Arb = True
      directional = False
      buystrategy = False
      margin = 210000
  #######################################################################################################################################
  elif (strattypes == "RSI-ADXNb"):
      generalconfig = genconfig.generalconfigNRSIADX
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfigRSI_ADX
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "RSIDualNb"):
      generalconfig = genconfig.generalconfigNRSIDual
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfig_RSIDual
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "RSI_2Nb"):
      generalconfig = genconfig.generalconfigNRSI2
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfig2_RSI
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "BB1Nb"):
      generalconfig = genconfig.generalconfigNBB1
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfigBB1
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "BB2Nb"):
      generalconfig = genconfig.generalconfigNBB2
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfigBB2
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "EMANb"):
      generalconfig = genconfig.generalconfigNMA
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfigEMA
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
      
  elif (strattypes == "SMANb"):
      generalconfig = genconfig.generalconfigBNMA
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfigSMA
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "RSI-ADXBNb"):
      generalconfig = genconfig.generalconfigBNRSIADX
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfigRSI_ADX
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "RSIDualBNb"):
      generalconfig = genconfig.generalconfigBNRSIDual
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfig_RSIDual
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "RSI_2BNb"):
      generalconfig = genconfig.generalconfigBNRSI2
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfig2_RSI
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "BB1BNb"):
      generalconfig = genconfig.generalconfigBNBB1
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfigBB1
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "BB2BNb"):
      generalconfig = genconfig.generalconfigBNBB2
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfigBB2
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
  elif (strattypes == "EMABNb"):
      generalconfig = genconfig.generalconfigBNMA
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfigEMA
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
      
  elif (strattypes == "SMABNb"):
      generalconfig = genconfig.generalconfigBNMA
      positionconfig = posconfig.positionconfigsinglebuydirecSL
      TIconfig = TIconfigs.TIconfigSMA
      intraday = True
      Arb = False
      directional = True
      buystrategy = True
      
  elif (strattypes == "RSI-ADXNs"):
      generalconfig = genconfig.generalconfigNRSIADX
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigRSI_ADX
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 110000
  elif (strattypes == "RSIDualNs"):
      generalconfig = genconfig.generalconfigNRSIDual
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfig_RSIDual
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 110000
  elif (strattypes == "RSI_2Ns"):
      generalconfig = genconfig.generalconfigNRSI2
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfig2_RSI
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 110000
  elif (strattypes == "BB1Ns"):
      generalconfig = genconfig.generalconfigNBB1
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigBB1
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 110000
  elif (strattypes == "BB2Ns"):
      generalconfig = genconfig.generalconfigNBB2
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigBB2
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 110000
  elif (strattypes == "SupertrendNs"):
      generalconfig = genconfig.generalconfigNST
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigST
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 110000
  
  elif (strattypes == "EMANs"):
      generalconfig = genconfig.generalconfigNMA
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigEMA
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 140000
  elif (strattypes == "SMANs"):
      generalconfig = genconfig.generalconfigNMA
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigSMA
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 140000
  elif (strattypes == "RSI-ADXBNs"):
      generalconfig = genconfig.generalconfigBNRSIADX
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigRSI_ADX
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 140000
  elif (strattypes == "RSIDualBNs"):
      generalconfig = genconfig.generalconfigBNRSIDual
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfig_RSIDual
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 140000
  elif (strattypes == "RSI_2BNs"):
      generalconfig = genconfig.generalconfigBNRSI2
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfig2_RSI
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 140000
  elif (strattypes == "BB1BNs"):
      generalconfig = genconfig.generalconfigBNBB1
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigBB1
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 140000
  elif (strattypes == "BB2BNs"):
      generalconfig = genconfig.generalconfigBNBB2
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigBB2
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 140000
  elif (strattypes == "SupertrendBNs"):
      generalconfig = genconfig.generalconfigBNST
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigST
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 140000
  elif (strattypes == "EMABNs"):
      generalconfig = genconfig.generalconfigBNMA
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigEMA
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 140000
  elif (strattypes == "SMABNs"):
      generalconfig = genconfig.generalconfigBNMA
      positionconfig = posconfig.positionconfigsingleselldirecSL
      TIconfig = TIconfigs.TIconfigSMA
      intraday = True
      Arb = False
      directional = True
      buystrategy = False
      margin = 140000

  trade = pd.DataFrame()
  trades = pd.DataFrame()
  positions = []
  positions1 = []
  positions2 = []

  start_date = start
  end_date = end
  delta = datetime.timedelta(days=1)

  directory = "Strategy "+str(strattypes)
  strategypath = os.path.join(yearpath, directory)

  file = Path(strategypath)
  if file.exists():
      pass
  else:
      os.mkdir(strategypath)  

  if directional == True:
          data = direc.getTIIndicatorData(start_date, end_date, Nifty_Path, Banknifty_Path, generalconfig, TIconfig)            
      
  while start_date <= end_date:
      trade = pd.DataFrame()
      date_string = start_date.strftime("%Y/Data%Y%m%d.pkl")
      BNPath = Banknifty_Path + date_string
      NPath = Nifty_Path + date_string
      my_fileN = Path(NPath)
      my_fileBN = Path(BNPath)
      if my_fileN.exists() and my_fileBN.exists():
          masterdfN = atom.LoadDF(NPath)
          masterdfBN = atom.LoadDF(BNPath)
          if (Arb == False):
              if (generalconfig["symbol"] == defs.BN):
                  masterdf = masterdfBN
              elif (generalconfig["symbol"] == defs.N):
                  masterdf = masterdfN

              if (intraday == True and directional == False):
                  trade = strategies.IntraDayStrategy(masterdf, generalconfig, positionconfig)
              elif (intraday == False and directional == False):
                  (trade, positions) = strategies.MultiDayStrategy(masterdf, positions, generalconfig, positionconfig)
              elif (intraday == True and directional == True):                    
                  trade = strategies.DirectionalStrategy(data, masterdf, generalconfig, positionconfig, TIconfig, start_date)
                  data.to_csv(strategypath+"/signaldata.csv")                
          else:
              if (intraday == True):
                  trade1 = strategies.IntraDayStrategy(masterdfBN, generalconfig[0], positionconfig[0])
                  trade2 = strategies.IntraDayStrategy(masterdfN, generalconfig[1], positionconfig[1])
                  trade = trade.append(trade1)
                  trade = trade.append(trade2)
              else:
                  (trade1, positions1) = strategies.MultiDayStrategy(masterdfBN, positions1, generalconfig[0], positionconfig[0])
                  (trade2, positions2) = strategies.MultiDayStrategy(masterdfN, positions2, generalconfig[1], positionconfig[1])
                  trade = trade.append(trade1)
                  trade = trade.append(trade2)
          if (len(trade) > 0):
              trades = trades.append(trade)
              
      start_date += delta        

  trades['date'] = pd.to_datetime(trades["date"])
  trades = trades.reset_index()
  trades = trades.drop(["index"],axis = 1)
  trades.to_csv(strategypath+"/trades.csv")
  if directional == True:
    Daily_Chart = rep.GetDailyChartTI(trades)
    Daily_Chart.to_csv(strategypath+"/Daily_Report.csv")
    weeklyreport = rep.WeeklyBreakDownTI(Daily_Chart)
    #weeklyreport = weeklyreport.reset_index(drop=True)
    weeklyreport.to_csv(strategypath+"/Weekly_Report.csv")
    report = rep.ReportTI(trades, Daily_Chart)
    report.to_csv(strategypath + "/Report.csv")
    monthlyreport = rep.MonthlyBreakDownTI(Daily_Chart)
    monthlyreport.to_csv(strategypath +"/Monthly_Report.csv")
    dayofweek = rep.DayOfWeekTI(Daily_Chart)
    dayofweek.to_csv(strategypath + "/day_of_week.csv")   
  else :   
    Daily_Chart = rep.GetDailyChart(trades)
    Daily_Chart.to_csv(strategypath+"/Daily_Report.csv")
    weeklyreport = rep.WeeklyBreakDown(Daily_Chart)
    #weeklyreport = weeklyreport.reset_index(drop=True)
    weeklyreport.to_csv(strategypath+"/Weekly_Report.csv")
    report = rep.Report(trades, Daily_Chart)
    report.to_csv(strategypath + "/Report.csv")
    monthlyreport = rep.MonthlyBreakDown(Daily_Chart)
    monthlyreport.to_csv(strategypath +"/Monthly_Report.csv")
    dayofweek = rep.DayOfWeek(Daily_Chart)
    dayofweek.to_csv(strategypath +"/day_of_week.csv")
  if buystrategy == True:
      Margin = utils.BuyMarginCalculator(trades, generalconfig['symbol'])
  else :
      Margin = margin
      
  return (Daily_Chart["Daily pnl"], weeklyreport["Daily pnl"], Margin)

import time
years = [2021, 2022]
for year in years:
    yearpath = os.path.join(parent_dir, str(year))    
    file = Path(yearpath)
    if file.exists():
        pass
    else:
        os.mkdir(yearpath)  
    if year == 2019:
        start = datetime.date(2019, 2, 1)
        end = datetime.date(2019, 12, 31)
    elif year == 2020:
        start = datetime.date(2020, 1, 1)
        end = datetime.date(2020, 12, 31)
    elif year == 2021:
        start = datetime.date(2021, 1, 1)
        end = datetime.date(2021, 12, 31)
    elif year == 2022:
        start = datetime.date(2022, 1, 1)
        end = datetime.date(2022, 9, 30)

    dailyArr = pd.DataFrame()
    weeklyArr = pd.DataFrame()

    for strategy in strategytypes :
        print("Running Strategy " + strategy + " from " + str(start) + " to " + str(end))
        tic = time.time()
        try:
            (daily, weekly, Margin) = RunStrategy(strategy, start, end, yearpath)
        except :
            print("Error in this Strategy")
            continue
        toc = time.time()
        print("Time taken to run this strategy ", toc-tic)
        dailyArr[strategy] = daily
        dailyArr = dailyArr.fillna(0)
        weeklyArr[strategy] = weekly
        weeklyArr.loc['Total', strategy] = weekly.sum()
        weeklyArr.loc['Margin', strategy] = Margin
        weeklyArr = weeklyArr.fillna(0)
        # print(weeklyArr)
    
    temp_weeklyArr = weeklyArr.drop(['Total', 'Margin'], axis=0)
    # print(temp_weeklyArr)
    weeklyCorr = temp_weeklyArr.corr()

    col_list = list(weeklyArr)
    weeklyArr['Mean Strategy'] = weeklyArr[col_list].mean(axis=1)
    weeklyArr['Sum Strategy'] = weeklyArr[col_list].sum(axis=1)

    df = pd.DataFrame()
    df = weeklyArr.cumsum(axis=0)
    Roll_max = df.rolling(window = weeklyArr.size, min_periods=1).max()
    Weekly_Drawdown = df - Roll_max
    Max_Drawdown = Weekly_Drawdown.min()
    weeklyArr.loc["No. of Win Weeks"] = weeklyArr[weeklyArr > 0].count()
    weeklyArr.loc["No. of Bad Weeks"] = weeklyArr[weeklyArr < 0].count()
    weeklyArr.loc["Max Drawdown"] = Max_Drawdown
    weeklyArr.loc['% Return'] = weeklyArr.loc['Total']/weeklyArr.loc['Margin']*100
    weeklyArr.loc['% Drawdown'] = weeklyArr.loc['Max Drawdown']/weeklyArr.loc['Margin']*100

    # print("\n")
    # print(weeklyArr)
    # print("\n")
    weeklyCorr.to_csv(yearpath+"/BasketCorr.csv")
    weeklyArr.to_csv(yearpath+"/BasketResults.csv") 

