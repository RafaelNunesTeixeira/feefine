from otree.api import *



doc = """
experiment
"""


class Constants(BaseConstants):
    name_in_url = 'intro'
    duration = 15
    fee = 1.5
    bonus = 5.00
    players_per_group = None
    num_rounds = 1
    instructions_template = __name__ +'/instructions.html'
    # """Amount allocated to each player"""
    rounds = 1
    roundshow= 20
    contact = __name__ +'/contact.html'
    papercups_template = __name__ + '/papercups.html'
    timeout = 5
    example = __name__ + '/case1.html'
    example2 = __name__ + '/case2.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    ##check-up

    ans1 = models.IntegerField(
        choices=[
            [1, '300'],
            [2, '400'],
            [3, '700'],
        ],
        label='How many points does Individual 1 get IN TOTAL?',
        )

    ans2 = models.IntegerField(
        choices=[
            [1, '300'],
            [2, '1000'],
            [3, '700'],
        ],
        label='How many EXTRA points does Individual 1 earn by taking this value?',
    )

    q1 = models.IntegerField(
        choices=[[1, 'As participant 1, and considering the decisions in all rounds.'], [2, 'As participant 2, and considering the decision in the first round.'],[3, 'For a randomized role, and considering the decisions in a randomized round.'],[4,'For a randomized role, and considering the decisions in all rounds.']],
        widget=widgets.RadioSelect,
    )

    q3 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelect,
    )

    q4 = models.IntegerField(
        choices=[2, 4, 1, 8, 100, 200],
        widget=widgets.RadioSelect,
    )

    q5 = models.IntegerField(
        choices=[33, 888, 10, 100, 88, 8],
        widget=widgets.RadioSelect,
    )

# FUNCTIONS



class Introduction(Page):
   pass

class questions2(Page):
    form_model = 'player'
    form_fields = ['ans1','ans2']

    def error_message(self, values):
        if int(values['ans1']) != 2:
            return 'Question 1 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['ans2']) != 3:
            return 'Question 2 is wrong. Please, read again the instructions below and give the correct answer.'


class questions(Page):
    form_model = 'player'
    form_fields = ['q1','q3','q4','q5']

    def error_message(self, values):
        if int(values['q1']) != 3:
            return 'Question 1 is wrong. Please, read again the instructions below and give the correct answer.'

        if int(values['q3']) != 1:
            return 'Question 2 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['q4']) != 1:
            return 'Question 3 is wrong. Please, read again the instructions below and give the correct answer.'



class formation(Page):
    pass
class ready(Page):
    pass


class start(Page):
    pass



page_sequence = [start,Introduction,questions2,questions,formation,ready]
