import csv

def kolonna(fails):
    try:
        with open(fails, 'r', newline='', encoding='utf-8') as csvfile:
            csvlasitajs = csv.reader(csvfile)
            for rinda in csvlasitajs:
                if len(rinda) > 1: 
                    print(rinda[1])
    except FileNotFoundError:
        print(f"CSV fails ar nosaukumu '{fails}' nav atrasts.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")

fails = '2.uzd.csv' 
kolonna("2.uzd.csv")



