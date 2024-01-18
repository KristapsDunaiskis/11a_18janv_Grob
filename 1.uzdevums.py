faila_nosaukums = "1.uzd.txt"
try:
    with open(faila_nosaukums, 'r', encoding='utf-8') as fails:
        saturs = fails.read()
        print("Faila saturs:")
        print(saturs)
except FileNotFoundError:
    print(f"Kļūda: Fails ar nosaukumu '{faila_nosaukums}' nav atrasts.")
except Exception as e:
    print(f"Kļūda: Neizdevās nolasīt failu. Kļūda: {e}")