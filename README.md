# py4SAIL
The original 4SAIL is based on FORTRAN, which can be found in http://teledetection.ipgp.jussieu.fr/prosail/

Hector Nieto translated the FORTRAN code into PYTHON code, which is the pypro4sail (https://github.com/hectornieto/pypro4sail). Thanks to the authors for their hard work and dedication.

This project is a modification of pypro4sail, because I have found some inconformity between these two versions of code, 
and the results of pypro4sail can't fully agree with the simalations displayed in some papers listed below:

[1] Verhoef, W., Jia, L., Xiao, Q., & Su, Z. (2007). Unified optical-thermal four-stream radiative transfer theory for homogeneous vegetation canopies. IEEE Transactions on Geoscience and Remote Sensing, 45, 1808-1822.

[2] Cao, B., Roujean, J.-L., Gastellu-Etchegorry, J.-P., Liu, Q., Du, Y., Lagouarde, J.-P., Huang, H., Li, H., Bian, Z., Hu, T., Qin, B., Ran, X., & Xiao, Q. (2021). A general framework of kernel-driven modeling in the thermal infrared domain. Remote Sensing of Environment, 252, 112157.

The possible mistakes are listed as follows:
------------------------------------
In pypro4sail\four_sail.py:

the function calc_lidf_verhoef calculated LIDF with 18 angles, while there are 13 angles used in FORTRAN code

the function weighted_sum_over_lidf also use 18 angles, while there are 13 angles used in FORTRAN code

This may not be a mistake but another parameterization scheme, but I have changed it to keep with the FORTRAN code

------------------------------------
In pypro4sail\four_sail.py line 437:

rsodt = ((tss + tsd) * tdo + (tsd + tss * rsoil * rdd) * too) * rsoil / dn

should be changed as:

rsodt = ((tss + tsd) * tdo + (tsd + tss * rsoil * rdd) * too) * rsoil / dn + rsod

------------------------------------
In pypro4sail\pypro4sail.py line 226:

tso = tss * too + tss * (tdo + rsoil * rdd * too) / (1. - rsoil * rdd)

should be changed as:

tso = tsstoo + tss * (tdo + rsoil * rdd * too) / (1. - rsoil * rdd)

------------------------------------

Besides, single wavelength instead of broadband is used in simulation.

I have changed above possible mistakes, and the new four_sail.py and pypro4sail.py have been uploaded.

In order to use, please replace the old four_sail.py and pypro4sail.py with these two modified files.

validation.ipynb shows the simulation results, which is consistent with the figures in Verhoef et al (2007).
