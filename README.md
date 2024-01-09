##Idejas ieradīšana

**Man bija uzdots uzdevums izveidot sistēmu, kas automatizēs kādu no manu ikdienas uzdevumiem. Es ilgu laiku domāju par ideju šim projektam. Tad mana izveidojas lieliska ideja, ko iedvesmoja nesenā situācija manā darbā.**
**Es strādāju viesnīcā ar kolektīvu apmēram 80 cilvēku. Mūsu vadība nolēma organizēt kopīgu Secret Santa pasākumu visos departamentos. Par to atbildīgu iecēla manu departamenta vadītāju, tāpēc es personīgi biju lieciniece šim procesam. Rezultāts neizdevās labi. Daži bija neapmierināti ar dāvanu budžetu, daži pat ne labi pazina personu, kuru bija jādāvina, daži nepiedalījās izlozē, lai izvilktu dāvanu saņēmēja vārdu, un daži nejauši izvilka pat divus vārdus. Beigās daudziem nepatika dāvanas, un kāds pat neko nesaņēma, un nebija zināms, kas bija vainīgs.**
**Tāpēc es nolēmu izveidot kodu, kas šogad varētu palīdzēt situācijā un nākamgad būtu noderīgs.**
#Sagatavošanās procesam
**Lai izveidotu šo kodu, es izmantoju izdomātas datu kopas. Atradu vietni ar nejaušiem vārdiem un nokopēju tur 100 vārdus. Tad otrā kolonnā sakārtoju tos pēc vārda, veidojot nejaušu izlozi. Pēc tam vietnē 220.lv pēc cenas kategorijas sakārtoju manuāli iekopēju katru preces ID Excel failā, ko vēlāk saglabāju kā CSV failu. Kad pienāca laiks manuāli izveidot 100 PDF darba algas izrakstus, sapratu, ka varētu izveidot kodu, lai atvieglotu šo procesu. Izmantojot Selenium bibliotēku, es atradu pirmo vietni, kas pamaniju, un izmantojot ciklu for, ieguvu 100 vēlamo algu izrakstes. Koda failu sauc salaryweb.py**
#Apraksts
**Secret Santa notiek lielā korporācijā ar nosaukumu X. X strādā 100 darbinieki, tāpēc personīgi organizēt izlozi bija neiespējami, un vadība izlēma, ka katrais darbinieks iepriekš izvēlēsies 2 vēlamās dāvanas vietnē 220.lv, atšķirīgās cenu kategorijās, lai neatkarīgi no tā, kam nonāk, visi būtu apmierināti ar dāvanām. Konkrētais dāvanas izdevums būs atkarīgs no bruto algas.**
#Uzdevums
**X mani iecēla par kvalificētu programmētāju, lai es izveidotu kodu kas automatizēs Secret Santa procesu. Uzņēmums sniedza šādu informāciju:**
