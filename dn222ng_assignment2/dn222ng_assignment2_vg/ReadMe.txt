Count Digits (countdigits.py)
Först skrivs en stor integer in till programmet som måste vara positivt. Sedan konverteras
inputet till en string som går igenom en for loop. Loopen kollar på den siffra som är längst bak
på talet och kollar om det är jämnt, ojämnt eller noll. Ifall talet är exempelvis jämnt blir det
plus 1 på en variabel som räknar antalet jämna. Samma princip på ojämna och noll.
I nästa iteration kollas siffran näst längst bak, därefter siffran före det osv.
Sedan printas det ut hur många jämna, ojämna och nollor det var.

Birthday (birthday_candles.py)
Programmet är i en loop som går 100 gånger. Först blir går programmet genom för birthday 1 och nollställer
boxes till 0. Sedan i en while-loop så medans antalet ljus är mindre än age kommer box += 1, boxbox (totala boxes) += 1 och 
antalet candles öka med 24. Därefter subtraheras candles med åldern.
Det printas bara "Before birthday 1, buy 1 box(es)" ifall en box köptes.
Sedan går programmet för birthday 2 fram till birthday 100.
Tillslut printas boxbox (totala antalet box) och återstående candles.

Salary (salary_revision.py)
I programmet finns ska en löner skrivas in som t.ex 312 214 423 3432 som sedan
delas in i en lista där lönerna går igenom tre funktioner: median, average och gap.

1. Median sorterar lönerna i storleksordning och ifall det är ojämnt antal löner
blir medianen längden på listan delat på 2. Ifall det är jämnt antal löner
adderas de två mellersta lönerna ihop och delas på två som är medianen.

2. Average konverterar lönerna från string till int och summerar ihop lönerna
och delar sedan med antalet löner som är genomsnittet.

3. Gap sorterar lönerna i storleksordning och konverterar listans värden från string till
int. Därefter tas max och min-värdet från listan och max subtraheras med min som är gap.

Resultatet från funktionerna printas sedan ut.