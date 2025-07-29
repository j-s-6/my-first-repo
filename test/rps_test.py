from app.rps import determine_winner

def test_winner():
    assert determine_winner("rock", "rock") == "TIE GAME"
    assert determine_winner("paper", "paper") == "TIE GAME"
    assert determine_winner("scissors", "scissors") == "TIE GAME"
    assert determine_winner("rock", "scissors") == "USER WINS"
    assert determine_winner("paper", "rock") == "USER WINS"
    assert determine_winner("scissors", "paper") == "USER WINS"
    assert determine_winner("rock", "paper") == "COMP WINS"
    assert determine_winner("paper", "scissors") == "COMP WINS"
    assert determine_winner("scissors", "rock") == "COMP WINS"
    assert determine_winner("banana", "rock") == "INVALID CHOICE"
    assert determine_winner("rock", "fire") == "INVALID CHOICE"
    assert determine_winner("x", "y") == "INVALID CHOICE"
    assert determine_winner("", "scissors") == "INVALID CHOICE"
    assert determine_winner("scissors", "") == "INVALID CHOICE"

    print("✅ All tests passed!")
