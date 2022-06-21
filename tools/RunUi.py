import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem
from PyQt5 import Qt
import pandas as pd
import numpy as np
from solutions import Triangles, Calendar, ComputerSale, TelecomCharge
# import PagesUi
import allpage


class pages_window(allpage.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(pages_window, self).__init__()
        self.setupUi(self)

        # 设置信号与槽函数
        # 页面切换
        self.pushButton_switch_tri.clicked.connect(self.display_triangle)
        self.pushButton_switch_cal.clicked.connect(self.display_calendar)
        self.pushButton_switch_computersale.clicked.connect(self.display_computersale)
        self.pushButton_switch_charge.clicked.connect(self.display_charge)
        # 提交按钮
        self.submitButton_tri.clicked.connect(self.onTriSubmitClicked)
        self.pushButton_submit_cal.clicked.connect(self.onCalSubmitClicked)
        self.submitButton_sale.clicked.connect(self.onSaleSubmitClicked)
        self.submitButton_charge.clicked.connect(self.onChargeSubmitClicked)
        # 清空按钮
        self.clearButton_tri.clicked.connect(self.onTriClearClicked)
        self.pushButton_clear_cal.clicked.connect(self.onCalClearClicked)
        self.clearButton_sale.clicked.connect(self.onSaleClearClicked)
        self.clearButton_charge.clicked.connect(self.onChargeClearClicked)
        # 测试按钮
        self.testButton_tri.clicked.connect(self.onTestTriClicked)
        self.testButton_cal.clicked.connect(self.onTestCalClicked)

    def display_triangle(self):
        self.stackedWidget.setCurrentIndex(0)

    def display_calendar(self):
        self.stackedWidget.setCurrentIndex(1)

    def display_computersale(self):
        self.stackedWidget.setCurrentIndex(2)

    def display_charge(self):
        self.stackedWidget.setCurrentIndex(3)

    # test by csv
    def onTestTriClicked(self):
        content = self.comboBox_tri.currentText()
        if content == "边界值法":

            print("使用边界值方法进行测试")
        elif content == "等价类法":
            print("使用等价类法进行测试")
        else:
            print("？？")

    def onTestCalClicked(self):
        kind = self.comboBox_cal.currentText()
        if kind == "边界值法":
            print("边界值法")
            Calendar.TestByCSV(0)
        elif kind == "等价类法":
            print("等价类法")
            resultpath = Calendar.TestByCSV(1)
            input_table = pd.read_csv(resultpath)
            input_table_rows = input_table.shape[0]
            input_table_cols = input_table.shape[1]
            input_table_header = input_table.columns.values.tolist()
            # 设置行列表头
            self.tableWidget_cal.setColumnCount(input_table_cols)
            self.tableWidget_cal.setRowCount(input_table_rows)
            self.tableWidget_cal.setHorizontalHeaderLabels(input_table_header)

            for i in range(input_table_rows):
                input_table_rows_value = input_table.iloc[[i]]
                input_table_rows_value_array = np.array(input_table_rows_value)
                input_table_rows_value_list = input_table_rows_value_array.tolist()[0]
                for j in range(input_table_cols):
                    input_table_items_list = input_table_rows_value_list[j]
                    input_table_items = str(input_table_items_list)  # 该数据转换成字符串
                    newItem = QTableWidgetItem(input_table_items)  # 该字符串类型的数据新建为tablewidget元素
                    # newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 显示为水平居中、垂直居中
                    self.tableWidget_cal.setItem(i, j, newItem)
            self.tableWidget_cal.setColumnWidth(0,90)
            self.tableWidget_cal.setColumnWidth(1,50)
            self.tableWidget_cal.setColumnWidth(2, 60)
            self.tableWidget_cal.setColumnWidth(3, 50)
            self.tableWidget_cal.setColumnWidth(4, 140)
            self.tableWidget_cal.setColumnWidth(6, 100)
            self.tableWidget_cal.setColumnWidth(7, 150)
            self.tableWidget_cal.show()

    # 三角形
    def onTriSubmitClicked(self):

        a = self.lineEdit_a.text()
        b = self.lineEdit_b.text()
        c = self.lineEdit_c.text()
        if a == '' or b == '' or c == '':
            pass
        else:
            a = float(a)
            b = float(b)
        c = float(c)
        result = Triangles.check(a, b, c)
        if result == -1:
            self.textBrowser_result.setText("不是三角形")
        elif result == 0:
            self.textBrowser_result.setText("等边三角形")
        elif result == 1:
            self.textBrowser_result.setText("等腰直角三角形")
        elif result == 2:
            self.textBrowser_result.setText("等腰锐角三角形")
        elif result == 3:
            self.textBrowser_result.setText("等腰钝角三角形")
        elif result == 4:
            self.textBrowser_result.setText("直角三角形")
        elif result == 5:
            self.textBrowser_result.setText("锐角三角形")
        elif result == 6:
            self.textBrowser_result.setText("钝角三角形")

    def onTriClearClicked(self):

        self.lineEdit_a.clear()
        self.lineEdit_b.clear()
        self.lineEdit_c.clear()
        self.textBrowser_result.clear()

    # 万年历
    def onCalSubmitClicked(self):

        year = self.lineEdit_year.text()

        month = self.lineEdit_month.text()
        day = self.lineEdit_day.text()
        if year == '' or month == '' or day == '':
            pass
        else:
            year = int(year)
            month = int(month)
            day = int(day)
            result = Calendar.GetNextDay(year, month, day)
        if result == '1':
            self.textBrowser_result_cal.setText("错误，年份出错")
        elif result == '2':
            self.textBrowser_result_cal.setText("错误，月份出错")
        elif result == '3':
            self.textBrowser_result_cal.setText("错误，日期出错")
        else:
            self.textBrowser_result_cal.setText(result)

    def onCalClearClicked(self):
        self.lineEdit_year.clear()
        self.lineEdit_month.clear()
        self.lineEdit_day.clear()
        self.textBrowser_result_cal.clear()

    # 电脑
    def onSaleSubmitClicked(self):
        host = self.lineEdit_host.text()
        display = self.lineEdit_display.text()
        peripheral = self.lineEdit_peripheral.text()
        if host == '' or display == '' or peripheral == '':
            pass
        else:
            host = int(host)
            display = int(display)
            peripheral = int(peripheral)

            result = ComputerSale.ComputeSale(host, display, peripheral)

            self.textBrowser_result_sale.setText(str(result))

    def onSaleClearClicked(self):
        self.lineEdit_host.clear()
        self.lineEdit_display.clear()
        self.lineEdit_peripheral.clear()
        self.textBrowser_result_sale.clear()

    # 电信收费
    def onChargeSubmitClicked(self):
        totaltime = self.lineEdit_totalTime.text()
        totalcount = self.lineEdit_totalcount.text()
        if totaltime == '' or totalcount == '':
            pass
        else:
            totaltime = int(totaltime)
            totalcount = int(totalcount)
            result = TelecomCharge.Charge(totaltime, totalcount)
            if result == 1:
                self.textBrowser_result_charge.setText("错误，通话时间应大于0")
            elif result == 2:
                self.textBrowser_result_charge.setText("错误，年度未按时缴费次数应不小于0")
            else:
                self.textBrowser_result_charge.setText(str(result))

    def onChargeClearClicked(self):
        self.lineEdit_totalTime.clear()
        self.lineEdit_totalcount.clear()
        self.textBrowser_result_charge.clear()


# def onTriSelected(self):
#     content = self.comboBox_tri.currentText()

# self.showTable()

# def showTable(self):
#     # input_path = "../TestCases/testcsv.csv"
#     input_table = pd.read_csv("../TestCases/testcsv.csv")
#     input_table_rows = input_table.shape[0]
#     input_table_cols = input_table.shape[1]
#     input_table_header = input_table.columns.values.tolist()
#     # 设置行列表头
#     self.tableWidget1.setColumnCount(input_table_cols)
#     self.tableWidget1.setRowCount(input_table_rows)
#     self.tableWidget1.setHorizontalHeaderLabels(input_table_header)
#
#     for i in range(input_table_rows):
#         input_table_rows_value = input_table.iloc[[i]]
#         input_table_rows_value_array = np.array(input_table_rows_value)
#         input_table_rows_value_list = input_table_rows_value_array.tolist()[0]
#         for j in range(input_table_cols):
#             input_table_items_list = input_table_rows_value_list[j]
#             input_table_items = str(input_table_items_list)  # 该数据转换成字符串
#             newItem = QTableWidgetItem(input_table_items)  # 该字符串类型的数据新建为tablewidget元素
#             # newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 显示为水平居中、垂直居中
#             self.tableWidget1.setItem(i, j, newItem)
#
#     self.tableWidget1.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = pages_window()
    main_window.show()
    sys.exit(app.exec_())
