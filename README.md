# File-Encryption-Decryption
A small file encryption and decryption application demonstrating AES encryption.
### Install the required libary

```
pip3 install cryptography
```
### Import the following modules 

```
from cryptography.fernet import Fernet
import os
```
## Encryption Process
### Create and save the key
```
key = Fernet.generate_key()

with open(filepath + '.key', 'wb') as filekey:
    filekey.write(key)

with open(filepath + '.key', 'rb') as filekey:
    key = filekey.read()
```
### Use the key to encrypt a file
```
fernet = Fernet(key)

with open(filepath, 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open(filepath, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
```
## Decryption Process
### Find and save the key
```
with open(filepath + '.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)
```
### Read the encrypted file
```
with open(filepath, 'rb') as enc_file:
    encrypted = enc_file.read()
```
### Decrypt the file
```
decrypted = fernet.decrypt(encrypted)
with open(filepath, 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
```
### Delete the key
```
if os.path.isfile(filepath + '.key'):
    os.remove(filepath + '.key')
```



