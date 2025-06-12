# PPY Projekt-System zarz±dzania ksi±¿kami
Nastêpuj±cy projekt sk³ada siê z kilku modu³ów, zaleca siê implementacjê ka¿dego z modu³ów
po kolei, a nastêpnie ³±czenie ich w jedn± ca³o¶æ.
Za³o¿enie projektu:
Stworzenie automatycznego systemu do ³adowania/wzbogacania oraz udostêpniania danych
dotycz±cych ksi±¿ek wydanych przez Penguin Random House
Modu³ 1 ? Pozyskanie danych
Projekt powinien oczekiwaæ na plik (xlsx lub csv) w okre¶lonej przez siebie lokalizacji (folder).
Wszystkie oczekiwane nazwy plików (wzory okre¶lone regexem) powinny zostaæ zawarte w pliku
konfiguracyjnym: config.json.
Je¿eli plik który pojawi siê w folderze nie zostanie rozpoznany, nale¿y go usun±æ.
Po rozpoznaniu pliku (przyk³adowe pliki wraz ze struktur± s± za³±czone w assignmencie)
powinien zostaæ za³adowany do skryptu przy u¿yciu biblioteki pandas.
Przyk³adowy plik wej¶ciowy oraz przyk³adowy plik konfiguracyjny dodany w assignmencie.
Modu³ 2 ? Transformacje (pandas)
Na potrzeby tego projektu nale¿y wykonaæ nastêpuj±ce transformacje:
-usuniecie kolumn zawieraj±cych ?internal? w nazwie.
-Przeformatowanie imion i nazwisk autorów, aby zawsze zaczyna³y siê z du¿ej litery
-usuniêcie rekordów od wydawnictw innych ni¿ Penguin Random House lub Random House, za
wyj±tkiem ksi±¿ek Stephena Kinga
-usuniêcie rekordów pustych
-*usuniêcie rekordów posiadaj±cych znaki chiñskie
-*usuniêcie potencjalnych duplikatów
Modu³ 3 ? Pobranie dodatkowych danych (requests):
Przy u¿yciu otwartego API Penguin Random House (penguinrandomhouse.biz - Penguin Random
House Rest Services API), nale¿y do ka¿dej ksi±¿ki do³±czyæ (je¿eli s± dostêpne) nastêpuj±ce
informacje:
-dywizja (która wyda³a ksi±¿kê)
-bio autora
-sugerowany przedzia³ wiekowy
Modu³ 4 ? zapisywanie danych i odczytywanie ? persistance
Ponowne uruchomienie skryptu powinno automatycznie odzyskiwaæ dane uzyskane w
poprzednim dzia³aniu. Mo¿na to zrealizowaæ przez serializacjê (pickle) lub przechowywanie
danych w JSON.
Zadania dodatkowe ? nie wymagane:
-U¿yj dodatkowego API (np. API do uzyskania informacji o twórczo¶ci mistrza grozy
https://stephen-king-api.onrender.com/), do uzyskania wiekszej ilo¶ci informacji o wybranych
przez siebie ksi±¿kach
-Dodaj prost± warstwê graficzn± po stronie przegl±darki
-
Uwagi ogólne:
-Struktura plików i folderów jest zale¿na od twórcy kodu.
-Rozwi±zania nie opisane w powy¿szym opisie zostawiam do w³asnej implementacji.
-Kod powinien byæ czysty i przejrzysty - nale¿y dodawaæ typy zmiennych, zwracany typ
metod oraz stosowaæ siê do ogólnie przyjêtych zasad dobrego kodu.
-Warto dodaæ dodatkowy log, aby ¶ledziæ dzia³anie programu nie tylko w konsoli
-Zadania oznaczone jako * s± dodatkowe.
-Aby unikn±æ hardcodeowania danych, warto skorzystaæ z config.json do przechowania
statycznych danych jak np. Url API.
-Kod nale¿y napisaæ samodzielnie, stwierdzenie niesamodzielno¶ci pracy mo¿e skutkowaæ
uzyskaniem 0 punktów.
-Zadania z ?*? nie s± obowi±zkowe.
-W razie w±tpliwo¶ci co do rozwi±zañ, dozwolonych bibliotek lub innych, nale¿y kontaktowaæ
siê z prowadz±cym przez Teams.