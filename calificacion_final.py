


week_1 = float(input("semana 1 ->  "))

week_2 = float(input("semana 2 ->  "))

week_3 = float(input("semana 3 ->  "))

week_4 = float(input("semana 4 ->  "))

def calculate_note(a,b,c,d):
    return a+b+c+d


note_final = calculate_note(week_1,week_2,week_3,week_4)

print(f"El promedio final es de : {note_final/4:.1f}")