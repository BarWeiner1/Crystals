import iotbx
from iotbx.reflection_file_reader import *
from iotbx.reflection_file_utils import *
#myFile = reflection_file_server()
#arrays = myFile.get_miller_arrays("6pti-sf-cif")
#print("Amplitudes" )
#print(myFile.get_amplitudes(myFile,"6mdq-sf.cif",True,"","refln.F_meas_au"))
#print("Phase" )
#print( get_phase_scores(arrays))
#print("Xray data")
#print(get_xray_data_scores(arrays, True))
#print("Experimental phases" )
#print(get_experimental_phases_scores(arrays, True))

my_file = any_reflection_file("6f0o-sf.cif")
#print(unpickle_miller_arrays("/Users/barweiner/Downloads/6pti-sf.cif"))
#print try_all_readers("6mdq-sf.cif")
miller_arrays = my_file.as_miller_arrays()
#i_obs = miller_arrays[0]

for i in miller_arrays[0]:
    for m in i:
        print m
    print("--------------------")