import ifcopenshell

in_prefix=r'D:\data\ifc\schependomlaan\As planned models'
out_prefix=in_prefix+ r'\consistent_guids'
files= [r'\IFC Schependomlaan incl planningsdata.ifc',
        r'\Week 26 26 june IFC Schependomlaan incl planningsdata.ifc',
        r'\Week 27 3 july IFC Schependomlaan incl planningsdata.ifc',
        r'\Week 28 10 july IFC Schependomlaan incl planningsdata.ifc',
        r'\Week 29 17 july IFC Schependomlaan incl planningsdata.ifc',
        r'\Week 30 24 july IFC Schependomlaan incl planningsdata.ifc',
        r'\Week 37 11 sept IFC Schependomlaan incl planningsdata.ifc']
tag_dict = {}
for f in files:
       m = ifcopenshell.open(in_prefix+f)
       if len(tag_dict) == 0:
           for elem in m.by_type("IfcBuildingElement"):
               tag_dict[elem['Tag']]=elem["GlobalId"]
       else:
           for elem in m.by_type("IfcBuildingElement"):
               # elem['GlobalId'] = tag_dict[elem['Tag']]
               elem.__setattr__('GlobalId',tag_dict[elem['Tag']])
           m.write(out_prefix+f)

