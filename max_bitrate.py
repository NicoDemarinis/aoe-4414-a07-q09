# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz 
#  
# Parameters:
#  
#  tx_w = power transmitter in watts
#  tx_gain_db = transmitter gain in db
#  freq_hz = frequency
#  dist_km = distance
#  rx_gain_db = reciever gain in db
#  n0_j = noise spectral density
#  bw_hz = bandwidth
#
# Output:
#  A description of the script output
#
# Written by Nicola DeMarinis
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys  # argv

# initialize script arguments
tx_w = float('nan') #
tx_gain_db = float('nan') #
freq_hz = float('nan') # 
dist_km = float('nan') # 
rx_gain_db = float('nan') # 
n0_j = float('nan') # 
bw_hz = float('nan') # 

# parse script arguments
if len(sys.argv)==8:
  
    tx_w = float(sys.argv[1]) #
    tx_gain_db = float(sys.argv[2]) #
    freq_hz = float(sys.argv[3]) # 
    dist_km = float(sys.argv[4]) # 
    rx_gain_db = float(sys.argv[5]) # 
    n0_j = float(sys.argv[6]) # 
    bw_hz = float(sys.argv[7]) # 
    
else:
  print(\
   'Usage: '\
   'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
  )
  exit()

# "constants"
c = 2.99792458*(10**8)

# write script below this line
#Find N
n_final = n0_j*bw_hz

#Find C
gt = 10**(tx_gain_db/10)
gr = 10**(rx_gain_db/10)
line_loss= 10**(-1/10)
lamb = c/freq_hz
la = 1
c_final = tx_w*line_loss*gt*la*gr*((lamb/(4*math.pi*dist_km))**2)

r_max = bw_hz*math.log2(1+(c_final/n_final))

#Print
print(math.floor(r_max))

