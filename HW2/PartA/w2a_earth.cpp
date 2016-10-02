// AUTHOR BrianAppleton appleton@bu.edu
// AUTHOR AlexBennett gottbenn@bu.edu
// AUTHOR CathrynCallahan cathcal@bu.edu
// AUTHOR PreranaHaridoss preranah@bu.edu

// git repository https://github.com/gottben/EC602

#include <iostream>
#include <iomanip>
using namespace std;

int main() {

	//Calculate average composition
	double mass_comp[] = {0.321, 0.301, 0.151, 0.139, 0.029, 0.018, 0.015, 0.014};
	double Z[] = {26, 8, 14, 12, 16, 28, 20, 13};
	double molar_mass[] = {55.845, 15.999, 20.086, 24.305, 32.065, 58.693, 40.078, 26.982};


	double molar_mass_aggregate = 0;
	double Z_aggregate = 0;
	double mass_comp_aggregate = 0;

	for (int x=0; x<8; x++) {
		molar_mass_aggregate += mass_comp[x]*molar_mass[x];
		Z_aggregate += mass_comp[x]*Z[x];
		mass_comp_aggregate += mass_comp[x];
	}

	double molar_mass_mean = molar_mass_aggregate / mass_comp_aggregate;
	double Z_mean = Z_aggregate / mass_comp_aggregate;

	//calculate estimate for number of electrons in TB
	double num_electrons_est = (5.98e24 / (molar_mass_mean/1000)) * 6.022e23 * Z_aggregate / 8 / 1e12;

	//calculate lower bound assuming -40% error in all parameters
	double num_electrons_est_lower = ((5.98e24*.6) / ((molar_mass_mean*1.4)/1000)) * 6.022e23 * (Z_aggregate*.6) / 8 / 1e12;

	//calculate upper bound assuming +40% error in all parameters
	double num_electrons_est_upper = ((5.98e24*1.4) / ((molar_mass_mean*0.6)/1000)) * 6.022e23 * (Z_aggregate*1.4) / 8 / 1e12;

	//outputs (in TB)
	//estimate, lower bound, upper bound
	cout << num_electrons_est << endl;
	cout << num_electrons_est_lower << endl;
	cout << num_electrons_est_upper << endl;

return 0;
}

