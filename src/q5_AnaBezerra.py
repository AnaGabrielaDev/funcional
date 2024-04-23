from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

users_json = {}

#QUESTÃO ESCOLHIDA: 1
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

@app.route('/fund_transfer', methods=['POST'])
def fund_transfer():
    account = request.form.get('user')
    password = request.form.get('password')
    if check_password_hash(users_json[account], password):
        return "Fund transfer successful!"
    else:
        return "Invalid password!"

if __name__ == '__main__':
    app.run(debug=True)