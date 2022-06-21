# 记录当月销售数量
Num_MainEngine_currentMonth = 0
Num_Display_currentMonth = 0
Num_Peripheral_currentMonth = 0


def ComputeSale(Num_MainEngine, Num_Display, Num_Peripheral):
    '''
    计算销售额
    :param Num_MainEngine: 主机数量
    :param Num_Display: 显示器数量
    :param Num_Peripheral: 外设数量
    :return:
    '''
    global Num_MainEngine_currentMonth
    global Num_Display_currentMonth
    global Num_Peripheral_currentMonth

    if Num_MainEngine == -1:
        Total_Sales = 25 * Num_MainEngine_currentMonth + 30 * Num_Display_currentMonth + 45 * Num_Peripheral_currentMonth
        if Total_Sales <= 1000:
            Commission = Total_Sales * 0.1
        elif Total_Sales > 1000 and Total_Sales <= 1800:
            Commission = Total_Sales * 0.15
        elif Total_Sales > 1800:
            Commission = Total_Sales * 0.2

        return Commission
    else:
        Num_MainEngine_currentMonth = Num_MainEngine_currentMonth + Num_MainEngine
        Num_Display_currentMonth = Num_Display_currentMonth + Num_Display
        Num_Peripheral_currentMonth = Num_Peripheral_currentMonth + Num_Peripheral
        if Num_MainEngine_currentMonth > 70:
            Num_MainEngine_currentMonth = 70
        if Num_Display_currentMonth > 80:
            Num_Display_currentMonth = 80
        if Num_Peripheral_currentMonth > 90:
            Num_Peripheral_currentMonth = 90


if __name__ == '__main__':
    # 说实话没看到这个题想让干啥
    MainEngine = 0
    Display = 0
    Peripheral = 0
    MainEngine = input("请输入主机数目")
    if MainEngine ==-1:
        ComputeSale(-1,0,0)
    else:
        Display = input("请输入显示器数目")
        Peripheral = input("请输入外设树木")

    ComputeSale(MainEngine,Display,Peripheral)
