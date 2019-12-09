import struct
import os

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

#Assimp variables
#scene = pyassimp.structs.Scene()


#scene.meshes = []
materialpath = "G:/Keytop/Textures/"
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
                    if(elecounter > 2):
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

                    #Fix Scientific Notation!!!!!!!!!

                    #if("e-" in Avalues[0]):
                    #    print("scientific notation detected")
                    #    tokens = Avalues[0].split("e-")
                    #    Avalues[0] = '%f' % (float(tokens[0]) * (10 ** -float(tokens[1])))
                    #    #print('%f' % (float(tokens[0]) * (10 ** -float(tokens[1]))))

                    #if("e-" in Avalues[1]):
                    #    print("scientific notation detected")
                    #    tokens = Avalues[1].split("e-")
                    #    Avalues[1] = '%f' % (float(tokens[0]) * (10 ** -float(tokens[1])))
                    #    #print('%f' % (float(tokens[0]) * (10 ** -float(tokens[1]))))

                    #if("e-" in Avalues[2]):
                    #    print("scientific notation detected")
                    #    tokens = Avalues[2].split("e-")
                    #    Avalues[2] = '%f' % (float(tokens[0]) * (10 ** -float(tokens[1])))
                    #    #print('%f' % (float(tokens[0]) * (10 ** -float(tokens[1]))))



                    #if("e-" in Bvalues[0]):
                    #    print("scientific notation detected")
                    #    tokens = Bvalues[0].split("e-")
                    #    Bvalues[0] = '%f' % (float(tokens[0]) * (10 ** -float(tokens[1])))
                    #    #print('%f' % (float(tokens[0]) * (10 ** -float(tokens[1]))))

                    #if("e-" in Bvalues[1]):
                    #    print("scientific notation detected")
                    #    tokens = Bvalues[1].split("e-")
                    #    Bvalues[1] = '%f' % (float(tokens[0]) * (10 ** -float(tokens[1])))
                    #    #print('%f' % (float(tokens[0]) * (10 ** -float(tokens[1]))))

                    #if("e-" in Bvalues[2]):
                    #    print("scientific notation detected")
                    #    tokens = Bvalues[2].split("e-")
                    #    Bvalues[2] = '%f' % (float(tokens[0]) * (10 ** -float(tokens[1])))
                    #    #print('%f' % (float(tokens[0]) * (10 ** -float(tokens[1]))))



                    #if("e-" in Cvalues[0]):
                    #    print("scientific notation detected")
                    #    tokens = Cvalues[0].split("e-")
                    #    Cvalues[0] = '%f' % (float(tokens[0]) * (10 ** -float(tokens[1])))
                    #    #print('%f' % (float(tokens[0]) * (10 ** -float(tokens[1]))))

                    #if("e-" in Cvalues[1]):
                    #    print("scientific notation detected")
                    #    tokens = Cvalues[1].split("e-")
                    #    Cvalues[1] = '%f' % (float(tokens[0]) * (10 ** -float(tokens[1])))
                    #    #print('%f' % (float(tokens[0]) * (10 ** -float(tokens[1]))))

                    #if("e-" in Cvalues[2]):
                    #    print("scientific notation detected")
                    #    tokens = Cvalues[2].split("e-")
                    #    Cvalues[2] = '%f' % (float(tokens[0]) * (10 ** -float(tokens[1])))
                    #    #print('%f' % (float(tokens[0]) * (10 ** -float(tokens[1]))))


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
#print(objects[1].mesh.faces[1].b.z)
#print(len(objects[1].mesh.faces))

#print("converting to Assimp structure.")

##Aobj = pyassimp.structs.Mesh()
#Aobj = scene.meshes[0]

#print(Aobj.vertices)
##Aobj.faces = []
##Aobj.vertices = []
#for assimpobjnum, srcaobj in enumerate(objects):
#    #print("object identified")

#    #enumerate
#    for cnt, curface in enumerate(srcaobj.mesh.faces):
#        #print(curface)
#        Aface = pyassimp.structs.Face()
#        Avert = pyassimp.structs.Vector3D()
#        Avert.x = float(curface.a.x)
#        Avert.y = float(curface.a.y)
#        Avert.z = float(curface.a.z)
        
#        Bvert = pyassimp.structs.Vector3D()
#        Avert.x = float(curface.a.x)
#        Avert.y = float(curface.a.y)
#        Avert.z = float(curface.a.z)
        
#        Cvert = pyassimp.structs.Vector3D()
#        Avert.x = float(curface.a.x)
#        Avert.y = float(curface.a.y)
#        Avert.z = float(curface.a.z)

#        indicearray = []
#        Aobj.vertices.append([Avert.x,Avert.y,Avert.z])
#        Aface.indices = [len(Aobj.vertices) - 1]
#        indicearray = [len(Aobj.vertices) - 1]

#        Aobj.vertices.append([Bvert.x,Bvert.y,Bvert.z])
#        Aface.indices.append(len(Aobj.vertices) - 1)
#        indicearray.append(len(Aobj.vertices) - 1)

