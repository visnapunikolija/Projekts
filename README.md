## Idejas ieradīšana

**Man bija uzdots uzdevums izveidot sistēmu, kas automatizēs kādu no manu ikdienas uzdevumiem. Es ilgu laiku domāju par ideju šim projektam. Tad mana izveidojas lieliska ideja, ko iedvesmoja nesenā situācija manā darbā.**

**Es strādāju viesnīcā ar kolektīvu apmēram 80 cilvēku. Mūsu vadība nolēma organizēt kopīgu Secret Santa pasākumu visos departamentos. Par to atbildīgu iecēla manu departamenta vadītāju, tāpēc es personīgi biju lieciniece šim procesam. Rezultāts neizdevās labi. Daži bija neapmierināti ar dāvanu budžetu, daži pat ne labi pazina personu, kuru bija jādāvina, daži nepiedalījās izlozē, lai izvilktu dāvanu saņēmēja vārdu, un daži nejauši izvilka pat divus vārdus. Beigās daudziem nepatika dāvanas, un kāds pat neko nesaņēma, un nebija zināms, kas bija vainīgs.**

**Tāpēc es nolēmu izveidot kodu, kas šogad varētu palīdzēt situācijā un nākamgad būtu noderīgs.**

## Sagatavošanās procesam
**Lai izveidotu šo kodu, es izmantoju izdomātas datu kopas. Atradu vietni ar nejaušiem vārdiem un nokopēju tur 100 vārdus (Vienkārši iedomāsimies, ka šajā uzņēmumā strādā 100 cilvēki no Latvijas ar ļoti ne latviskiem vārdiem). Tad otrā kolonnā sakārtoju tos pēc vārda, veidojot nejaušu izlozi. Pēc tam vietnē 220.lv pēc cenas kategorijas sakārtoju manuāli iekopēju katru preces ID Excel failā, ko vēlāk saglabāju kā CSV failu. Kad pienāca laiks manuāli izveidot 100 PDF darba algas izrakstus, sapratu, ka varētu izveidot kodu, lai atvieglotu šo procesu. Izmantojot Selenium bibliotēku, es atradu pirmo vietni, kas pamaniju, un izmantojot ciklu for, ieguvu 100 vēlamo algu izrakstes. Koda failu sauc salaryweb.py**

## Apraksts

**Secret Santa notiek pietiekami lielā uzņēmūma ar nosaukumu X. X strādā 100 darbinieki, tāpēc personīgi organizēt izlozi bija neiespējami, un vadība izlēma, ka katrais darbinieks iepriekš izvēlēsies 2 vēlamās dāvanas vietnē 220.lv, atšķirīgās cenu kategorijās, lai neatkarīgi no tā, kam nonāk, visi būtu apmierināti ar dāvanām. Konkrētais dāvanas izdevums būs atkarīgs no bruto algas.**

## Uzdevums

**X mani iecēla par kvalificētu programmētāju, lai es izveidotu kodu kas automatizēs Secret Santa procesu. Uzņēmums sniedza šādu informāciju:**

- Excel failu, kurā ir darbinieka vārds, kas dāvina dāvanu (pirmajā kolonnā), un darbinieka vārds, kurš saņem dāvanu (otrā kolonnā). Faila nosaukums ir "names.xlsx"
- CSV failu, kurā ir darbinieka vārds, dāvanas ID vērtībā no 30 līdz 50 eiro un dāvanas ID vērtībā no 60 līdz 90 eiro. Visi šie dati ir atdalīti ar komatu un atrodas attiecīgajā secībā. Faila nosaukums ir "gifts.csv"
- 100 PDF failus, kuros ir informācija par katra darbinieka decembra algu. Faili atrodas mapē ar nosaukumu "payslips"

**Mana uzdevuma būtība ir tāda, ka darbinieks ievada savu pilno vārdu terminālī un saņem informāciju par darbinieku, kam viņš dāvina dāvanu. Turklāt Google Chrome  automātiski tiek atvērts logs ar vietni 220.lv , kur dāvana jau ir ievietota pirkuma groze. Ja darbinieka decembra bruto alga ir mazāka par 1600 eiro, tad viņš dāvina dāvanu vērtībā no 30 līdz 50 eiro. Ja taču viņa alga ir lielāka par 1600 eiro, tad dāvana ir vērtībā no 60 līdz 90 eiro.**

## Python bibliotēkas

**Es izmantoju šādas bibliotēkas:**

1. selenium
  - Lai strādātu ar Google Chrome un turpmāk izmantot vietni 220.lv un vietni payslips.com
2. PyPDF2
  - Lai strādātu ar PDF failiem un būtu iespēja noteikt darbinieku algu
3. pathlib
  - Lai būtu iespējams iegūt algu Pdf failus no konkrētas mapes
4. pandas
  - Lai strādātu ar Excel failu
5. time
  - Lai vēlāk, strādājot ar Selenium bibliotēku, būtu iespējams aizkavēt procesu uz noteiktu laiku  
