# happy2.py

def happy():
  return "Happy Birthday to you!\n"

def verseFor(person):
  lyrics = happy()*2 + "Happy birthday, dear " + person + ".\n" + happy()
  return lyrics

def main():
  persons = ["Ye Tun", "Thura", "Pu Kywe"]
  for person in persons:
    print(verseFor(person))

main()
