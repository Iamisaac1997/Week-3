class Network:

    def __init__(self):
        self.w11 = 0.5
        self.w12 = 0.6
        self.w21 = 1.5
        self.w22 = -0.8
        self.b11 = 0.3
        self.b12 = 1.25
        self.wh1 = 0.6
        self.wh2 = -0.8
        self.b2 = 0.3
        self.wh31 = 0.5
        self.wh32 = -0.4
        self.b31 = 0.2
        self.b32 = 0.5

    def forward(self,x1,x2):
        h1 = self.w11 * x1 + self.w21 * x2 + self.b11 * 1
        h2 = self.w12 * x1 + self.w22 * x2 + self.b12 * 1
        h3 = self.wh1 * h1 + self.wh2 * h2 + self.b2 * 1

        O1 = self.wh31 * h3 + self.b31 * 1
        O2 = self.wh32 * h3 + self.b32 * 1

        return O1,O2

nn = Network()

List=[[0.75,1.25],[-1,0.5]]


for i in range(2):
    outputs=nn.forward(List[i][0],List[i][1])
    print(outputs)
