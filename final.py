import gmpy2
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
        return self.deepGcdextend(a,b)
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
def PowerMod(a,b,c):
    ans = 1
    a = a % c
    while(b>0):
        if(b % 2 == 1):
            ans = (ans * a) % c
        b = b//2
        a = (a * a) % c
    return ans
class RSA:
    p,q=0,0
    N=p*q
    e=65535
    m,c=0,0
    def Encrypt(self,m,p,q,e):
        self.p,self.q,self.e,self.m=p,q,e,m
        self.N=p*q
        return PowerMod(m,e,self.N)
    def Decrypt(self,c,p,q,e):
        dSolver=EnclidAlogrism()
        #return PowerMod(c,gmpy2.invert(e,(p-1)*(q-1)),p*q)
        return PowerMod(c,dSolver.inverseof(e,(p-1)*(q-1)),p*q)

def EEA(a,b):
    g=EnclidAlogrism()
    return g.gcdextend(a, b)

def inverse(a,n):
    g=EnclidAlogrism()
    return g.inverseof(a,n)

def multiply_and_square(a,e,n):
    return PowerMod(a,e,n)

def RSA_enc(p,q,e,m):
    rsa=RSA()
    return rsa.Encrypt(m,p,q,e)

def RSA_dec_given_pq(p,q,e,c):
    De=RSA()
    return De.Decrypt(c,p,q,e)

## Please submit all the code above this line !!!
## The code below this line should not be submitted to OJ !!!
def main():
    #1
    a = 220008190813060514172414202418162473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639477074095512480796227391561801824887394139579933613278628104952355769470429079061808809522886423955917442317693387325171135071792698344550223571732405562649211
    b = 179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639479889735177768741618302107051448115080910246755937681237426900258951040875394506673937916489039005637257224383606487241814360108088853329912322798696840339821
    s,t = EEA(a,b)
    print("Problem 1: s = {}, t = {}".format(s,t))
    c,s,t=gmpy2.gcdext(a,b)
    print("Answer 1: s = {0}, t = {1}".format(s,t))

    #2
    a = 96369814566225467924653014805513492896964134518515264524627861474879778069831660663897677046727957192703934803972250616430609259595745097617769926942112134367594307837488500988473653982226257757541106532514633452399397504073793231177982720744337722569856046005247772492366591236471725562440735800298613269
    n = 44942328371557897693232629769725618340449424473557664318357520289433168951375240783177119330601884005280028469967848339414697442203604155623211857659874685278281817008285075796549731383684036558774922646581626556912205960275419478430830337938065417964147352294054171657328684516830612551814252127299848723248
    b = inverse(a,n)


    print("Problem 2: The inverse of a with module n is {}".format(b))
    print("Answer 2: The inverse of a with module n is {}".format(gmpy2.invert(a,n)))

    3
    a = 26430018304661698227244889550916468317489455778956328592921983469699792309163665193972706206594036869415691968221117606771494540098970766552365207210568611105852640630040412543297842462434526788081852074542946114404279053789976397875435006094029065093695673255562607050336148424707698012085470002233698228862346738763599120210887024055251199687451392437357330469313875769415203278005429487989371958004062135384988676187092753933346466785135069682592239769739616884935612245424974736666329142491909330198993521032748920319427468193197363789859738402941190883470502934385251934875320122360082927644910373611459923294476
    e = 14409405982160132058252555071975393865919464165649477935316970889691161917952938338402420626169849869240199817340818785857661040902521177902522865655959315955027296333658575625679171649648237486715107874038848080146760431808160047758267886816563159460881275453304962088598750789947602763231536498803689415008248542306983990585872732303067442760485939483530499206750926623632218337793608305495353477797937055213103722548287089239675029998455237837122665431788486963392282333218897305536581935858534831705616909506614608137265328584496490209976683510539438184418619421230489065033982087166936851293061923363455338233631
    n = 64543139452648583804777033627501791038942806480746416798824757337964931888296539408775325373896296201833019433336591701850604192958009038518829207716785069084776737389127085606861435151087914978789508354621086437098048489783165288663090667930959738070532371062440986402482696167926970371372070378265809277766155735077364001364843786628965534680520817227913435893489039438222319565950285009689464886596531381136997433211960842826747978689934063604682788246549928760755145469051762866022916315234333425333466441336354964665001026523519003032764174124744508998760069425321286184310908109489080474275209430911312055696378
    #a,e,n=2,123,35
    res = multiply_and_square(a,e,n)
    print("Problem 3: a^e mod n = {}".format(res))
    print("Answer 3: a^e mod n = {}".format(pow(a,e,n)))

    #4
    p = 6703903964971298549787012499102923063739682910296196688861780721860882015036773488400937149083451713845015929093243025426876941405973284973216824503042159
    q = 6703903964971298549787012499102923063739682910296196688861780721860882015036773488400937149083451713845015929093243025426876941405973284973216824503042857
    e = 96369814566225467924653014805513492896964134518515264524627861474879778069831660663897677046727957192703934803972250616430609259595745097617769926942112134367594307837488500988473653982226257757541106532514633452399397504073793231177982720744337722569856046005247772492366591236471725562440735800298613269
    m = 21901117025114964040305392436625187040695163470237446020295807020233905780163699671113037884909456394676262692845266679688481847750843861143699416191759070117456891447204693850314865556867390187774234481269014465723277071717132283569144455204933053504034742139896220841279932710423798768213939953157869023930
    c = RSA_enc(p,q,e,m)
    print("Problem 4: ciphertext c = {}".format(c))
    print("Answer 4: ciphertext c = {}".format(pow(m,e,p*q)))

    #5
    p = 92848022024833655041372304737256052921065477715975001419347548380734496823522565044177931242947122534563813415992433917108481569319894167972639736788613656007853719476736625612543893748136536594494005487213485785676333621181690463942417781763743640447405597892807333854156631166426238815716390011586838580891
    q = 149600854933825512159828331527177109689118555212385170831387365804008437367913613643959968668965614270559113472851544758183282789643129469226548555150464780229538086590498853718102052468519876788192865092229749643546710793464305243815836267024770081889047200172952438000587807986096107675012284269101785114471
    e = 4099852173630681822722339660229701793484497077549023050739406744299194740794285841565894857183257305962091658478256403457898496259755474199072635097327398971990092224918103250375455707498928712201945370461644425637423044616348028546654820134532012544433519158531485300462390097592776352017667386632661678681500542766835469056490039928380877979712159080905348869475217939844173751698241442662611990406492300411900572847532884748092860563495914734527293634873292356463076178294881900968373918292064527855306925898818421646057616238873254251939953144948550922456255743607156013509822605943382352582252129366170771186337
    c = 1965004133006974659995314560167723896560162823992014763466676295156568780181324759118466356116827422439409513865820570400810380977333397895810023254515182242123244875173658899005048988942666876614798046351776061310094809679938914368938218289806790724992660151078718864505196754907261135221257146114289875149015431301569207527108638684989789729747097766650481983822742788958528594215002940645806662061041825912562593269329369550470854629711422167160350497882132054038403027493105855840606846063029571758386220434189610971724518330438082401592895354255430599515214166039595157639322144199213475742435020500518884278854
    m = RSA_dec_given_pq(p,q,e,c)
    print("Problem 5: message m = {}".format(m))

if __name__ == "__main__":
    main()