import numpy as np
import ReadSift


R = ReadSift.ReadSift('00000000.sift')

print R

Y = ReadSift.CountSift('00000000.sift')

print Y
