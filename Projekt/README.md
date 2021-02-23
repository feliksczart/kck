# Dice pipes detector
Projekt ten służy do wykrywania liczby oczek na kostce do gry. 
Działa on w następujący sposób:
  
  • Najpierw wczytuje zdjęcie i dzięki przejściu przez różne funkcje konwersji obrazu i odpowiedniej selekcji prostokątnych konturów (porównywanie pól), jest w stanie rozpoznać obszar, w którym znajduje się kostka. Jeśli jakiś rozpozna, to zwraca zdjęcie, które jest przybliżeniem na ów obszar, a także współrzędne środka przybliżenia obszaru.
        
  • Następnie korzystając z wcześniej przygotowanych zbliżeń, rozpoznaje kształty kół i nakłada na zdjęcie kontury wielokąta przypominającego okrąg, w miejscu, gdzie dany kształt został wykryty.
        
  • Zaznaczone kontury kółek stanowią listę, której długość jest odpowiedzią, na to ile oczek zostało wyrzuconych. Za pomocą wcześniej przygotowanej listy współrzędnych środków przybliżeń na obszary, w których znajdują się kostki, program wie, gdzie na oryginalnym zdjęciu należy umieścić etykiety opisujące sumę oczek.


# Sprawozdanie
https://drive.google.com/file/d/1G61L9EuZWBdSKE0-xhmGSWhOW4kPm6wc/view?usp=sharing
