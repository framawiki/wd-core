#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  python pwb.py wd/wikinews
#
#
translationsOccupations = {
		'~ algae':{'ar':'~ الطحالب'},
		'~ amphibians':{'ar':'~ البرمائيات'},
		'~ annelid':{'ar':'~ الحلقيات'},
		'~ arthropods':{'ar':'~ المفصليات'},
		'~ brachiopods':{'ar':'~ ذوات القوائم الذراعية'},
		'~ bryozoans':{'ar':'~ المرجانيات'},
		'~ chordates':{'ar':'~ الحبليات'},
		'~ cnidarians':{'ar':'~ القراصات'},
		'~ crustaceans':{'ar':'~ القشريات'},
		'~ ctenophore':{'ar':'~ الممشطيات'},
		'~ echinoderms':{'ar':'~ الشوكيات'},
		'~ entoprocts':{'ar':'~ داخليات الشرج'},
		'~ fungus':{'ar':'~ الفطريات'},
		'~ gastrotrichs':{'ar':'~ شعريات البطن'},
		'~ insects':{'ar':'~ الحشرات'},
		'~ mammals':{'ar':'~ الثدييات'},
		'~ molluscs':{'ar':'~ الرخويات'},
		'~ myriapods':{'ar':'~ كثيرات الأرجل'},
		'~ plants':{'ar':'~ النباتات'},
		'~ prokaryotes':{'ar':'~ بدائيات النوى'},
		'~ reptiles':{'ar':'~ الزواحف'},
		'~ rotifers':{'ar':'~ الدوارات'},
		'~ sea spiders':{'ar':'~ العناكب البحرية'},
		'~ sponges':{'ar':'~ الإسفنجيات'},
		'~ trilobites':{'ar':'~ ثلاثية الفصوص'},
		'~ virus':{'ar':'~ الفيروسات'},
		'~ waterbears':{'ar':'~ دب الماء'},
		'~ worms':{'ar':'~ الديدان'},
    }
	
