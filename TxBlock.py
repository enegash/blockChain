# TxBlock

from BlockChain import CBlock
from Signatures import generate_keys, sign, verify
from Transaction import Tx
import pickle
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class TxBlock (CBlock):
	
	def __init__(self, previousBlock):
		# Reference to the parent class to use the constructor
		super(TxBlock, self).__init__([], previousBlock)

	def addTx(self, Tx_in):
		self.data.append(Tx_in)

	def is_valid(self):
		if not super(TxBlock, self).is_valid():
			return False
		for tx in self.data:
			if not tx.is_valid():
				return False
		return True


if __name__ == "__main__":
	pr1, pu1 = generate_keys()
	pr2, pu2 = generate_keys()
	pr3, pu3 = generate_keys()
	pr4, pu4 = generate_keys()

	Tx1 = Tx()
	Tx1.add_input(pu1, 1)
	Tx1.add_output(pu2, 1)
	Tx1.sign(pr1)

	if Tx1.is_valid():
		print("Success! Tx is valid.")
	
	savefile = open("tx.dat", "wb")
	pickle.dump(Tx1, savefile)
	savefile.close()	

	loadfile = open("tx.dat", "rb")
	newTx = pickle.load(loadfile)

	if newTx.is_valid():
		print("Success! Loaded Tx is valid.")
	loadfile.close()

	root = TxBlock(None)
	root.addTx(Tx1)
	
	Tx2 = Tx()
	Tx2.add_input(pu2, 1.1)
	Tx2.add_output(pu3, 1)
	Tx2.sign(pr2)
	root.addTx(Tx2)

	B1 = TxBlock(root)


	Tx3 = Tx()
	Tx3.add_input(pu3, 1.1)
	Tx3.add_output(pu1, 1)
	Tx3.sign(pr3)
	B1.addTx(Tx2)
	
	Tx4 = Tx()
	Tx4.add_input(pu1, 1.1)
	Tx4.add_output(pu2, 1)
	Tx4.add_reqd(pu3)
	Tx4.sign(pr1)
	Tx4.sign(pr3)
	B1.addTx(Tx4)

	savefile = open("block.dat", "wb")
	pickle.dump(B1, savefile)
	savefile.close()

	loadfile = open("block.dat", "rb")
	load_B1 = pickle.load(loadfile)

	load_B1.is_valid()

	print(bytes(str(load_B1.data), 'utf'))

	for b in [root, B1, load_B1, load_B1.previousBlock]:
		if b.is_valid():
			print("Success! Valid block.")
		else:
			print("ERROR! Bad block.")

	B2 = TxBlock(B1)
	Tx5 = Tx()
	Tx5.add_input(pu3, 1)
	Tx5.add_output(pu1, 100)
	Tx5.sign(pr3)
	B2.addTx(Tx5)	

	load_B1.previousBlock.addTx(Tx4)
	for b in [B2, load_B1]:
		if b.is_valid():
			print("ERROR! Bad block verified.")
		else:
			print("Success! Bad blocks detected.")
	
	# Test mining rewards and tx fees
	pr4, pu4 = generate_keys()
	B3 = TxBlock(B2)
	B3.addTx(Tx2)
	B3.addTx(Tx3)
	B3.addTx(Tx4)
	Tx6 = Tx()
	Tx6.add_output(pu4, 25)
	B3.addTx(Tx6)
	if B3.is_valid():
		print("Success! Block reward succeds.")
	else:
		print("ERROR! Block reward fail.")


	B4 = TxBlock(B3)
	B4.addTx(Tx2)
	B4.addTx(Tx3)
	B4.addTx(Tx4)
	Tx7 = Tx()
	Tx7.add_output(pu4, 25.2)
	B4.addTx(Tx7)
	if B4.is_valid():
		print("Success! Tx fees succeeds.")
	else:
		print("ERROR! Tx fees fail.")

	# Greedy Miner
	B5 = TxBlock(B4)
	B5.addTx(Tx2)
	B5.addTx(Tx3)
	B5.addTx(Tx4)
	Tx8 = Tx()
	Tx8.add_output(pu4, 26.2)
	B5.addTx(Tx8)
	if not B5.is_valid():
		print("Success! Greedy Miner was detected..")
	else:
		print("ERROR! Greedy Miner was not detected.")




	loadfile.close()
