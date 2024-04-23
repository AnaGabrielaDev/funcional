create_transaction = lambda transaction_type, amount, accountConfirmation, user, password: \
    receive_cash(amount) if transaction_type == "Cash" else \
    fund_transfer(user, password, accountConfirmation) if transaction_type == "Fund Transfer" else \
    request_credit_account_details(user, password, accountConfirmation) if transaction_type == "Credit" and accountConfirmation else \
    None

fund_transfer = lambda user, password, AccountAllowed: fund_transfer_details(user, password) or accountConfirmation(AccountAllowed)
accountConfirmation = lambda AccountAllowed: [close_transaction() if AccountAllowed else cancel_transaction()] #abstrai a confirmacao de conta para que ja venha confirmado de outra camada do sistema (O que seria o controle chamaria uma funcao de confirmacao de conta e passaria o resultado)
fund_transfer_details = lambda user, password: print({"user": user, "password": "*****"}) #somente para mostrar os dados de usuario

receive_cash = lambda ammount: receive_cash_printer(ammount) or print_payment_receipt()
receive_cash_printer = lambda value: print("Payment Receipt of ", value,'$')
print_payment_receipt = lambda: print("Print Payment Receipt") or complete_transaction()
complete_transaction = lambda: print("Transaction completed!")

request_credit_account_details = lambda user, password, accountConfirmation: print("Requesting Credit Account Details...") or request_payment_from_bank()
request_payment_from_bank = lambda: print("Requesting Payment from Bank") or provide_bank_deposit_details()
provide_bank_deposit_details = lambda: print("Provide Bank Deposit Details") or check_payment_confirmation(True)

check_payment_confirmation = lambda bank_confirmation: [confirm_payment_approval_from_bank() if bank_confirmation else cancel_transaction()][0]

confirm_payment_approval_from_bank = lambda: print("Confirm Payment Approval from Bank") or close_transaction()
cancel_transaction = lambda: print("Cancel Transaction")
close_transaction = lambda: print("Close Transaction")

print_create_transaction = lambda : print("Type 'Cash' or 'Credit' or 'Fund Transfer'\n")

transaction = lambda type, amount, AccountAllowed, user, password: (print_create_transaction(), create_transaction(type, amount, AccountAllowed, user, password)) or print(type + " Selected")

#se chamar pelo index, la os dados estao sendo enviados para q1
q1 = lambda type, amount, AccountAllowed, user, password: transaction(type, amount, AccountAllowed, user, password) 

#Nao implementei dados mocados para uma lista de usuario mas seria possivel utilizar o banco de dados para guardar as transacoes que o usuario fez, o score de credito e afins. 
#Tentei utilizar os dados como parametros pois poderiam ser reaproveitados no exercicio 5.