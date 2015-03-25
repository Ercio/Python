class Gate(object):
	def __init__(self, paid):
                self.paid = paid

	def open_gate(self):
		print "== OPEN =="

	def close_gate(self):
		print "== CLOSED =="

	def gate_welcomes(self):
                self.close_gate()
		print "Welcome."
		self.gate_informs(self)

	def gate_informs(self):
		print "Insert " + self.paid
		self.put_coin()
	
        def gate_returns_rest(self,coin):
                if isinstance(self.coin, double):
                        return self.coin-self.paid

	def gate_gets_paid(self,coin):
                if isinstance(self.coin, double):
                        if (self.coin == self.paid) or (self.coin > self.paid):
                            print "Enter. "
                            self.gate_returns_rest(self,self.coin)	#zwroc reszte
                            self.open_gate(self)

		elif (self.coin < self.paid):
			print "Insert " + (self.coin-self.paid)
			self.gate_gets_paid(self,self.coin-self.paid)
			
        def put_coin(self):
		self.coin = input("--> ")
		self.gate_gets_paid(self,self.coin)

bramka = Gate(2.0)
bramka.gate_welcomes(bramka)
