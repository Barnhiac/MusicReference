__author__ = 'Tonic Labs'
# -*- coding: UTF-8 -*-


##    0     1    2      3      4     5       6       7      8      9     10      11   12
C = ['C', 'C#', 'D', 'D#/E♭', 'E', 'E#/F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B', 'C']
G = ['G', 'G#/A♭', 'A', 'A#/B♭', 'B', 'C', 'C#', 'D', 'D#/E♭', 'E', 'E#/F', 'F#/G♭', 'G']
D = ['D', 'D#/E♭', 'E', 'E#/F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B', 'C', 'C#', 'D']
A = ['A', 'A#/B♭', 'B', 'C', 'C#', 'D', 'D#/E♭', 'E', 'E#/F', 'F#/G♭', 'G', 'G#/A♭', 'A']
E = ['E', 'E#/F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B', 'C', 'C#', 'D', 'D#/E♭', 'E']
BORCFLAT = ['B', 'C', 'C#', 'D', 'D#/E♭', 'E', 'E#/F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B']
GFLATORFSHARP = ['F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B', 'C', 'C#', 'D', 'D#/E♭', 'E', 'E#/F', 'F#/G♭']
DFLATORCSHARP = ['C#', 'D', 'D#/E♭', 'E', 'E#/F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B', 'C', 'C#']
AFLAT = ['G#/A♭', 'A', 'A#/B♭', 'B', 'C', 'C#', 'D', 'D#/E♭', 'E', 'E#/F', 'F#/G♭', 'G', 'G#/A♭']
EFLAT = ['D#/E♭', 'E', 'E#/F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B', 'C', 'C#', 'D', 'D#/E♭']
BFLAT = ['A#/B♭', 'B', 'C', 'C#', 'D', 'D#/E♭', 'E', 'E#/F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭']
F = ['E#/F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B', 'C', 'C#', 'D', 'D#/E♭', 'E', 'E#/F']
majorpentscale = [0, 1, 2, 4, 5]
major = [0, 2, 4, 5, 7, 9, 11]
minor = [0, 2, 3, 5, 7, 8, 10]
minor_pent = [0, 2, 3, 4, 6]


def melodic_scale(key):
    if key == "C":
        return C
    elif key == "G":
        return G
    elif key == "D":
        return D
    elif key == "A":
        return A
    elif key == "E":
        return E
    elif key == "B":
        return BORCFLAT
    elif key == "GFLAT/FSHARP":
        return GFLATORFSHARP
    elif key == "DFlat":
        return DFLATORCSHARP
    elif key == "AFlat":
        return AFLAT
    elif key == "EFlat":
        return EFLAT
    elif key == "BFlat":
        return BFLAT
    elif key == "F":
        return F


def major_scale(key):
    if key == "C":

        return [e for i, e in enumerate(C) if i in major]
    elif key == "G":
        return [e for i, e in enumerate(G) if i in major]

    elif key == "D":
        return [e for i, e in enumerate(D) if i in major]

    elif key == "A":
        return [e for i, e in enumerate(A) if i in major]

    elif key == "E":
        return [e for i, e in enumerate(E) if i in major]

    elif key == "B/CFLAT":
        return [e for i, e in enumerate(BORCFLAT) if i in major]
    elif key == "GFLAT/FSHARP":
        return [e for i, e in enumerate(GFLATORFSHARP) if i in major]

    elif key == "DFLAT/CSHARP":
        return [e for i, e in enumerate(DFLATORCSHARP) if i in major]

    elif key == "AFLAT":
        return [e for i, e in enumerate(AFLAT) if i in major]

    elif key == "EFLAT":
        return [e for i, e in enumerate(EFLAT) if i in major]

    elif key == "BFLAT":
        return [e for i, e in enumerate(BFLAT) if i in major]

    elif key == "F":
        return [e for i, e in enumerate(F) if i in major]


def major_pentatonic(key):
    x = [e for i, e in enumerate(major_scale(key)) if i in majorpentscale]
    return x



def natural_minor(key):
    if key == "C":

        return [e for i, e in enumerate(C) if i in minor]
    elif key == "G":
        return [e for i, e in enumerate(G) if i in minor]

    elif key == "D":
        return [e for i, e in enumerate(D) if i in minor]

    elif key == "A":
        return [e for i, e in enumerate(A) if i in minor]

    elif key == "E":
        return [e for i, e in enumerate(E) if i in minor]

    elif key == "B/CFLAT":
        return [e for i, e in enumerate(BORCFLAT) if i in minor]
    elif key == "GFLAT/FSHARP":
        return [e for i, e in enumerate(GFLATORFSHARP) if i in minor]

    elif key == "DFLAT/CSHARP":
        return [e for i, e in enumerate(DFLATORCSHARP) if i in minor]

    elif key == "AFLAT":
        return [e for i, e in enumerate(AFLAT) if i in minor]

    elif key == "EFLAT":
        return [e for i, e in enumerate(EFLAT) if i in minor]

    elif key == "BFLAT":
        return [e for i, e in enumerate(BFLAT) if i in minor]

    elif key == "F":
        return [e for i, e in enumerate(F) if i in minor]



