Funkcja adjust_gamma:  
1.  image - obrazek 
2.  gamma - wspolczynnik gamma
Funkcja draw_easy:  
Jest odpowiedzialna za znalezienie kontur, i przybliżenie obrazka   
1.  dst - wartość threshingu
2.  v - wspolczynnik gamma  
3.  x - indeks obrazka
Funkcja kosteczki:  
Detekcja kółek, wywołuje funkcje policzone_oczka    
1.  image - przyblizony obrazek 
2.  indexior - indeks obrazka   
3.  base_img_coords - koordynaty gdzie mamy napisać text ile jest oczek na kostce   
4.  original - oryginalna wersja obrazka    
Funkcja policzone_oczka:  
Zapisuje obraz wraz z ilością oczek 
1.  img - oryginalne zdjecie    
2.  indi - ilość oczek  
3.  base_img_coords - koordynaty gdzie mamy napisać text ile jest oczek na kostce   
4.  indexior - indeks obrazka   
