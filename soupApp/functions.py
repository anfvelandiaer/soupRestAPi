import random

#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Directions are:
# +. left to right
# -. right to left
# .+ top to bottom
# .- bottom to top

def convertStr(string):
    newString = ''.join(string)
    newString = newString.replace("\'", "")
    newString = newString.replace("[", "")
    newString = newString.replace("]", "")
    newString = newString.split(", ")
    return newString

all_directions = ('+-', '+.', '++', '.+', '.-', '--', '-.', '-+')

dirconv = {
    '-': -1,
    '.': 0,
    '+': 1,
}

letters = u"abcdefghijklmnñopqrstuvwxyz"


class Grid(object):
    def __init__(self, wid, hgt):
        self.wid = wid
        self.hgt = hgt
        self.data = ['.'] * (wid * hgt)
        self.words = []
        self.positions = []
        self.hunts = []
        self.name = "intuition"
        self.wordsList = []

    def to_text(self):
        result = []
        for row in range(self.hgt):
            result.append(''.join(str(self.data[row * self.wid: (row + 1) * self.wid])))
        s = ','.join(result)
        s = s.replace("\'", "")
        s = s.replace("[", "")
        s = s.replace("]", "")
        s = s.replace(", ", ",")
        s = s.split(",")
        
        return {"matrix": s, "positions": self.positions, "hunts": self.hunts, "name": self.name, "words": self.wordsList}

    def pick_word_pos(self, wordlen, directions):
        xd, yd = random.choice(directions)
        minx = (wordlen - 1, 0, 0)[xd + 1]
        maxx = (self.wid - 1, self.wid - 1, self.wid - wordlen)[xd + 1]
        miny = (wordlen - 1, 0, 0)[yd + 1]
        maxy = (self.hgt - 1, self.hgt - 1, self.hgt - wordlen)[yd + 1]
        x = random.randint(minx, maxx)
        y = random.randint(miny, maxy)
        return x, y, xd, yd

    def write_word(self, word, ox, oy, xd, yd):
        x, y = ox, oy
        for c in word.decode():
            p = x + self.wid * y
            e = self.data[p]
            if e != '.' and e != c:
                return False
            x += xd
            y += yd

        x, y = ox, oy
        position = []
        for c in word.decode():
            p = x + self.wid * y
            if c != ']' and c != '[' and c != '\'':
                position.append(str(p))
                self.data[p] = c
                x += xd
                y += yd
        self.positions.append(position)
        return True

    def place_words(self, words, directions, wordsList, hunts, tries=100):
        # Sort words into descending order of length
        self.wordsList = wordsList
        self.hunts = hunts
        words = list(words)
        words.sort(key=lambda x: len(x), reverse=True)

        for word in words:
            wordlen = len(word)
            while True:
                x, y, xd, yd = self.pick_word_pos(wordlen, directions)
                if self.write_word(word, x, y, xd, yd):
                    self.words.append((word, x, y, xd, yd))
                    break
                tries -= 1
                if tries <= 0:
                    return False
        return True

    def fill_in_letters(self):
        for p in range(self.wid * self.hgt):
            if self.data[p] == '.':
                self.data[p] = random.choice(letters)


def make_grid(words=[], wordsList=[], hunts=[], tries=100,):
    # Parse and validate the style parameter.
    size, directions = ('15x15', all_directions)
    size = size.split('x')
    if len(size) != 2:
        raise ValueError("Invalid style parameter: %s" % stylep)
    try:
        wid, hgt = map(int, size)
    except ValueError:
        raise ValueError("Invalid style parameter: %s" % stylep)

    directions = [(dirconv[direction[0]], dirconv[direction[1]])
                  for direction in directions]

    while True:
        grid = Grid(wid, hgt)
        if grid.place_words(words, directions, wordsList, hunts):
            break
        tries -= 1
        if tries <= 0:
            return None

    grid.fill_in_letters()
    return grid


def makeTable(name, words, hunts):
    random.seed()
    newWords = convertStr(words)
    newHunts = convertStr(hunts)
    print(type(newWords))
    print(newWords)
    words_to_use = ["".join(str(w.lower().split())).encode('utf-8')
                    for w in newWords]
    grid = make_grid(words_to_use, newWords, newHunts)
    if grid is None:
        print("Can't make a grid")
    else:
        print(grid.to_text())
    
    return grid.to_text()
