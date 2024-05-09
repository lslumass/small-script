#!/usr/bin/python

#script for calculating pair-interaction lifetime, like hydrogen bond or salt bridge
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as mda
from MDAnalysis.analysis.hydrogenbonds import HydrogenBondAnalysis

u = mda.Universe('ana.gro', 'ana.trr')
saltbrs = HydrogenBondAnalysis(
    universe=u,
    donors_sel="resname ARG LYS and name SC2",
    hydrogens_sel="resname ARG LYS and name SC1",
    acceptors_sel="resname POPG and name PO4",
    d_a_cutoff=6.0,
    d_h_cutoff=10.0,
    d_h_a_angle_cutoff=0,
    update_selections=False
)

saltbrs.run(
    step=1,
    verbose=True
)

tau_max = 300
window_step = 1
tau_frames, saltbrs_lifetime = saltbrs.lifetime(
    tau_max=tau_max,
    window_step=window_step
)
tau_times = tau_frames * u.trajectory.dt

def fit_biexponential(tau_timeseries, ac_timeseries):
    """Fit a biexponential function to a hydrogen bond time autocorrelation function

    Return the two time constants
    """
    from scipy.optimize import curve_fit

    def model(t, A, tau1, B, tau2):
        """Fit data to a biexponential function.
        """
        return A * np.exp(-t / tau1) + B * np.exp(-t / tau2)

    params, params_covariance = curve_fit(model, tau_timeseries, ac_timeseries, [1, 0.5, 1, 2])

    fit_t = np.linspace(tau_timeseries[0], tau_timeseries[-1], 1000)
    fit_ac = model(fit_t, *params)

    return params, fit_t, fit_ac

params, fit_t, fit_ac = fit_biexponential(tau_times, saltbrs_lifetime)
A, tau1, B, tau2 = params
time_constant = A * tau1 + B * tau2
print(f"time_constant = {time_constant:.2f} ps")

plt.plot(tau_times, saltbrs_lifetime, label="data")
plt.plot(fit_t, fit_ac, label="fit")
plt.text(15,0.5, 'lifetime = '+ str(round(time_constant,2)) + ' ps')

plt.title(r"Salt bridge lifetime", weight="bold")
plt.xlabel(r"$\tau\ \rm (ps)$")
plt.ylabel(r"$C(\tau)$")
plt.legend()
plt.show()
