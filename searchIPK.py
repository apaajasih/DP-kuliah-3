# Buatlah Perhitungan IPK untuk semester ini berdasarkan nilai yang di input
# Mata kuliah semster ini adalah Algoritma, Perancangan Objek, Kalkulus, Etika Profesi, Databases, dan Englis

nilaiAlgoritma = int(input("Masukkan nilai Algoritma: "))
SKSalgoritma = int(input("masukan sks algoritma anda : "))
nilaiPerancanganObjek = int(input("Masukkan nilai Perancangan Objek: "))
SKSperancanganObjek = int(input("masukan sks perancangan objek anda : "))
nilaiKalkulus = int(input("Masukkan nilai Kalkulus: "))
SKSkalkulus = int(input("masukan sks kalkulus anda : "))
nilaiEtikaProfesi = int(input("Masukkan nilai Etika Profesi: "))
SKSetikaProfesi = int(input("masukan sks etika profesi anda : "))
nilaiDatabases = int(input("Masukkan nilai Databases: "))
SKSdataBases = int(input("masukan sks data bases anda : "))
nilaiEnglish = int(input("Masukkan nilai English: "))
SKSenglis1 = int(input("masukan sks englis 1 anda : "))


def hitungTotal(nilai, sks):
    if nilai < 30:
        return 0 * sks
    elif nilai <= 34:
        return 1 * sks
    elif nilai <= 39:
        return 1.25 * sks
    elif nilai <= 44:
        return 1.5 * sks
    elif nilai <= 49:
        return 1.75 * sks
    elif nilai <= 54:
        return 2 * sks
    elif nilai <= 59:
        return 2.25 * sks
    elif nilai <= 64:
        return 2.5 * sks
    elif nilai <= 69:
        return 2.75 * sks
    elif nilai <= 74:
        return 3 * sks
    elif nilai <= 79:
        return 3.25 * sks
    elif nilai <= 84:
        return 3.5 * sks
    elif nilai <= 89:
        return 3.75 * sks
    else:
        return 4 * sks


totalAlgoritma = hitungTotal(nilaiAlgoritma, SKSalgoritma)
totalPerancanganObjek = hitungTotal(nilaiPerancanganObjek, SKSperancanganObjek)
totalKalkulus = hitungTotal(nilaiKalkulus, SKSkalkulus)
totalEtikaProfesi = hitungTotal(nilaiEtikaProfesi, SKSetikaProfesi)
totalDataBases = hitungTotal(nilaiDatabases, SKSdataBases)
totalEnglis1 = hitungTotal(nilaiEnglish, SKSenglis1)

totalSKS = SKSalgoritma + SKSperancanganObjek + SKSkalkulus + SKSetikaProfesi + SKSdataBases + SKSenglis1

IPK = (totalAlgoritma + totalPerancanganObjek + totalKalkulus + totalEtikaProfesi + totalDataBases + totalEnglis1) / totalSKS

print("Total IPK kamu adalah ", str(IPK))

