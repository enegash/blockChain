# TxBlock

from BlockChain import CBlock
from Signatures import generate_keys, sign, verify
from Transaction import Tx
import pickle
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class TxBlock (CBlock):
	
	def __init__(self, previousBlock):
		pass

	def addTx(self, Tx_in):
		pass

	def is_valid(self):
		return False


if __name__ == "__main__":
	pr1, pu1 = generate_keys()
	pr2, pu2 = generate_keys()
	pr3, pu3 = generate_keys()

	Tx1 = Tx()
	Tx1.add_input(pu1, 1)
	Tx1.add_output(pu2, 1)
	Tx1.sign(pr1)

	print(Tx1.is_valid())
	
	# Store the BlockChain to the disk.
	message = b"Some text"
	sig = sign(message, pr1)
	print(verify(message,sig,pu1))

	# To pickle first need to create a file, and enable for binary writting. 
	# Then dump string data using dumps() or binary data using dump() to the file and close it.
	# Private Key that you've loaded you use private_bytes() to serialize the key.
	savefile = open("save.dat", "wb")
	# Moved loading and serialization to the Signatures Model
#	pu_ser = pu1.public_bytes(
#		encoding=serialization.Encoding.PEM,
#		format=serialization.PublicFormat.SubjectPublicKeyInfo
#	)
	pickle.dump(pu1, savefile)
	#pickle.dump(Tx1.inputs[0][0], savefile)
	#pickle.dump(Tx1, savefile)
	savefile.close()

	# Pickle has trouble with handling the private and public keys. 
	# Will need to use Serialization and de-serialization.
	loadfile = open("save.dat", "rb")
	new_pu = pickle.load(loadfile)
#	loaded_pu = serialization.load_pem_public_key(
#		new_pu,
#		backend = default_backend()
#	)
	print(verify(message, sig, new_pu))
	
	#newTx = pickle.load(loadfile)
	#print(newTx.is_valid())
	
