from __future__ import division

import args as args
import iotbx.pdb
import mmtbx.f_model
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
f_obs = abs(xray_structure.structure_factors(d_min=1.5).f_calc())
r_free_flags = f_obs.generate_r_free_flags()
# instantiate fmodel object
fmodel = mmtbx.f_model.manager(f_obs          = f_obs,r_free_flags   = r_free_flags,xray_structure = xray_structure)
fft_map = fmodel.electron_density_map().fft_map(map_type="mFobs-DFmodel")
fft_map.apply_sigma_scaling()
map_data = fft_map.real_map_unpadded(in_place=False)
# output map in X-plor formatted file
fft_map.as_xplor_map(
  file_name="mfo-dfm.xplor",
  title_lines=["mFobs-DFmodel"],
  gridding_first=(0, 0, 0),
  gridding_last=fft_map.n_real())
# we can compute another map
#map_coeffs = fmodel.electron_density_map(
#).map_coefficients(map_type = "2mFobs-DFmodel")
# output it as MTZ file
#mtz_dataset = map_coeffs.as_mtz_dataset(column_root_label="2mFoDFc")
#mtz_object = mtz_dataset.mtz_object()
#mtz_object.write(file_name = "amap.mtz")
# and get actual map values
#fft_map = map_coeffs.fft_map(resolution_factor=0.25)
#fft_map.apply_volume_scaling()
#map_data = fft_map.real_map_unpadded()
#for i in map_data:
 # print(i)