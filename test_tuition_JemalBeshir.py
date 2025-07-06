import tuition_JemalBeshir

def main ():
    # credits, resident, dt, expected value
        tests = [
            (0, True, False, 0),
            (0, True, True, 0),
            (0, False, False, 0),
            (0, False, True, 0),
            (1, True, False, 822),
            (1, True, True, 940),
            (1, False, False, 1911),
            (1, False, True, 2029),
            (8, True, False, 3391),
            (8, True, True, 4335),
            (8, False, False, 12103),
            (8, False, True, 13047),
            (9, True, False, 4280.5),
            (9, True, True, 5342.5),
            (9, False, False, 14081.5),
            (9, False, True, 15143.5),
            (11, True, False, 5014.5),
            (11, True, True, 6312.5),
            (11, False, False, 16993.5),
            (11, False, True, 18291.5),
            (12, True, False, 5389.5),
            (12, True, True, 6817.5),
            (12, False, False, 18445.5),
            (12, False, True, 19873.5),
            (15, True, False, 5389.5),
            (15, True, True, 6817.5),
            (15, False, False, 18445.5),
            (15, False, True, 19873.5),
    ]
        for credits, resident, dt, correct in tests:

            result = tuition_JemalBeshir.calculate_tuition(credits=credits, resident=resident, dt=dt)

            if round(result, 2) == correct:
                print(True)
            else: 
                 print(False)
