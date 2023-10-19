from cryptography.fernet import Fernet

key = 'iHCcn_NjpufxYR9xgekkG5pUQePnResLeyyNYagot1E='

def encrypt_password(password):
    return Fernet(key=key).encrypt(password.encode()).decode()

def decrypt_password(encrypted_pw):
    return Fernet(key=key).decrypt(encrypted_pw).decode()
