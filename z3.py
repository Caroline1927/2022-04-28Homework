
"""Zadanie 3.
Liderem nazywamy element, kt贸ry wyst臋puje wi臋cej ni偶 饾憳
2
, gdzie 饾憳 jest liczb膮 rozpatrywanych element贸w. Za艂贸偶my, 偶e mamy ci膮g liczb ca艂kowitych zapisanych na papierowej ta艣mie. Zak艂adaj膮c ponadto,
偶e na ta艣mie znajduje si臋 lider, zastanawiamy si臋, na ile sposob贸w mo偶emy przeci膮膰 ta艣m臋 na dwie
cz臋艣ci w taki spos贸b, by na obu znalaz艂 si臋 lider, kt贸rego warto艣膰 jest taka sama.
Przyk艂ad danych wej艣ciowych:
6
4 3 4 4 4 2
Wyj艣cie:
2
Komentarze:
1. W pierwszym wierszu wej艣cia znajduje si臋 liczba ca艂kowita 2 鈮? 饾憶 鈮? 10000, kt贸ra oznacza liczb臋
liczb na ta艣mie. Drugi wiersz wej艣cia zawiera ci膮g liczb ca艂kowitych z przedzia艂u (鈭?10000; 10000).
2. Liczba 2 na wyj艣ciu oznacza, 偶e ta艣m臋 mo偶na przeci膮膰 na dwa sposoby, tj. zawieraj膮cy liczb臋 4 i 3
4 4 4 2 albo 4 3 4 i 4 4 2. Tylko w ten spos贸b spe艂nimy warunki zadania.
Na podstawie powy偶szych informacji napisz program, kt贸ry realizuje powy偶szy algorytm w oparciu o
dane wprowadzone przez u偶ytkownika i/lub wczytuje z pliku tekstowego. Program powinien poinformowa膰 u偶ytkownika o liczbie ci臋膰 oraz o liczbach na obu cz臋艣ciach ta艣my, a tak偶e zapisa膰 wyniki w
nowym pliku tekstowym."""


from typing import Optional

k = 6
numbers = [5, 3, 5, 5, 5, 2]


def find_leader(nums: list[int]) -> Optional[int]:
    counts = {nums.count(x): x for x in set(nums)}
    if max(counts.keys()) > len(nums) // 2:
        return counts[max(counts.keys())]


def calculate_ways(nums: list[int]) -> int:
    result = 0
    for i in range(1, len(nums)):
        if find_leader(nums[:i]) == find_leader(nums[i:]):
            result += 1
    return result


print(calculate_ways(numbers))
