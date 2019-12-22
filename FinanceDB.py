import datetime

PAY_PERIOD_ONCE=1
PAY_PERIOD_MONTH=2
PAY_PERIOD_2MONTH=3
PAY_PERIOD_3MONTH=4
PAY_PERIOD_4MONTH=5
PAY_PERIOD_SEMIYEAR=6
PAY_PERIOD_YEAR=7

# class PaySchedule:
#   period:
#     once
#     month
#     2month
#     3month
#     year
#   duedate (list) each items
#     once: mm/dd/yyyy (list)
#     month: dd (list)
#     2month: mm/dd/yyyy first date to count from (only one item)
#     3month: mm/dd/yyyy first date to count from (only one item)
#     year: mm/dd (list)
#
class PaySchedule:
  def __init__(self, period, duedate):
    self.period = period
    self.duedate = duedate

# class Bank:
#   name: string
#   transactions (list of Transaction objects)
#
class Bank:
  def __init__(self, name):
    self.name = name
    self.transactions = []

# class Transaction
#   info: string (custom for Other, from Payment or Income)
#   amount: fload < 0 payment or; >0 income
#   payment: reference to Bill or Income, None of other
#   status:
#     Planned: month befor duedate (does not exist in DB)
#     Billed: bill sent/recieved, 3 days befor payday for autopay incomes/bills
#     Scheduled: payment scheduled, payday for autopay
#     Completed: deposited to/withdrawed from bank
#   check: check number
#   started: mm/dd/yyyy when transaction is scheduled
#   finished: mm/dd/yyyy
#
#   DB note: status does not exist in DB. Calculated as:
#     Planned: no transaction in DB, but Bill or Payment in range (1 month to duedate )
#     Billed: exist in DB, but started and finished are NULL, bank ID may be NULL.
#     Scheduled: exist in DB, started is Date and finished is NULL
#     Completed: exist in DB, started and finished are Date 
#
class Transaction:
  def __init__(self, info, amount, payment = None, status = "Planned", check = None, start = None, finish = None):
    self.info = info
    self.amount = amount
    self.payment = payment
    self.status = status
    self.check = check
    self.start = start
    self.finish = finish

# class Payment:
#   info: string
#   amount: float
#   duedate: PaySchedule
#   autobill: bool
#   autopay: bool
#   bank: reference to Bank if autopay, other None
#   active: bool False if payment is deactivated or payed-off once payment
#
#  DB notes: autopay does not exist in DB, it's true iff bank is not NULL
#
class Payment:
  def __init__(self, info, amount, duedate, autobill = False, bank = None, active = True):
    self.info = info
    self.amount = amount
    self.duedate = duedate
    self.autobill = autobill
    self.autopay = bank != None
    self.active = active
    self.bank = bank

# class Income:
#   info: string
#   amount: float
#   payday: PaySchedule
#   autopay: bool
#   bank: reference to Bank if direct deposit or None if by paycheck
#   active: bool False if income is deactivated or payed-off once payment
#
#  DB notes: autopay does not exist in DB, it's true iff bank is not NULL
#
class Income:
  def __init__(self, info, amount, payday, bank = None, active = True):
    self.info = info
    self.amount = amount
    self.payday = payday
    self.autopay = bank != None
    self.active = active
    self.bank = bank

#
class PaymentRecord:
  def __init__(self, payment, transaction = None):
    self.payment = payment
    self.transaction = transaction

class FinanceDB:
  def __init__(self, DBpath):
    pass

  def getFirstMonth(self):
    # TODO:
    return 2019*12+9

  def getMonthData(self, month):
    # TODO:
    return self.payments

  def getPaymentsList(self):
    # TODO:
    return self.payments
