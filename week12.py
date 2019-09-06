class Tasit():
    __tasit_miktari = []

    def __init__(self, motor_gucu, koltuk_sayisi, km_durumu, model, satis_yili, tekerlek_sayisi=4):
        self.motor_gucu = motor_gucu
        self.koltuk_sayisi = koltuk_sayisi
        self.km_durumu = km_durumu
        self.model = model
        self.satis_yili = satis_yili
        self.__tasit_miktari.append("1")

    def koltuk_sayisi_goster(self):
        print("Koltuk sayisi: ", self.koltuk_sayisi)

    def model_goster(self):
        print("Modeli: ", self.model)

    def km_durumu_gonder(self):
        return self.km_durumu

    @classmethod
    def __tasit_sayisi_guncelle(self):
        self.__tasit_miktari.append("1")

    @classmethod
    def __tasit_miktari_goster(cls):
        uzunluk = len(cls.__tasit_miktari)
        print("Tasit Miktari: ", uzunluk)


class Araba(Tasit):
    def __init__(self,motor_gucu, koltuk_sayisi, km_durumu, model, satis_yili, max_hiz, tekerlek_sayisi=4):
        super().__init__(motor_gucu, koltuk_sayisi, km_durumu, model, satis_yili)
        self.max_hiz = max_hiz

    def arabayi_durdur(self):
        print("Araba durdu")

    def gaza_bas(self):
        print("Araba hizlaniyor...")

    def arabayi_yavaslat(self):
        print("Araba yavasliyor...")

    def arabanin_durumunu_goster(self):
        if issubclass(Araba, Tasit):
            print("Bu sinif Tasit sinifindan miras alinmistir")
        else:
            print("Araba sinifi Tasit sinifindan miras alinmamistir.")

    def model_goster(self):
        print("Araba sinifinin methodu: ", self.model)

tasit = Tasit(200, 10, 10000, "Kamyon", 2001, 1000)
araba = Araba(100, 4, 50000, "Renault", 1991, 5000) 

tasit.model_goster()
araba.model_goster()

araba.arabanin_durumunu_goster()
araba.arabayi_durdur()
araba.arabayi_yavaslat()
araba.gaza_bas()
print("Araba km durumu",araba.km_durumu_gonder())

tasit.koltuk_sayisi_goster()
print("Tasit km durumu: ",tasit.km_durumu_gonder())

tasit._Tasit__tasit_sayisi_guncelle()
tasit._Tasit__tasit_miktari_goster()

araba.arabanin_durumunu_goster()