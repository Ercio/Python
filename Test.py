import unittest
import Gate

gate = Gate(2.0)

class GateTests(unittest.TestCase):
	def testGate(self):
		self.assertTrue(gate.gate_welcomes())

	def assertPaid(self):
		self.assertEqual(gate.paid, 2.0)
