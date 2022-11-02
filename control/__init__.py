from otree.api import *
import csv
import random




doc = """
experiment
"""


class Constants(BaseConstants):
    name_in_url = 'ctr'
    duration = 10
    fee = 1
    bonus = 5.00
    players_per_group = None
    num_rounds = 10
    instructions_template = 'Intro/instructions.html'
    # """Amount allocated to each player"""
    rounds = 1
    roundshow= 26
    contact = 'Intro/contact.html'
    example = 'Intro/case.html'
    papercups_template = 'Intro/papercups.html'
    timeout = 5
    case = 'Intro/case.html'
    cases = [
        [1, 100, 800],
        [2, 200, 800],
        [3, 170, 730],
        [4, 270, 730],
        [5, 550, 350],
        [6, 650, 350],
        [7, 600, 400],
        [8, 500, 400],
        [9, 360, 510],
        [10, 620, 210],
         ]


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            player.participant.seed = random.random()

    for player in subsession.get_players():
        random.seed(player.participant.seed)
        l1 = random.sample([1, 2, 3, 4, 5, 6, 7, 8 , 9, 10], 10)
        teste=(player.round_number)-1
        case=l1[teste]-1
        player.case = Constants.cases[case][0]
        player.p1 = Constants.cases[case][1]
        player.p2 =  Constants.cases[case][2]



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    case = models.IntegerField()
    p1 = models.IntegerField()
    p2 = models.IntegerField()
    decision = models.IntegerField()
    dictator = models.IntegerField()
    receiver = models.IntegerField()

class decision(Page):
    form_model = 'player'
    form_fields = ['decision','dictator','receiver']
    @staticmethod
    def vars_for_template(player: Player):
        return dict( p1 = player.p1, p2 = player.p2)
    @staticmethod
    def js_vars(player: Player):
        return dict(jvp1 = player.p1, jvp2 = player.p2)

page_sequence = [decision]
