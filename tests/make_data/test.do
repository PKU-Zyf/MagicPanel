import delimited "C:\Users\PKU-Z\Desktop\MagicPanel\tests\result.csv", encoding(GBK) clear
egen id = group(unit)
xtset id time
xtreg 专利数量 人才政策 i.time 人均gdp population, fe robust
