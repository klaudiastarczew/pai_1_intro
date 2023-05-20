# Podstawy i komunikacja z web API

## Co to są circuit breakers i do czego służą? Dlaczego to jest ważny element aplikacji Netfixa? 

Circuit breakers to mechanizmy używane w systemach rozproszonych w celu zapobiegania rozprzestrzenianiu się błędów. Służą one do ochrony systemu przed tzw. cascading failures, czyli sytuacją, w której jeden błąd w jednym komponencie powoduje kolejne błędy w innych komponentach, co może doprowadzić do całkowitej awarii systemu. 

W aplikacjach takich jak Netflix, circuit breakers odgrywają istotną rolę. W przypadku awarii jednego z serwisów, circuit breaker wykrywa ten problem i tymczasowo odłącza dostęp do uszkodzonego komponentu. Dzięki temu pozostałe części systemu nie są negatywnie dotknięte i mogą nadal działać bez zakłóceń. Circuit breakers zapewniają wysoką dostępność, odporność na awarie i poprawę ogólnej stabilności aplikacji Netflix.


## Patrząc od strony programisty w Netflixie czy Allegro budującego serwis, dlaczego chcemy uniknąć cascading failures?

Netflix i Allegro są dużymi aplikacjami obsługującymi setki lub nawet tysiące żądań na sekundę, unikanie cascading failures jest niezwykle istotne. Jeśli w jednym z serwisów wystąpi błąd lub spowolnienie, a inne serwisy są wciąż zależne od tego uszkodzonego komponentu, może to prowadzić do narastających problemów. 
Circuit breakers pozwalają wykryć awarię i tymczasowo odciąć dostęp do uszkodzonego komponentu, minimalizując wpływ na resztę systemu. Zapewnia to odporność na awarie, poprawia wydajność i stabilność całej aplikacji.



## Patrząc od strony programisty w Amazonie budującego serwis, dlaczego graceful degradation jest ważny?

Dla programistów w Amazonie istotne jest wprowadzenie łagodnego degradowania (graceful degradation), ponieważ umożliwia to systemowi utrzymanie minimalnej funkcjonalności nawet w przypadku problemów. Gdy wystąpią problemy z jedną z usług lub komponentów, system będzie w stanie nadal działać, ograniczając funkcje, które mogą być zależne od uszkodzonej części. Dzięki temu system może zachować integralność i obsługiwać żądania, nawet jeśli niektóre funkcje są niedostępne lub działają w ograniczonym zakresie.



## Użycie curl i jq do wypisania nazw super bohaterów z pliku JSON
                
curl -s --fail https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json
| jq '.members[].name'

----
