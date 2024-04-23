from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash
from q1_AnaBezerra import q1
app = Flask(__name__)

users_json = {}

#QUESTÃO ESCOLHIDA: 1, o fluxo de transações foi implementado em um servidor web, onde é possível criar contas e realizar transferências de fundos
#Somente para esclarecer que esses usuarios estao sendo criados in memory, nao persistem apos o server ser desligado

@app.route('/create_account', methods=['POST'])
def create_account():
    account = request.form.get('user')
    password = request.form.get('password')
    users_json[account] = generate_password_hash(password)

    return("User created:" + account + " Password (hashed): " + users_json[account])

@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"

get_account = lambda: request.form.get('user')
get_password = lambda: request.form.get('password')
get_amount = lambda: str(request.form.get('amount'))
get_transaction_type = lambda: str(request.form.get('transaction_type'))

transfer_message = lambda account, amount: "Transaction of " + amount + " by " + account + " successfully transferred!"
invalid_password_message = lambda: "Invalid password!"
check_password = lambda account, password: check_password_hash(users_json[account], password)

@app.route('/payment', methods=['POST'])
def payment():
    transaction_type = get_transaction_type()
    user = get_account()
    password = get_password()
    amount = get_amount()
    allowed = check_password(user, password)
    q1(transaction_type, amount, allowed, user, password) 
    
    return transfer_message(user, amount) if check_password(user, password) else invalid_password_message()

if __name__ == '__main__':
    app.run(debug=True)