def natural_minor_pentatonic(key):
    return [e for i, e in enumerate(natural_minor(key)) if i in minor_pent]

def scale_giver():
    tonic = (input("What key would you like to know?").upper())
    scaleform = (input("What scale would you like to know? Major, the Major Pentatonic, "
                       "the Natural Minor, the pentatonic of the Natural Minor, or the Blues scale?").upper())

    if scaleform == "MAJOR":
        print(major_scale(tonic))

    elif scaleform == "MAJOR PENTATONIC":
        print(major_pentatonic(tonic))

    elif scaleform == "NATURAL MINOR":
        print(natural_minor(tonic))

    elif scaleform == "NATURAL MINOR PENTATONIC":
        print(natural_minor_pentatonic(tonic))

    elif scaleform == "BLUES":
        sharp_fourth = melodic_scale(tonic)[6]
        blues = natural_minor_pentatonic(tonic)[0:3] + [sharp_fourth] + natural_minor_pentatonic(tonic)[3:]
        print(blues)

    elif scaleform == "MELODIC":
        print(melodic_scale(tonic))

    else:
        print("You must enter either: Major, Major Pentatonic, Natural Minor, Natural Minor Pentatonic, Melodic, or "
              "Blues")


    again = input("Do you want to find information about another key? Yes or No?").upper()
    if again == "YES":
        program()
    else:
        print("Thanks for your interest!")


def chord_giver():
    tonic = (input("What chord would you like to know?").upper())
    scaleform = (input("What form of the chord would you like to know?").upper())
    if scaleform == "MAJOR":
        print ([major_scale(tonic)[0] + major_scale(tonic)[2] + major_scale(tonic)[4]])
    elif scaleform == "MINOR":
        print([natural_minor(tonic)[0] + natural_minor(tonic)[2] + natural_minor(tonic)[4]])
    elif scaleform == "DIMINISHED":
        print([major_scale(tonic)[0] + melodic_scale(tonic)[3] + melodic_scale(tonic)[6]])
    elif scaleform == "AUGMENTED":
        print([major_scale(tonic)[0] + melodic_scale(tonic)[4] + melodic_scale(tonic)[8]])
    elif scaleform == "MAJOR7":
        print([major_scale(tonic)[0] + major_scale(tonic)[2] + major_scale(tonic)[4] + major_scale(tonic)[6]])
    elif scaleform == "DOMINANT7":
        print([major_scale(tonic)[0] + major_scale(tonic)[2] + major_scale(tonic)[4] + melodic_scale(tonic)[10]])
    elif scaleform == "SIXTH":
        print([natural_minor(tonic)[0] + natural_minor(tonic)[2] + natural_minor(tonic)[4] + natural_minor(tonic)[5]])
    elif scaleform == "DOMINANT9":
        print([major_scale(tonic)[0] + major_scale(tonic)[2] + major_scale(tonic)[4] + melodic_scale(tonic)[10] +
               major_scale(tonic)[1]])
    elif scaleform == "MAJOR9":
        print([major_scale(tonic)[0] + major_scale(tonic)[2] + major_scale(tonic)[4] + major_scale(tonic)[6] +
               major_scale(1)])
    elif scaleform == "MINOR7":
        print([melodic_scale(tonic)[0] + melodic_scale(tonic)[3] + melodic_scale(tonic)[7] + melodic_scale(tonic)[10]])
    elif scaleform == "MINOR9":
        print([melodic_scale(tonic)[0] + melodic_scale(tonic)[3] + melodic_scale(tonic)[7] + melodic_scale(tonic)[10]+
               natural_minor(tonic)[1]])
    elif scaleform == "SUS2":
        ask = (input("Major or minor?").upper())
        if ask == "MAJOR":
            print([major_scale(tonic)[0] + major_scale(tonic)[1] + major_scale(tonic)[4]])
        elif ask == "MINOR":
            print([natural_minor(tonic)[0] + natural_minor(tonic)[1] + natural_minor(tonic)[4]])
        else:
            print("Please specify either major or minor")
            return chord_giver()
    elif scaleform == "SUS4":
        ask = (input("Major or minor?").upper())
        if ask == "MAJOR":
            print([major_scale(tonic)[0] + major_scale(tonic)[3] + major_scale(tonic)[4]])
        elif ask == "MINOR":
            print([natural_minor(tonic)[0] + natural_minor(tonic)[3] + natural_minor(tonic)[4]])
        else:
            print("Please specify either major or minor")
            return chord_giver()
    else:
        print("The options for chords are: Major, Minor, Diminished, Augmented, Major 7th, Minor 7th, Dominant 7th, 6th"
              "Dominant 9th, Major 9th, Minor 9th, sus2, or sus4. Please enter one of these when you are asked about the"
              "chord forms.")

    again = input("Do you want to find information about another key? Yes or No?").upper()
    if again == "YES":
        return program()
    else:
        print("Thanks for your interest!")