#        Aobj.vertices.append([Cvert.x,Cvert.y,Cvert.z])
#        Aface.indices.append(len(Aobj.vertices) - 1)
#        indicearray.append(len(Aobj.vertices) - 1)

#        Aobj.faces.append(indicearray)
        
        
#print(Aobj.vertices)        
#scene.meshes[0] = Aobj

##scene.meshes.append(Aobj)
#print(scene.meshes)
##print(scene.meshes[0].faces[12].indices[2])
#pyassimp.export(scene, 'out.dae', 'collada')


print("converting to .obj")

outtext = ""
materialtext = ""
faces = []
verts = []


materials = []


outtext += "\n"
outtext += "mtllib parsedmaterials.mtl"


outtext += "\n"
outtext += "o Main"




for objcount, obj in enumerate(objects):


    #create material array
    
    objecttexture = os.path.basename(obj.mesh.diffusemap)

    if(objecttexture != "none"):
        #print(objecttexture)
        if(objecttexture not in materials):
            materials.append(objecttexture)


        #objmaterialname = materials.index(objecttexture)



finalcount = 0

for objcount, obj in enumerate(objects):
    if(os.path.basename(obj.mesh.diffusemap) != "none"):
        objmaterialname = materials.index(os.path.basename(obj.mesh.diffusemap))
    if(obj.mesh.faces):
        outtext += "\n\n"
        #outtext += "o {}".format(obj.name) #hide for now cuz its laggy as fuck
        for facecount, face in enumerate(obj.mesh.faces):
            roundprecision = 3
            outtext += "\n"
            outtext += "v {} {} {}".format(face.a.x,face.a.y,face.a.z)
            myface = [len(verts)]
            verts.append(len(verts))

            outtext += "\n"
            outtext += "v {} {} {}".format(face.b.x,face.b.y,face.b.z)
            myface.append(len(verts))
            verts.append(len(verts))

            outtext += "\n"
            outtext += "v {} {} {}".format(face.c.x,face.c.y,face.c.z)
            myface.append(len(verts))
            verts.append(len(verts))

            #faces.append(myface)
            faces.append(face)


        for facecount2, face2 in enumerate(obj.mesh.faces):

            outtext += "\n"
            outtext += "vt {} {}".format(face.a.u,face.a.v)

            outtext += "\n"
            outtext += "vt {} {}".format(face.b.u,face.b.v)

            outtext += "\n"
            outtext += "vt {} {}".format(face.c.u,face.c.v)

        for facecount3, face3 in enumerate(obj.mesh.faces):
            outtext += "\n"

            #outtext += "f "
            #outtext += "{}/{}".format((facecount2 * 3) + 1,(facecount2 * 3) + 1)
            #outtext += " "

            #outtext += "{}/{}".format((facecount2 * 3) + 2,(facecount2 * 3) + 2)
            #outtext += " "

            #outtext += "{}/{}".format((facecount2 * 3) + 3,(facecount2 * 3) + 3)
            #outtext += " "
            outtext += "f "
            outtext += "{}/{}".format((finalcount * 3) + 1,(finalcount * 3) + 1)
            outtext += " "

            outtext += "{}/{}".format((finalcount * 3) + 2,(finalcount * 3) + 2)
            outtext += " "

            outtext += "{}/{}".format((finalcount * 3) + 3,(finalcount * 3) + 3)
            outtext += " "
            outtext += "\n"
            finalcount += 1

        if(os.path.basename(obj.mesh.diffusemap) != "none"):
            outtext += "usemtl " + str(objmaterialname)





outtext += "\n\n"
#outtext += "usemtl None"
outtext += "\n"
outtext += "s off"
curcount = 1
#for facecount, face in enumerate(faces):
    #outtext += "\n"

    #outtext += "f "
    #outtext += "{}/{}".format(face[0],face[0])
    #outtext += " "
    #outtext += "{}/{}".format(face[1],face[1])
    #outtext += " "
    #outtext += "{}/{}".format(face[2],face[2])
    #print(float(face.b.z))
    
    #outtext += "f "
    #outtext += "{}/{}".format(curcount,curcount)
    #outtext += " "
    #curcount += 1
    #outtext += "{}/{}".format(curcount,curcount)
    #outtext += " "
    #curcount += 1
    #outtext += "{}/{}".format(curcount,curcount)
    #outtext += " "
    #curcount += 1












for matcount, mat in enumerate(materials):
    materialtext += "\n"

    materialtext += "newmtl " + str(matcount)


    materialtext += "\n"
    materialtext += "Kd 0.8 0.8 0.8"

    materialtext += "\n"
    materialtext += "map_Kd " + materialpath + mat

    materialtext += "\n"




print(materials)
#print(outtext)
outfile = open("outnew.obj", "w")
outfile.write(outtext)
outfile.close()

outmfile = open("parsedmaterials.mtl", "w")
outmfile.write(materialtext)
outmfile.close()