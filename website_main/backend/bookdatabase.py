import json

# key:value pairs of isbn:character
isbn_database = {
    9789849608806: "Sonic",                # test
    9780140126709: "Old_Major",            # Animal Farm
    78073007998: "Harry_Potter",           # Harry Potter and the Prisoner of Azkaban
    10999007997: "Bilbo_Baggins",          # The Hobbit
    9780140177398: "George_and_Lennie",    # Of Mice and Men
    9780439023511: "Katniss_Everdeen",     # Hunger Games: Mockingjay
    9780143106357: "Big_Joao",             # Jorge Amada
    9780241447383: "Michelle_Obama",       # Michelle Obama (Shocking!)
    9781551113531: "Ice_Cube",             # War of the worlds
    9780141439730: "Hyde"                  # Dr. Jekyll and Mr. Hyde
}

# key:value pairs of character:[health:int, attackname:str, attackdamage: int]
char_database = {
    "Sonic": [100, "spin jump", 20],

    "Old_Major": [160, "bite", 40],

    "Harry_Potter": [120, "magic", 35],

    "Bilbo_Baggins": [160, "rock throwing", 40],

    "George_and_Lennie": [230, "dropkick", 40],

    "Katniss_Everdeen": [140, "bow and arrow", 60],

    "Michelle_Obama": [5, "force feeds school lunch", 500],

    "Big_Joao": [150, "punch", 30],

    "Ice_Cube": [140, "dropkick", 30],

    "Hyde": [200, "slash", 50]

}
