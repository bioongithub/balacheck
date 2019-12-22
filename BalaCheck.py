import sys
from PyQt5.QtWidgets import *

from Utils import LoadFromUI

from MonthsPage import MonthsPage
from PaymentsPage import PaymentsPage
from FinanceDB import FinanceDB

class BalaCheck:
  def __init__(self, page):
    self.monthsPageName   = 'monthsPage'
    self.banksPageName    = 'banksPage'
    self.paymentsPageName = 'paymentsPage'
    self.incomesPageName  = 'incomesPage'

    self.db = FinanceDB('balacheck.db')

    self.page = page
    self.pages = {}
    for pn in [self.monthsPageName, self.banksPageName, self.paymentsPageName, self.incomesPageName]:
      self.pages[pn] = self.page.findChild(QWidget, pn)

    self.monthsPage = MonthsPage(self, self.pages[self.monthsPageName])
    self.paymentsPage = PaymentsPage(self, self.pages[self.paymentsPageName])

if __name__ == "__main__":
  app = QApplication([])

  window = QWidget()
  window.setWindowTitle("Balancing Check")
  window.resize(720, 520)

  gridLayout = QGridLayout(window)
  window.setLayout(gridLayout)

  page = LoadFromUI('BalaCheck.ui')
  appRoot = BalaCheck(page)

  gridLayout.addWidget(page)

  window.show() 
 
  sys.exit(app.exec())
