func playRockPaperScissors(userChoice: String) -> String {
    let rockPaperScissors = ["Rock", "Paper", "Scissors"]
    guard let computerChoice = rockPaperScissors.randomElement() else {
        return "Error: Could not generate computer's choice"
    }
    
    switch userChoice {
    case "Rock":
        switch computerChoice {
        case "Rock":
            return "Tie"
        case "Paper":
            return "Computer wins"
        case "Scissors":
            return "You win"
        default:
            return "Error: Invalid computer's choice"
        }
    case "Paper":
        switch computerChoice {
        case "Rock":
            return "You win"
        case "Paper":
            return "Tie"
        case "Scissors":
            return "Computer wins"
        default:
            return "Error: Invalid computer's choice"
        }
    case "Scissors":
        switch computerChoice {
        case "Rock":
            return "Computer wins"
        case "Paper":
            return "You win"
        case "Scissors":
            return "Tie"
        default:
            return "Error: Invalid computer's choice"
        }
    default:
        return "Error: Invalid user's choice"
    }
}
