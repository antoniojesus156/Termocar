Potencia = 0
Temperatura_actual = 0
Calefacción = 0

def on_button_pressed_a():
    if input.light_level() >= 200:
        basic.show_string("Que tenga un buen día")
    else:
        basic.show_number(Potencia)
input.on_button_pressed(Button.A, on_button_pressed_a)

# This is an Easter egg

def on_forever():
    global Potencia
    if input.light_level() < 200 and Temperatura_actual <= Calefacción:
        if Temperatura_actual > 12:
            Potencia = Calefacción - Temperatura_actual + 1
        else:
            Potencia = 10
    else:
        Potencia = 0
basic.forever(on_forever)

def on_forever2():
    global Calefacción, Temperatura_actual
    # Java o Pyton
    Calefacción = 22
    Temperatura_actual = input.temperature()
basic.forever(on_forever2)
