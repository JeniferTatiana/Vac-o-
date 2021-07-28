def avgcity(ciudades):
yearcount = {}
import csv
with open("Dalziel2016_data.csv", "r") as f:
    my_csv = csv.DictReader(f)
    for line in my_csv:
        myyear = line['year']
        yearcount[myyear] = yearcount.get(myyear, 0)
        yearcount[myyear] = yearcount[myyear] + 1
        for year in ['1906', '1907', '1908','1909']:
            print(year, yearcount[year])
    return
def avgyear(years):
    print()
    return
def avgbiweek(biweeks):
    print()
    return
