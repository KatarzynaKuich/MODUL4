#Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem. Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.
#Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.
#Do zadania dodaj krótką dokumentację i umieść je w zdalnym repozytorium. Link prześlij Mentorowi.

def palindrom(slowo):
    max=len(slowo)
    for i in range(0,max):
      if slowo[i] != slowo[max-i-1]:
       return False

print("\nPalindromy")
print("\nPODAJ słowo:")

s =(input().upper())
if palindrom(s)==False:
  print("\nSłowo",s,"nie jest palindormem.")
else:
  print("\nSłowo",s,"jest palindormem.")
