#Signatures.py
#https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/ 

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

def generate_keys():
	private = rsa.generate_private_key(
		public_exponent=65537,
		key_size=2048
	)

	public = private.public_key()

	return private, public


def sign(message, private):
	message = bytes(str(message), 'utf-8')
	sig = private.sign(
		message,
		padding.PSS(
			mgf = padding.MGF1(hashes.SHA256()),
			salt_length = padding.PSS.MAX_LENGTH
		),
		hashes.SHA256()
	)

	return sig


def verify(message, sig, public):
	message = bytes(str(message), 'utf-8')
	try:
		public.verify(
			sig,
			message,
			padding.PSS(
				mgf = padding.MGF1(hashes.SHA256()),
				salt_length = padding.PSS.MAX_LENGTH
			),
			hashes.SHA256()
		)
		
		return True
	except InvalidSignature:
		return False
	except:
		print("ERROR! Executing public.verify.")


if __name__ == '__main__':
	pr, pu = generate_keys()

	print(pr, "\n", pu)

	message = b"This is a secret message"
	sig = sign(message, pr)
	correct = verify(message, sig, pu)

	if correct:
		print("Success! Good signature.")
	else:
		print("ERROR! Signature is bad")

	# Attempt to hack RSA encryption. Sending your private key with a different signature.
	pr2, pu2 = generate_keys()
	sig2 = sign(message, pr2)
	correct = verify(message, sig2, pu)
	if correct:
		print("ERROR! Bad signature checks out.")
	else:
		print("Success! Bad signature caught.")


