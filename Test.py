import unittest
import Gate

class GateTests(unittest.TestCase):
	def testGate(self):
		self.assertTrue(Gate(2.0).gate_welcomes())

	def assertPaid(self):
