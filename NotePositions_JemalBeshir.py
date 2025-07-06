import argparse

def note_num(note):
    """
    Addings this method cause I like the if , then using 
    another method in the get_fret makes it clean.
    Used something similar in my Java course.
    """
    if note == "A": return 0
    if note =="A#":return 1
    if note =="Bb": return 1
    if note =="B": return 2
    if note =="C": return 3
    if note =="C#": return 4
    if note =="Db": return 4
    if note =="D": return 5
    if note =="D#": return 6
    if note =="Eb": return 6
    if note =="E": return 7
    if note =="F": return 8
    if note =="F#": return 9
    if note =="Gb": return 9
    if note =="G": return 10
    if note =="G#": return 11
    if note =="Ab": return 11

def get_fret(target, string):
    """ Finds the fret that will produce a given note on a given string.

    We assume that note names will be one- or two-character strings. The
    first character will be a capital letter between A and G. The second
    character, if any, will be either # or b.

    Args:
        target (str): the note whose position is to be determined.
        string (str): the note of the open string.

    Returns:
        int: the fret that will produce the target note on the specified
        string (0 represents the open string).
    """
    target_num = note_num(target)
    string_num = note_num(string)
    fret = (target_num-string_num) %12 #12 because of the distance between open string and target note, mod of the number of semitones being 12
    return fret

def get_frets(target, strings):
    """ Given a list of strings, finds the fret on each string that will
    produce a given note.

    We assume that note names will be one- or two-character strings. The
    first character will be a capital letter between A and G. The second
    character, if any, will be either # or b.

    Args:
        target (str): the note whose position is to be determined.
        strings (list of str): a list of the notes of open strings.

    Returns:
        dict of (str: int): a dictionary whose keys are the string names
        specified in the strings parameter and whose values are fret
        positions on those strings. For example, if strings has the
        value ['G', 'C', 'E', 'A'], this function will return {'G': 4,
        'C': 11, 'E': 7, 'A': 2}.
    """
    result = {}
    for string in strings:
        strge_fret = get_fret(target, string)
        result[string] = strge_fret
    return result
def parse_args(arglist):
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("strings", nargs="+")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    import sys
    args = parse_args(sys.argv[1:])
    result = get_frets(args.target, args.strings)
    print(f"{args.target} is")
    for string, fret in result.items():
        print(f"  fret {fret} of the {string} string")
