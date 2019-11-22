import struct
#import pyassimp
from pyassimp import *
class mesh: 
    diffusemap = "none"
    diffusecolor = "127.5 127.5 127.5"
    facecount = 0     # class attribute 
    faces = []
    smoothed = "undefined"

class vert: 
    x = 0
    y = 0
    z = 0
    u = 0
    v = 0
blankvert = vert()
class triangle: 
    a = blankvert
    b = blankvert
    c = blankvert

class object: 
    type = "undefined"     # class attribute 
    name = "NoName"
    gameobjectname = "NoGameObjectName"
    zonename = "NoZone"
    mesh = None


print("Initializing.")

groups = []
splitgroups = []
meshgroups = [] #ehhh


objects = []
meshes = []

fileName = "G:/p9lscript/NewMap.P9L"
f = open(fileName, mode='r')
fileContent = f.read()
groups = fileContent.split("\n\n")
#cnt = 0
#fix groups
for cnt, group in enumerate(groups):
    #print(cnt/len(groups)*100," percent complete         \r")
    splitgroups.append(group.split("\n"))
    lines = group.split("\n")
    #print("Group {}: {}".format(cnt, line
    #if("Faces" in group):
    #    meshgroups.append(group.split("\n"))
    #cnt += 1
       
    #OBJECT PARSER
    if(cnt > 0):
        newobj = object()
        newobj.mesh = mesh()
        tempmesh = newobj.mesh
        for line, tag in enumerate(lines):
            #create a temporary mesh - this will only be given to the object if a mesh is required
                

            if(tag.startswith("ZoneName")):
                newobj.zonename = tag[9:]
               
            if(tag.startswith("ObjectName")):
                newobj.name = tag[11:]
                
            if(tag.startswith("Type")):
                newobj.type = tag[5:]

            if(tag.startswith("GameObjectName")):
                newobj.gameobjectname = tag[15:]



            #Utilize the presence of a Diffuse Map to determine the presence of a mesh, as type seems to be unused for meshes
            if(tag.startswith("DiffuseMap")):
                tempmesh.diffusemap = tag[11:]
                #define our object's mesh class
                #newobj.mesh = tempmesh

            if(tag.startswith("DiffuseColour")):
                tempmesh.diffusecolor = tag[14:]

            if(tag.startswith("Smoothed")):
                tempmesh.smoothed = tag[9:]

            if(tag.startswith("Faces")):
                tempmesh.facecount = int(tag[6:])
                #this signifies the end of an object block and the start of face data, so we transition to parse the faces
                    
                faceblockline = line + 1
                faceblocks = lines[faceblockline:]
                    
                localfaceList = []
                elecounter = 0
                elementcurtri = []

                for element, eleline in enumerate(faceblocks):
                    elementcurtri.append(eleline)
                    elecounter += 1
                    if(elecounter == 3):
                        elecounter = 0
                        localfaceList.append(elementcurtri)
                        elementcurtri = []
                    
                ##grouping works
                localfacearrayToSend = []
                for facenum, curface in enumerate(localfaceList):
                        
                    myA = curface[0][2:]
                    myB = curface[1][2:]
                    myC = curface[2][2:]
                        
                    Avalues = myA.split(" ")
                    Bvalues = myB.split(" ")
                    Cvalues = myC.split(" ")

                    A = vert()
                    A.x = Avalues[0]
                    A.y = Avalues[1]
                    A.z = Avalues[2]
                    A.u = Avalues[3]
                    A.v = Avalues[4]

                    B = vert()
                    B.x = Bvalues[0]
                    B.y = Bvalues[1]
                    B.z = Bvalues[2]
                    B.u = Bvalues[3]
                    B.v = Bvalues[4]

                    C = vert()
                        
                    C.x = Cvalues[0]
                    C.y = Cvalues[1]
                    C.z = Cvalues[2]
                    C.u = Cvalues[3]
                    C.v = Cvalues[4]
                    newTri = triangle()
                    newTri.a = A
                    newTri.b = B
                    newTri.c = C
                    localfacearrayToSend.append(newTri)
                #localfaceList = []
                tempmesh.faces = localfacearrayToSend
        #keep this here
        objects.append(newobj)
            
header = splitgroups[0]

levelName = header[0][10:]
localTime = header[1][10:]
defaultStart = header[2][13:]

print("Level Name: {}".format(levelName))
print("Time of Export: {}".format(localTime))

#parse objects
#objnum = 0
#for objnum, curobject in enumerate(splitgroups):
    #if("Faces" in tag):
    #    meshes.append(splitgroups[meshnum])



#print(objects[0].gameobjectname)
print(objects[1].mesh.faces[1].b.z)
#print(len(objects[1].mesh.faces))
   



