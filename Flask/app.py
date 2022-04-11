from locale import currency
import os
from flask import Flask, request, url_for, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    
    menu = f'''
        Go <a href="{url_for('exchange')}">here</a> to change money
        To exchange 50 CHF go <a href="{url_for('cantor', currency='CHF', amount=50, _external=True)}">here</a>
    
    <img src ="{url_for('static', filename='zdj.jpg')}"><br>
    {url_for('static', filename='zdj.jpg')}
    { os.path.join(app.static_folder, 'zdj.jpg')}
    
    '''
    return f'<h1> Hello world </h1><br>{menu}'


@app.route('/about')
def about():
    return '<h1>Python</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Welcone {}!</h1>'.format(name)

@app.route('/time')
def time():
    time_now = datetime.now().strftime('%H:%M:%S')
    return time_now

@app.route('/links')
def links():
    body = '''<a href='http://www.google.com' target="_blank">Google</a> <br />
    It's whe website of Google</a>
    <hr>
    <a href='https://www.bing.com/' target="_blank">Bing</a> <br />
    It's whe website of Bing</a>
    
    '''
    return body

@app.route('/cantor/<string:currency>/<int:amount>')
def cantor(currency, amount):
    message = f'<h1>You selected {currency} and amount {amount}</h1>'
    return message

@app.route('/exchange', methods=['GET', 'POST'])
def exchange():

    if request.method == 'GET':
        body='''
        <form id="exchange_form" action="/exchange" method='POST'>
        <label for="currency">Currency</label>
        <input type='text' id="currency" name="currency" values="EUR"><br>
        <label for="amount">Amount</label>
        <input type="text" id="amount" name="amount" values="100"><br>
        <input type="submit" values="Send">
        </form>
        '''
        
        return body
    else:
        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']

        amount = 100
        if 'amount' in request.form:
            amount = request.form['amount']
        body = f'You want to exchange {amount} {currency}'

        return redirect(url_for('cantor', currency=currency, amount=amount))

@app.route('/exchange_process', methods = ['GET', 'POST'])
def exchange_process():
    
    currency = 'EUR'
    if 'currency' in request.form:
        currency = request.form['currency']

    amount = 100
    if 'amount' in request.form:
        amount = request.form['amount']

    body = f'You want to exchange {amount} {currency}'

    return body

@app.route('/color')
def color():

    print(request.query_string)

    color = 'black'
    if 'color' in request.args:
        color = request.args['color']

    style = 'normal'
    if 'style' in request.args:
        style = request.args['style']

    return f'<h1 style = "color: {color}; font-style: {style};"> Hello World!!!!!!!!!!</h1>'
    #http://127.0.0.1:5000/color?color=green&style=bold&italic




if __name__ == '__main__':
    app.run(debug = True)