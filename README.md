# Secure Channel Establishment with MetaMask and Diffie-Hellman

This project demonstrates how to establish a secure communication channel between a web client and a server using MetaMask for Ethereum-based authentication and Diffie-Hellman (DH) key exchange for cryptographic security.

## Features

- MetaMask integration for Ethereum wallet connectivity and message signing.
- Diffie-Hellman key exchange for secure, encrypted communication.
- Flask server for signature verification and DH key exchange handling.
- JavaScript client-side for wallet connection, message signing, and DH key derivation.

## Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x
- Flask
- Web3.py

### Installation

1. Clone the repository:
```
git clone https://your-repository-url.git
```

2. Install Python dependencies:
```
pip install -r requirements.txt
```

### Running the Application

1. Start the Flask server:
```
python server.py
```

2. Open the client-side HTML file in a web browser using https (wamp, mamp, lamp etc) and connect to MetaMask.

## Usage

- Click the "Connect to MetaMask" button to authenticate and authorize the application.
- Fill in the sender and recipient Ethereum addresses and a message.
- Click "Connect & Sign" to sign the message, establish a secure channel, and derive a shared secret key.

## Security Considerations

Ensure that you understand the security implications of using cryptographic operations, including the management of nonces, key material, and the secure transmission of public keys.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your proposed changes.

## License

Distributed under the MIT License. See `LICENSE` for more information.
