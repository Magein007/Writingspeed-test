import random
import time
import os

def laske_oikeat_sanat(kaikki, kirjoitetut):
    oikein = 0
    for sana in kirjoitetut:
        if sana in kaikki:
            oikein += 1
    return oikein

def laske_vaarat_sanat(kaikki, kirjoitetut):
    vaarin = 0
    for sana in kirjoitetut:
        if sana not in kaikki:
            vaarin += 1
    return vaarin

def tulosta_raportti(kaikki_sanat, kirjoitetut_sanat, kesto): #raportin tulostus
    oikeat_sanat = laske_oikeat_sanat(kaikki_sanat, kirjoitetut_sanat)    
    vaarat_sanat = laske_vaarat_sanat(kaikki_sanat, kirjoitetut_sanat)
    laske_merkit_minuutissa(annetut_sanat, kirjoituksen_kesto) #laskee kuinka nopeaa käyttäjä kirjoittaa
    laske_sanat_minuutissa(annetut_sanat, kirjoituksen_kesto)
    print('')
    print(f'Kirjoitit sanat ajassa {kirjoituksen_kesto} sekuntia')
    print(f'Kirjoitit oikein {oikeat_sanat}/{len(kirjoitetut_sanat)} sanaa')
    print(f'Kirjoitit vaarin {vaarat_sanat}/{len(kirjoitetut_sanat)} sanaa')
    print('')

def laske_merkit_minuutissa(kirjoitetut_sanat, kesto): #laskee kirjoitusnopeuden
    merkit = 0
    for sana in kirjoitetut_sanat:
        merkit += len(sana)
    merkkeja_minuutissa = merkit / (kesto / 60)
    print('Kirjoitusnoputesi oli',round(merkkeja_minuutissa, 2),'merkkiä minuutissa')

def laske_sanat_minuutissa(kirjoitetut_sanat, kesto):
    merkit = 0
    for sana in kirjoitetut_sanat:
        merkit += len(sana)
    sanoja_minuutissa = (merkit/5) / (kesto/60)
    print('Kirjoitit',round(sanoja_minuutissa, 0),'sanaa minuutissa')

####                             Pääohjelma alkaa                           ####

