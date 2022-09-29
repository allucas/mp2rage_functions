# mp2rage_functions

This repository includes functions for working with MP2RAGE data. 

# Removing MP2RAGE background noise

Following O'Brien et. al.  (10.1371/journal.pone.0099676), the function `remove_mp2rage_bg.py` takes the INV1, INV2 and original UNI and generates a mask for the background, removing most of the noise. If the mask is too aggressive, change the multiplying factor (the number 200 on line 34).

### Usage

```
python remove_mp2rage_bg.py -inv1 path/to/inv1.nii -inv2 path/to/inv2.nii.gz -uni path/to/uni.nii.gz -o path/to/output.nii.gz 
```
