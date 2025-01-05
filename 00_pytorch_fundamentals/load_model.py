import torch  

# 加载模型  
model = torch.load('model.pth')  

# 打印模型结构  
print(model)  

# 如果模型是 nn.Module 的子类，可以直接查看参数  
for name, param in model.named_parameters():  
    print(name, param.data)  # 打印每个参数的值