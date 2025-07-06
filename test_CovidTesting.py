from test_CovidTesting import CovidTesting2_JemalBeshir
def test_sample():
    assert CovidTesting2_JemalBeshir.is_valid_sample(0.97) == True
    assert CovidTesting2_JemalBeshir.is_valid_calibration(4) == True
    assert CovidTesting2_JemalBeshir.is_valid_sample(0.89) == False
    assert CovidTesting2_JemalBeshir.is_valid_calibration(8) == False    
