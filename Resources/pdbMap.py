from __future__ import division

import args as args
import iotbx.pdb
import iotbx.xplor.map
import libtbx as libtbx
from cctbx.miller import fft_map
from libtbx.math_utils import ifloor, iceil
import libtbx.option_parser
import sys

def run(args):
  if (len(args) == 0): args = ["--help"]
d_min = 2
pdb_inp = iotbx.pdb.input("6f0o.pdb")
xray_structure = pdb_inp.xray_structure_simple()
print("d_min:", d_min)
f_calc = xray_structure.structure_factors(d_min=d_min).f_calc()
fft_map = f_calc.fft_map()
coeffs= fft_map.map_coefficients
print(coeffs)
n = fft_map.n_real()
print("unit cell gridding:", n)
fft_map.as_xplor_map(file_name="unit_cell.map")
block_first = tuple([ifloor(i*0.2) for i in n])
block_last = tuple([max(f+10, iceil(i*0.7)) for f,i in zip(block_first, n)])
print("block first:", block_first)
print "block last: ", block_last
fft_map.as_xplor_map(file_name="block.map", gridding_first=block_first, gridding_last=block_last)
