import qrcode
import json
import requests

# Function to transfer an NFT token using Stacks blockchain API (simulated)
def transfer_nft(sender_wallet, recipient_wallet, token_id, nft_data):
    # Simulating an API call to transfer NFT
    response = {
        "status": "success",
        "transaction_id": "0xabc123def456",
        "sender": sender_wallet,
        "recipient": recipient_wallet,
        "token_id": token_id,
        "nft_data": nft_data
    }
    
    # Simulate transferring the NFT
    return response

# Function to generate QR code for recipient address
def generate_qr_code(wallet_address):
    # Generate a QR code for the wallet address
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(wallet_address)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(f"{wallet_address}_qrcode.png")
    print(f"QR code generated for {wallet_address}.")

# Sender and recipient Bitcoin wallets
sender_wallet = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
recipient_wallet = "1BoatSLRHtKNngkdXEeobR76b53LETtpyT"
token_id = "NFT12345"

# Example NFT metadata (which can be any data associated with the token)
nft_data = {
    "name": "Digital Artwork #123",
    "description": "A unique piece of digital art.",
    "image": "https://example.com/nft12345.png"
}

# Transfer the NFT
transfer_result = transfer_nft(sender_wallet, recipient_wallet, token_id, nft_data)

# Convert transfer result to JSON format
transfer_json = json.dumps(transfer_result, indent=4)
print("Transfer result in JSON format:")
print(transfer_json)

# Generate QR code for recipient wallet address
generate_qr_code(recipient_wallet)
