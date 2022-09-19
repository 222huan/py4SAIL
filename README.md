# py4SAIL
The original 4SAIL is based on FORTRAN, which can be found in http://teledetection.ipgp.jussieu.fr/prosail/
Reference:
Verhoef, W., Jia, L., Xiao, Q., & Su, Z. (2007). Unified optical-thermal four-stream radiative transfer theory for homogeneous vegetation canopies. Ieee Transactions on Geoscience and Remote Sensing, 45, 1808-1822.

Hector Nieto translated the FORTRAN code into PYTHON code, which is the pypro4sail (https://github.com/hectornieto/pypro4sail)
This project is a modification of pypro4sail, because I have found some inconformity between these two versions of the code, 
and the results of pypro4sail can't fully agree with the simalations displayed in some papers

The possible mistakes are listed as follows:
------------------------------------
In pypro4sail\four_sail.py:
the function calc_lidf_verhoef calculated LIDF with 18 angles, while there are 13 angles used in FORTRAN code
the function weighted_sum_over_lidf also use 18 angles, while there are 13 angles used in FORTRAN code
This may not be a mistake but another parameterization scheme, but I change it to keep with the FORTRAN code

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


I have changed above possible mistakes, and the new four_sail.py and pypro4sail.py have been uploaded.
In order to use, please replace the old four_sail.py and pypro4sail.py with these two modified files 
