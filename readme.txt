the task
Przed laty Bajtazar grał na swoim starym telefonie komórkowym w grę Wąż. Dziś pracuje jako programista
i z sentymentu chciałby napisać własną wersję tej gry. A jako że mamy już rok 2022, Bajtazar chciałby
wprowadzić do niej trochę koloru i przenieść ją na zdecydowanie większy ekran komputera. Twoim zadaniem
będzie pomóc mu w napisaniu jednego z modułów jego gry.
Swoją grę Bajtazar nazwał Kolorowy wąż. Gra odbywa się na kwadratowej planszy, podzielonej na m2 pól
ułożonych w m wierszach i m kolumnach. Wiersze planszy numerujemy od 1 do m z góry na dół, a kolumny
od 1 do m od lewej do prawej. Po tej planszy porusza się kolorowy wąż, który staje się coraz dłuższy, w miarę
jak konsumuje rozmieszczone na planszy przekąski. Przekąski mają różne kolory i to one determinują kolory
poszczególnych fragmentów węża, gdy ten się wydłuża. Twój moduł będzie odpowiedzialny za określanie,
jakiego koloru fragmenty węża znajdują się na poszczególnych polach planszy w określonych chwilach czasu.
Zasady gry: Dla uproszczenia opisu wszystkie dostępne kolory numerujemy od 0 do m2 − 1. Na początku
gry w polu na przecięciu wiersza 1 i kolumny 1 znajduje się wąż, złożony wyłącznie z głowy, w kolorze 0.
Na planszy rozmieszczonych jest p przekąsek; każda z nich zajmuje jedno pole planszy i ma określony kolor.
Kolory przekąsek mogą się powtarzać. Gracz steruje ruchami głowy węża tak, że w każdej jednostce czasu głowa
przesuwa się o jedno pole w górę, w dół, w lewo lub w prawo. Za głową podążają pozostałe fragmenty węża w ten
sposób, że pole, które przed wykonaniem ruchu zajmowała głowa węża, teraz zajmuje drugi fragment węża;
pole zajmowane przez drugi fragment zajmuje trzeci fragment itd. Ruch głowy nigdy nie odbywa się w stronę
pola, na którym znajduje się pierwszy za głową fragment węża (czyli wąż nigdy się nie „cofa”). Ponadto
głowa nigdy nie może wyjść poza planszę ani na inne pole zawierające fragment węża – w tej sytuacji gracz
przegrywa. Gdy głowa ruszy się na pole zajmowane przez przekąskę, wąż konsumuje tę przekąskę, wskutek
czego przekąska znika z planszy, a wąż wydłuża się o jeden fragment. Odbywa się to w ten sposób, że głowa
węża przyjmuje kolor skonsumowanej przekąski i po wykonaniu ruchu znajduje się w polu, które zajmowała
przekąska, a pozostałe fragmenty węża w tym ruchu nie przemieszczają się.
Przykładowo, rozważmy planszę 6 × 6, na której rozmieszczono pięć przekąsek w kolorach 1, 2, 1, 3, 5. Na
rysunku położenia przekąsek oznaczono liczbami oznaczającymi ich kolory. Początkowe położenie głowy węża
oznaczono cyfrą 0, a pozostałe pola oznaczono kropkami. Załóżmy, że głowa węża wykonuje kolejno ruchy:
w prawo, w prawo, w dół, w dół, w prawo, w prawo, w dół i w lewo. Wówczas kolejne położenia węża –
zaznaczonego na planszy na czerwono – są następujące:
0.1... .01... .01... .01... ..0... ..0... ..0... ...... ......
..2... ..2... ..2... ..2... ..1... ..1... ..1... ..0... ......
...13. ...13. ...13. ...13. ..213. ..213. ..213. ..121. ..012.
...... ...... ...... ...... ...... ...... ...... ....3. ...31.
5..... 5..... 5..... 5..... 5..... 5..... 5..... 5..... 5.....
...... ...... ...... ...... ...... ...... ...... ...... ......
Twój moduł dostaje opis kolejnych ruchów wykonywanych przez gracza i musi odpowiadać na zapytania
o to, czy w danym momencie w danym polu planszy znajduje się fragment węża, a jeśli tak, to jakiego jest
on koloru. Możesz założyć, że wąż w trakcie wykonywania ruchów nie wyjdzie poza planszę ani nie wejdzie na
pole, na którym znajduje się jakiś jego fragment.
Wejście
W pierwszym wierszu wejścia znajdują się trzy liczby całkowite m, p oraz n oznaczające długość (i zarazem
szerokość) planszy, liczbę przekąsek na planszy oraz liczbę poleceń do obsłużenia.
Każdy z kolejnych p wierszy zawiera trzy liczby całkowite wi
, ki
i ci (1 ≤ wi
, ki ≤ m, 0 ≤ ci ≤ m2 − 1)
oznaczające, że w polu w wierszu wi
i kolumnie ki znajduje się jedna przekąska węża w kolorze ci
. Wszystkie
pary (wi
, ki) na wejściu będą różne i żadna nie będzie równa (1, 1), czyli początkowemu położeniu węża.
Kolejne n wierszy zawiera opis poleceń. Polecenie składa się z jednej litery G, D, L, P albo z litery Z i dwóch
liczb całkowitych w
′
j
, k
′
j
. Pierwsze cztery polecenia oznaczają, w którą stronę przemieściła się głowa węża:
w górę (G), w dół (D), w lewo (L) czy w prawo (P). Natomiast polecenie „Z w
′
j k
′
j
” oznacza zapytanie o to, jaki
kolor fragmentu węża w danym momencie znajduje się w polu w wierszu w
′
j
i kolumnie k
′
j
. Możesz założyć, że
wśród poleceń znajdzie się co najmniej jedno takie zapytanie.
Wyjście
Dla każdego zapytania należy wypisać na wyjściu jedną liczbę całkowitą z zakresu [0, m2 − 1] oznaczającą
kolor fragmentu węża, który w danym momencie zajmuje pole opisane w zapytaniu, bądź "." w przypadku,
gdy w danym momencie w tym polu żadnego fragmentu węża nie ma.
Przykład
Dla danych wejściowych:
6 5 14
1 3 1
5 1 5
2 3 2
3 4 1
3 5 3
Z 1 1
Z 1 2
P
P
D
D
P
Z 3 5
P
Z 3 5
D
Z 3 5
L
Z 3 5
poprawnym wynikiem jest:
0
"."
3
3
1
2


