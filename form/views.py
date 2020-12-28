from django.shortcuts import render
from form.forms import MyForm
from .recommendation.recommend import Recommender

def responseform(request):
    form = MyForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            recommender = Recommender()
            initialData = {'n_participant':0,'years':0,'province_Adana':0,'province_Adıyaman':0,'province_Afyonkarahisar':0,'province_Aksaray':0,'province_Amasya':0,'province_Ankara':0,'province_Antalya':0,'province_Ardahan':0,'province_Artvin':0,'province_Aydın':0,'province_Ağrı':0,'province_Balıkesir':0,'province_Bartın':0,'province_Batman':0,'province_Bayburt':0,'province_Bilecik':0,'province_Bingöl':0,'province_Bitlis':0,'province_Bolu':0,'province_Burdur':0,'province_Bursa':0,'province_Denizli':0,'province_Diyarbakır':0,'province_Düzce':0,'province_Edirne':0,'province_Elazığ':0,'province_Erzincan':0,'province_Erzurum':0,'province_Eskişehir':0,'province_Gaziantep':0,'province_Giresun':0,'province_Gümüşhane':0,'province_Hakkâri':0,'province_Hatay':0,'province_Isparta':0,'province_Iğdır':0,'province_Kahramanmaraş':0,'province_Karabük':0,'province_Karaman':0,'province_Kars':0,'province_Kastamonu':0,'province_Kayseri':0,'province_Kilis':0,'province_Kocaeli':0,'province_Konya':0,'province_Kütahya':0,'province_Kırklareli':0,'province_Kırıkkale':0,'province_Kırşehir':0,'province_Malatya':0,'province_Manisa':0,'province_Mardin':0,'province_Mersin':0,'province_Muğla':0,'province_Muş':0,'province_Nevşehir':0,'province_Niğde':0,'province_Ordu':0,'province_Osmaniye':0,'province_Rize':0,'province_Sakarya':0,'province_Samsun':0,'province_Siirt':0,'province_Sinop':0,'province_Sivas':0,'province_Tekirdağ':0,'province_Tokat':0,'province_Trabzon':0,'province_Tunceli':0,'province_Uşak':0,'province_Van':0,'province_Yalova':0,'province_Yozgat':0,'province_Zonguldak':0,'province_Çanakkale':0,'province_Çankırı':0,'province_Çorum':0,'province_İstanbul':0,'province_İzmir':0,'province_Şanlıurfa':0,'province_Şırnak':0,'type_Eğlence':0,'type_Konferans':0,'type_Kongre':0,'type_Yarışma':0,'sector_Bilim':0,'sector_E-Spor':0,'sector_Ekonomi':0,'sector_Endüstri':0,'sector_Eğlence':0,'sector_Kariyer':0,'sector_Teknoloji':0,'sector_Tekstil':0,'sector_Yapı - Tasarım':0,'scope_Ülke':0,'scope_İl':0}
            province = "province_{0}".format(form.cleaned_data['City'])
            types = "type_{0}".format(form.cleaned_data['Type'])
            sector = "sector_{0}".format(form.cleaned_data['Sector'])
            scope = "scope_{0}".format(form.cleaned_data['Scope'])
            initialData['n_participant'] = int(form.cleaned_data['Participant'])
            initialData['years'] = int(form.cleaned_data['Year'])
            initialData[province] = 1
            initialData[types] = 1
            initialData[sector] = 1
            initialData[scope] = 1
            testData = list(initialData.values())
            recommends = recommender.recommend(testData)
            return render(request, 'index_base_layout.html', {'form':form,'recommends':recommends})

            
    return render(request, 'index_base_layout.html', {'form':form})