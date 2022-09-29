import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import medfilt

## Argument Parser
import argparse
import os
import subprocess

# Parse all the required arguments
parser = argparse.ArgumentParser()

# Global arguments
parser.add_argument("-inv1", "--inv1_path")
parser.add_argument("-inv2","--inv2_path")
parser.add_argument("-uni","--uni_path")
parser.add_argument("-o","--output_nifti")



args = parser.parse_args()

inv1_name = args.inv1_path
inv2_name = args.inv2_path
uni_name = args.uni_path
output = args.output_nifti

inv1 = nib.load(inv1_name).get_fdata()
inv2 = nib.load(inv2_name).get_fdata()
uni = nib.load(uni_name).get_fdata()


beta=(np.mean(uni[-30:-10,-30:-10,-30:-10])*200)
INV1final = inv1
uni_fixed = np.real(((INV1final)*inv2-beta) / (np.abs(INV1final)**2 + np.abs(inv2)**2 + 2*beta))

uni_fixed_mask = -uni_fixed

uni_fixed_mask[uni_fixed>0] = -uni_fixed[uni_fixed>0]*(-1)

uni_fixed_mask = medfilt(uni_fixed_mask, 5)

uni_fixed_new = uni*(uni_fixed_mask<0.45)

uni_fixed_nifti = nib.Nifti1Image(uni_fixed_new, nib.load(uni_name).affine)
nib.save(uni_fixed_nifti, output)