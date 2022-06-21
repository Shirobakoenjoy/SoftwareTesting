import pandas as pd

def CheckIsleap(year):
    if year % 4 != 0:
        return 0
    elif year % 100 != 0:
        return 1
    elif year % 400 == 0:
        return 1
    else:
        return 0

def GetNextDay(year, month, day):
    iserror = 0
    if year <= 0:
        print("错误，年份错误")
        return str(1)
        iserror = 1
    nextday = day
    # print(year,month,day)
    if month > 12 or month < 1:
        print("错误，月份错误")
        return str(2)
        iserror = 1
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day < 1 or day > 31:
            print("错误，日期错误")
            return str(3)
            iserror = 1
        nextday = day + 1
        if nextday == 32:
            nextday = 1
            month = month + 1
            if month == 13:
                month = 1
                year = year + 1
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day < 1 or day > 30:
            print("错误，日期错误")
            return str(3)
            iserror = 1
        nextday = day + 1
        if nextday == 31:
            nextday = 1
            month = month + 1
    else:
        nextday = day + 1
        isLeap = CheckIsleap(year)
        if isLeap == 1:
            if day < 1 or day > 29:
                print("错误，日期错误")
                return str(3)
                iserror = 1
            if nextday == 30:
                nextday = 1
                month = 3
        else:
            if day < 1 or day > 28:
                print("错误，日期错误")
                return str(3)
                iserror = 1
            if nextday == 29:
                nextday = 1
                month = 3

    if iserror == 0:
        print("第二天日期为:" + str(year) + "/" + str(month) + "/" + str(nextday))
        return str(year)+"/"+str(month)+"/"+str(nextday)

def changeResult(result):
    if result == '1':
        return "error year"
    elif result == '2':
        return "error month"
    elif result == '3':
        return "error day"
    else:
        return result

def TestByCSV(kind):
    if kind ==0:
        pass
    elif kind ==1:
        head_row = pd.read_csv('../TestCases/testcsv.csv', nrows=0)
        # print("表头", list(head_row))
        head_row_list = list(head_row)
        csv_result = pd.read_csv('../TestCases/testcsv.csv', usecols=head_row_list)
        row_list = csv_result.values.tolist()

        rows = csv_result.shape[0]
        for i in range(rows):
            currentresult = GetNextDay(row_list[i][1],row_list[i][2],row_list[i][3])
            currentresult = changeResult(currentresult)
            row_list[i][5]=currentresult
            if currentresult == row_list[i][4]:
                row_list[i][6]= True
            else:
                row_list[i][6] = False


        finalres = pd.DataFrame(columns=head_row_list, data=row_list)
        store_path = '../result/trytest.csv'
        finalres.to_csv('../result/trytest.csv', index=False,encoding='utf-8')

        return store_path

if __name__ == '__main__':
    TestByCSV(1)
    # today = input("请输入今天的日期(格式为:year/month/day,如2021/7/12):")
    # a = today.split("/")
    # year = int(a[0])
    # month = int(a[1])
    # day = int(a[2])
    # iserror = 0
    # if year <= 0:
    #     print("错误，年份错误")
    #     iserror = 1
    # nextday = day
    # # print(year,month,day)
    # if month > 12 or month < 1:
    #     print("错误，月份错误")
    #     iserror = 1
    # if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    #     if day < 1 or day > 31:
    #         print("错误，日期错误")
    #         iserror = 1
    #     nextday = day + 1
    #     if nextday == 32:
    #         nextday = 1
    #         month = month + 1
    #         if month == 13:
    #             month = 1
    #             year = year + 1
    # elif month == 4 or month == 6 or month == 9 or month == 11:
    #     if day < 1 or day > 30:
    #         print("错误，日期错误")
    #         iserror = 1
    #     nextday = day + 1
    #     if nextday == 31:
    #         nextday = 1
    #         month = month + 1
    # else:
    #     nextday = day + 1
    #     isLeap = CheckIsleap(year)
    #     if isLeap == 1:
    #         if day < 1 or day > 29:
    #             print("错误，日期错误")
    #             iserror = 1
    #         if nextday == 30:
    #             nextday = 1
    #             month = 3
    #     else:
    #         if day < 1 or day > 28:
    #             print("错误，日期错误")
    #             iserror = 1
    #         if nextday == 29:
    #             nextday = 1
    #             month = 3
    #
    # if iserror == 0:
    #     print("第二天日期为:" + str(year) + "/" + str(month) + "/" + str(nextday))
