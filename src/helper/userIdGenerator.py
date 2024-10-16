import hashlib


def generate_user_id(name: str) -> str:
  encoded_username = name.encode("utf-8")

  # Create a SHA-256 hash object
  sha256_hash = hashlib.sha256()

  # Update the hash object with the encoded username
  sha256_hash.update(encoded_username)

  # Get the hexadecimal representation of the hash
  hashed_username = sha256_hash.hexdigest()

  return hashed_username
