import unittest
from Gate import Gate

gate = Gate(2.0)

class GateTests(unittest.TestCase):
	#def testGate(self):
	#	self.assertTrue(gate.gate_welcomes())

	def testFailItself(self):
		self.fail()

	def assertPaid(self):
		pay = gate.paid
		self.assertEqual(pay, 2.0)

if __name__ == '__main__':
	unittest.main()