sanalista = ['imarrella', 'kohouma', 'sallivasti', 'julmettu', 'puolasto', 'villiruusu', 'paksunema', 'vaaputtaa', 'niinikuitu', 'kannustus', 'kesähuvila', 'kurjasti', 'kojootti', 'oikonoja', 'vihkimätön', 'keljusti', 'profetia', 'kiltsi', 'liehittely', 'pajunvitsa', 'tähtitorni', 'poikatukka', 'puolto', 'ehtoisa', 'murre', 'lähetysten', 'isäntäeliö', 'harmitella', 'neodyymi', 'flokki', 'painate', 'opastin', 'kiri', 'pörhössä', 'savuliha', 'uhrautuva', 'parfait', 'yrjötä', 'kintere', 'lausuma', 'uljaasti', 'yökylmä', 'passittaa', 'ruhjoutuma', 'saakelisti', 'pyssymies', 'syöttäjä', 'lämmitä', 'läntätä', 'kynämies', 'rasvoittaa', 'vaihtaa', 'laadukkuus', 'räsähtely', 'iljanko', 'sakkokorko', 'harmoninen', 'amanuenssi', 'helkatti', 'vihkivesi', 'sukkamekko', 'isäukko', 'yrmeästi', 'orkesteri', 'naamioida', 'raksua', 'tasajalkaa', 'pyhänseutu', 'painoasu', 'tiehyetön', 'neofasismi', 'satama', 'haavainen', 'kurkkulava', 'painotyö', 'koulupäivä', 'tiikkinen', 'syanidi', 'läänitys', 'tarjoilla', 'rahka', 'kupristaa', 'puristi', 'murhata', 'kulti', 'joka ainoa', 'epäkäs', 'unhottaa', 'kuunsirppi', 'reunempaa', 'siansaparo', 'lähemmin', 'rabies', 'nekrologi', 'aulius', 'tuijottaa', 'yliö', 'litrahinta', 'pehku', 'rupinen', 'suffiksi', 'tavallinen', 'puoliryhmä', 'lautamies', 'sanoutua', 'köllikkä', 'haastaa', 'vetoapu', 'pankkiauto', 'pelipaita', 'sivuluisu', 'enchilada', 'yksiin', 'palokuja', 'vähemmän', 'hälyttyä', 'tippapullo', 'orastua', 'embryologi', 'suojatyö', 'painiote', 'rinki', 'salamenot', 'sassiin', 'adoptio', 'suurus', 'metsämies', 'tirahtaa', 'sotija', 'rämeä', 'tyräkki', 'mulkaista', 'vaikertaa', 'rääpiäiset', 'tähdennys', 'rahanarvo', 'norkko', 'huonontua', 'kärkevyys', 'rengassumu', 'suunnaton', 'paperilaji', 'kokosivu', 'emikasvi', 'kähvellys', 'rihla', 'sotaakäyvä', 'kajaus', 'rubato', 'muovituote', 'napista', 'fuusioida', 'anomalia', 'tyhmentää', 'kauris', 'oppiaine', 'ukkoetana', 'kerätä', 'heimoside', 'pakkorako', 'jeremiadi', 'taimmaksi', 'rantaloma', 'silmukka', 'uinahdus', 'vilpitön', 'tuoreutua', 'sähkökoje', 'kihlapari', 'loinen', 'silkkinen', 'kuorettuma', 'aine', 'emäntäväki', 'kierreura', 'junarata', 'pääteasema', 'bakteeri', 'juoksettaa', 'jylhistyä', 'ankkuroida', 'juomahimo', 'marssija', 'tuoremehu', 'paljous', 'etsijä', 'lentävä', 'vuorottelu', 'vilkunta', 'kuuntelu', 'köysinippu', 'tilinumero', 'koepaperi', 'piippumies', 'moiskahdus', 'moittia', 'huohottaa', 'pyyheliina', 'hymistely', 'myräkkä', 'vankistua', 'vinous', 'rotanraato', 'kengittää', 'kotiin', 'murtautua', 'hankasilmu', 'kiihoke', 'viriili', 'kuultava', 'siivu', 'mitalisija', 'tietoisku', 'tapaluokka', 'kauppaetu', 'tournedos', 'tuhantisen', 'päälaenluu', 'rullautua', 'maanpinta', 'domino', 'hinata', 'sivuhuone', 'pienvesi', 'kirkas', 'alahuone', 'syönnös', 'rinnastua', 'lamaan', 'kalsea', 'hartsi', 'jäätelö', 'hajottaa', 'paksunema', 'kaste', 'mäkitupa', 'äkkipäätä', 'ruokis', 'höystö', 'remahtaa', 'roikua', 'porista', 'köysi', 'ukkovarvas', 'roskakori', 'sademetsä', 'mormyska', 'lämpötila', 'filamentti', 'kivitasku', 'päätäi', 'tyhjiin', 'nauhakenkä', 'ritari', 'estimointi', 'verorästi', 'pusia', 'alkukesä', 'lainaamo', 'veroinen', 'arkaainen', 'vibrato', 'kuiskaaja', 'ruutukaava', 'monotonia', 'pinnaus', 'akkavalta', 'varjostin', 'ahtautua', 'holhooja', 'maantiede', 'kasi', 'hara', 'täynnä', 'niukahtaa', 'löhöily', 'avec', 'puupala', 'nettotulo', 'puusolu', 'nelinpeli', 'jyvä', 'kauraryyni', 'neuralgia', 'kovalle', 'piilokas', 'läpinäkyvä', 'roskaantua', 'viivytellä', 'osatavoite', 'perussana', 'rytmikaava', 'työsyvyys', 'vastatuuli', 'nuotata', 'jäänlähtö', 'kalvia', 'valssaamo', 'saattoväki', 'estradi', 'puolata', 'kiintiöidä', 'vetoinen', 'tyrä', 'pitoteippi', 'törrötys', 'uuninpelti', 'jauhennin', 'teräsköysi', 'tukka', 'raksaa', 'mummeli', 'kovettuma', 'väristä', 'rinta', 'tuikkia', 'diivata', 'armonaika', 'ruokajono', 'narskua', 'tukkamuoti', 'kopautella', 'näverrin', 'rinkka', 'rokata', 'ruuna', 'makeutus', 'kuiskinta', 'tukkeentua', 'perillä', 'lakikirja', 'syssyyn', 'ulkoväylä', 'hajottamo', 'jukuripää', 'brokadi', 'nykytaide', 'stuertti', 'talkita', 'lasiesine', 'liskolintu', 'vihoissa', 'iskias', 'koivunoksa', 'alppiseutu', 'kantohihna', 'kakkara', 'laskeutuma', 'lukuarvo', 'yläaste', 'tylpistys', 'hautuumaa', 'tykkänään', 'turha', 'mielityö', 'railolossi', 'sivumpaa', 'tontittaa', 'porakone', 'paikkuu', 'porrastus', 'laimistua', 'artefakti', 'kehotella', 'avokallio', 'sohlata', 'kymmenes', 'nollapiste', 'mitenkään', 'artroosi', 'kotoisa', 'lähettiläs', 'hematiitti', 'vastakarva', 'raki', 'yksityinen', 'ohimolohko', 'lupalappu', 'poli', 'työrupeama', 'armagnac', 'selkeentyä', 'tauditon', 'kriisiapu', 'karja', 'hipsutella', 'ikämies', 'etelätuuli', 'suorakaide', 'kaduttaa', 'kielikorva', 'korvata', 'viljalaji', 'värimalli', 'kalatuote', 'öljylamppu', 'tinktuura', 'palonalku', 'edeltää', 'keidas', 'rompsu', 'kellonaika', 'tyydytys', 'cameorooli', 'ohjehinta', 'niemeke', 'tällään', 'rousku', 'suipistaa', 'mesi', 'pötsi', 'kokemus', 'tytärpuoli', 'määräpäivä', 'simsetti', 'apupisto', 'navigointi', 'myyntikate', 'helteinen', 'paloittelu', 'maatyömies', 'mätky', 'jyrrätä', 'juustopala', 'mesikaste', 'lakikirja', 'niskasärky', 'tuku', 'anagrammi', 'jakkupuku', 'myöstää', 'kalahissi', 'venonen', 'humala', 'karkottaa', 'vakava', 'letkautus', 'yhtenevyys', 'sivukautta', 'kanisteri', 'ilkeillä', 'sepittäjä', 'aikalainen', 'muusikko', 'sisäpaisti', 'matkaradio', 'elämänpuu', 'muhina', 'hybridi', 'karmiva', 'laiska', 'linnake', 'kaljaasi', 'maanmies', 'riimukivi', 'sivuseinä', 'kellastua', 'puksuttaa', 'ryminä', 'keskeltä', 'urputus', 'lausunto', 'pyh', 'chanson', 'desigramma', 'valmistelu', 'pippalot', 'pussirotta', 'mutkistaa', 'parasiitti', 'optimi', 'maitolava', 'tuiskia', 'vertyä', 'oppikirja', 'graafinen', 'napakasti', 'jasmike', 'rimsu', 'lomaosake', 'sirkushuvi', 'rannekoru', 'ymmälleen', 'lyyrisyys', 'munuainen', 'pomomies', 'kentauri', 'trokari', 'yölämmitys', 'vastailla', 'erota', 'puhuja', 'voipua', 'sirriin', 'saman tien', 'jota', 'raspi', 'valonarka', 'väistö', 'varikko', 'armada']
listan_pituus = len(sanalista)

