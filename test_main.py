import main

def test_grade_A():
    assert main.calculate_grade(0.95) == 'A'

def test_grade_B():
    assert main.calculate_grade(0.85) == 'B'

def test_grade_C():
    assert main.calculate_grade(0.75) == 'C'

def test_grade_D():
    assert main.calculate_grade(0.65) == 'D'

def test_grade_F():
    assert main.calculate_grade(0.55) == 'F'

def test_invalid_score_high():
    assert main.calculate_grade(1.5) == 'Error: Score out of range.'

def test_invalid_score_low():
    assert main.calculate_grade(-0.1) == 'Error: Score out of range.'

def test_non_numeric_input():
    assert main.calculate_grade('abc') == 'Error: Please enter a numeric value.'
