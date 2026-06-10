from logic_utils import check_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_shows_go_lower():
    # Bug fix: when guess > secret, message must say Go LOWER, not Go HIGHER
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_shows_go_higher():
    # Bug fix: when guess < secret, message must say Go HIGHER, not Go LOWER
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_hints_consistent_across_attempts():
    # Regression: string conversion on even attempts used to flip hints
    for guess, secret in [(90, 50), (10, 50), (51, 50), (49, 50)]:
        outcome, message = check_guess(guess, secret)
        if guess > secret:
            assert "LOWER" in message
        else:
            assert "HIGHER" in message
