enum Playing {

    case rock, paper, scissors
}

enum GamingResult {
    case tie, winer, loser
}

func playRockPaperScissors(_ moveUser: Playing) -> GamingResult {
    
    let gameOptions = [Playing.rock, Playing.paper, Playing.scissors]
    let moveSystem = gameOptions.randomElement()!

    if moveUser == moveSystem {
        return gamingResult.tie
    } else if (moveUser == .rock && moveSystem == .scissors) || (moveUser == .paper && moveSystem == .rock) || (moveUser == .scissors && moveSystem == .paper) {
        return gamingResult.winner
    } else {
        return gamingResult.loser
    }

}


let moveUser = Playing.rock

let gamingResult = playRockPaperScissors(moveUser)

switch gamingResult {
case .tie:
    print("Tie :|")
case .winner:
    print("Winner! :)")
case .loser:
    print("Loser :(")
    
}