kysytyt_sanat = [] #sanat joita ohjelma on kysynyt käyttäjältä
annetut_sanat = [] #käyttäjän syöttämien sanojen lista

kirjoitetut_sanat = 0

####                              Käyttöliittymä                            ####

while True:
    os.system('clear')

    print('Tämä ohjelma testaa kirjoitusnopeutesi.')
    print('')
    print('Ohjelma antaa sinulle halluamasi määrän satunnaisia sanoja kirjoitettavaksi\njoka sinun tulee kirjoittaa ja hyväksyä Enterillä')
    print('')
    print('Testin jälkeen ohjelma antaa kirjoitusnopeutesi yksiköissä\nmerkkiä / min sekä sanaa / min. Yksi sana vastaa viittä (5) merkkiä.')
    print('')

    n = input('Kuinka monta sanaa haluat kirjoittaa? ') #kirjoitettavien sanojen määrä
    if n.isdigit():
        n = int(n)
        if n > 0 and n <= 20:
            ajanhetki_1 = time.time() #ottaa muistiin kellonajan ohjelman käynnistyessä

            while True:
                os.system('clear') #tyhjentää input-ruudun sanan jälkeen
                
                for i in range(1): #tulostaa satunnaisen sanan listasta
                    valittu_sana = (random.choice(sanalista))
                    kysytyt_sanat.append(valittu_sana)
                    print(f'{valittu_sana}')

                x = input('<-> ')
                annetut_sanat.append(x) #lisää kirjoitetut sanat toiseen listaan
                kirjoitetut_sanat += 1

                if kirjoitetut_sanat >= n and n > 0:
                    ajanhetki_2 = time.time() #ottaa muistiin kellonajan ohjelman loppuessa
                    break
        else:
            os.system('clear')
            print('Anna luku 1-20 välillä')
            time.sleep(1)
            continue
    elif n == 0:
            os.system('clear')
            print('virheellinen syöttö')
            time.sleep(1)
            continue
    else:
        os.system('clear')
        print('virheellinen syöttö, anna positiivinen luku')
        time.sleep(1)
        continue

# \/ Ajan laskeminen \/ #

    kirjoitusaika = ajanhetki_2 - ajanhetki_1
    kirjoituksen_kesto = round(kirjoitusaika, 2) #laskee kirjoittamiseen kuluneen ajan

# \/ Raportin tulostaminen luettavalla formaatilla \/ #

    os.system('clear')
    print('    Kysytyt sanat:',kysytyt_sanat)
    print('Kirjoitetut sanat:',annetut_sanat)
    print('')
    tulosta_raportti(annetut_sanat, kysytyt_sanat, kirjoituksen_kesto)
    print('')

    while True: #Ohjelman jatkaminen
        vastaus = input('Yritä uudestaan? (kyllä / ei): ')
        if vastaus in ('kyllä','ei'):
            break
        print('virheellinen syöttö.')

    if vastaus == 'kyllä':
        del kysytyt_sanat[:] #tyhjentää sanat joita ohjelma on kysynyt käyttäjältä
        del annetut_sanat[:] #tyhjentää käyttäjän syöttämien sanojen listan
        kirjoitetut_sanat = 0
        continue
    else:
        os.system('clear')
        print('Hei hei')
        time.sleep(1.5)
        os.system('clear')
        break
