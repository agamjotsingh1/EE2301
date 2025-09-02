Ie = 1.06e-3
Rc = 2200
Re = 1000
Vt = 25.875e-3
Rdashe = Vt/Ie
Reff = Rdashe*Re/(Re + Rdashe)

Vt = 25.875e-3
Rin_base = beta*Vt/Ie

print(Rc/Reff)
