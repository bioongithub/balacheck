# balacheck
PyQt script to balance checkbooks. Open source. Work in progress.

## Idea
Idea is to collect transaction from banks and payed, scheduled and current payments, show expected balances and
let custimer to see that all bank accounts are secure against overdrafts. The program also allows the customer
to have notification that next bill payments are coming. Paymants may be one time or recurrent. Recurrent payments 
may be scheduled monthly, semimonthly, every two, three or four month, yearly and semiyearly. 

##Planed structure
UI is PyQt in `.ui` file. All `.ui` files are in `UI` directory. All windows (Tabs) are in one `BalaCheck.ui` file.
Other dialogs are placed to its own separate `.ui` files. The project is supposed to be open in QtCreator project 
(`BalaCheck.pyproject` file)

##UI
UI has 4 pages (dialog tab windows):
1. Month payments
2. Banks
3. Payments
4. Incomes

### Month payments
Month payments page contains tab page for each month. Month page contains list of payments, scheduled for this month.
Month is selected as a tab. Current month payments are represented as a table. Each payment is a table row.
There are columns:
- Name of bill source. 
- Billed amount
- Due date of the payment
- Date when bill has been payed or blank, if it's not.
- To pay: amount has been payed
- Payed by: type of paymet (by check or online transfer) and name of bank

### Banks

### Payments
The Payments page contains a table of payments. It might be recurent or scheduled (but not payed) one-time payments.
Each payment is represented by row. There are columns:
- Name of payment destination
- Amont to be payed
- Due date of the payment
- Period of payment, if it's recurrent payment
- Bank name from which payment already made or from which bank it will be done for automatic payments

### Incomes
