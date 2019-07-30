from iotbx.pdb import hierarchy
pdb_in = hierarchy.input(file_name="6f0o.pdb")
pdb_atoms = pdb_in.hierarchy.atoms()
for i in pdb_atoms:
    print i.xyz
    print i.b





xray_structure = pdb_in.input.xray_structure_simple()
sel_cache = pdb_in.hierarchy.atom_selection_cache()
c_alpha_sel = sel_cache.selection("name ca") # XXX not case sensitive!
c_alpha_atoms = pdb_atoms.select(c_alpha_sel)
c_alpha_xray_structure = xray_structure.select(c_alpha_sel)
c_alpha_hierarchy = pdb_in.hierarchy.select(c_alpha_sel)
