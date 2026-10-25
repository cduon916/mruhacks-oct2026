import json

# key:value pairs of isbn:[characters]
isbn_database = {
    9789849608806: "Sonic",                # test
    9780140126709: "Old Major",            # Animal Farm
    78073006991: "Harry Potter",           # Harry Potter and the Prisoner of Azkaban
    10999007997: "Bilbo Baggins",          # The Hobbit
    9780140177398: "George and Lennie",    # Of Mice and Men
    9780439023511: "Katniss Everdeen",     # Hunger Games: Mockingjay
    9780143106357: "Big Joao",             # Jorge Amada
    9780241447383: "Michelle_Obama",       # Michelle Obama (Shocking!)
    9781551113531: "Ice Cube",             # War of the worlds
    9780141439730: "Hyde"                  # Dr. Jekyll and Mr. Hyde
}

# key:value pairs of character:[health:int, attackname:str, attackdamage]
char_database = {
    "Sonic": [100, "spin jump", 20],

    "Harry Potter": [120, "magic", 35],

    "Bilbo Baggins": [160, "rock throwing", 40],

    "George and Lennie": [230, "dropkick", 40],

    "Katniss Everdeen": [140, "bow and arrow", 60],

    "Hyde": [200, "slash", 50],

    "Michelle_Obama": [5, "force feeds school lunch", 500],

    "Big Joao": [150, "punch", 30],

    "Ice Cube": [140, "dropkick", 30]


}
