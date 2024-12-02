import oqs

# Initialize a Key Encapsulation Mechanism
kem = oqs.KeyEncapsulation("Kyber512")

# Display the KEM's name (manually specified in this case)
print("Using KEM: Kyber512")

# Generate Key Pair
public_key = kem.generate_keypair()
print("Public Key Generated")

# Encapsulation
ciphertext, shared_secret_enc = kem.encap_secret(public_key)
print("Ciphertext and Shared Secret (Encapsulation) Generated")

# Decapsulation
shared_secret_dec = kem.decap_secret(ciphertext)
print("Shared Secret (Decapsulation) Generated")

# Validate Shared Secrets
if shared_secret_enc == shared_secret_dec:
    print("Key exchange successful and quantum-safe!")
else:
    print("Key exchange failed!")
