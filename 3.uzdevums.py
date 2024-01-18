nosaukums = input("Ievadiet faila nosaukumu: ")

try:
    with open(nosaukums, 'r', encoding='utf-8') as fails:
        rindas = fails.readlines()

        if len(rindas) >= 3:
            print("Trešās rindas saturs:", rindas[2].strip())
        else:
            print("Failā nav pietiekami daudz rindu.")
except FileNotFoundError:
    print(f"Kļūda: Fails ar nosaukumu '{nosaukums}' nav atrasts.")
except Exception as e:
    print(f"Neizdevās nolasīt failu. {e}")
