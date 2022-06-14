
def read():
    numbers=[]
    with open('01number.txt','r',encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names=["Facundo","Miguel","Pepea,","Christian"]
    with open("02names.txt","w",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n") 

def run():
    read()


if __name__=="__main__":
    run()