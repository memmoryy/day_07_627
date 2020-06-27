import yaml

with open("./data2.yaml" , "r",encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print("返回的数据为：",data)
    print("返回的数据类型为：",type(data))