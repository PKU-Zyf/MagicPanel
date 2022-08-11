import excel "C:\Users\PKU-Z\Desktop\MagicPanel\manual\example\example.xlsx", sheet("Sheet1") firstrow clear
egen id = group(城市名)
xtset id 年份
xtreg 专利申请量 人才政策 i.年份 人均GDP, fe robust
