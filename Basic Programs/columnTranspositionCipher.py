key='HARIKESH'
userval='HACKTOBERFEST'
col=len(key)
if((len(userval)%col)!=0):userval+="x"*(len(userval)%col)
userval=userval.replace(' ', '') # remove white spaces from key 
o=[]
for i in key:
 o.append(i)  # generating list for keys
h=[]
for i in range(col):
 h.append(userval[i:len(userval):col]) # generating list for plaintext column wise 
dic=dict(zip(o,h))    # adding both lists
so=sorted(dic.keys())    # sorting alphabateically keys of cipher
print(''.join(dic[i]for i in so)) # join func for displaaying in string format
