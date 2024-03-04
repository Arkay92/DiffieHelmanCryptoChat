from flask import Flask, request, jsonify
from web3 import Web3, HTTPProvider
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import os

app = Flask(__name__)

# Initialize web3 with your Ethereum provider
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

@app.route('/establish_secure_channel', methods=['POST'])
def establish_secure_channel():
    data = request.json
    
    # Ensure all required fields are present in the request
    if not all(key in data for key in ['message', 'signature', 'sender_address', 'recipient_address']):
        return jsonify({'error': 'Missing required fields in request'}), 400

    message = data['message']
    signature = data['signature']
    sender_address = data['sender_address']
    recipient_address = data['recipient_address']

    # Verify the client's signature
    try:
        recovered_address = w3.eth.account.recover_message(w3.eth.account.messages.encode_defunct(text=message), signature=signature)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    if recovered_address.lower() != sender_address.lower():
        return jsonify({'error': 'Signature verification failed'}), 400

    # Proceed with Diffie-Hellman key exchange
    try:
        parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
        server_private_dh_key = parameters.generate_private_key()
        server_public_dh_key = server_private_dh_key.public_key()

        # Here, we simulate the client's part of the key exchange for demonstration purposes
        client_private_dh_key = parameters.generate_private_key()
        client_public_dh_key = client_private_dh_key.public_key()

        # Server computes the shared secret
        server_shared_secret = server_private_dh_key.exchange(client_public_dh_key)

        # Generate a secure nonce for HKDF
        nonce = os.urandom(16)  # 16 bytes = 128 bits

        # Derive a symmetric key using HKDF
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,  # Suitable for AES-256
            salt=nonce,
            info=b'handshake data',
            backend=default_backend()
        )
        derived_key = hkdf.derive(server_shared_secret)

        return jsonify({
            'serverPublicDHKey': server_public_dh_key.public_numbers().encode_point().hex(),
            'derivedKey': derived_key.hex()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
