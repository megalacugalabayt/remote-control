#a simple remote control with python for understanding classes

import random
import time as duduperi

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["trt"],kanal="trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):
        if(self.tv_durum=="Açık"):
            print("Televizyon açık...")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if(self.tv_durum=="Kapalı"):
            print("Televizyon Kapalı...")
        else:
            print("Televizyon Kapanıyor...")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):
        while True:
            cevap = input("Sesi azalt:'<'\nSesi Arttır>\nÇıkış:çıkış")

            if(cevap=="<"):
                if(self.tv_ses !=0):
                    self.tv_ses-=1
                    print("Ses",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses!=99):
                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)

            elif(cevap=="çıkış"):
                return Kumanda()
            
            else:
                print("Ses Güncellendi:",self.tv_ses)

    def kanal_ekle(self,kanal_ismi):

        print("Kanal Ekleniyor....")
        duduperi.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi")

    def rastgele_kanal(self):

        rastgele= random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]

        print("Şu anki kanal:",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "TV Durumu:{}\n TV Ses:{}\n Kanal Listesi: {}\nŞu Anki Kanal:{}\n".format(self.tv_durum,format(self.tv_ses),format(self.kanal_listesi),format(self.kanal))

kumanda = Kumanda() 

print("""
    TV Uygulaması
    
    1. Tv Aç
    
    2.Tv Kapat

    3.Ses Ayarları
    
    4.Kanal Ekle
    
    5.Kanal Sayısını Öğrenme
    
    6.Rastgele Kanal Seçme
    
    7.Televizyon Bilgileri
    
    
    Çıkmak için "q" ya basınız.
    
    """)

while True:
        işlem= input("İşlem Seçiniz:")

        if(işlem == "q"):
            print("Programdan Çıkış Yapılıyor....")
            duduperi.sleep(2)
            
            break

        elif(işlem == "1"):
            kumanda.tv_ac()

        elif(işlem=="2"):
            kumanda.tv_kapat()

        elif(işlem=="3"):
            kumanda.ses_ayarları()

        elif(işlem=="4"):
            kanal_isimleri = input("Kanal isimlerini','ile ayırarak yazınız..")

            kanal_listesi= kanal_isimleri.split(",")

            for eklenecekler in kanal_listesi:
                kumanda.kanal_ekle(eklenecekler)

        elif(işlem=="5"):
            kumanda.__len__()

        elif(işlem=="6"):
            kumanda.rastgele_kanal()

        elif(işlem=="7"):
            print(kumanda)

        else:
            print("Geçersiz işlem")
