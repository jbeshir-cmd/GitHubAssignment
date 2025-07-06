import NotePositions_JemalBeshir

def test_get_fret():
    assert NotePositions_JemalBeshir.get_fret("C", "C") == 0
    assert NotePositions_JemalBeshir.get_fret("A", "C") == 6
    assert NotePositions_JemalBeshir.get_fret("C", "A") == 6
    assert NotePositions_JemalBeshir.get_fret("G#", "C") == NotePositions_JemalBeshir.get_fret("Ab", "C")

def test_get_frets():
    result = NotePositions_JemalBeshir.get_frets("C", ["G"])
    assert isinstance(result, dict)
    assert len(result) == 1
    assert result["G"] == NotePositions_JemalBeshir.get_fret("C", "G")

    strings = ["G", "D", "A"]
    result = NotePositions_JemalBeshir.get_frets("C", strings)
    assert isinstance(result, dict)
    assert len(result) == len(strings)
    for string in strings:
        assert result[string] == NotePositions_JemalBeshir.get_fret("C", string)

test_get_fret()
test_get_frets()
print("All tests passed.")