placesTable={
   "Q5113":{ "ar": "الطيور","en": "birds" },
   "Q1358":{ "ar": "عنكبيات","en": "Arachnida" },
   "Q152":{ "ar": "الأسماك","en": "fishes" },
   "Q10908":{ "ar": "البرمائيات","en": "amphibia" },
   "Q19436":{ "ar": "عريضات الأجنحة","en": "Eurypterid" },
   "Q193006":{ "ar": "قليلات الأشواك","en": "Oligochaeta" },
   "Q831482":{ "ar": "حزازيات حقيقية","en": "Bryopsida" },
   "Q127282":{ "ar": "شعاعيات الزعانف","en": "Actinopterygii" },
   "Q20635347":{ "ar": "ملتوياوات","en": "Spirochaetia" },
   "Q1349847":{ "ar": "سحناوات","en": "Thermomicrobia" },
   "Q132763":{ "ar": "سوادانية","en": "Ustilaginomycetes" },
   "Q136846":{ "ar": "زملولانية","en": "Exobasidiomycetes" },
   "Q10431061":{ "ar": "أروميانية","en": "Blastocladiomycetes" },
   "Q74083":{ "ar": "الأسماك المدرعة","en": "Ostracoderm" },
   "Q188360":{ "ar": "غلصميات الأرجل","en": "Branchiopoda" },
   "Q1069627":{ "ar": "سكيرانية","en": "Saccharomycetes" },
   "Q146300":{ "ar": "أنبوبيات","en": "Tubulinea" },
   "Q135200":{ "ar": "مخندقانية","en": "Taphrinomycetes" },
   "Q1135978":{ "ar": "مستحراوات مكورة","en": "Thermococci" },
   "Q244147":{ "ar": "مؤتلفات","en": "Symphyla" },
   "Q212798":{ "ar": "مهتزات","en": "Turbellaria" },
   "Q133571":{ "ar": "لقنورانية","en": "Lecanoromycetes" },
   "Q132159":{ "ar": "درينانية","en": "Dothideomycetes" },
   "Q2563582":{ "ar": "متكيسة رئوية","en": "Pneumocystidomycetes" },
   "Q17157":{ "ar": "سيسيرنينتيات","en": "Secernentea" },
   "Q25349":{ "ar": "نجم البحر","en": "starfish" },
   "Q25368":{ "ar": "ذوات الصدفتين","en": "Bivalvia" },
   "Q1051432":{ "ar": "ميثاناوات جرثومية","en": "Methanomicrobia" },
   "Q275657":{ "ar": "مخاطيات الأبواغ","en": "Myxosporea" },
   "Q10584811":{ "ar": "بويغيات مكروية","en": "Microsporea" },
   "Q25371":{ "ar": "أسماك غضروفية","en": "Chondrichthyes" },
   "Q15129663":{ "ar": "أعراف قرصية","en": "Cristidiscoidia" },
   "Q510333":{ "ar": "بيركولوزوا","en": "Heterolobosea" },
   "Q1149748":{ "ar": "حزازيات ذئبية","en": "Lycopodiopsida" },
   "Q221563":{ "ar": "ثنائيات الذنب","en": "Diplura" },
   "Q132809":{ "ar": "مطثيات","en": "Clostridia" },
   "Q4867740":{ "ar": "بطنيات القدم","en": "Gastropoda" },
   "Q1422487":{ "ar": "حزازيات سبخية","en": "Sphagnopsida" },
   "Q589697":{ "ar": "دودة البلوط","en": "Enteropneusta" },
   "Q306579":{ "ar": "متقلبات ألفا","en": "Alphaproteobacteria" },
   "Q5605610":{ "ar": "سيكادانية","en": "Cycadopsida" },
   "Q83483":{ "ar": "قنفذ البحر","en": "sea urchin" },
   "Q425920":{ "ar": "طفيليات دموية حيوانية","en": "Haematozoa" },
   "Q131796":{ "ar": "رخصيات","en": "Mollicutes" },
   "Q273179":{ "ar": "مكعبيات","en": "Box jellyfish" },
   "Q194257":{ "ar": "صفيحية الخياشيم الغضروفية","en": "Elasmobranchii" },
   "Q8316":{ "ar": "ثنائيات الفلقة","en": "Dicotyledones" },
   "Q276412":{ "ar": "صدفيات","en": "Ostracoda" },
   "Q3178797":{ "ar": "مخروطانيات","en": "Conoidasida" },
   "Q1953103":{ "ar": "مستحراوات متقلبة","en": "Thermoprotei" },
   "Q160830":{ "ar": "لحميات الزعانف","en": "Sarcopterygii" },
   "Q943568":{ "ar": "عتيقاوات كروية","en": "Archaeoglobi" },
   "Q136674":{ "ar": "متقلبات بيتا","en": "Betaproteobacteria" },
   "Q127470":{ "ar": "خيار البحر","en": "sea cucumber" },
   "Q610887":{ "ar": "ثاليات","en": "Thaliacea" },
   "Q128257":{ "ar": "رأسيات القدم","en": "Cephalopoda" },
   "Q132649":{ "ar": "رأسيات الدرقة","en": "Cephalocarida" },
   "Q188549":{ "ar": "جلكانيات","en": "Hyperoartia" },
   "Q190090":{ "ar": "كيسيات","en": "Ascidiacea" },
   "Q12207651":{ "ar": "حزازيات قرناء","en": "Anthocerotopsida" },
   "Q28524":{ "ar": "زهريات شعاعية","en": "Anthozoa" },
   "Q271631":{ "ar": "أوليات الذنب","en": "Protura" },
   "Q43447":{ "ar": "أم أربعة وأربعين","en": "Chilopoda" },
   "Q851400":{ "ar": "سيستويديات","en": "Cystoids" },
   "Q6074541":{ "ar": "فطريات طحلبية","en": "Phycomycetes" },
   "Q207547":{ "ar": "مثقوبات","en": "Trematode" },
   "Q10811":{ "ar": "زواحف","en": "reptile" },
   "Q3730841":{ "ar": "عصوانيات","en": "Bacteroidia" },
   "Q188906":{ "ar": "عديدة الأصداف","en": "chiton" },
   "Q223597":{ "ar": "طلائعيات بيضية","en": "Oomycetes" },
   "Q586245":{ "ar": "مخروطيات الأسنان","en": "Conodont" },
   "Q133551":{ "ar": "ملاسانية","en": "Leotiomycetes" },
   "Q132609":{ "ar": "أشنيات خضراء","en": "Chlorophyceae" },
   "Q132180":{ "ar": "عوفنيات","en": "Eurotiomycetes" },
   "Q22933896":{ "ar": "ميدوزات فنجانية","en": "Scyphomedusae" },
   "Q162678":{ "ar": "دياتوم","en": "Diatomea" },
   "Q1566901":{ "ar": "بلاستويديات","en": "Blastoid" },
   "Q136797":{ "ar": "متقلبات إيبسيلونية","en": "Epsilonproteobacteria" },
   "Q19106":{ "ar": "عنكبوت البحر","en": "Pycnogonida" },
   "Q811147":{ "ar": "كرات نافحة","en": "Gasteroid fungi" },
   "Q134668":{ "ar": "متقلبات غاما","en": "Gammaproteobacteria" },
   "Q138088":{ "ar": "حلمية الأسنان","en": "Thelodonti" },
   "Q3452046":{ "ar": "جبائل","en": "Sarcodina" },
   "Q10596701":{ "ar": "سويطيانية","en": "Neocallimastigomycetes" },
   "Q133607":{ "ar": "سوردارانية","en": "Sordariomycetes" },
   "Q189069":{ "ar": "مندمجات الأقواس","en": "synapsid" },
   "Q159715":{ "ar": "ديدان شريطية","en": "Cestoda" },
   "Q240433":{ "ar": "سوطيات","en": "Mastigophora" },
   "Q1329304":{ "ar": "صنوبرانية","en": "Pinopsida" },
   "Q488032":{ "ar": "مخفيات النبت","en": "Cryptophyceae" },
   "Q1763065":{ "ar": "طحالب ذهبية","en": "Chrysophyceae" },
   "Q132016":{ "ar": "أشنيات أولفانية","en": "Ulvophyceae" },
   "Q17156":{ "ar": "لافصيميات","en": "Adenophorea" },
   "Q209924":{ "ar": "إسفنجيات جيرية","en": "calcareous sponge" },
   "Q1390":{ "ar": "حشرة","en": "insects" },
   "Q190701":{ "ar": "قافزات الذيل","en": "Springtail" },
   "Q7377":{ "ar": "ثدييات","en": "mammal" },
   "Q3329480":{ "ar": "متقلبات زيتا","en": "Zetaproteobacteria" },
   "Q19430":{ "ar": "سيفيات الذيل","en": "Xiphosura" },
   "Q1137709":{ "ar": "أصيصيانية","en": "Chytridiomycetes" },
   "Q12673556":{ "ar": "بكتيريا ملتوية","en": "Spirochaetes" },
   "Q132662":{ "ar": "فكيات الأرجل","en": "Maxillopoda" },
   "Q332403":{ "ar": "جرابتوليت","en": "Graptolithinia" },
   "Q272388":{ "ar": "فنجانيات","en": "Scyphozoa" },
   "Q182978":{ "ar": "لينات الدرقة","en": "Malacostraca" },
   "Q1011212":{ "ar": "جنتوانية","en": "Gnetopsida" },
   "Q134677":{ "ar": "سراخس كنباثية","en": "Equisetopsida" },
   "Q149128":{ "ar": "عصيات","en": "Bacilli" },
   "Q13389544":{ "ar": "كببيانية","en": "Glomeromycetes" },
   "Q623286":{ "ar": "داخليات الفك","en": "Entognatha" },
   "Q15129670":{ "ar": "عرفيات قرصية","en": "Cristidiscoidea" },
   "Q20388475":{ "ar": "بفلوفيانية","en": "Pavlovophyceae" },
   "Q843232":{ "ar": "فنجانيانية","en": "Pezizomycetes" },
   "Q307535":{ "ar": "متقلبات دلتا","en": "Deltaproteobacteria" },
   "Q167367":{ "ar": "ألفية الأرجل","en": "Diplopoda" },
   "Q648056":{ "ar": "فطريات ناقصة","en": "Fungi imperfecti" },
   "Q131630":{ "ar": "ذوات منشأ الحركة","en": "Kinetoplastea" },
   "Q21447558":{ "ar": "بويغيات متشنكوفيلية","en": "Metchnikovellea" },
   "Q28805588":{ "ar": "عفنانية","en": "Mucoromycetes" },
   "Q642852":{ "ar": "حزازيات يشعورية","en": "Polytrichopsida" },
   "Q19962619":{ "ar": "زرقاويات","en": "Glaucocystophyceae" },
   "Q18952":{ "ar": "كثيرات الأشعار","en": "Polychaeta" },
   "Q132006":{ "ar": "شقرانانية","en": "Pucciniomycetes" },
   "Q839350":{ "ar": "سرجيات","en": "Clitellata" },
   "Q1151744":{ "ar": "طحالب مترابطة","en": "Zygnematophyceae" },
   "Q184573":{ "ar": "طحالب بنية","en": "Phaeophyceae" },
   "Q12967693":{ "ar": "سراخس ماراتية","en": "Marattiopsida" },
   "Q1096274":{ "ar": "حزازيات إسويطية","en": "Isoetopsida" },
   "Q147868":{ "ar": "مرشانتاناوت","en": "Marchantiopsida" },
   "Q373615":{ "ar": "سراخس رقيقة المباغ","en": "leptosporangiate fern" },
   "Q11937877":{ "ar": "قشريات متعددة","en": "Multicrustacea" },
   "Q1054206":{ "ar": "ملحاوات عصوية","en": "Halobacteria" },
   "Q238314":{ "ar": "أصداف نابية","en": "Scaphopoda" },
   "Q28960":{ "ar": "يرقانيات","en": "Appendicularia" },
   "Q21025810":{ "ar": "أشنيات خضراء متشجرة","en": "Chlorodendrophyceae" },
   "Q490800":{ "ar": "متشعبات الأرجل","en": "Remipedia" },
   "Q27720":{ "ar": "غاريقونانية","en": "Agaricomycetes" },
   "Q867927":{ "ar": "ميثاناوات نارية","en": "Methanopyri" },
   "Q865046":{ "ar": "فصيات","en": "Lobosea" },
   "Q181989":{ "ar": "أبابيات","en": "Hydrozoa" },
   "Q1208690":{ "ar": "طحالب كارية","en": "Charophyceae" },

    }