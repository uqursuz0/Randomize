import random
def görev():
    try:
        görevsayısı=int(input("seçenek sayısını giriniz"))
        görevlistesi=[]
        for i in range(görevsayısı):
            elem = input(f"{i+1}.görevi yazınız.")
            görevlistesi.append(elem)
        print(random.choice(görevlistesi))
        görev()
    except:
        print("done")
görev()