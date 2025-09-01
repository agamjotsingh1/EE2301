Ic = 3.65e-3
Vt = 25.875e-3
eta = 1
gm = Ic/(eta*Vt)
ro = 1000

Vb = 3.21
Ve = 2.516
Ie = 4.49e-3
Ib = 21.74e-6

beta = Ic/Ib
RL = 470
RE = 470
R1 = 18e+3
R2 = 51e+3

Re = RE*RL/(RE + RL)
Rin = 1/(1/R1 + 1/R2 + 1/(beta*Re))

print(gm*ro)
print(Rin)
