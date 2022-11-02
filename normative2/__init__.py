from otree.api import *
import csv
import random




doc = """
fee
"""


class Constants(BaseConstants):
    name_in_url = 'nor2'
    duration = 10
    fee = 1
    bonus = 5.00
    players_per_group = None
    num_rounds = 5
    instructions_template = 'Intro/instructions.html'
    # """Amount allocated to each player"""
    rounds = 5
    roundshow= 26
    contact = 'Intro/contact.html'
    example = 'Intro/case1.html'
    papercups_template = 'Intro/papercups.html'
    timeout = 5
    case = 'Intro/case.html'
    info = 'fine/info.html'
    cases = [
        [4, 170, 730, 430, 95],
        [1, 270, 730, 330, 85],
        [5, 550, 350, 150, 65],
        [2, 650, 350, 150, 40],
        [3, 620, 210, 150, 15],
         ]


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            player.participant.seed = random.random()

    for player in subsession.get_players():
        random.seed(player.participant.seed)
        l1 = random.sample([1, 2, 3, 4, 5], 5)
        teste=(player.round_number)-1
        case=l1[teste]-1
        player.case = Constants.cases[case][0]
        player.p1 = Constants.cases[case][1]
        player.p2 =  Constants.cases[case][2]
        player.mean1 = Constants.cases[case][3]
        player.mean2 = Constants.cases[case][4]



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    case = models.IntegerField()
    p1 = models.IntegerField()
    p2 = models.IntegerField()
    norm1 = models.IntegerField(max=100, min=0)
    norm2 = models.IntegerField()
    mean1 = models.IntegerField()
    mean2 = models.IntegerField()

class decision(Page):
    form_model = 'player'
    form_fields = ['norm1', 'norm2']
    @staticmethod
    def vars_for_template(player: Player):
        return dict( case=player.case, p1 = player.p1, p2 = player.p2, mean= player.mean1)
    @staticmethod
    def js_vars(player: Player):
        return dict(jvp1 = player.p1, jvp2 = player.p2, case=player.case)

class instru(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


page_sequence = [instru, decision]
