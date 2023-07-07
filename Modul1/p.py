def createQueue():
    q=[]
    return (q)
def enqueue(q,data):
    q.insert(0,data)
    return (q)
def dequeue(q):
    data=q.pop()
    return (data)
def isEmpty(q):
    return (q==[])
def size(q):
    return (len(q))
def show(q):
    return (q)

q=createQueue()
a=[]
jumlah=int(input("Masukkan proses dalam CPU : "))
for i in range(jumlah):
    nama=str(input("Nama proses ke-"+str(i)+": "))
    waktu=int(input("Waktu proses : "))
    a.append(nama)
    a.append(waktu)
    enqueue(q,a)
    a=[]
print()
waktu_proses=int(input("Waktu proses CPU : "))
print(show(q))
i=1
while not isEmpty(q):
    print("Iterasi ke-"+str(i))
    i+=1
    b=[]
    item=dequeue(q)
    sisa=item[1]-waktu_proses
    b.append(item[0])
    b.append(sisa)
if b[1]>0 and b[1]!=0:
    enqueue(q,b)
    print(" proses " + item[0] +" sedang diproses, dan sisa proses "+item[0]+"= ",sisa)
elif b[1]<=0:
    print(" Proses "+str(item[0])+" selesai")
print(" Data proses yang tersisa="+str(show(q)))
b = []