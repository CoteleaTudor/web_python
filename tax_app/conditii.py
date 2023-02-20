"""
    Este necesar să se creeze o funcție a cărei esență este: calculul impozitului din suma de bani specificată. Această funcție poate fi apoi utilizată pentru a calcula impozitul pe salarii sau TVA, împrumuturi bancare etc.

PASI

+    Creați un folder „tax-app”
+    acesta conține două fișiere „app.py”, „tax.py”, acestea sunt două module - modulul principal și biblioteca noastră
    în „tax.py” declarați funcția „calculateTax()”
    Calculele în interiorul funcției necesită obținerea a 3 valori din contextul de apelul: suma de bani, dobândă (procentul), scopul sumei (salariu, împrumut, ...), declarați 3 variabile cu nume corespunzătoare în locul corespunzător al codului funcției in baza indicatiilor de mai sus
    dupa, in interiorul functiei, se declara o alta variabila in care se va pastra rezultatul calculului impozitului din suma, se calculeaza impozitul dupa formula de calcul a procentului din suma.
    întrucât această funcție trebuie să returneze nu numai valoarea impozitului calculat, ci și suma inițială, procentul și chiar scopul sumei de bani (dar știm că funcțiile pot returna o singură valoare), va fi necesar de a împacheta suma, procentul, impozitul, scopul într-o structură, fie dict sau listă
    alegeți tipul structurii (argumentând de ce în comentarii), lăsați funcția să împacheteze în continuare acele 4 valori în tipul selectat de structura și returnați-o înapoi în contextul din care este apelata functia
    Folosiți comentarii precum PYTHON DOCSTRINGS pentru a scrie o mini documentație pentru funcția dvs., care descrie argumentele și valorile returnate
    functia este gata
    importați funcția în modulul app.py
    scrieti cod in modulul principal care va permite utilizatorului sa-si introduca salariul de la tastatura
    Calculați impozitul pe venit (din salariu) folosind funcția
    afisati rezultatul pe consolă

BONUS: folosind verificarea tipului - asigurați-vă că funcția primeste doar tipul de date necesar ca argumente, altfel - aruncați erori folosind „raise” TypeError
"""