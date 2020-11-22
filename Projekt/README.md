Funkcja adjust_gamma:  

* image - obrazek 
* gamma - wspolczynnik gamma

Funkcja draw_easy:  

Jest odpowiedzialna za znalezienie kontur, i przybliżenie obrazka   
* dst - wartość threshingu
* v - wspolczynnik gamma  
* x - indeks obrazka

Funkcja kosteczki:  

Detekcja kółek, wywołuje funkcje policzone_oczka  

* image - przyblizony obrazek 
* indexior - indeks obrazka   
* base_img_coords - koordynaty gdzie mamy napisać text ile jest oczek na kostce   
* original - oryginalna wersja obrazka    

Funkcja policzone_oczka:  

Zapisuje obraz wraz z ilością oczek 

* img - oryginalne zdjecie    
* indi - ilość oczek  
* base_img_coords - koordynaty gdzie mamy napisać text ile jest oczek na kostce   
* indexior - indeks obrazka   
