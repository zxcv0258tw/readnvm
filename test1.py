import numpy as np
import ReadSift

def readnvmfile(filename):
	#filename = 'xxxx.nvm'
	T = []
	f = open(filename,'r')
	data = f.readlines()
	
	
	for i in range(len(data)):
		if data[i] == "\n":
			#print i
			T.append(i)
   	#print T
	
	start = T[0]+1
	
	data[start] = np.float32(data[start])
	G = []
	for v in range(data[start]):
		g = data[3+v]
		
		tmp1 = g.split('\t')
		#G = np.asarray([tmp1[0]])
		G.append(tmp1[0])
	G = np.array(G)
	print G
	
	start1 = T[1]+1
	data[start1] = np.float32(data[start1])
	
	for a in range(1):
		b = data[33+a]
        	
		tmp = b.split(' ')
		Q = [tmp[0],tmp[1],tmp[2],tmp[6]]
		
		#print Q[3]
		tmpoffset = 7
		for i in range(int(tmp[6])):
			ImId = int(tmp[tmpoffset+i*4])
			Q.append(ImId)
			#print Q			
			siftname = G[ImId][0:30]+'sift'
			print siftname
			feaId = int(tmp[tmpoffset+1+i*4])
			Q.append(feaId)
			#print Q			
			loc, des = ReadSift.ReadSift(siftname)
			x = double(loc[feaId][0])
			y = double(loc[feaId][1])
			#print len(loc)
			Q.append(des[feaId])
			#print des[Q[-1]]
			x_nvm = double(tmp[tmpoffset+2+i*4])
			y_nvm = double(tmp[tmpoffset+3+i*4])
			Q.append(x_nvm)
			Q.append(y_nvm)
			# check 
			err = np.absolute(x_nvm-x)+np.absolute(y_nvm-y)
			print err
			Q.append(err)
		print Q
			
		#Q = np.array(Q)
		#print Q
		
