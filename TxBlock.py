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
	
	savefile = open("tx.dat", "wb")
	pickle.dump(Tx1, savefile)
	savefile.close()	

	loadfile = open("tx.dat", "rb")
	newTx = pickle.load(loadfile)

	print(newTx.is_valid())
	loadfile.close()	
