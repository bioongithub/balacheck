import sqlite3

class DBtable(Object):
  def __init__(self, tname, attr):
    self.tname = tname
    self.attr = attr

  def Create(self, db_cursor):
    cmd = "CREATE TABLE "+self.name+" (id INTEGER NOT NULL PRIMARY KEY"
    for at in self.attr:
      cmd += ", " + at[0] + " " + at[2]
    for at in self.attr:
      if len(at) > 3 and at[3] != None:
        cmd += ", " + at[3]
    cmd += ")")
    db_cursor.execute(cmd)

  def add(self, db_cursor, obj):
    #cmd = "INSERT INTO banks ("+bankList[0]+") VALUES (\""+name+"\")"
    cmd = None
    for at in self.attr:
      if cmd == None:
        cmd = "INSERT INTO "+tname+" ("
      else:
        cmd += ", "
      cmd += at[0]
    cmd += ") VALUES ("
    for at in self.attr:
      str(getattr(obj, at[0]))
    cmd += ")"
    db_cursor.execute(cmd)

  def getAll(self, db_cursor):
    cmd = None
    for at in self.attr:
      if cmd == None:
        cmd = "SELECT "
      else:
        cmd += ", "
      cmd += at[0]
    cmd += " FROM "+tname
    db_cursor.execute(cmd)
      
class DBbanks(DBtable)
  def __init__(self, DB):
    attr = [("name", "", "VARCHAR(64)")]
    super(DBbanks, self).__init__("banks", attr)
      
class DBtransactions(DBtable)
  def __init__(self, DB):
    attr = [
        ("info", "", "VARCHAR(128)"),
        ("amount", float(0.0), "DECIMAL(9,2)"),
        ("'check'", int(0), "INT"),
        ("start", None, "DATE"),
        ("finish", None, "DATE"),
        ("bank", int(0), "INT", "FOREIGN KEY (bank) REFERENCES banks(id) ON DELETE CASCADE"),
        ("payment", int(0), "INT", "FOREIGN KEY (payment) REFERENCES payments(id) ON UPDATE CASCADE"),
        ("income", int(0), "INT", "FOREIGN KEY (income) REFERENCES incomes(id) ON UPDATE CASCADE"),
      ]
    super(DBtransactions, self).__init__("transactions", attr)
      
class DBpayments(DBtable)
  def __init__(self, DB):
    attr = [
        ("info", "", "VARCHAR(128)"),
        ("amount", float(0.0), "DECIMAL(9,2)"),
        ("duedate", None, "DATE"),
        ("autobill", False, "BOOL"),
        ("active", False, "BOOL"),
        ("bank", int(0), "INTEGER", "FOREIGN KEY (bank) REFERENCES banks(id) ON UPDATE CASCADE")
      ]
    super(DBpayments, self).__init__("payments", attr)

class DBincomes(DBtable)
  def __init__(self, DB):
    attr = [
        ("info", "", "VARCHAR(128)"),
        ("amount", float(0.0), "DECIMAL(9,2)"),
        ("payday", None, "DATE"),
        ("active", False, "BOOL"),
        ("bank", int(0), "INT", "FOREIGN KEY (bank) REFERENCES banks(id) ON UPDATE CASCADE")
      ]
    super(DBincomes, self).__init__("incomes", attr)

class DB:
  def __init__(self, fname):
    self.fname = fname

    banks = DBbanks()

    self.db = sqlite3.connect(fname)
    cursor = self.db.cursor()
    banks.Create(cursor)

  def addBank(self, name):
    banks.add(
    self.cursor.execute("INSERT INTO banks ("+bankList[0]+") VALUES (\""+name+"\")")
    rowid = self.cursor.lastrowid
    self.db.commit()
    return rowid

  def readAllBanks(self, record_list):
    recordstr = ", ".join(record_list)
    self.cursor.execute("SELECT "+recordstr+" FROM banks")
    return self.cursor.fetchall()

  def addPayment(self, info, amount, duedate, autobill, bank):
    command = "INSERT INTO payments (info, amount, duedate, autobill, active, bank) "+\
        "VALUES (\""+info+"\", "+str(amount)+", \""+\
        str(duedate.year)+"\\"+str(duedate.month)+"\\"+str(duedate.day)+"\", "+\
        str(1 if autobill else 0)+", 1, "+str(bank)+")"
    print(command)
    self.cursor.execute(command)
    rowid = self.cursor.lastrowid
    self.db.commit()
    return rowid

  def readAllPayments(self, record_list):
    recordstr = ", ".join(record_list)
    self.cursor.execute("SELECT "+recordstr+" FROM payments")
    return self.cursor.fetchall()
