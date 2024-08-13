from datetime import date

def calcular_edad(fecha_nacimiento):
    fecha_actual = date.today()
    edad_dias = (fecha_actual - fecha_nacimiento).days
    return edad_dias

def calcular_dias_faltantes_para_80_anos(fecha_nacimiento):
    fecha_80_anos = fecha_nacimiento.replace(year=fecha_nacimiento.year + 80)
    fecha_actual = date.today()
    dias_faltantes = (fecha_80_anos - fecha_actual).days
    return dias_faltantes

fecha_nacimiento = input('ingresa tu fcha de nacimiento (YYYY-MM-DD):')
fecha_nacimiento = date.fromisoformat(fecha_nacimiento)

edad_dias = calcular_edad(fecha_nacimiento)
dias_faltantes = calcular_dias_faltantes_para_80_anos(fecha_nacimiento)

print(f'Has vivido {edad_dias} días')
print(f'Te faltan {dias_faltantes} días para cumplir 80 años')