from otree.api import *
import random

c = Currency  # old name for currency; you can delete this.

doc = """
experiment
"""


class Constants(BaseConstants):
    name_in_url = 'end'
    players_per_group = 2
    num_rounds = 1
    contact = 'Intro/contact.html'
    papercups_template = 'Intro/papercups.html'

class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    if subsession.round_number == 1:
        check = random.randint(0,20)
        for player in subsession.get_players():
            player.round=check
            player.rol=player.id_in_group


class Group(BaseGroup):
    pass

class Player(BasePlayer):
   exp=models.BooleanField(label="Have you ever participated in a similar experiment?")
   strategy = models.StringField(label="What motivated your decisions while taking points?")
   round = models.IntegerField()
   rol = models.IntegerField()


class end(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round=player.round, rol=player.rol)

class discussion(Page):
    form_model = 'player'
    form_fields = ['exp','strategy']


page_sequence = [discussion, end]
