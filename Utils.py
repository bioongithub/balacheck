import os

from PyQt5 import QtWidgets as QW, uic

def LoadFromUI(fname):
  ui = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'UI', fname)
  page = uic.loadUi(ui)
  return page