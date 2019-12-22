from datetime import date
from PyQt5.QtWidgets import *

def MonthName(yearMonth):
  year = yearMonth//12
  month = yearMonth%12
  months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  return str(year) + ", " + months[month]

class MonthsPage:
  def __init__(self, root, page):
    self.root = root
    self.page = page
    today = date.today()

    monthsList = self.page.findChild(QTabWidget, "monthsList")
    for idx in range(0, monthsList.count()):
      monthsList.removeTab(idx);

    self.currentMonthIdx = today.year*12 + today.month-1
    self.firstMonthIdx = self.root.db.getFirstMonth()
    selectMonth = self.currentMonthIdx - self.firstMonthIdx
    for yearMonth in range(self.firstMonthIdx, self.currentMonthIdx+6):
      monthsList.addTab(QWidget(), MonthName(yearMonth))
    monthsList.currentChanged.connect(self.onChange)
    monthsList.setCurrentIndex(selectMonth)

  #@pyqtSlot()
  def onChange(self,i):
    monthData = self.root.db.getMonthData(self.firstMonthIdx + i)
    currentMonth = self.page.findChild(QTableWidget, "currentMonth")
    currentMonth.setRowCount(len(monthData))
    for irec in range(0, len(monthData)):
      rec = monthData[irec]
      currentMonth.setItem(irec, 0, QTableWidgetItem(rec.name))
      currentMonth.setItem(irec, 1, QTableWidgetItem('${:,.2f}'.format(rec.amount)))
      currentMonth.setItem(irec, 2, QTableWidgetItem(str(rec.duedate)))


