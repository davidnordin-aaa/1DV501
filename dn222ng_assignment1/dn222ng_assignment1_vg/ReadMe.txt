Sum of Three (sumofthree.py)
Först vill programmet att ett input på ett tresiffrigt tal ska skrivas in (ex. 456). Därefter räknar datorn ut tre variablar:
num1, num2, num3. 
- num1 är talet genom modulus 10 som då blir entalet (i detta fall, 456 modulus 10 = 6)
- num2 är talet delat på 10 och därefter genom modulus som då blir 10-talet ((456/10) modulus 10 = 5.6 = 5 (int = inga decimaler))
- num3 är talet delat på 100 som då blir 100-talet (456 / 100 = 4.56 = 4 (int = inga decimaler))

Till sist adderas num1, num2, num3 ihop så det blir 4 + 5 + 6 = 15 som sedan skrivs ut.

Change (change.py)
Programmet vill få in ett price(price) och ett payment(pay) där change räknas ut genom change = payment - price. Därefter skrivs
change ut som är växeln i kr. Därefter kommer det många if-satser för varje individuella sedel och kr som finns om change är större/lika med
1000kr får kunden en 1000kr sedel och change subtraheras med 1000. Det är samma princip med alla typer av växlar: från 1000kr till 1kr.

Taxes (tax.py)
Programmet vill få in en oskattad lön på en månad (salary). Därefter kommer det tre variablar tax1, tax2, tax3 som räknar ut skatten för varje
typ av skatt som presenteras i uppgiften. 
- tax1: salary * 0.3 och den gäller på alla positiva värden i salary.
- tax2: (salary - 38 000) * 0.05 som gäller i intervallet 38 000 < salary < 50 000.
- tax3: (salary - 50 000) * 0.05 som gäller ifall salary > 50 000

Om salary = 32 000 kr kommer bara tax1 appliceras som leder till skatten 9 600 kr.
Om salary = 46 000 kr kommer tax1 och tax2 appliceras som sedan adderas ihop till skatten 14 200 kr.
Om salary = 79 000 kr kommer tax1, tax2 och tax3 appliceras och sedan adderas ihop till skatten 27 200 kr.
Till sist skrivs den gällande skatten ut.

Quadratic Equation (quadratic_equation.py)
Programmet vill få in värden på de tre variablarna A, B och C. Därefter räknas variabeln res ut som då är (B^2 - 4AC),
res kommer avgöra vilka gällande lösningar som finns i ekvationen. Sedan kommer det en if-sats som gäller
ifall A = 0 eller A och B = 0 och då räknas -C/B ut som då är lösningen i det fallet. Annars om res < 0 finns det inga lösningar
då det blir roten ur ett negativt tal som är icke-reellt. 
Annars räknas solution1 (s1) ut som är (-B + roten ur(B^2 - 4AC) / 2A) och solution2 (s2) som är (-B - roten ur(B^2 - 4AC) / 2A)
Ifall res = 0 finns det bara 1 lösning, s1. Annars om res > 0 finns det två lösningar, s1 och s2.