from flask import Flask, jsonify, request
from blockchain import keys_list
import rsa

app = Flask(__name__)

threshold_value = 60

def get_gain(current):

    if (current >= 90):
        return 9
    elif (current >= 80):
        return 8
    elif (current >= 70):
        return 7
    elif (current >= 60):
        return 6
    elif (current >= 50):
        return 5
    elif (current >= 40):
        return 4
    elif (current >= 30):
        return 3
    elif (current >= 20):
        return 2
    else:
        return 1

def calculate_avg(list):
    value = 0
    sum = 0
    for x in list:
        energy = rsa.decrypt(x["encrypted_data"], keys_list[x["key"]]).decode()
        value += get_gain(energy) * energy
        sum += get_gain(energy)
    return (value)/ (sum)

@app.route('/calculate', methods=['POST'])
def add_gusess():
    print(keys_list)
    list_block = request.get_json()
    print(list_block)
    value = calculate_avg(list_block)
    print(value)
    return {"avg": value,
            "threshold" : threshold_value}

app.run(host='127.0.0.1', port = 5001)