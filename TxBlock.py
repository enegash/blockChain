# TxBlock

from Blockchain import CBlock
from Signatures import generate_keys, sign, verify
from Transactions import Tx
import pickle
from cryptography.hazmat.primitives import serialization

class TxBlock (CBlock):
	
	def __init__(self, previousBlock):
		pass

	def addTx(self, Tx_in):
		pass

	def is_valid(self):
		return False


if __name__ == "__main__":
	pr1, pu1 = generate_keys()
	pr2, pu1 = generate_keys()
	pr3, pu1 = generate_keys()

	Tx`= Tx()
	Tx1.add_input(pu1, 1)
	Tx2.add_output(pu2, 1)
	Tx1.sign(pr1)

	print(Tx1.is_valid())
	
	# Store the BlockChain to the disk.
	message = b"Some text"
	sig = sign(message, pr1)

	# To pickle first need to create a file, and enable for binary writting. 
	# Then dump string data using dumps() or binary data using dump() to the file and close it.
	savefile = open("save.dat", "wb")
	pem = public_key.public_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PublicFormat.SubjectPublicKeyInfo
	)

	pickle.dump(Tx1.inputs[0][0], savefile)
	#pickle.dump(Tx1, savefile)
	savefile.close()

	# Pickle has trouble with handling the private and public keys. 
	# Will need to use Serialization and de-serialization.
	loadfile = open("save.dat", "rb")
	newTx = pickle.load(loadfile)

	print(newTx.is_valid())
	
