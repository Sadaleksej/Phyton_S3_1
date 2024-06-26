from collections import Counter
import re

txt = '''Россия священная наша держава,
 Россия любимая наша страна. Могучая воля, 
 великая слава Твое достоянье на все времена!
  Славься, Отечество наше свободное, Братских народов
   союз вековой, Предками данная мудрость народная! 
   Славься, страна! Мы гордимся тобой! От южных морей
    до полярного края Раскинулись наши леса и поля. Одна 
    ты на свете! Одна ты такая Хранимая Богом родная земля! 
    Славься, Отечество наше свободное, Братских народов союз 
    вековой, Предками данная мудрость народная! Славься, страна! 
    Мы гордимся тобой! Широкий простор для мечты и для жизни 
    Грядущие нам открывают года. Нам силу дает наша верность 
    Отчизне. Так было, так есть и так будет всегда! Славься,
     Отечество наше свободное, Братских народов союз вековой, 
     Предками данная мудрость народная! Славься, страна! Мы гордимся тобой!'''


cnt = Counter(x for x in re.findall(r'[А-я\']{2,}', txt.lower()))
print("10 наиболее часто встречающихся слов: \n", cnt.most_common(10))