from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

class someClass:
	string = None
	num = 37612894

	def __init__(self, mystring):
		self.string = mystring

	# Representation is a method that returns a string containing a printable representation of an object.
	def __repr__(self):
		return self.string + "^^^" + str(self.num)

class CBlock:
	data = None
	previousHash = None
	previousBlock = None

	# Constructor
	def __init__(self, data, previousBlock):
		self.data = data
		self.previousBlock = previousBlock
		if previousBlock != None:
			self.previousHash = previousBlock.computeHash()

	def computeHash(self):
		digest = hashes.Hash(hashes.SHA256(), backend = default_backend)
		digest.update(bytes(str(self.data), 'utf8'))
		digest.update(bytes(str(self.previousHash), 'utf8'))		
		
		return digest.finalize()

	def is_valid(self):
		if self.previousBlock == None:
			return True
		return self.previousBlock.computeHash() == self.previousHash

#To ensure we don't run this if we import BlockChain.py
if __name__ == '__main__':
	root = CBlock('I am root', None)
	B1 = CBlock('I am a child.', root)
	B2 = CBlock('I am B1s brother', root)
	B3 = CBlock(12354, B1)
	B4 = CBlock(someClass('Hi there!'), B3)
	B5 = CBlock("Top block", B4)

	for b in [B1, B2, B3, B4, B5]:
		if B1.previousBlock.computeHash() == B1.previousHash:
			print("Success! Hash is good.")
		else:
			print("ERROR! Hash is no good.")

	# Attempt to impersonate a hacker. 
	B3.data = 12345
	if B4.previousBlock.computeHash() == B4.previousHash:
		print("ERROR! Unable to detect tampering.")
	else:
		print("Success! Tampering detected.")

	print(B4.data)
	B4.data.num = 1234567
	print(B4.data)
	if B5.previousBlock.computeHash() == B5.previousHash:
		print("ERROR! Unable to detect tampering.")
	else:
		print("Success! Tampering detected.")
