class CharacterSetHelper:
    # Created b/c sometimes JSON import doesn't work.
    def __init__(self):  
        self.basic = {
    "a": [
        "а",
        "à",
        "á",
        "ạ",
        "ą"
    ],
    "c": [
        "с",
        "ƈ",
        "ċ"
    ],
    "d": [
        "ԁ",
        "ɗ"
    ],
    "e": [
        "е",
        "ẹ",
        "ė",
        "ė",
        "é",
        "è"
    ],
    "g": [
        "ġ"
    ],
    "h": [
        "һ"
    ],
    "i": [
        "і",
        "í",
        "ì",
        "ï"
    ],
    "j": [
        "ј",
        "ʝ"
    ],
    "k": [
        "κ"
    ],
    "l": [
        "ӏ",
        "ḷ"
    ],
    "n": [
        "ո"
    ],
    "o": [
        "о",
        "ο",
        "օ",
        "ȯ",
        "ọ",
        "ỏ",
        "ơ",
        "ö",
        "ó",
        "ò"
    ],
    "p": [
        "р"
    ],
    "q": [
        "զ"
    ],
    "s": [
        "ʂ"
    ],
    "u": [
        "υ",
        "ս",
        "ü",
        "ú",
        "ù"
    ],
    "v": [
        "ν",
        "ѵ"
    ],
    "x": [
        "х",
        "ҳ"
    ],
    "y": [
        "у",
        "ý"
    ],
    "z": [
        "ʐ",
        "ż"
    ]
        }
        self.full = {
            "a": [
                "⍺",
                "ａ",
                "𝐚",
                "𝑎",
                "𝒂",
                "𝒶",
                "𝓪",
                "𝔞",
                "𝕒",
                "𝖆",
                "𝖺",
                "𝗮",
                "𝘢",
                "𝙖",
                "𝚊",
                "ɑ",
                "α",
                "𝛂",
                "𝛼",
                "𝜶",
                "𝝰",
                "𝞪",
                "а"
            ],
            "b": [
                "𝐛",
                "𝑏",
                "𝒃",
                "𝒷",
                "𝓫",
                "𝔟",
                "𝕓",
                "𝖇",
                "𝖻",
                "𝗯",
                "𝘣",
                "𝙗",
                "𝚋",
                "Ƅ",
                "Ь",
                "Ꮟ",
                "ᑲ",
                "ᖯ"
            ],
            "c": [
                "ｃ",
                "ⅽ",
                "𝐜",
                "𝑐",
                "𝒄",
                "𝒸",
                "𝓬",
                "𝔠",
                "𝕔",
                "𝖈",
                "𝖼",
                "𝗰",
                "𝘤",
                "𝙘",
                "𝚌",
                "ᴄ",
                "ϲ",
                "ⲥ",
                "с",
                "ꮯ",
                "𐐽"
            ],
            "d": [
                "ⅾ",
                "ⅆ",
                "𝐝",
                "𝑑",
                "𝒅",
                "𝒹",
                "𝓭",
                "𝔡",
                "𝕕",
                "𝖉",
                "𝖽",
                "𝗱",
                "𝘥",
                "𝙙",
                "𝚍",
                "ԁ",
                "Ꮷ",
                "ᑯ",
                "ꓒ"
            ],
            "e": [
                "℮",
                "ｅ",
                "ℯ",
                "ⅇ",
                "𝐞",
                "𝑒",
                "𝒆",
                "𝓮",
                "𝔢",
                "𝕖",
                "𝖊",
                "𝖾",
                "𝗲",
                "𝘦",
                "𝙚",
                "𝚎",
                "ꬲ",
                "е",
                "ҽ"
            ],
            "f": [
                "𝐟",
                "𝑓",
                "𝒇",
                "𝒻",
                "𝓯",
                "𝔣",
                "𝕗",
                "𝖋",
                "𝖿",
                "𝗳",
                "𝘧",
                "𝙛",
                "𝚏",
                "ꬵ",
                "ꞙ",
                "ſ",
                "ẝ",
                "ք"
            ],
            "g": [
                "ｇ",
                "ℊ",
                "𝐠",
                "𝑔",
                "𝒈",
                "𝓰",
                "𝔤",
                "𝕘",
                "𝖌",
                "𝗀",
                "𝗴",
                "𝘨",
                "𝙜",
                "𝚐",
                "ɡ",
                "ᶃ",
                "ƍ",
                "ց"
            ],
            "h": [
                "ｈ",
                "ℎ",
                "𝐡",
                "𝒉",
                "𝒽",
                "𝓱",
                "𝔥",
                "𝕙",
                "𝖍",
                "𝗁",
                "𝗵",
                "𝘩",
                "𝙝",
                "𝚑",
                "һ",
                "հ",
                "Ꮒ"
            ],
            "i": [
                "˛",
                "⍳",
                "ｉ",
                "ⅰ",
                "ℹ",
                "ⅈ",
                "𝐢",
                "𝑖",
                "𝒊",
                "𝒾",
                "𝓲",
                "𝔦",
                "𝕚",
                "𝖎",
                "𝗂",
                "𝗶",
                "𝘪",
                "𝙞",
                "𝚒",
                "ı",
                "𝚤",
                "ɪ",
                "ɩ",
                "ι",
                "ι",
                "ͺ",
                "𝛊",
                "𝜄",
                "𝜾",
                "𝝸",
                "𝞲",
                "і",
                "ꙇ",
                "ӏ",
                "ꭵ",
                "Ꭵ",
                "𑣃"
            ],
            "j": [
                "ｊ",
                "ⅉ",
                "𝐣",
                "𝑗",
                "𝒋",
                "𝒿",
                "𝓳",
                "𝔧",
                "𝕛",
                "𝖏",
                "𝗃",
                "𝗷",
                "𝘫",
                "𝙟",
                "𝚓",
                "ϳ",
                "ј"
            ],
            "k": [
                "𝐤",
                "𝑘",
                "𝒌",
                "𝓀",
                "𝓴",
                "𝔨",
                "𝕜",
                "𝖐",
                "𝗄",
                "𝗸",
                "𝘬",
                "𝙠",
                "𝚔"
            ],
            "l": [
                "‎׀‎",
                "|",
                "∣",
                "⏽",
                "￨",
                "1",
                "‎١‎",
                "۱",
                "𐌠",
                "‎𞣇‎",
                "𝟏",
                "𝟙",
                "𝟣",
                "𝟭",
                "𝟷",
                "🯱",
                "Ｉ",
                "Ⅰ",
                "ℐ",
                "ℑ",
                "𝐈",
                "𝐼",
                "𝑰",
                "𝓘",
                "𝕀",
                "𝕴",
                "𝖨",
                "𝗜",
                "𝘐",
                "𝙄",
                "𝙸",
                "Ɩ",
                "ｌ",
                "ⅼ",
                "ℓ",
                "𝐥",
                "𝑙",
                "𝒍",
                "𝓁",
                "𝓵",
                "𝔩",
                "𝕝",
                "𝖑",
                "𝗅",
                "𝗹",
                "𝘭",
                "𝙡",
                "𝚕",
                "ǀ",
                "Ι",
                "𝚰",
                "𝛪",
                "𝜤",
                "𝝞",
                "𝞘",
                "Ⲓ",
                "І",
                "Ӏ",
                "‎ו‎",
                "‎ן‎",
                "‎ا‎",
                "‎𞸀‎",
                "‎𞺀‎",
                "‎ﺎ‎",
                "‎ﺍ‎",
                "‎ߊ‎",
                "ⵏ",
                "ᛁ",
                "ꓲ",
                "𖼨",
                "𐊊",
                "𐌉"
            ],
            "m": [
                "rn"
            ],
            "n": [
                "𝐧",
                "𝑛",
                "𝒏",
                "𝓃",
                "𝓷",
                "𝔫",
                "𝕟",
                "𝖓",
                "𝗇",
                "𝗻",
                "𝘯",
                "𝙣",
                "𝚗",
                "ո",
                "ռ"
            ],
            "o": [
                "ం",
                "ಂ",
                "ം",
                "ං",
                "०",
                "੦",
                "૦",
                "௦",
                "౦",
                "೦",
                "൦",
                "๐",
                "໐",
                "၀",
                "‎٥‎",
                "۵",
                "ｏ",
                "ℴ",
                "𝐨",
                "𝑜",
                "𝒐",
                "𝓸",
                "𝔬",
                "𝕠",
                "𝖔",
                "𝗈",
                "𝗼",
                "𝘰",
                "𝙤",
                "𝚘",
                "ᴏ",
                "ᴑ",
                "ꬽ",
                "ο",
                "𝛐",
                "𝜊",
                "𝝄",
                "𝝾",
                "𝞸",
                "σ",
                "𝛔",
                "𝜎",
                "𝝈",
                "𝞂",
                "𝞼",
                "ⲟ",
                "о",
                "ჿ",
                "օ",
                "‎ס‎",
                "‎ه‎",
                "‎𞸤‎",
                "‎𞹤‎",
                "‎𞺄‎",
                "‎ﻫ‎",
                "‎ﻬ‎",
                "‎ﻪ‎",
                "‎ﻩ‎",
                "‎ھ‎",
                "‎ﮬ‎",
                "‎ﮭ‎",
                "‎ﮫ‎",
                "‎ﮪ‎",
                "‎ہ‎",
                "‎ﮨ‎",
                "‎ﮩ‎",
                "‎ﮧ‎",
                "‎ﮦ‎",
                "‎ە‎",
                "ഠ",
                "ဝ",
                "𐓪",
                "𑣈",
                "𑣗",
                "𐐬"
            ],
            "p": [
                "⍴",
                "ｐ",
                "𝐩",
                "𝑝",
                "𝒑",
                "𝓅",
                "𝓹",
                "𝔭",
                "𝕡",
                "𝖕",
                "𝗉",
                "𝗽",
                "𝘱",
                "𝙥",
                "𝚙",
                "ρ",
                "ϱ",
                "𝛒",
                "𝛠",
                "𝜌",
                "𝜚",
                "𝝆",
                "𝝔",
                "𝞀",
                "𝞎",
                "𝞺",
                "𝟈",
                "ⲣ",
                "р"
            ],
            "q": [
                "𝐪",
                "𝑞",
                "𝒒",
                "𝓆",
                "𝓺",
                "𝔮",
                "𝕢",
                "𝖖",
                "𝗊",
                "𝗾",
                "𝘲",
                "𝙦",
                "𝚚",
                "ԛ",
                "գ",
                "զ"
            ],
            "r": [
                "𝐫",
                "𝑟",
                "𝒓",
                "𝓇",
                "𝓻",
                "𝔯",
                "𝕣",
                "𝖗",
                "𝗋",
                "𝗿",
                "𝘳",
                "𝙧",
                "𝚛",
                "ꭇ",
                "ꭈ",
                "ᴦ",
                "ⲅ",
                "г",
                "ꮁ"
            ],
            "s": [
                "ｓ",
                "𝐬",
                "𝑠",
                "𝒔",
                "𝓈",
                "𝓼",
                "𝔰",
                "𝕤",
                "𝖘",
                "𝗌",
                "𝘀",
                "𝘴",
                "𝙨",
                "𝚜",
                "ꜱ",
                "ƽ",
                "ѕ",
                "ꮪ",
                "𑣁",
                "𐑈"
            ],
            "t": [
                "𝐭",
                "𝑡",
                "𝒕",
                "𝓉",
                "𝓽",
                "𝔱",
                "𝕥",
                "𝖙",
                "𝗍",
                "𝘁",
                "𝘵",
                "𝙩",
                "𝚝"
            ],
            "u": [
                "𝐮",
                "𝑢",
                "𝒖",
                "𝓊",
                "𝓾",
                "𝔲",
                "𝕦",
                "𝖚",
                "𝗎",
                "𝘂",
                "𝘶",
                "𝙪",
                "𝚞",
                "ꞟ",
                "ᴜ",
                "ꭎ",
                "ꭒ",
                "ʋ",
                "υ",
                "𝛖",
                "𝜐",
                "𝝊",
                "𝞄",
                "𝞾",
                "ս",
                "𐓶",
                "𑣘"
            ],
            "v": [
                "∨",
                "⋁",
                "ｖ",
                "ⅴ",
                "𝐯",
                "𝑣",
                "𝒗",
                "𝓋",
                "𝓿",
                "𝔳",
                "𝕧",
                "𝖛",
                "𝗏",
                "𝘃",
                "𝘷",
                "𝙫",
                "𝚟",
                "ᴠ",
                "ν",
                "𝛎",
                "𝜈",
                "𝝂",
                "𝝼",
                "𝞶",
                "ѵ",
                "‎ט‎",
                "𑜆",
                "ꮩ",
                "𑣀"
            ],
            "w": [
                "ɯ",
                "𝐰",
                "𝑤",
                "𝒘",
                "𝓌",
                "𝔀",
                "𝔴",
                "𝕨",
                "𝖜",
                "𝗐",
                "𝘄",
                "𝘸",
                "𝙬",
                "𝚠",
                "ᴡ",
                "ѡ",
                "ԝ",
                "ա",
                "𑜊",
                "𑜎",
                "𑜏",
                "ꮃ"
            ],
            "x": [
                "᙮",
                "×",
                "⤫",
                "⤬",
                "⨯",
                "ｘ",
                "ⅹ",
                "𝐱",
                "𝑥",
                "𝒙",
                "𝓍",
                "𝔁",
                "𝔵",
                "𝕩",
                "𝖝",
                "𝗑",
                "𝘅",
                "𝘹",
                "𝙭",
                "𝚡",
                "х",
                "ᕁ",
                "ᕽ"
            ],
            "y": [
                "ɣ",
                "ᶌ",
                "ｙ",
                "𝐲",
                "𝑦",
                "𝒚",
                "𝓎",
                "𝔂",
                "𝔶",
                "𝕪",
                "𝖞",
                "𝗒",
                "𝘆",
                "𝘺",
                "𝙮",
                "𝚢",
                "ʏ",
                "ỿ",
                "ꭚ",
                "γ",
                "ℽ",
                "𝛄",
                "𝛾",
                "𝜸",
                "𝝲",
                "𝞬",
                "у",
                "ү",
                "ყ",
                "𑣜"
            ],
            "z": [
                "𝐳",
                "𝑧",
                "𝒛",
                "𝓏",
                "𝔃",
                "𝔷",
                "𝕫",
                "𝖟",
                "𝗓",
                "𝘇",
                "𝘻",
                "𝙯",
                "𝚣",
                "ᴢ",
                "ꮓ",
                "𑣄"
            ],
            "A": [
                "Ａ",
                "𝐀",
                "𝐴",
                "𝑨",
                "𝒜",
                "𝓐",
                "𝔄",
                "𝔸",
                "𝕬",
                "𝖠",
                "𝗔",
                "𝘈",
                "𝘼",
                "𝙰",
                "Α",
                "𝚨",
                "𝛢",
                "𝜜",
                "𝝖",
                "𝞐",
                "А",
                "Ꭺ",
                "ᗅ",
                "ꓮ",
                "𖽀",
                "𐊠"
            ],
            "B": [
                "Ｂ",
                "ℬ",
                "𝐁",
                "𝐵",
                "𝑩",
                "𝓑",
                "𝔅",
                "𝔹",
                "𝕭",
                "𝖡",
                "𝗕",
                "𝘉",
                "𝘽",
                "𝙱",
                "Ꞵ",
                "Β",
                "𝚩",
                "𝛣",
                "𝜝",
                "𝝗",
                "𝞑",
                "В",
                "Ᏼ",
                "ᗷ",
                "ꓐ",
                "𐊂",
                "𐊡",
                "𐌁"
            ],
            "C": [
                "🝌",
                "𑣲",
                "𑣩",
                "Ｃ",
                "Ⅽ",
                "ℂ",
                "ℭ",
                "𝐂",
                "𝐶",
                "𝑪",
                "𝒞",
                "𝓒",
                "𝕮",
                "𝖢",
                "𝗖",
                "𝘊",
                "𝘾",
                "𝙲",
                "Ϲ",
                "Ⲥ",
                "С",
                "Ꮯ",
                "ꓚ",
                "𐊢",
                "𐌂",
                "𐐕",
                "𐔜"
            ],
            "D": [
                "Ⅾ",
                "ⅅ",
                "𝐃",
                "𝐷",
                "𝑫",
                "𝒟",
                "𝓓",
                "𝔇",
                "𝔻",
                "𝕯",
                "𝖣",
                "𝗗",
                "𝘋",
                "𝘿",
                "𝙳",
                "Ꭰ",
                "ᗞ",
                "ᗪ",
                "ꓓ"
            ],
            "E": [
                "⋿",
                "Ｅ",
                "ℰ",
                "𝐄",
                "𝐸",
                "𝑬",
                "𝓔",
                "𝔈",
                "𝔼",
                "𝕰",
                "𝖤",
                "𝗘",
                "𝘌",
                "𝙀",
                "𝙴",
                "Ε",
                "𝚬",
                "𝛦",
                "𝜠",
                "𝝚",
                "𝞔",
                "Е",
                "ⴹ",
                "Ꭼ",
                "ꓰ",
                "𑢦",
                "𑢮",
                "𐊆"
            ],
            "F": [
                "𝈓",
                "ℱ",
                "𝐅",
                "𝐹",
                "𝑭",
                "𝓕",
                "𝔉",
                "𝔽",
                "𝕱",
                "𝖥",
                "𝗙",
                "𝘍",
                "𝙁",
                "𝙵",
                "Ꞙ",
                "Ϝ",
                "𝟊",
                "ᖴ",
                "ꓝ",
                "𑣂",
                "𑢢",
                "𐊇",
                "𐊥",
                "𐔥"
            ],
            "G": [
                "𝐆",
                "𝐺",
                "𝑮",
                "𝒢",
                "𝓖",
                "𝔊",
                "𝔾",
                "𝕲",
                "𝖦",
                "𝗚",
                "𝘎",
                "𝙂",
                "𝙶",
                "Ԍ",
                "Ꮐ",
                "Ᏻ",
                "ꓖ"
            ],
            "H": [
                "Ｈ",
                "ℋ",
                "ℌ",
                "ℍ",
                "𝐇",
                "𝐻",
                "𝑯",
                "𝓗",
                "𝕳",
                "𝖧",
                "𝗛",
                "𝘏",
                "𝙃",
                "𝙷",
                "Η",
                "𝚮",
                "𝛨",
                "𝜢",
                "𝝜",
                "𝞖",
                "Ⲏ",
                "Н",
                "Ꮋ",
                "ᕼ",
                "ꓧ",
                "𐋏"
            ],
            "I": [
                "l"
            ],
            "J": [
                "Ｊ",
                "𝐉",
                "𝐽",
                "𝑱",
                "𝒥",
                "𝓙",
                "𝔍",
                "𝕁",
                "𝕵",
                "𝖩",
                "𝗝",
                "𝘑",
                "𝙅",
                "𝙹",
                "Ʝ",
                "Ϳ",
                "Ј",
                "Ꭻ",
                "ᒍ",
                "ꓙ"
            ],
            "K": [
                "K",
                "Ｋ",
                "𝐊",
                "𝐾",
                "𝑲",
                "𝒦",
                "𝓚",
                "𝔎",
                "𝕂",
                "𝕶",
                "𝖪",
                "𝗞",
                "𝘒",
                "𝙆",
                "𝙺",
                "Κ",
                "𝚱",
                "𝛫",
                "𝜥",
                "𝝟",
                "𝞙",
                "Ⲕ",
                "К",
                "Ꮶ",
                "ᛕ",
                "ꓗ",
                "𐔘"
            ],
            "L": [
                "𝈪",
                "Ⅼ",
                "ℒ",
                "𝐋",
                "𝐿",
                "𝑳",
                "𝓛",
                "𝔏",
                "𝕃",
                "𝕷",
                "𝖫",
                "𝗟",
                "𝘓",
                "𝙇",
                "𝙻",
                "Ⳑ",
                "Ꮮ",
                "ᒪ",
                "ꓡ",
                "𖼖",
                "𑢣",
                "𑢲",
                "𐐛",
                "𐔦"
            ],
            "M": [
                "Ｍ",
                "Ⅿ",
                "ℳ",
                "𝐌",
                "𝑀",
                "𝑴",
                "𝓜",
                "𝔐",
                "𝕄",
                "𝕸",
                "𝖬",
                "𝗠",
                "𝘔",
                "𝙈",
                "𝙼",
                "Μ",
                "𝚳",
                "𝛭",
                "𝜧",
                "𝝡",
                "𝞛",
                "Ϻ",
                "Ⲙ",
                "М",
                "Ꮇ",
                "ᗰ",
                "ᛖ",
                "ꓟ",
                "𐊰",
                "𐌑"
            ],
            "N": [
                "Ｎ",
                "ℕ",
                "𝐍",
                "𝑁",
                "𝑵",
                "𝒩",
                "𝓝",
                "𝔑",
                "𝕹",
                "𝖭",
                "𝗡",
                "𝘕",
                "𝙉",
                "𝙽",
                "Ν",
                "𝚴",
                "𝛮",
                "𝜨",
                "𝝢",
                "𝞜",
                "Ⲛ",
                "ꓠ",
                "𐔓"
            ],
            "O": [
                "0",
                "‎߀‎",
                "০",
                "୦",
                "〇",
                "𑓐",
                "𑣠",
                "𝟎",
                "𝟘",
                "𝟢",
                "𝟬",
                "𝟶",
                "🯰",
                "Ｏ",
                "𝐎",
                "𝑂",
                "𝑶",
                "𝒪",
                "𝓞",
                "𝔒",
                "𝕆",
                "𝕺",
                "𝖮",
                "𝗢",
                "𝘖",
                "𝙊",
                "𝙾",
                "Ο",
                "𝚶",
                "𝛰",
                "𝜪",
                "𝝤",
                "𝞞",
                "Ⲟ",
                "О",
                "Օ",
                "ⵔ",
                "ዐ",
                "ଠ",
                "𐓂",
                "ꓳ",
                "𑢵",
                "𐊒",
                "𐊫",
                "𐐄",
                "𐔖"
            ],
            "P": [
                "Ｐ",
                "ℙ",
                "𝐏",
                "𝑃",
                "𝑷",
                "𝒫",
                "𝓟",
                "𝔓",
                "𝕻",
                "𝖯",
                "𝗣",
                "𝘗",
                "𝙋",
                "𝙿",
                "Ρ",
                "𝚸",
                "𝛲",
                "𝜬",
                "𝝦",
                "𝞠",
                "Ⲣ",
                "Р",
                "Ꮲ",
                "ᑭ",
                "ꓑ",
                "𐊕"
            ],
            "Q": [
                "ℚ",
                "𝐐",
                "𝑄",
                "𝑸",
                "𝒬",
                "𝓠",
                "𝔔",
                "𝕼",
                "𝖰",
                "𝗤",
                "𝘘",
                "𝙌",
                "𝚀",
                "ⵕ"
            ],
            "R": [
                "𝈖",
                "ℛ",
                "ℜ",
                "ℝ",
                "𝐑",
                "𝑅",
                "𝑹",
                "𝓡",
                "𝕽",
                "𝖱",
                "𝗥",
                "𝘙",
                "𝙍",
                "𝚁",
                "Ʀ",
                "Ꭱ",
                "Ꮢ",
                "𐒴",
                "ᖇ",
                "ꓣ",
                "𖼵"
            ],
            "S": [
                "Ｓ",
                "𝐒",
                "𝑆",
                "𝑺",
                "𝒮",
                "𝓢",
                "𝔖",
                "𝕊",
                "𝕾",
                "𝖲",
                "𝗦",
                "𝘚",
                "𝙎",
                "𝚂",
                "Ѕ",
                "Տ",
                "Ꮥ",
                "Ꮪ",
                "ꓢ",
                "𖼺",
                "𐊖",
                "𐐠"
            ],
            "T": [
                "⊤",
                "⟙",
                "🝨",
                "Ｔ",
                "𝐓",
                "𝑇",
                "𝑻",
                "𝒯",
                "𝓣",
                "𝔗",
                "𝕋",
                "𝕿",
                "𝖳",
                "𝗧",
                "𝘛",
                "𝙏",
                "𝚃",
                "Τ",
                "𝚻",
                "𝛵",
                "𝜯",
                "𝝩",
                "𝞣",
                "Ⲧ",
                "Т",
                "Ꭲ",
                "ꓔ",
                "𖼊",
                "𑢼",
                "𐊗",
                "𐊱",
                "𐌕"
            ],
            "U": [
                "∪",
                "⋃",
                "𝐔",
                "𝑈",
                "𝑼",
                "𝒰",
                "𝓤",
                "𝔘",
                "𝕌",
                "𝖀",
                "𝖴",
                "𝗨",
                "𝘜",
                "𝙐",
                "𝚄",
                "Ս",
                "ሀ",
                "𐓎",
                "ᑌ",
                "ꓴ",
                "𖽂",
                "𑢸"
            ],
            "V": [
                "𝈍",
                "‎٧‎",
                "۷",
                "Ⅴ",
                "𝐕",
                "𝑉",
                "𝑽",
                "𝒱",
                "𝓥",
                "𝔙",
                "𝕍",
                "𝖁",
                "𝖵",
                "𝗩",
                "𝘝",
                "𝙑",
                "𝚅",
                "Ѵ",
                "ⴸ",
                "Ꮩ",
                "ᐯ",
                "ꛟ",
                "ꓦ",
                "𖼈",
                "𑢠",
                "𐔝"
            ],
            "W": [
                "𑣯",
                "𑣦",
                "𝐖",
                "𝑊",
                "𝑾",
                "𝒲",
                "𝓦",
                "𝔚",
                "𝕎",
                "𝖂",
                "𝖶",
                "𝗪",
                "𝘞",
                "𝙒",
                "𝚆",
                "Ԝ",
                "Ꮃ",
                "Ꮤ",
                "ꓪ"
            ],
            "X": [
                "᙭",
                "╳",
                "𐌢",
                "𑣬",
                "Ｘ",
                "Ⅹ",
                "𝐗",
                "𝑋",
                "𝑿",
                "𝒳",
                "𝓧",
                "𝔛",
                "𝕏",
                "𝖃",
                "𝖷",
                "𝗫",
                "𝘟",
                "𝙓",
                "𝚇",
                "Ꭓ",
                "Χ",
                "𝚾",
                "𝛸",
                "𝜲",
                "𝝬",
                "𝞦",
                "Ⲭ",
                "Х",
                "ⵝ",
                "ᚷ",
                "ꓫ",
                "𐊐",
                "𐊴",
                "𐌗",
                "𐔧"
            ],
            "Y": [
                "Ｙ",
                "𝐘",
                "𝑌",
                "𝒀",
                "𝒴",
                "𝓨",
                "𝔜",
                "𝕐",
                "𝖄",
                "𝖸",
                "𝗬",
                "𝘠",
                "𝙔",
                "𝚈",
                "Υ",
                "ϒ",
                "𝚼",
                "𝛶",
                "𝜰",
                "𝝪",
                "𝞤",
                "Ⲩ",
                "У",
                "Ү",
                "Ꭹ",
                "Ꮍ",
                "ꓬ",
                "𖽃",
                "𑢤",
                "𐊲"
            ],
            "Z": [
                "𐋵",
                "𑣥",
                "Ｚ",
                "ℤ",
                "ℨ",
                "𝐙",
                "𝑍",
                "𝒁",
                "𝒵",
                "𝓩",
                "𝖅",
                "𝖹",
                "𝗭",
                "𝘡",
                "𝙕",
                "𝚉",
                "Ζ",
                "𝚭",
                "𝛧",
                "𝜡",
                "𝝛",
                "𝞕",
                "Ꮓ",
                "ꓜ",
                "𑢩"
            ],
            "ij": [
                "ĳ"
            ],
            "st": [
                "ﬆ"
            ]
        }

    def get_basic(self): return self.basic
    def get_full(self): return self.full


if __name__ == "__main__":
    set_received = CharacterSetHelper().get_full()
    print(set_received["a"][0])
