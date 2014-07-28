class Game(object):

    def __init__(self, home, away):
        self.home = home
        self.away = away

    def winner(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score
        if self.home_score > self.away_score:
            return "Home Team"
        elif self.home_score == self.away_score:
            return "Tie"
        else:
            return "Away Team"

    def margin(self):
        result = self.home_score - self.away_score
        return result

    def display(self):
        return "%s Vs %s" % (self.home.name, self.away.name)


class Team(object):

    def __init__(self, name, venue, est):
        self.name = name
        self.venue = venue
        self.est = est
        self.players = []
        self.the_bench = []

    def starting_five(self, player):
        if len(self.players) < 5 and player not in self.players:
            self.players.append(player)
        elif player not in self.the_bench and player not in self.players:
            return self.the_bench.append(player)

    def subs(self, on=None, off=None):
        self.players.remove(off)
        self.the_bench.append(off)
        if on in self.the_bench:
            self.players.append(on)
            self.the_bench.remove(on)

    def reserves(self):
        return self.the_bench


    def starters(self):
        return self.players


class Player(object):
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def player_age(self):
        self.age = 0

    def player_num(self):
        self.number = 0

    def current_age(self):
        #self.dob is current date of birth
        current_year = 2014
        current = current_year - self.dob
        return current