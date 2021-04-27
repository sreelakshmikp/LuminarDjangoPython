population={"ind":100,"china":200,"nz":10,"wi":40,"ais":35}
print(population["ind"])
print(population.get("ind"))
data=sorted(population,key=population.get)
print(data)
data=sorted(population,key=population.get,reverse=True)
print(data)