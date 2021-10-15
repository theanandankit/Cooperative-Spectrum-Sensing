import datetime
import hashlib
import json
import rsa
from flask import Flask, jsonify, request
import json
import requests

keys_list = {}
threshold_value = 60

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0', value=0)
 
    def create_block(self, proof, previous_hash, value):
        result = get_chain_add(str(value))
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'key' : str(result["public_key"]),
                 'encrypted_data' : str(result["value"])}
        self.chain.append(block)
        return block
       
    def print_previous_block(self):
        return self.chain[-1]
       
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
         
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
                 
        return new_proof
 
    def hash(self, block):
        encoded_block = json.dumps(block).encode("utf-8")
        return hashlib.sha256(encoded_block).hexdigest()
 
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
         
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
               
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
             
            if hash_operation[:2] != '00':
                return False
            previous_block = block
            block_index += 1
         
        return True
 
def get_chain_add(value):
    publicKey, privateKey = rsa.newkeys(512)
    keys_list[str(publicKey)] = privateKey
    enc = rsa.encrypt(value.encode(), publicKey)
    return {'value': str(enc, encoding='latin-1'),
            'public_key' : str(publicKey)}

if __name__=="__main__":
    app = Flask(__name__)
    blockchain = Blockchain()
 
# Mining a new block
@app.route('/mine_block', methods=['POST'])
def mine_block():
    list_value = request.get_json()
    send_data = []
    for x in list_value:
        previous_block = blockchain.print_previous_block()
        previous_proof = previous_block['proof']
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(proof, previous_hash, x["value"])
     
        body = {"message": "A block is MINED",
                    "index": block['index'],
                    "timestamp": block['timestamp'],
                    "proof": block['proof'],
                    "previous_hash": block['previous_hash'],
                    "key" : block['key'],
                    "encrypted_data" : block['encrypted_data']}
        
        send_data.append(body)
    return jsonify(send_data), 200
 
# Display blockchain in json format
@app.route('/get_chain', methods=['GET'])
def display_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200
 
# Check validity of blockchain
@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
     
    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200

@app.route('/getkey', methods=['GET'])
def getkey():
    return jsonify(keys_list), 200

#calculation part
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
        energy = rsa.decrypt(bytes(x["encrypted_data"], encoding='latin-1'), keys_list[x["key"]]).decode()
        value += get_gain(int(energy)) * int(energy)
        sum += get_gain(int(energy))
    return (value)/ (sum)

@app.route('/calculate', methods=['POST'])
def add_gusess():
    list_block = request.get_json()
    value = calculate_avg(list_block)
    return {"avg": value,
            "threshold" : threshold_value}
 
# Run the flask server locally
if __name__=="__main__":
    app.run(host='127.0.0.1', port=5000)
