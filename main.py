from optparse import Values
from random import shuffle
from urllib import response

class Card:
    suits=["Spades","Hearts","Diamonds","Clubs"]
    values=[None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    def __init__(self,v,s):
        self.values=v
        self.suits=s
    def __lt__(self,c2):
        if self.values < c2.values:
            return True
        if self.values==c2.values:
            if self.suits < c2.suits:
                return True
            else:
                return False
        return False
    def __gt__(self,c2):
        if self.values > c2.values:
            return True
        if self.values == c2.values:
            if self.suits > c2.suits:
                return True
            else:
                return False
        return False
    
class Deck:
    def __init__(self):
        self.cards=[]
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards)==0:
            return()
        else:
            return self.cards.pop()

class Player:
    def __init__(self,name):
        self.win=0
        self.card=None
        self.name=name

class Game:
    def __init__(self):
        name1=input("Enter Player 1 name: ")
        name2=input("Enter Player 2 name: ")
        self.decks=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)
    def win(self,winner):
        w='{} wins this round'
        w=w.format(winner)
        print(w)
    def draw(self,p1n,p1c,p2n,p2c):
        d="{} Drew {} and {} Drew {}"
        d=d.format(p1n,p1c.values,p2n,p2c.values)
        print(d)
    def play_game(self):
        cards=self.decks.cards
        print("Begin Game")
        while len(cards) >= 2:
            n="Q to quit or any key to play "
            response=input(n)
            if response == 'q':
                break
            p1c=self.decks.rm_card()
            p2c=self.decks.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c>p2c:
                self.p1.win+=1
                self.win(self.p1.name)
            elif p2c>p1c:
                self.p2.win+=1
                self.win(self.p2.name)
            else:
                print('Draw')
        win=self.winner(self.p1,self.p2)
        print('War is over.{} wins'.format(win))
    def winner(self,p1,p2):
        if p1.win > p2.win:
            return p1.name
        if p1.win < p2.win:
            return p2.name
        return 'It is a tie'
game=Game()
game.play_game()