import base64

def decode_base64(encoded_string):
 # Decode the base64 string
 decoded_bytes = base64.b64decode(encoded_string)
 # Convert bytes to string
 decoded_string = decoded_bytes.decode('utf-8')
 return decoded_string

# Example usage
encoded_string = 'your_base64_encoded_string_here'
decoded_string = decode_base64(encoded_string)
print("Decoded String:", decoded_string)
