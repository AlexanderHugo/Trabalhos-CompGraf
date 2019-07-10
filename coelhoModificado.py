from OpenGL.GL import *
import math
# http://pyopengl.sourceforge.net/context/tutorials/shader_1.html

def calculaNormalFace(face,verticeMAP):
    x = 0
    y = 1
    z = 2
    
    v0 = verticeMAP[face[x]]
    v1 = verticeMAP[face[y]]
    v2 = verticeMAP[face[z]]
    
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    
    NLength = math.sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])

    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)
 
def MTL(filename):
    contents = {}
    mtl = None
    for line in open(filename, "r"):
        if line.startswith('format'): continue
        if line.startswith('comment'): continue
        if line.startswith('property'): continue
        if line.startswith('element'): continue
        if line.startswith('end_header'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'ply':
            mtl = contents[values[1]] = {}
        elif mtl is None:
            raise ValueError, "ply file doesn't start with newmtl stmt"
        #elif values[0] == 'map_Kd':
		#pass
        else: 
            mtl[values[0]] = map(float, values[1:])
    return contents
 
class OBJ:
    def __init__(self, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.normCalcArray = []
        self.faces = []
        self.norms = []
        self.shader = []
 
        material = None
        for line in open(filename, "r"):
            if line.startswith('#'): continue
            if line.startswith('format'): continue
            if line.startswith('comment'): continue
            if line.startswith('property'): continue
            if line.startswith('element'): continue
            if line.startswith('end_header'): continue                               
            if line.startswith('ply'): continue       
            values = line.split()
            if not values: continue
            if values[0] == '3':
                v = map(int, values[1:4])
                self.faces.append(v)
                # self.norms.append(calculaNormalFace((self.texcoords[int(v[0])],self.texcoords[int(v[1])],self.texcoords[int(v[2])])))                
                self.normCalcArray.append(calculaNormalFace(v,self.vertices))
                
            else:
                v = map(float, values[0:3])
                self.vertices.append(v)
                print values[4]
                b = float(values[4])
                self.shader.append(b)
            print self.shader
            print len(self.shader)
            print len(self.vertices)
            
        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        glFrontFace(GL_CCW)
        
        #print self.normCalcArray
        j = 0
        print len(self.faces)        
        for i in range(len(self.faces)):
            
            #vertices, normals, texture_coords, material = face
            vertices = self.faces[i]
            norm = self.normCalcArray[i]         
            #print vertices
            #print shader
            
            
 
            #glBegin(GL_POLYGON)
            glBegin(GL_TRIANGLE_STRIP)
            glColor4f(0.5, 0.0, 0.0);
            
            
            for k in range(len(vertices)):
                
                glVertex3fv(self.vertices[int(vertices[k])])
                #quit()                
                glNormal3fv(norm)
                

                #if texture_coords[i] > 0:
                #    glTexCoord2fv(self.texcoords[texture_coords[i] - 1])
                
            glEnd()
        glDisable(GL_TEXTURE_2D)
        glEndList()
        
        
