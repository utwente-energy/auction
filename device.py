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


# !!! IMPORTANT !!!
# You need to change the class name below! e.g. class EVController(Comm):
class Device():
	def __init__(self, name):
		# Some local variables
		self.price = 0     	# Last price
		self.target = 0		# Target consumption
		self.bid = DemandFunction()
		
		self.name = name
			
	def create_function(self, interval):
		# First reset the bidFunction:
		self.bid.clear()
		
		# To Jules
		# Here you can define your own bid to send to the controller
		# Usually, as in teh lecture, this depends on teh current state
		# So usually, it is good to read some data from the device here
		# And then construct a bid
		
		# Constructing a bid is done as in this example:
		self.bid.addLine(2000,0,-1000,1000)
		# Here, the following parameters are used:
			# - Starting power in Watts
			# - Ending power in Watts
			# - Starting price (ranging from -1000 to 1000)
			# - Ending price (ranging from -1000 to 1000)
		# Be careful:
			# - A higher price should alsways result in an equal or lower power consumption! 
			# So a bid is decreasing!
			# - Take care that you do not overwrite points
			# So usually, construct a function from "left to right
			# Start at the lowest price (-1000) with the highest demand
			# And then work towards a price of 1000
		
	def control_device(self, power):
		print("Setting device output to: "+str(power))
		
		# Here, you get the control result
		# This is a power in watts, stored in the "power" variable as printed above!
		# Then, based on the resulting power, coming from your bid and the selected price by the auctioneer
		# you have to change the operation of the device
		# e.g. change the charge current
		# or turn on/off the IoT device
		
		
		
	
	def request_bid(self, interval):
		self.create_function(interval)
		# Communicate the bid back
		return self.bid
	
	def receive_price(self, price):
		# Get the demand for the price
		target = self.bid.demandForPrice(price)
		
		# print("Cleared the market")
		# print("    price:  "+str(price))
		# print("    target: "+str(target))
		# print(" ")
		self.control_device(target)
