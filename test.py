from pypro4sail import pypro4sail
import matplotlib.pyplot as plt
import numpy as np

# Common leaf distributions
PLANOPHILE = (1, 0)
ERECTOPHILE = (-1, 0)
PLAGIOPHILE = (0, -1)
EXTREMOPHILE = (0, 1)
SPHERICAL = (-0.35, -0.15)
UNIFORM = (0, 0)

[emisVeg, emisSoil, T_Veg, T_Soil, LAI, hot_spot, solar_zenith, solar_azimuth, LIDF] = \
[0.98, 0.94, 302, 299, 4, 0.05, 37.5, 0, pypro4sail.SPHERICAL]

VZA = np.arange(0, 61, 1)
VAA = np.arange(0, 360, 1)
T = np.zeros((len(VAA), len(VZA)))

for view_zenith in VZA:
    for view_azimuth in VAA:
        Lw, TB_obs, emiss = pypro4sail.run_TIR(emisVeg, emisSoil, T_Veg, T_Soil, LAI, hot_spot, solar_zenith, solar_azimuth,
                                           view_zenith, view_azimuth,
                                           LIDF, T_VegSunlit=310, T_SoilSunlit=323, T_atm=260, wav=9.5)
        T[view_azimuth][view_zenith] = TB_obs

r, theta = np.meshgrid(VZA, np.deg2rad(VAA))  # 转换为弧度
ax = plt.subplot(111, projection='polar')
ax.set_theta_direction(-1)       #顺时针
ax.set_theta_zero_location('N')  #北方向为0°
ax.contourf(theta, r, T, cmap='jet')
ax.set_rgrids([15, 30, 45, 60])  # 括号内设置为[]，隐藏格网线
#plt.thetagrids

plt.show()

