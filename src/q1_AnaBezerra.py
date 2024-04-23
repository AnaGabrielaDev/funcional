create_transaction = lambda transaction_type: receive_cash() and transaction_type == "Cash" or fund_transfer() and transaction_type == "Fund Transfer" or request_credit_account_details and transaction_type == "Credit"

fund_transfer = lambda: fund_transfer_details(getAccount(), "asd")

fund_transfer_details = lambda account, password: print({"user": account, "password": password})
getAccount = lambda: str(input("Account"))

receive_cash = lambda: receive_cash_printer(receive_cash_input())
receive_cash_printer = lambda value: print("Payment Receipt of ", value,'$')
receive_cash_input = lambda: int(input("How much Cash? "))
print_payment_receipt = lambda: print("Print Payment Receipt") or complete_transaction()
complete_transaction = lambda: print("Transaction completed!")

request_credit_account_details = lambda: print("Request Credit Account Details") or request_payment_from_bank()
request_payment_from_bank = lambda: print("Request Payment from Bank") or provide_bank_deposit_details()
provide_bank_deposit_details = lambda: print("Provide Bank Deposit Details") or check_payment_confirmation(True)

check_payment_confirmation = lambda bank_confirmation: [confirm_payment_approval_from_bank() if bank_confirmation else cancel_transaction()][0]

confirm_payment_approval_from_bank = lambda: print("Confirm Payment Approval from Bank") or close_transaction()
cancel_transaction = lambda: print("Cancel Transaction")
close_transaction = lambda: print("Close Transaction")

q1 = lambda: create_transaction(input("Type 'Cash' or 'Credit' or 'Fund Transfer'\n"))
