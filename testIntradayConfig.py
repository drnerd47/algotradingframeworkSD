import datetime
import atomic as atom
import definitions as defs
from pathlib import Path
import pandas as pd
import strategies
import reporting as rep
import generalconfigs as genconfigs
import positionconfigs as posconfings
import warnings
import GetConfigs
import time
import DefaultConfigs as defcon
import OptimizedConfigs as opcon

warnings.filterwarnings("ignore")

user = "RI"

if user == "SD":
  Root = "D:/Work/Sykes and Ray/"
  Result_path = "D:/Work/Sykes and Ray/NIFTYOptionsData/OptionsData/Results/"
elif user == "RI":
  Root = "../"
  Result_path = "Results/"

Banknifty_Path = Root + "NIFTYOptionsData/OptionsData/Banknifty/"
Nifty_Path = Root + "NIFTYOptionsData/OptionsData/Nifty/"

year = 2022
startmonth = 1
endmonth = 12
start_date = datetime.date(year, startmonth, 1)
end_date = datetime.date(year, endmonth, 31)
delta = datetime.timedelta(days=1)

# Default Config
config = opcon.ind_straddle_BN_4
# Optimized Config
approach = "INDAL"
tic = time.time()

(generalconfig, positionconfig) = GetConfigs.GetINDStraddlesConfig(config)

trade = pd.DataFrame()
trades = pd.DataFrame()

while start_date <= end_date:
  date_string = start_date.strftime("%Y/Data%Y%m%d.csv")
  BNPath = Banknifty_Path + date_string
  NPath = Nifty_Path + date_string
  my_fileN = Path(NPath)
  my_fileBN = Path(BNPath)
  print(date_string)
  if my_fileN.exists() and my_fileBN.exists():
    masterdfN = atom.LoadDF(NPath)
    masterdfBN = atom.LoadDF(BNPath)
    if (generalconfig["symbol"] == defs.BN):
      trade = strategies.IntraDayStrategy(masterdfBN, generalconfig, positionconfig)
    elif (generalconfig["symbol"] == defs.N):
      trade = strategies.IntraDayStrategy(masterdfN, generalconfig, positionconfig)
    if (len(trade) > 0):
      trades = trades.append(trade)
  else:
    print("No data for " + start_date.strftime("%Y-%m-%d"))
  start_date += delta

toc = time.time()
print("Time taken to run this Strategy ", toc-tic)

trades['date'] = pd.to_datetime(trades["date"])
trades = trades.reset_index()
trades = trades.drop(["index"],axis = 1)

print("\n")
print(trades)
trades.to_csv(Result_path + approach + "trades.csv")

print("\n")
Daily_Chart = rep.GetDailyChart(trades)
print(Daily_Chart)
Daily_Chart.to_csv(Result_path + approach + "DailyChart.csv")

print("\n")
report = rep.Report(trades, Daily_Chart)
print(report)
report.to_csv(Result_path + approach + "Report.csv")

print("\n")
weeklyreport = rep.WeeklyBreakDown(Daily_Chart)
print(weeklyreport)
weeklyreport.to_csv(Result_path + approach + "WeeklyReport.csv")

print("\n")
monthlyreport = rep.MonthlyBreakDown(Daily_Chart)
print(monthlyreport)

print("\n")
dayofweek = rep.DayOfWeek(Daily_Chart)
print(dayofweek)