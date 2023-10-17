//
//  ViewController.swift
//  whatIsNumber
//
//  Created by Carlos Rios on 3/04/23.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var numberUser: UITextField!
    @IBOutlet weak var answerColdOrHot: UILabel!
    @IBOutlet weak var putANumber: UILabel!
    
    let numberRandom = Int.random(in: 1...100)
    var counterTryUser = 0

    @IBAction func checkNumberUser(_ sender: Any) {
        
        checkUserAnswer()
        
    }

    
    func checkUserAnswer () {
        guard let numberText = numberUser.text, let userNumber = Int(numberText) else {
            answerColdOrHot.text = "Ingresa un número válido."
            return
        }
        counterTryUser += 1
        
        if userNumber == numberRandom {
            answerColdOrHot.text = "¡Felicidades! Adivinaste el número en \(counterTryUser) intentos."
        } else {
            let difference = abs(numberRandom - userNumber)
            if difference <= 5 {
                answerColdOrHot.text = "¡Muy caliente! Pero no es el número."
            } else if difference <= 10 {
                answerColdOrHot.text = "¡Caliente! Pero no es el número."
            } else if difference <= 20 {
                answerColdOrHot.text = "¡Tibio! Pero no es el número."
            } else {
                answerColdOrHot.text = "¡Frío! Sigue intentando."
            }
        
        }
    }
}
