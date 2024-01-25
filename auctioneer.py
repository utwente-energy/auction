   # Copyright 2024 University of Twente

   # Licensed under the Apache License, Version 2.0 (the "License");
   # you may not use this file except in compliance with the License.
   # You may obtain a copy of the License at

       # http://www.apache.org/licenses/LICENSE-2.0

   # Unless required by applicable law or agreed to in writing, software
   # distributed under the License is distributed on an "AS IS" BASIS,
   # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   # See the License for the specific language governing permissions and
   # limitations under the License.

from demandFunction import DemandFunction
import math
import time
import random

class Auctioneer():
	def __init__(self):
		print("Starting the acutioneer")
				
		self.children = []  # List with all the children
		
		self.target = 0    # The desired consumption
		self.bids = DemandFunction()
		
		self.intervals = 10 # number of intervals to simulate
		
	def simulate(self):
		for interval in range(0, self.intervals):
			# Simualte intervals
			# Select the target power consumption in Watts
			self.target = 5000 * random.random() # TO Jules; This is where you have to configure the desiret target power for the fleet EVs in this interval
			print(interval, self.target)
			
			# Do the control
			self.request_bids(interval)
			self.clear_market(self.target)
		
	
	def request_bids(self, interval):
		print("Requesting bids")
			
		# First reset the bidFunction:
		self.bids.clear()
		
		for child in self.children:
			response = child.request_bid(interval)
			self.bids.addFunction(response)
	
	def clear_market(self, target):
		# Get the price:
		price = self.bids.priceForDemand(self.target)

		# Make it an integer:
		price = int(round(price))
	
		# Send the price to all children
		for child in self.children:
			child.receive_price(price)
		
		print("Cleared the market")
		print("    price:  "+str(price))
		print("    target: "+str(self.target))
		print(" ")
		
	def add_device(self, device):
		self.children.append(device)
		

