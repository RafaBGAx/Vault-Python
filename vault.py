import hashlib
import os

def hash_password(plain_password):

    salt = os.urandom(16).hex()
    
    salted_input = plain_password + salt
    
    final_hash = hashlib.sha256(salted_input.encode()).hexdigest()
    
    return salt, final_hash


password_input = "secure_password123"

salt1, hash1 = hash_password(password_input)
salt2, hash2 = hash_password(password_input)

print(f"User 1 | Salt: {salt1} | Hash: {hash1[:32]}...")
print(f"User 2 | Salt: {salt2} | Hash: {hash2[:32]}...")

if hash1 != hash2:
    print("\nSUCCESS")
else:
    print("\nFalse")