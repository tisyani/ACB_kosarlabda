f = open ("eredmenyek.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class eredmenyek:
    def __init__(self, hazai, idegen, hp, ip, hely, ido):
        self.hazai = hazai
        self.idegen = idegen
        self.hp = int(hp)
        self.ip = int(ip)
        self.hely = hely
        self.ido = ido

eredmenyekek = []
for i in range(1, len(sorok)):
    darabok = sorok[i].strip().split(";")
    e = eredmenyek(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    eredmenyekek.append(e)

hazaidb = 0
idegendb = 0

for e in eredmenyekek:
    if e.hazai == "Real Madrid":
        hazaidb += 1
    if e.idegen == "Real Madrid":
        idegendb += 1

print(f"Real Madrid: {hazaidb} {idegendb} ")