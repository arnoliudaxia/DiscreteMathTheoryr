p=23
g=5
class People:
    privateKey=0
    selfFactor,publicKey=0
    def genPublicKey(self):
        self.privateKey=pow(g,self.selfFactor,p)
    def calPrivateKey(self,publicKey):
        return pow(publicKey,self.selfFactor,p)

Alice=People()
Alice.genPublicKey()