def chords(tonic, scaleform):
    if scaleform == "MAJOR":
        print ([major_scale(tonic)[0] + major_scale(tonic)[2] + major_scale(tonic)[4]])
    elif scaleform == "MINOR":
        print([natural_minor(tonic)[0] + natural_minor(tonic)[2] + natural_minor(tonic)[4]])
    elif scaleform == "DIMINISHED":
        print([major_scale(tonic)[0] + melodic_scale(tonic)[3] + melodic_scale(tonic)[6]])
    elif scaleform == "AUGMENTED":
        print([major_scale(tonic)[0] + melodic_scale(tonic)[4] + melodic_scale(tonic)[8]])
    elif scaleform == "MAJOR7":
        print([major_scale(tonic)[0] + major_scale(tonic)[2] + major_scale(tonic)[4] + major_scale(tonic)[6]])
    elif scaleform == "DOMINANT7":
        print([major_scale(tonic)[0] + major_scale(tonic)[2] + major_scale(tonic)[4] + melodic_scale(tonic)[10]])
    elif scaleform == "SIXTH":
        print([natural_minor(tonic)[0] + natural_minor(tonic)[2] + natural_minor(tonic)[4] + natural_minor(tonic)[5]])
    elif scaleform == "DOMINANT9":
        print([major_scale(tonic)[0] + major_scale(tonic)[2] + major_scale(tonic)[4] + melodic_scale(tonic)[10] +
               major_scale(tonic)[1]])
    elif scaleform == "MAJOR9":
        print([major_scale(tonic)[0] + major_scale(tonic)[2] + major_scale(tonic)[4] + major_scale(tonic)[6] +
               major_scale(1)])
    elif scaleform == "MINOR7":
        print([melodic_scale(tonic)[0] + melodic_scale(tonic)[3] + melodic_scale(tonic)[7] + melodic_scale(tonic)[10]])
    elif scaleform == "MINOR9":
        print([melodic_scale(tonic)[0] + melodic_scale(tonic)[3] + melodic_scale(tonic)[7] + melodic_scale(tonic)[10]+
               natural_minor(tonic)[1]])
    elif scaleform == "SUS2":
        ask = (input("Major or minor?").upper())
        if ask == "MAJOR":
            print([major_scale(tonic)[0] + major_scale(tonic)[1] + major_scale(tonic)[4]])
        elif ask == "MINOR":
            print([natural_minor(tonic)[0] + natural_minor(tonic)[1] + natural_minor(tonic)[4]])
        else:
            print("Please specify either major or minor")
            return chord_giver()
    elif scaleform == "SUS4":
        ask = (input("Major or minor?").upper())
        if ask == "MAJOR":
            print([major_scale(tonic)[0] + major_scale(tonic)[3] + major_scale(tonic)[4]])
        elif ask == "MINOR":
            print([natural_minor(tonic)[0] + natural_minor(tonic)[3] + natural_minor(tonic)[4]])
        else:
            print("Please specify either major or minor")
            return chord_giver()
def key_giver():
    set_one = []
    first = (input("What is the first chord you would like to input? C, D, G, etc.").upper())
    first_form = (input("What is the scaleform of the first chord? Major, Minor, Diminished, etc.").upper())
    set_one.append(first)
    second = (input("What is the next chord?").upper())
    second_form = ((input("What is the scaleform of the second chord? Major, Minor, Diminished, etc.").upper()))
    set_one.append(second)
    third = (input("What is the next chord?").upper())
    third_form = ((input("What is the scaleform of the third chord? Major, Minor, Diminished, etc.").upper()))
    set_one.append(third)
    finish = (input("Do you have any more chords to input").upper())
    while finish != "NO":
        addition = (input("What is the next chord?").upper())
        set_one.append(addition)
        finish = (input("Do you have any more chords?").upper())
        if finish == "NO":
            break
        elif len(set_one) >= 8:
            break
    ##TODO: Write something that will compare set_one to all other keys. Something like, if we take the chords that have
    ##TODO: been given as an input, then compare those chords against each other to figure out the important notes.
    ##TODO: Then take those notes deemed as important, which were shared by all of the chords listed, and use those to
    ##TODO: isolate possible keys and give the possibilities as a percentage where the percentage is how much the notes
    ##TODO: in the chords given match up to the possible scales.

    group = []
    chord_one = chords(first, first_form)
    group.append(chord_one)
    chord_two = chords(second, second_form)
    group.append(chord_two)
    chord_three = chords(third, third_form)
    group.append(chord_three)
    x = [e for i, e in enumerate(group) if i in major_scale(first)]
    print(x)


def program():
    inquiry = input("Would you like to know a scale or a chord?").upper()
    if inquiry == "SCALE":
        return scale_giver()
    elif inquiry == "CHORD":
        return chord_giver()

    again = input("Do you want to find information about another key? Yes or No?").upper()
    if again == "YES":
        return (program())
    else:
        print("Thanks for your interest!")
print (program())