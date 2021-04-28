

class EnclidAlogrism:
    a=b=0
    lastx=1
    lasty=0
    x=0
    y=1
    factorList=[]
    def __init__(self):
        self.factorList.clear()
    def gcdextend(self,a,b):
        if(b==0):
            return self.lastx,self.lasty
        xtemp=self.x
        ytemp=self.y
        self.x=self.lastx-int(a/b)*self.x
        self.y=self.lasty-int(a/b)*self.y
        self.lastx=xtemp
        self.lasty=ytemp
        #print("x:{0} y:{1} 商:{2}".format(self.x, self.y,int(a/b)))
        self.factorList.append(int(a / b))
        d= self.gcdextend(b, a % b)
        return d
    def deepGcdextend(self,a,b):
        input=[0,0]
        input[0]=a
        input[1]=b
        while input[1]!=0:
            xtemp = self.x
            ytemp = self.y
            factor=(input[0]//input[1])
            self.x = self.lastx - factor * self.x
            self.y = self.lasty - factor * self.y
            self.lastx = xtemp
            self.lasty = ytemp
            #print("x:{0} y:{1} 商:{2}".format(self.x, self.y,factor))
            self.factorList.append(factor)
            temp=input[1]
            input[1]=input[0]%input[1]
            input[0]=temp
        return self.lastx,self.lasty
    def gcdc(self,a, b):
        if (b == 0):
            return a
        else:
            #print("{0} {1}".format(a % b, b))
            c = self.gcdc(b, a % b)

        return c
    def inverseof(self,a,n):
        self.deepGcdextend(a,n)
        self.factorList.pop()
        self.factorList.reverse()
        self.factorList.pop()
        #print(self.factorList)
        inverseList = [0] * (len(self.factorList) + 1)
        inverseList[0] = 1
        inverseList[1] = self.factorList[0]
        for i in range(len(self.factorList) - 1):
            inverseList[i + 2] = inverseList[i] + inverseList[i + 1] * self.factorList[i + 1]
        #print(inverseList)

        B = 0
        if (len(self.factorList) % 2 == 0):
            return inverseList[-1]
        else:
            return n - inverseList[-1]
# n=105
# a=61
# g1=EnclidAlogrism()
# #print(g1.gcdextend(a,n))
# #print(g1.inverseof(a,n))
# print(g1.high(a,n))

