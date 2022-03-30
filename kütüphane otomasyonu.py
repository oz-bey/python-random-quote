

import sqlite3 as db

class database:
    def __init__(self):
        try:
            self.baglan = db.connect("kitaplar.db")
        except db.OperationalError:
            exit(1)
        self.cursor = self.baglan.cursor()
    def YeniTablo(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Kitaplar(id PRIMARYKEY,\
                            kitapAdi CHAR(50),\
                            yazarAdi CHAR(50),\
                            yayinEvi CHAR(50)\
                            )')
    def KitapEkle(self,id,kitapAdi,yazarAdi,yayinevi):
        kitapDictionary = [(id,kitapAdi,yazarAdi,yayinevi)]
        self.cursor.executemany("INSERT INTO Kitaplar\
                                (id,kitapAdi,yazarAdi,yayinevi)\
                                values(?,?,?,?)",kitapDictionary)
        self.baglan.commit()



    def KitapListele(self):

        print("Kitaplar")
        print("==========")
        self.cursor.execute("select * from Kitaplar")
        yazdir = self.cursor.fetchall()
        print(yazdir)
    def KitapSil(self):
        kitapID = input("Kitap Numarası Giriniz:")
        self.cursor.execute("delete from Kitaplar where id=:kitapID",{"kitapID":kitapID})#tupple kullanıldı
        self.baglan.commit()
def main():
    vt = database()
    vt.YeniTablo()

    print("Kütüphane Otomasyonu")
    print("=============")
    secenek = input("Lütfen işlem seçin\n1)Kitap Ekle\n2)Kitap Sil\n3)Kitap Düzenle\n4)Listele\nSeçenek:")
    if(secenek == "1"):
        id = input("Kitap No:")
        kitapAdi = input("Kitap Adı:")
        yazarAdi = input("Yazar Adı:")
        yayinEvi = input("Yayın Evi:")
        vt.KitapEkle(id,kitapAdi,yazarAdi,yayinEvi)
        print("Eklendi")
        main()
    elif(secenek == "2"):
        vt.KitapSil()
    elif(secenek == "4"):
        vt.KitapListele()
    main()

if __name__ == '__main__':
    main()