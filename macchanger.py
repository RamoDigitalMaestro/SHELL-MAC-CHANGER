import subprocess 

# Yeni hedef Mac adresimizi Belirliyoruz
YeniMac = str(input("Yeni Mac Adresinizi giriniz ornek(00:11:22:33:44:55) : ")) 
# İnterface Adresimizi Belirtiyoruz
İnterface = input("İnterface Adresinizi giriniz: ")

def MacDegistirici(YeniMac,İnterface):
# İnternet Bağlantımızı kapatıyoruz    
    subprocess.call(["sudo","ifconfig",İnterface,"down"])
# Yeni Mac Adresimizi Belirtiyoruz     
    subprocess.call(["sudo","ifconfig",İnterface,"hw","ether",YeniMac])
# İnternet'e Tekrardan Bağlanıyoruz   
    subprocess.call(["sudo","ifconfig",İnterface,"up"]) 
    
# Mac adresimizi kontrol ediyoruz     
oncekimac = subprocess.check_output(["ifconfig"])
# Fonksiyonumuzu cağırıp mac değiştirme işlemini uyguluyoruz
MacDegistirici(YeniMac,İnterface)
# Tekrardan mac adresimizi Kontrol ediyoruz
yenimac = subprocess.check_output(["ifconfig"])

 
if oncekimac == yenimac:
    print("Mac adresi değiştirme işlemi başarısız oldu") 

else:
    print("Mac adresiniz başarılı bir şekilde değiştirildi Yeni Mac Adresiniz: ",YeniMac)  
    
    
