from collections import Counter
import unicodedata
import re

def _normalize(s: str) -> str:

    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    s = s.casefold()
    s = re.sub(r"[^a-z0-9]", "", s)
    return s

def es_anagrama(a: str, b: str) -> bool:
    return Counter(_normalize(a)) == Counter(_normalize(b))


print(es_anagrama("Roma", "Amor"))           
print(es_anagrama("Eleven plus two", "Twelve plus one"))  
print(es_anagrama("Hola", "Halo"))     
