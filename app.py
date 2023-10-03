from flask import Flask, request, jsonify
from helper import fetch_currency

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    print(source_currency)
    print(amount)
    print(target_currency)

    final_amount = fetch_currency(amount, source_currency, target_currency) 

    respose = {
        'fulfillmentText':"{} {} is {} {}".format(amount, source_currency, final_amount, target_currency) 
    }
    print(str(final_amount))
    return jsonify(respose)
if __name__ == "__main__":
    app.run(debug=True)

