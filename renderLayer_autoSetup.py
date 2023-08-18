
import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
from maya.app.renderSetup.model.renderSetup import instance
import maya.cmds as cmds


BG_layer = 'BG_layer'  
STAGE_layer = 'STAGE_layer'    
FG_layer = 'FG_layer'
BG_shadow = 'BG_shadow'

BG_layer_geos = []
STAGE_layer_geos = []
FG_layer_geos = []

BG_layer_transforms = []
STAGE_layer_transforms = []
FG_layer_transforms = []


allGeo_from_Scene = cmds.ls(geometry=True, long=True )

for geo in allGeo_from_Scene:
            
        groupsInHierarchy = geo.split('|')
        print(groupsInHierarchy)
        
        for groupName in groupsInHierarchy:
            
               
            if groupName == BG_layer:
                BG_layer_geos.append(geo) 
                
            elif groupName == STAGE_layer:
                STAGE_layer_geos.append(geo)
                
            elif groupName == FG_layer:  
                FG_layer_geos.append(geo)
            else:
                print ('the ojbect is not under any layer group')  
                
                
print(BG_layer_geos)
print(STAGE_layer_geos)  
print(FG_layer_geos)  


# getting the transforms of each geo and appending to the transforms list
# the expression line of the render layer setup window can only accept 'transforms' not 'shapes'

for shapeName in BG_layer_geos:
    currentBGTransform = cmds.listRelatives(shapeName, parent=True, type='transform')[0]
    print(currentBGTransform)

    BG_layer_transforms.append(currentBGTransform)
    print(BG_layer_transforms)
    
    
    
for shapeName in STAGE_layer_geos:
    currentSTAGETransform = cmds.listRelatives(shapeName, parent=True, type='transform')[0]
    print(currentSTAGETransform)

    STAGE_layer_transforms.append(currentSTAGETransform)  
    print('THIS IS STAGE TRANSFORM')
    print (STAGE_layer_transforms)  
    
    
    
for shapeName in FG_layer_geos:
    currentFGTransform = cmds.listRelatives(shapeName, parent=True, type='transform')[0]
    print(currentFGTransform)

    FG_layer_transforms.append(currentFGTransform)  
    
cmds.select(clear=True)       
 



'''
Creating render layers based on the sorted geo by layer lists

'''


def create_layer_pass(name):
    
    layerName = '{}_pass'.format(name)
    collectionName = '{}_geo'.format(name)
    
    rs = instance()

    #this creates a render layer 
    rl = rs.createRenderLayer(layerName)
    
    #This creates a lights collection instance inside the created render layer
    l1 = rl.lightsCollectionInstance()

    # create and append collections under the layers    
    c1 = rl.createCollection(collectionName)
    
    # assigning geometry to the propper layer
    
     # BACKGROUND LAYER

    if name == BG_layer:
    # the expression line in the render layer setup window can not accept '[]' 
    # and imtems have to be either separated by a ',' or by a space.
    # here I am creating a string expression by removing the list parethesis 
    # and separating each item with a comma. 
    # This is because the "join" python command conects each item with nothing.   
        BG_layer_geos_expression = ''.join(str(','+item) for item in BG_layer_transforms)       
        
        print('THIS IS THE EXPRESSION.......................')
        print(BG_layer_geos_expression)
       
        c1.getSelector().setPattern(BG_layer_geos_expression)
        
    else:
        print('name is not BG_layer')  

    # STAGE LAYER

    if name == STAGE_layer:
 
        STAGE_layer_geos_expression = ''.join(str(','+item) for item in STAGE_layer_transforms)       
        
        print('THIS IS STAGE EXPRESSION.......................')
        print(STAGE_layer_geos_expression)
       
        c1.getSelector().setPattern(STAGE_layer_geos_expression)
        
    else:
        print('name is not STAGE_layer') 


    # FG LAYER

    if name == FG_layer:
 
        FG_layer_geos_expression = ''.join(str(','+item) for item in FG_layer_transforms)       
        
        print('THIS IS STAGE EXPRESSION.......................')
        print(FG_layer_geos_expression)
       
        c1.getSelector().setPattern(FG_layer_geos_expression)
        
    else:
        print('name is not FG_layer') 
        
        
        
# layer names to create

layerList_toCreate = [BG_layer,STAGE_layer,FG_layer, BG_shadow]
    
for eachLayerName in layerList_toCreate:
    
    create_layer_pass(eachLayerName)
                              







                