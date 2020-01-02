import math

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

from Utils import LoadFromUI

class PaymentsPage:
  def __init__(self, root, page):
    self.root = root
    self.page = page

    self.payments = self.root.db.getPaymentsList()
    self.paymentsList = self.page.findChild(QTableWidget, "paymentsList")
    self.paymentsList.setRowCount(len(self.payments))
    for irec in range(0, len(self.payments)):
      rec = self.payments[irec]
      self.paymentsList.setItem(irec, 0, QTableWidgetItem(rec.name, QTableWidgetItem.UserType+irec))
      self.paymentsList.setItem(irec, 1, QTableWidgetItem('${:,.2f}'.format(rec.amount)))
      self.paymentsList.setItem(irec, 2, QTableWidgetItem(str(rec.duedate)))

    self.paymentsList.doubleClicked.connect(self.onMonthsListDClick)
    self.paymentsList.itemSelectionChanged.connect(self.onMonthsListSelect)

    addPaymentBtn = self.page.findChild( QPushButton, "addPaymentBtn")
    addPaymentBtn.clicked.connect(self.onAddPayment)

    self.deletePaymentBtn = self.page.findChild( QPushButton, "deletePaymentBtn")
    self.deletePaymentBtn.clicked.connect(self.onDeletePayment)

  def EditPayment(self, paymentIdx):
    self.addPaymentForm = LoadFromUI('EditPayment.ui')
    paymentName = self.addPaymentForm.findChild(QLineEdit, 'paymentName')
    billedAmount = self.addPaymentForm.findChild(QLineEdit, 'billedAmount')
    dueDate = self.addPaymentForm.findChild(QDateEdit, 'dueDate')
    autoPayment = self.addPaymentForm.findChild( QCheckBox, 'autoPayment')
    payDate = self.addPaymentForm.findChild(QDateEdit, 'payDate')
    payBank = self.addPaymentForm.findChild(QComboBox, 'payBank')
    payPeriod = self.addPaymentForm.findChild(QComboBox, 'payPeriod')
    self.buttonBox = self.addPaymentForm.findChild(QDialogButtonBox, 'buttonBox')

    if paymentIdx < 0:
      self.addPaymentForm.setWindowTitle('Add Payment')
      self.buttonBox.button( QDialogButtonBox.Ok ).setEnabled( False )
    else:
      self.addPaymentForm.setWindowTitle('Edit Payment')
      rec = self.payments[paymentIdx]
      paymentName.setText(rec.name)
      billedAmount.setText('{:,.2f}'.format(rec.amount))
      dueDate.setDate(rec.duedate)

      self.setOKEnable(paymentName, billedAmount)

    autoPayment.stateChanged.connect(self.onAutoPaymentChanged)

    billedAmount.setValidator( QtGui.QDoubleValidator(0, math.inf, 2, self.addPaymentForm) );

    paymentName.textChanged.connect(self.onTextChanged)
    billedAmount.textChanged.connect(self.onTextChanged)

    dueDate.setDate(QDate.currentDate())

    payDate.setDate(QDate.currentDate())

    self.addPaymentForm.setWindowModality(Qt.ApplicationModal)
    res = self.addPaymentForm.exec()
    if res == 1:
      print("==> Accepted ",
        paymentName.text(),
        float(billedAmount.text()),
        autoPayment.isChecked(),
        dueDate.date().toString(),
        payPeriod.currentText(),
        flush=True)

      if autoPayment.isChecked():
        print("==> autoPay ",
          payDate.date().toString(),
          payBank.currentText() if payBank.count() > 0 else '<None>',
          flush=True)

  #@pyqtSlot()
  def onAutoPaymentChanged(self, status):
    # Depends on auto pay status, enable or disable auto pay option editors
    autoPayOptions = self.addPaymentForm.findChild(QGroupBox, 'autoPayOptions')
    autoPayOptionsList = autoPayOptions.findChildren(QWidget)
    autoPayOptions.setEnabled(status != 0)
    for opt in autoPayOptionsList:
      opt.setEnabled(status != 0)

  def onTextChanged(self, text):
    # If payment name and amount are valid values, enable OK button.
    paymentName = self.addPaymentForm.findChild(QLineEdit, 'paymentName')
    billedAmount = self.addPaymentForm.findChild(QLineEdit, 'billedAmount')
    self.setOKEnable(paymentName, billedAmount)

  def setOKEnable(self, paymentName, billedAmount):
    self.buttonBox.button( QDialogButtonBox.Ok ).setEnabled(
      not (not  paymentName.text().split() or not billedAmount.text()) )

  #@pyqtSlot()
  def onAddPayment(self):
    self.EditPayment(-1)

  def onMonthsListDClick(self, mi):
    headItem = self.paymentsList.item(mi.row(), 0)
    irec = headItem.type() - QTableWidgetItem.UserType
    self.EditPayment(irec)

  #@pyqtSlot()
  def onDeletePayment(self):
    rows = self.paymentsList.selectionModel().selectedRows()
    print("==> delete payment(s) ", len(rows), flush=True)

  def onMonthsListSelect(self):
    self.deletePaymentBtn.setEnabled(self.paymentsList.selectionModel().hasSelection())
