class Gate(object):
	def __init__(self, paid):
                self.paid = paid

	def open_gate(self):
		print "== OPEN =="

	def close_gate(self):
		print "== CLOSED =="

        def put_coin(self):
		coin = float(input("--> "))
		self.gate_gets_paid(self.paid,coin)

	def gate_informs(self):
		print "Insert " + str(self.paid)
		self.put_coin()
	
        def gate_returns_rest(self,coin):
                if isinstance(coin, float):
                        return coin-self.paid

	def gate_gets_paid(self,price,coin):
		self.paid = price
                if isinstance(coin, float):
                        if (coin > self.paid):
                            print "Please, take the rest: " + str(self.gate_returns_rest(coin))
			    print "Enter. "
                            self.open_gate()

			elif (coin == self.paid):
			    print "Enter. "
			    self.open_gate()

			elif (coin > 0 and coin < self.paid):
				while (self.paid-coin > 0):
				   print "Insert " + str((self.paid)-coin)
				   new_coin = float(input("--> "))
				   self.gate_gets_paid(self.paid-coin,new_coin)
        
        def gate_welcomes(self):
                self.close_gate()
		print "Welcome."
		self.gate_informs()
                

bramka = Gate(2.0)
bramka.gate_welcomes()
