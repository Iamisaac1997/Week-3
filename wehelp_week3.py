import numpy as np

class Network:
    
    def __init__(self, weight, bias):
                                                                                                                           
        self.weight = [np.array(w) for w in weight]                                               # 將 weight & bias 轉為 numpy 
        self.bias = [np.array(b) for b in bias]

    def forward(self, inputs):
        
        activation = np.array(inputs)                                                             # activation 是當前層的輸出值

        for layer_weight, layer_bias in zip(self.weight, self.bias):
            activation = np.dot(layer_weight, activation) + layer_bias                            # np.dot(layer_weight, activation) 計算權重與輸入的點相乘並加上 layer_bias
        
        return activation.tolist()                                                                # 轉換回list


weight_1 = [                                                                                      # 第1個 Network 的 weight & bias
    [[0.5, 0.2], [0.6, -0.6]],                                                                    # 第1層 weight（2 個神經元，2 個輸入）
    [[0.8, 0.4]]                                                                                  # 第2層 weight（1 個神經元，2 個輸入）
]

bias_1 = [
    [0.3, 0.25],                                                                                  # 第1層的bias（2 個神經元）
    [-0.5]                                                                                        # 第2層的bias（1 個神經元）
]

nn = Network(weight_1, bias_1)                                                                    # 代入 weight & bias

List = [                                                                                          # 兩題 x1, x2數值代入
    [1.5, 0.5],  
    [0, 1]       
]

print("Network 1:")
for i, inputs in enumerate(List):
    outputs = nn.forward(inputs) 
    print(f"{inputs}:{outputs}")


weight_2 = [                                                                                      # 第2個 Network 的weight & bias
    [[0.5, 1.5], [0.6, -0.8]],                                                                    # 第1層的 weight（2 個神經元，2 個輸入）
    [[0.6, -0.8]],                                                                                # 第2層的 weight（1 個神經元，2 個輸入）
    [[0.5], [-0.4]]                                                                               # 第3層的 weight（2 個神經元，1 個輸入）
]

bias_2 = [
    [0.3, 1.25],                                                                                  # 第1層的bias（2 個神經元）
    [0.3],                                                                                        # 第2層的bias（1 個神經元）
    [0.2, 0.5]                                                                                    # 第3層的bias（2 個神經元）
]

nn = Network(weight_2, bias_2)

List = [
    [0.75, 1.25],
    [-1, 0.5]      
]

print("\nNetwork 2:")
for i, inputs in enumerate(List):
    outputs = nn.forward(inputs)
    print(f"{inputs}:{outputs}")