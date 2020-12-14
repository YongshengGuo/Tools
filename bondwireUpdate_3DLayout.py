'''
Created on 2020-12-10

@author: yguo
'''
from itertools import groupby
global oDesktop
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("Layout")
wireList = [(oEditor.GetPropertyValue("BaseElementTab",wire, "Start Layer"),wire) for wire in oEditor.FindObjects("Layer","WIRE")]
wireList.sort(key=lambda x:x[0])
for k,g in groupby(wireList,key=lambda x:x[0]):
#     print(list(g))
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:BaseElementTab",
                [
                    "NAME:PropServers"
                ] + [x[-1] for x in g],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:PlacementLayer",
                        "Value:=", k
                    ]
                ]
            ]
        ])