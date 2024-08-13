from datetime import date

def calcular_edad(fecha_nacimiento):
    fecha_actual = date.today()
    edad_dias = (fecha_actual - fecha_nacimiento).days
    return edad_dias

fecha_nacimiento = input('ingresa tu fecha de nacimiento (YYYY-MM-DD):')
fecha_nacimiento = date.fromisoformat(fecha_nacimiento)
edad_dias = calcular_edad(fecha_nacimiento)



print(f'Has vivido {edad_dias}')