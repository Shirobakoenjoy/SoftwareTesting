'''
电信收费
'''


def Charge(TotalTime, UnChargeCount):
    '''
    电信收费
    :param TotalTime: 本月通话分钟数
    :param UnChargeCount: 本年度未缴费次数
    :return: TotalCharge: 总计应缴费用
    '''
    # 健壮性
    if TotalTime<0:
        print("通话时间应大于等于0")
        return 1
    if UnChargeCount<0:
        print("年度未按时缴费次数应大于等于0")
        return 2

    BaseCharge = 25
    CallCharge = TotalTime * 0.15
    CanUnChargeCount = 1
    DiscountRate = 0.01
    # 得到允许的未缴费次数与折扣率
    if TotalTime > 0 and TotalTime <= 60:
        CanUnChargeCount = 1
        DiscountRate = 0.01
    elif TotalTime > 60 and TotalTime <= 120:
        CanUnChargeCount = 2
        DiscountRate = 0.015
    elif TotalTime > 120 and TotalTime <= 180:
        CanUnChargeCount = 3
        DiscountRate = 0.02
    elif TotalTime > 180 and TotalTime <= 300:
        CanUnChargeCount = 3
        DiscountRate = 0.025
    elif TotalTime > 300:
        CanUnChargeCount = 6
        DiscountRate = 0.03
    # 计算折扣
    if UnChargeCount <= CanUnChargeCount:
        DiscountCharge = CallCharge * DiscountRate
    else:
        DiscountCharge = 0

    TotalCharge = BaseCharge + CallCharge - DiscountCharge
    print("本月应收费用:",TotalCharge)
    return TotalCharge


if __name__ == '__main__':
    totalTime = input("请输入总计通话时间:")
    unChargeCount = input("请输入年度累计未按时缴费次数:")
    Charge(totalTime, unChargeCount)