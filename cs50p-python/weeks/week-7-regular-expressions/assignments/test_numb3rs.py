from numb3rs import validate

def test_validation():
        
    assert validate("255.2.33.22") == True
    assert validate("256.2.33.44") == False
    assert validate("01.23.12.212") == True

def test_edge_cases():

    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_alphabets():

    assert validate("fifty two.sixty three.34.56") == False

def test_long():
    assert validate("111.12.44.9999.66.33") == False

def test_short():
    assert validate("11.676.32") == False
    
def test_range():
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False