import numpy as np
from scipy.integrate import simpson
from ..utils.tools import *

#
#  Refractive indices
#  The refractive indices depend on wavelengths (and temperature).
#
#  Reference:
#
#  WU et al. Optical Engineering 1993 32(8) 1775
#  Li et al. Journal of Applied Physics 96, 19 (2004)


def calc_n(lamb):
    """
    calc_n calculates the refractive indices (n_o, n_e) of 5CB for the wavelength lamb
    """
    l1 = 0.210; l2 = 0.282;
    n0e = 0.455; g1e = 2.325; g2e = 1.397
    n0o = 0.414; g1o = 1.352; g2o = 0.470

    n_e = 1 + n0e + g1e*(lamb**2 * l1**2)/(lamb**2-l1**2) + g2e*(lamb**2 * l2**2)/(lamb**2-l2**2)
    n_o = 1 + n0o + g1o*(lamb**2 * l1**2)/(lamb**2-l1**2) + g2o*(lamb**2 * l2**2)/(lamb**2-l2**2)

    return n_o, n_e

def calc_n_s(lamb,s):
    """
    calc_n_s calculates the refractive indices (n_o,n_e) of 5CB for the wavelength lamb
    and order parameter s
    """
    l1 = 0.210; l2 = 0.282;
    n0e = 0.455; g1e = 2.325; g2e = 1.397
    n0o = 0.414; g1o = 1.352; g2o = 0.470

    n_e = 1 + n0e + g1e*(lamb**2 * l1**2)/(lamb**2-l1**2) + g2e*(lamb**2 * l2**2)/(lamb**2-l2**2)
    n_o = 1 + n0o + g1o*(lamb**2 * l1**2)/(lamb**2-l1**2) + g2o*(lamb**2 * l2**2)/(lamb**2-l2**2)

    S0 = 0.68
    delta_n = (n_e - n_o)/S0
    abt = (n_e + 2*n_o)/3.0
    n_e = abt + 2/3*s*delta_n
    n_o = abt - 1/3*s*delta_n
     
    return n_o, n_e


def white_balance(ws, whiteRGB = np.asarray([1.0, 1.0, 1.0]), exposureFactor = 1.0):
    """
    
    """
    #print ("Exposure factor is:", exposureFactor)
    #x0 = 0.964; y0 = 1.000; z0 = 0.825
    x0, y0, z0 = rgb2xyz(np.asarray (whiteRGB).reshape(1,1,3)).reshape(3)
    x0, y0, z0 = np.asarray([0.95046, 1.     , 1.08875])
    s1 = x0/sum(ws[:,0])*exposureFactor; s2 = y0/sum(ws[:,1])*exposureFactor; s3 = y0/sum(ws[:,2])*exposureFactor
    #### QUESTION FOR ELISE. error in s3? should it be z0?
    #print ("White balance scaling factor: %.2f, %.2f, %.2f" % (s1, s2, s3))

    return s1, s2, s3
