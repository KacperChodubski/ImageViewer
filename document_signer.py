import hashlib
import random
from tkinter import messagebox

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode
import os
import getpass
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime


def save_xml_signature(xml_signature, filename):
    with open(filename, 'w') as f:
        f.write(xml_signature)

    messagebox.showinfo("Success", f"File successfully signed. A signature has been saved to {filename}")

def generate_xades_signature(file_info, user_info, encrypted_hash, signature_time):
    # Create the root element
    root = ET.Element("XAdESSignatures")

    # Create the Signature element and add it to the root
    signature = ET.SubElement(root, "Signature")

    # Add document information
    doc_info = ET.SubElement(signature, "DocumentInformation")
    ET.SubElement(doc_info, "Size").text = str(file_info['size'])
    ET.SubElement(doc_info, "Extension").text = file_info['extension']
    ET.SubElement(doc_info, "ModificationDate").text = file_info['modification_date']

    # Add user information
    user_info_elem = ET.SubElement(signature, "UserInfo")
    ET.SubElement(user_info_elem, "Name").text = user_info['name']
    ET.SubElement(user_info_elem, "ID").text = user_info['id']

    # Add encrypted document hash
    ET.SubElement(signature, "EncryptedDocumentHash").text = encrypted_hash.decode()

    # Add timestamp
    ET.SubElement(signature, "Timestamp").text = signature_time.strftime("%Y-%m-%d %H:%M:%S")

    # Generate a pretty-printed XML string
    rough_string = ET.tostring(root, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")

    return pretty_xml


def gather_file_info(file_path):
    # Ensure the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No file found at {file_path}")

    # Gather file information
    file_info = {
        'size': os.path.getsize(file_path),  # Size in bytes
        'extension': os.path.splitext(file_path)[1],  # File extension
        'modification_date': datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S'),
        # Last modification date
    }

    return file_info


def gather_user_info():
    user_info = {
        'name': getpass.getuser(),  # Get the login name of the user
        'id': str(random.randint(0, 10000))
    }
    return user_info


def hash_document(file_path):
    with open(file_path, 'rb') as f:
        document = f.read()
    return SHA256.new(document)


def decrypt_rsa_private_key(encrypted_key_path, pin, iv_path):
    """Decrypt an RSA private key using an AES key derived from a hashed PIN and IV for CBC mode."""
    # Hash the PIN
    pin_hash = SHA256.new(pin.encode('utf-8')).digest()

    # Load the IV
    with open(iv_path, 'rb') as iv_file:
        iv = iv_file.read()

    # Decrypt the RSA private key
    with open(encrypted_key_path, 'rb') as key_file:
        encrypted_key = key_file.read()
        cipher_aes = AES.new(pin_hash, AES.MODE_CBC, iv)
        decrypted_key = cipher_aes.decrypt(encrypted_key).rstrip(b" ")
    return decrypted_key


def sign(document_path, encrypted_key_path, pin, iv_path):
    """Sign a document by hashing it and encrypting the hash with an RSA private key."""
    document_hash = hash_document(document_path)
    rsa_private_key = decrypt_rsa_private_key(encrypted_key_path, pin, iv_path)
    key = RSA.import_key(rsa_private_key)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(document_hash)

    encrypted_hash = b64encode(signature)
    file_info = gather_file_info(document_path)
    user_info = gather_user_info()
    signature_time = datetime.now()

    xml_signature = generate_xades_signature(file_info, user_info, encrypted_hash, signature_time)
    save_xml_signature(xml_signature, 'signature.xml')