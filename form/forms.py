from django import forms

class MyForm(forms.Form):
    City = forms.CharField(label="Şehir", max_length=100)  
    Type  = forms.CharField(label="Etkinlik Türü", max_length = 100)  
    Sector = forms.CharField(label="Etkinlik Sektörü", max_length = 100)  
    Scope = forms.CharField(label="Etkinlik Kapsamı", max_length = 100) 
    Participant = forms.CharField(label="Katılımcı Sayısı", max_length = 100)   
    Year = forms.CharField(label="Etkinlik Kaç Yıldır Düzenleniyor?", max_length = 100)  
