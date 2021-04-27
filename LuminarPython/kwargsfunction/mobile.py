mobiles={
    "galaxy":{"frontcam":"12px","rearcam":"30px","ram":4,"price":20000},
    "galaxy1":{"frontcam":"10px","rearcam":"20px","ram":4,"price":30000}
}
mobilename=input("enter mobile name")
spec=input("enter specification")
# print(mobile[mobilename][spec]) -->error
if mobilename in mobiles:
    print(mobiles[mobilename]["price"])
    if spec in mobiles[mobilename]:
        print(mobiles[mobilename][spec])
    else:
        print("invalid specification")
else:
    print("no mobiles exist with the given name")