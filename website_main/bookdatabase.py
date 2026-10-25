import json

# key:value pairs of isbn:[characters]
isbn_database = {
    123456: ["Sonic"],                  #test
    0140126708: ["Old Major"]  ,         # animal farm
    0439136369: ["Harry Potter"],            #Harry Potter and the Prisoner of Azkaban
    #059035342X: ["Harry Potter"],           # Harry Potter and the Sorcerer's Stone; note: ISBN contains alphanum
    0345339681: ["Bilbo Baggins"],           # The Hobbit
    0446310786: ["Mockingbird"],             # To Kill a Mockingbird
    0140177396: ["George and Lennie"],       # Of Mice and Men
    9780439023511: ["Katniss Everdeen"],     # Hunger Games: Mockingjay
    9780141439730: ["Hyde"],                 # The Strange Case of Dr Jekyll and Mr Hyde and Other Tales of Terror
    9780241447383: ["Michelle Obama"]       # The Extraordinary Life of Michelle Obama
}

# key:value pairs of character:[health:int, attackname:str, attackdamage]
char_database = {
    "Sonic": [100, "spin jump", 20],

    "Harry Potter": [120, "magic", 35],

    "Bilbo Baggins": [160, "rock throwing", 40],

    "Mockingbird": [60, "rapid pecking", 35],

    "George and Lennie": [230, "dropkick", 40],

    "Katniss Everdeen": [140, "bow and arrow", 60],

    "Hyde": [200, "slash", 50],

    "Michelle Obama": [5, "force feeds school lunch", 500]


}
