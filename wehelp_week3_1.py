class Network:

  def __init__(self):
      self.w11 = 0.5
      self.w12 = 0.6
      self.w21 = 0.2
      self.w22 = -0.6
      self.b11 = 0.3
      self.b12 = 0.25
      self.wh1 = 0.8
      self.wh2 = 0.4
      self.b21 = -0.5

  def forward(self,x1,x2):
    h1 = self.w11 * x1 + self.w22 * x2 + self.b11
    h2 = self.w21 * x1 + self.w22 * x2 + self.b12
    O1 = h1 * self.wh1 + h2 * self.wh2 + self.b21

    return O1

nn=Network()

List=[[1.5,0.5],[0,1]]

for i in range(2):
  outputs=nn.forward(List[i][0],List[i][1])
  print(outputs)
