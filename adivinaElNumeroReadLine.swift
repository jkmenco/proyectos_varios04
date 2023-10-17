import Foundation

let numberRandom = Int.random(in: 1...100)
var counterTryUser = 0

print()

print("\t.:Juego adivina el número:.")

playGame()

func playGame()
     
    while numberRandom > 0 {
        
        print("Digite un numero ->")
        
        let userNumber = Int(readLine()!)!
        
        counterTryUser += 1
        
        if userNumber == numberRandom {
            print("¡Felicidades! Adivinaste el número en \(counterTryUser) intentos.")
            break
        } else {
            let difference = abs(numberRandom - userNumber)
            
            if difference <= 5 {
                print("¡Muy caliente! Pero no es el número.")
            } else if difference <= 10 {
                print("¡Caliente! Pero no es el número.")
            } else if difference <= 20 {
                print("¡Tibio! Pero no es el número.")
            } else {
                print("¡Frío! Sigue intentando.")
            }
            
        }
    }
