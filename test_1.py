import oqs
import time

# Algorithm used for KEM
algorithm = "Kyber1024"  # CRYSTALS-Kyber implementation

# Check if algorithm is supported
if algorithm not in oqs.get_enabled_kem_mechanisms():
    print(f"Algorithm {algorithm} is not supported by liboqs on this platform.")
    exit(1)

print(f"Using algorithm: {algorithm}")

# Initialize KEM
kem = oqs.KeyEncapsulation(algorithm)

# Generate key pair
start = time.time()
public_key = kem.generate_keypair()
end = time.time()
print(f"Keypair generation completed in {(end - start) * 1000:.2f} ms")

# Encapsulation
start = time.time()
ciphertext, shared_secret_enc = kem.encap_secret(public_key)
end = time.time()
print(f"Encapsulation completed in {(end - start) * 1000:.2f} ms")

# Decapsulation
start = time.time()
shared_secret_dec = kem.decap_secret(ciphertext)
end = time.time()
print(f"Decapsulation completed in {(end - start) * 1000:.2f} ms")

# Validate shared secrets
if shared_secret_enc == shared_secret_dec:
    print("Shared secret successfully validated.")
else:
    print("Shared secret mismatch!")

# Clean up
del kem
