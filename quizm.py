suallar=[
    {
    "sual":"Elektrik yükü miqdarı ilə maqnit selini əlaqələndirən element hansıdır?",
    "cavablar":[
        "Müqavimət",
        "Tutum",
        "İnduktivlik",
        "Memristor"
    ],
    "düzgünCavab":"D"
},
    {
    "sual":"Müqavimət, tutum, induktivlik və memristor aşağıdakılardan hansını xarakterizə edir?",
    "cavablar":[
        "Dəyişən cərəyanı",
        "Elektrik dövrələrini",
        "Sabit cərəyanı",
        "Komputer sxemlərini"
    ],
    "düzgünCavab":"B"
},
    
    {
    "sual":"Dəyişən cərəyan transformatorunu sabit cərəyana qoşsaq nə baş verər?",
    "cavablar":[
        "Transformator işləyər",
        "Transformator işləməz",
        "Transformatorun sarğısı yanar",
        "Sabit cərəyan dəyişən cərəyana çevrilər"
    ],
    "düzgünCavab":"C"
},
     
     {
    "sual":"Aşağıdakılardan hansı süzgəclərin tezliklərinə görə növlərinə aiddir?",
    "cavablar":[
        "Zolaq süzgəcləri",
        "K tipli süzgəclər",
        "M tipli süzgəclər",
        "Reaktiv süzgəclər"
    ],
    "düzgünCavab":"A"
},
         
]

umumibal=0
sualnomresi=1
for sual in suallar:
    pro=f"""
    {sualnomresi}. {sual["sual"]}
        A) {sual["cavablar"][0]}
        B) {sual["cavablar"][1]}
        C) {sual["cavablar"][2]}
        D) {sual["cavablar"][3]}
    """

    print(pro)
    cavab=input("Cavabınızı daxil edin : ")
    if cavab==sual["düzgünCavab"]:
        umumibal+=10
    sualnomresi+=1
    
print(f'Yoxlama bitdi, sizin ümumi balınız {umumibal}-dır')

