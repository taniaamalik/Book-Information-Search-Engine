# Erlina Rohmawati     175150201111045
# Tania Malik Iryana 175150201111053
# Alvina Eka Damayanti 175150201111056
# Jeowandha Ria Wiyani 175150207111029

import time
import booleanModel as BRM

awal = time.time()  

#membaca file korpus
corpus = open('D:/Tania/UB/Semester 6/STKI/Project Akhir/corpusGoodRead.txt','rt', encoding="utf-8")
readCorpus = corpus.read()
corpus.close()
print("Proses Preprocessing ...")
corpusLengkap = BRM.cleaningTag(readCorpus)
corpusTanpaTag = BRM.cleaningTag(readCorpus)
judul, penulis = BRM.getCorpusLine(corpusTanpaTag)
corpusToken = BRM.cleaningTokenisasi(corpusTanpaTag)
corpusTanpaStopword = BRM.stopwordRemoval(corpusToken)

print("Proses Cari term ...")
terms = BRM.cariTerm(corpusTanpaStopword)
print("Proses Membuat Incident Matrix ...")
inMatrix = BRM.kemunculanKata(terms, corpusTanpaStopword) 
akhir = time.time()
print ("Total Waktu Proses " + str(akhir-awal) + " Detik." )

cari = True
while (cari):
    print("\n----------------------------Program Pencari Buku------------------------------------")
   
    query = input("\nMasukan kata kunci untuk mencari buku: ").lower()
    awal = time.time() 
    queryList = query.split(" ")
    postfixList = BRM.infixToPostfix(query, terms)
    hasil = BRM.hasilPostfix(postfixList, corpusTanpaStopword, terms, inMatrix)
    hasil_str = ""
    hasilCorpus = []
    count = 0
    for i in range(len(hasil)):
        if hasil[i] == 1:
            count +=1
            hasilCorpus.append(corpusLengkap[i])
            hasil_str = hasil_str + '\n'+ str(count) + ". "+ str(judul[i]) + ", oleh " + str(penulis[i])
            
    print("\nDocument yang mengandung kata '" + str(query) + "' yaitu di: " + str(hasil_str))
    print("----------------------------------------------------------------")
    akhir = time.time()
    print ("Total Waktu Proses " + str(akhir-awal) + " Detik." )
    print("----------------------------------------------------------------")
    if "not" in queryList:
        indexNot = queryList.index("not") + 1
        BRM.booleanNot(inMatrix.get(queryList[indexNot]))
    
    while True:     
        pilihan = input("Pilihan Menu :\n"+
            "1. Lihat Sinopsis\n"+
            "2. Cari Buku Lain\n"+
            "3. Keluar\n"
            "Masukkan pilihan : ")
        if (pilihan == "1"):
            buku =int(input("Masukkan nomor urut buku : "))
            if(buku in range(0, len(hasilCorpus)+1)):
                print("\n"+ str(hasilCorpus[buku-1]))
            else:
                print("input yang anda masukkan salah, coba lagi!\n")
                continue
        elif (pilihan == "2"):
            break
        elif (pilihan == "3"):
            print("\n------------------ Terimakasih -----------------------")
            cari = False
            break
        else:
            print("input yang anda masukkan salah, coba lagi!\n")
            continue