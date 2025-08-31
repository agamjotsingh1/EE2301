import numpy as np

kp = 76.2
Id =  6.107e-3
ro = 1000
rl  = 1000
reff =  ro * rl / (ro + rl)
vgs = 8.8926 - 6.107
vto = 1.38
gm = 2 * Id / (vgs - vto)

print(gm * reff)
