class Gate(object):
	def __init__(self, paid):
                self.paid = paid

	def open_gate(self):
		print "== OPEN =="

	def close_gate(self):
		print "== CLOSED =="

	def gate_welcomes(self):
                close_gate()
		print "Welcome."
		gate_informs(self)

	def gate_informs(self):
		print "Insert " + paid
		put_coin()
	
        def gate_returns_rest(self,coin):
                if isinstance(coin, double):
                        return coin-paid

	def gate_gets_paid(self,coin):
                if isinstance(coin, double):
                        if (coin == paid) or (coin > paid):
                            print "Enter. "
                            gate_returns_rest(self,coin)	#zwroc reszte
                            open_gate(self)

		elif (coin < paid):
			print "Insert " + (coin-paid)
			gate_gets_paid(self,coin-paid)
			
        def put_coin(self):
		coin = input("--> ")
		gate_gets_paid(self,coin)

bramka = Gate(2.0)
bramka.gate_welcomes()
