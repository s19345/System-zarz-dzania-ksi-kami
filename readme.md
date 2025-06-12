# PPY Projekt-System zarz�dzania ksi��kami
Nast�puj�cy projekt sk�ada si� z kilku modu��w, zaleca si� implementacj� ka�dego z modu��w
po kolei, a nast�pnie ��czenie ich w jedn� ca�o��.
Za�o�enie projektu:
Stworzenie automatycznego systemu do �adowania/wzbogacania oraz udost�pniania danych
dotycz�cych ksi��ek wydanych przez Penguin Random House
Modu� 1 ? Pozyskanie danych
Projekt powinien oczekiwa� na plik (xlsx lub csv) w okre�lonej przez siebie lokalizacji (folder).
Wszystkie oczekiwane nazwy plik�w (wzory okre�lone regexem) powinny zosta� zawarte w pliku
konfiguracyjnym: config.json.
Je�eli plik kt�ry pojawi si� w folderze nie zostanie rozpoznany, nale�y go usun��.
Po rozpoznaniu pliku (przyk�adowe pliki wraz ze struktur� s� za��czone w assignmencie)
powinien zosta� za�adowany do skryptu przy u�yciu biblioteki pandas.
Przyk�adowy plik wej�ciowy oraz przyk�adowy plik konfiguracyjny dodany w assignmencie.
Modu� 2 ? Transformacje (pandas)
Na potrzeby tego projektu nale�y wykona� nast�puj�ce transformacje:
-usuniecie kolumn zawieraj�cych ?internal? w nazwie.
-Przeformatowanie imion i nazwisk autor�w, aby zawsze zaczyna�y si� z du�ej litery
-usuni�cie rekord�w od wydawnictw innych ni� Penguin Random House lub Random House, za
wyj�tkiem ksi��ek Stephena Kinga
-usuni�cie rekord�w pustych
-*usuni�cie rekord�w posiadaj�cych znaki chi�skie
-*usuni�cie potencjalnych duplikat�w
Modu� 3 ? Pobranie dodatkowych danych (requests):
Przy u�yciu otwartego API Penguin Random House (penguinrandomhouse.biz - Penguin Random
House Rest Services API), nale�y do ka�dej ksi��ki do��czy� (je�eli s� dost�pne) nast�puj�ce
informacje:
-dywizja (kt�ra wyda�a ksi��k�)
-bio autora
-sugerowany przedzia� wiekowy
Modu� 4 ? zapisywanie danych i odczytywanie ? persistance
Ponowne uruchomienie skryptu powinno automatycznie odzyskiwa� dane uzyskane w
poprzednim dzia�aniu. Mo�na to zrealizowa� przez serializacj� (pickle) lub przechowywanie
danych w JSON.
Zadania dodatkowe ? nie wymagane:
-U�yj dodatkowego API (np. API do uzyskania informacji o tw�rczo�ci mistrza grozy
https://stephen-king-api.onrender.com/), do uzyskania wiekszej ilo�ci informacji o wybranych
przez siebie ksi��kach
-Dodaj prost� warstw� graficzn� po stronie przegl�darki
-
Uwagi og�lne:
-Struktura plik�w i folder�w jest zale�na od tw�rcy kodu.
-Rozwi�zania nie opisane w powy�szym opisie zostawiam do w�asnej implementacji.
-Kod powinien by� czysty i przejrzysty - nale�y dodawa� typy zmiennych, zwracany typ
metod oraz stosowa� si� do og�lnie przyj�tych zasad dobrego kodu.
-Warto doda� dodatkowy log, aby �ledzi� dzia�anie programu nie tylko w konsoli
-Zadania oznaczone jako * s� dodatkowe.
-Aby unikn�� hardcodeowania danych, warto skorzysta� z config.json do przechowania
statycznych danych jak np. Url API.
-Kod nale�y napisa� samodzielnie, stwierdzenie niesamodzielno�ci pracy mo�e skutkowa�
uzyskaniem 0 punkt�w.
-Zadania z ?*? nie s� obowi�zkowe.
-W razie w�tpliwo�ci co do rozwi�za�, dozwolonych bibliotek lub innych, nale�y kontaktowa�
si� z prowadz�cym przez Teams.