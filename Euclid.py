a=12345
b=123
#while(1):

class GCDc:
    a=b=0
    lastx=1
    lasty=0
    x=0
    y=1
    def gcdextend(a=int,b=int):
        if(b==0):
            return a,GCDc.lastx,GCDc.lasty
        xtemp=GCDc.x
        ytemp=GCDc.y
        GCDc.x=GCDc.lastx-int(a/b)*GCDc.x
        GCDc.y=GCDc.lasty-int(a/b)*GCDc.y
        GCDc.lastx=xtemp
        GCDc.lasty=ytemp
        print("x:{0} y:{1}".format(GCDc.x, GCDc.y))
        d= GCDc.gcdextend(b, a % b)
        return d

    def gcdc(a, b):
        if (b == 0):
            return a
        else:
            print("{0} {1}".format(a % b, b))
            c = GCDc.gcdc(b, a % b)

        return c

print(GCDc.gcdc(a,b))