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

from device import Device
from auctioneer import Auctioneer
import math
import time
import random

dev1 = Device("Device1")
dev2 = Device("Device2")
dev3 = Device("Device3")

auctioneer = Auctioneer()

auctioneer.add_device(dev1)
auctioneer.add_device(dev2)
auctioneer.add_device(dev3)

auctioneer.simulate()