from django import forms


provinces = [
    ('','Seçiniz'),
    ('Adana','Adana'),
    ('Adıyaman','Adıyaman'),
    ('Afyonkarahisar','Afyonkarahisar'),
    ('Ağrı','Ağrı'),
    ('Aksaray','Aksaray'),
    ('Amasya','Amasya'),
    ('Ankara','Ankara'),
    ('Antalya','Antalya'),
    ('Ardahan','Ardahan'),
    ('Artvin','Artvin'),
    ('Aydın','Aydın'),
    ('Balıkesir','Balıkesir'),
    ('Bartın','Bartın'),
    ('Batman','Batman'),
    ('Bayburt','Bayburt'),
    ('Bilecik','Bilecik'),
    ('Bingöl','Bingöl'),
    ('Bitlis','Bitlis'),
    ('Bolu','Bolu'),
    ('Burdur','Burdur'),
    ('Bursa','Bursa'),
    ('Çanakkale','Çanakkale'),
    ('Çankırı','Çankırı'),
    ('Çorum','Çorum'),
    ('Denizli','Denizli'),
    ('Diyarbakır','Diyarbakır'),
    ('Düzce','Düzce'),
    ('Edirne','Edirne'),
    ('Elazığ','Elazığ'),
    ('Erzincan','Erzincan'),
    ('Erzurum','Erzurum'),
    ('Eskişehir','Eskişehir'),
    ('Gaziantep','Gaziantep'),
    ('Giresun','Giresun'),
    ('Gümüşhane','Gümüşhane'),
    ('Hakkâri','Hakkâri'),
    ('Hatay','Hatay'),
    ('Iğdır','Iğdır'),
    ('Isparta','Isparta'),
    ('İstanbul','İstanbul'),
    ('İzmir','İzmir'),
    ('Kahramanmaraş','Kahramanmaraş'),
    ('Karabük','Karabük'),
    ('Karaman','Karaman'),
    ('Kars','Kars'),
    ('Kastamonu','Kastamonu'),
    ('Kayseri','Kayseri'),
    ('Kilis','Kilis'),
    ('Kırıkkale','Kırıkkale'),
    ('Kırklareli','Kırklareli'),
    ('Kırşehir','Kırşehir'),
    ('Kocaeli','Kocaeli'),
    ('Konya','Konya'),
    ('Kütahya','Kütahya'),
    ('Malatya','Malatya'),
    ('Manisa','Manisa'),
    ('Mardin','Mardin'),
    ('Mersin','Mersin'),
    ('Muğla','Muğla'),
    ('Muş','Muş'),
    ('Nevşehir','Nevşehir'),
    ('Niğde','Niğde'),
    ('Ordu','Ordu'),
    ('Osmaniye','Osmaniye'),
    ('Rize','Rize'),
    ('Sakarya','Sakarya'),
    ('Samsun','Samsun'),
    ('Şanlıurfa','Şanlıurfa'),
    ('Siirt','Siirt'),
    ('Sinop','Sinop'),
    ('Sivas','Sivas'),
    ('Şırnak','Şırnak'),
    ('Tekirdağ','Tekirdağ'),
    ('Tokat','Tokat'),
    ('Trabzon','Trabzon'),
    ('Tunceli','Tunceli'),
    ('Uşak','Uşak'),
    ('Van','Van'),
    ('Yalova','Yalova'),
    ('Yozgat','Yozgat'),
    ('Zonguldak','Zonguldak')
]
types = [
    ('','Seçiniz'),
    ('Konferans','Konferans'),
    ('Yarışma','Yarışma'),
    ('Eğlence','Eğlence'),
    ('Kongre','Kongre')
]
sectors = [
    ('','Seçiniz'),
    ('Kariyer','Kariyer'),
    ('Yapı - Tasarım','Yapı - Tasarım'),
    ('Bilim','Bilim'),
    ('Teknoloji','Teknoloji'),
    ('Ekonomi','Ekonomi'),
    ('Endüstri','Endüstri'),
    ('Eğlence','Eğlence'),
    ('E-Spor','E-Spor'),
    ('Tekstil','Tekstil')
]
scopes = [
    ('','Seçiniz'),
    ('Ülke','Ülke'),
    ('İl','İl')
]

class MyForm(forms.Form):
    City = forms.ChoiceField(label="Şehir", choices=provinces)  
    Type  = forms.ChoiceField(label="Etkinlik Türü", choices=types)  
    Sector = forms.ChoiceField(label="Etkinlik Sektörü", choices=sectors)  
    Scope = forms.ChoiceField(label="Etkinlik Kapsamı", choices=scopes) 
    Participant = forms.IntegerField(label="Katılımcı Sayısı")   
    Year = forms.IntegerField(label="Etkinlik Kaç Yıldır Düzenleniyor?")  
    
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}
