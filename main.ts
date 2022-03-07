let Potencia = 0
let Calefacción = 0
let Temperatura_actual = 0
input.onButtonPressed(Button.A, function () {
    if (input.lightLevel() >= 200) {
        basic.showString("hola soy oscar")
    } else {
        basic.showNumber(Potencia)
    }
})
basic.forever(function () {
    // Java o Pyton
    Calefacción = 22
    Temperatura_actual = input.temperature()
})
// This is an Easter egg
basic.forever(function () {
    if (input.lightLevel() < 200 && Temperatura_actual <= Calefacción) {
        if (Temperatura_actual > 12) {
            Potencia = Calefacción - Temperatura_actual + 1
        } else {
            Potencia = 10
        }
    } else {
        Potencia = 0
    }
})
