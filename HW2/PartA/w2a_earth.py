# AUTHOR BrianAppleton appleton@bu.edu

#--Composition information
	#via wikipedia: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC350422/
	#Earth's mass = 5.98x10^24 kG
	#composition by mass:
	#32.1% iron (Z = 26, 55.845 g/mol)
	#30.1% oxygen (Z = 8, 15.999 g/mol)
	#15.1% silicon (Z = 14, 28.086 g/mol)
	#13.9% magnesium (Z = 12, 24.305 g/mol)
	#2.9% sulfur (Z = 16, 32.065 g/mol)
	#1.8% nickel (Z = 28, 58.693 g/mol)
	#1.5% calcium (Z = 20, 40.078 g/mol)
	#1.4% aluminum (Z = 13, 26.982 g/mol)

#--Calculate average composition
mass_comp = [0.321, 0.301, 0.151, 0.139, 0.029, 0.018, 0.015, 0.014]
Z = [26, 8, 14, 12, 16, 28, 20, 13]
molar_mass = [55.845, 15.999, 20.086, 24.305, 32.065, 58.693, 40.078, 26.982]


molar_mass_aggregate = 0;
Z_aggregate = 0;
mass_comp_aggregate = 0;

for x in range(0,8):
	molar_mass_aggregate += mass_comp[x]*molar_mass[x]
	Z_aggregate += mass_comp[x]*Z[x]
	mass_comp_aggregate += mass_comp[x]

molar_mass_mean = molar_mass_aggregate / mass_comp_aggregate
Z_mean = Z_aggregate / mass_comp_aggregate

#calculate estimate for number of electrons in TB
num_electrons_est = (5.98e24 / (molar_mass_mean/1000)) * 6.022e23 * Z_aggregate / 8 / 1e12

#calculate lower bound assuming -40% error in all parameters
num_electrons_est_lower = ((5.98e24*.6) / ((molar_mass_mean*1.4)/1000)) * 6.022e23 * (Z_aggregate*.6) / 8 / 1e12

#calculate upper bound assuming +40% error in all parameters
num_electrons_est_upper = ((5.98e24*1.4) / ((molar_mass_mean*0.6)/1000)) * 6.022e23 * (Z_aggregate*1.4) / 8 / 1e12

#outputs (in TB)
#estimate, lower bound, upper bound
print (num_electrons_est)
print (num_electrons_est_lower)
print (num_electrons_est_upper)




