from graph_tool.all import *
from graph_tool.clustering import *
from graph_tool.centrality import *

g=Graph(directed=False)
t = g.new_edge_property("int")
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
v4 = g.add_vertex()
v5 = g.add_vertex()
v6 = g.add_vertex()
v7 = g.add_vertex()
v8 = g.add_vertex()
v9 = g.add_vertex()
v10 = g.add_vertex()
v11 = g.add_vertex()
v12 = g.add_vertex()
v13 = g.add_vertex()
v14 = g.add_vertex()
v15 = g.add_vertex()
v16 = g.add_vertex()

e1 = g.add_edge(v1, v2)
t[e1]=2
#e2 = g.add_edge(v1, v3)
#t[e2]=1
#e3 = g.add_edge(v1, v4)
#t[e3]=1
#e4 = g.add_edge(v1, v5)
#t[e4]=1
#e5 = g.add_edge(v1, v6)
#t[e5]=1
#e6 = g.add_edge(v1, v12)
#t[e6]=1
e7 = g.add_edge(v1, v15)
t[e7]=2
e8 = g.add_edge(v1, v16)
t[e8]=2
#e9 = g.add_edge(v2, v3)
#t[e9]=1
#e10 = g.add_edge(v2, v5)
#t[e10]=1
#e11 = g.add_edge(v2, v6)
#t[e11]=1
#e12 = g.add_edge(v2, v9)
#t[e12]=1
#e13 = g.add_edge(v2, v10)
#t[e13]=1
e14 = g.add_edge(v2, v15)
t[e14]=2
e15 = g.add_edge(v2, v16)
t[e15]=2
e16 = g.add_edge(v3, v4)
t[e16]=2
e17 = g.add_edge(v3, v6)
t[e17]=2
e18 = g.add_edge(v3, v7)
t[e18]=2
e19 = g.add_edge(v3, v8)
t[e19]=2
e20 = g.add_edge(v4, v8)
t[e20]=2
e21 = g.add_edge(v5, v7)
t[e21]=2
e22 = g.add_edge(v5, v9)
t[e22]=2
e23 = g.add_edge(v5, v14)
t[e23]=2
#e24 = g.add_edge(v5, v15)
#t[e24]=1
#e25 = g.add_edge(v5, v16)
#t[e25]=1
e26 = g.add_edge(v6, v7)
t[e26]=2
e27 = g.add_edge(v6, v8)
t[e27]=2
#e28 = g.add_edge(v6, v9)
#t[e28]=1
e29 = g.add_edge(v6, v11)
t[e29]=2
e30 = g.add_edge(v6, v12)
t[e30]=2
#e31 = g.add_edge(v6, v13)
#t[e31]=1
#e32 = g.add_edge(v6, v16)
#t[e32]=1
e33 = g.add_edge(v7, v8)
t[e33]=2
e34 = g.add_edge(v7, v11)
t[e34]=2
e35 = g.add_edge(v7, v12)
t[e35]=2
e36 = g.add_edge(v7, v13)
t[e36]=2
e37 = g.add_edge(v8, v11)
t[e37]=2
e38 = g.add_edge(v8, v12)
t[e38]=2
#e39 = g.add_edge(v8, v14)
#t[e39]=1
e40 = g.add_edge(v9, v10)
t[e40]=2
#e41 = g.add_edge(v9, v11)
#t[e41]=1
e42 = g.add_edge(v9, v13)
t[e42]=2
#e43 = g.add_edge(v9, v15)
#t[e43]=1
#e44 = g.add_edge(v10, v11)
#t[e44]=1
e45 = g.add_edge(v10, v13)
t[e45]=2
#e46 = g.add_edge(v10, v15)
#t[e46]=1
e47 = g.add_edge(v11, v12)
t[e47]=2
#e48 = g.add_edge(v11, v13)
#t[e48]=1
#e49 = g.add_edge(v11, v15)
#t[e49]=1
#e50 = g.add_edge(v11, v16)
#t[e50]=1
#e51 = g.add_edge(v12, v14)
#t[e51]=1
#e52 = g.add_edge(v12, v15)
#t[e52]=1
#e53 = g.add_edge(v12, v16)
#t[e53]=1
e54 = g.add_edge(v13, v14)
t[e54]=2
#e55 = g.add_edge(v13, v15)
#t[e55]=1
#e56 = g.add_edge(v13, v16)
#t[e56]=1
#e57 = g.add_edge(v14, v16)
#t[e57]=1
e58 = g.add_edge(v15, v16)
t[e58]=2

graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(900, 900), output="two-nodes.png")

print(global_clustering(g))
#a=local_clustering(g)
#for i in range(16):
#	print(a[i])


#a=closeness(g, weight=None, source=None, vprop=None, norm=True, harmonic=False)
#for i in range(0,16):
#	print(a[i])