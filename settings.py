from os import environ

SESSION_CONFIGS = [
   dict(
       name='intro',
       app_sequence=['Intro'],
        num_demo_participants=1,
      ),
    dict(
        name='control',
        app_sequence=['control'],
        num_demo_participants=1,
    ),
    dict(
        name='control2',
        app_sequence=['control2'],
        num_demo_participants=1,
    ),
    dict(
        name='fine',
        app_sequence=['fine'],
        num_demo_participants=1,
    ),
    dict(
        name='fee',
        app_sequence=['fee'],
        num_demo_participants=1,
    ),
    dict(
        name='emp1',
        app_sequence=['emp1'],
        num_demo_participants=1,
    ),
    dict(
        name='emp2',
        app_sequence=['emp2'],
        num_demo_participants=1,
    ),
    dict(
        name='normative',
        app_sequence=['normative'],
        num_demo_participants=1,
    ),
    dict(
        name='normative2',
        app_sequence=['normative2'],
        num_demo_participants=1,
    ),
    dict(
        name='right',
        app_sequence=['right'],
        num_demo_participants=1,
    ),
    dict(
        name='right2',
        app_sequence=['right2'],
        num_demo_participants=1,
    ),
    dict(
        name='end',
        app_sequence=['end'],
        num_demo_participants=2,
    ),
    dict(
        name='feeO1',
        app_sequence=['Intro', 'control', 'fee','emp1','normative','right','survey','end'],
        num_demo_participants=2,
    ),
    dict(
        name='fineO1',
        app_sequence=['Intro', 'control', 'fine', 'emp2', 'normative2', 'right2','survey', 'end'],
        num_demo_participants=2,
    ),
    dict(
        name='feeO2',
        app_sequence=['Intro',  'fee', 'control2', 'emp1', 'normative', 'right', 'survey', 'end'],
        num_demo_participants=2,
    ),
    dict(
        name='fineO2',
        app_sequence=['Intro',  'fine', 'control2','emp2', 'normative2', 'right2', 'survey', 'end'],
        num_demo_participants=2,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']


ROOMS = [
    dict(
        name='ExperimentG1',
        display_name='Experiment - ABS1',
    ),

    dict(
        name='ExperimentG2',
        display_name='Experiment - ABS2',
    ),

    dict(
        name='ExperimentG3',
        display_name='Experiment - ABS3',
        participant_label_file='_rooms/ABS.txt',
    ),
    dict(
        name='ExperimentG4',
        display_name='Experiment - ABS4',
        participant_label_file='_rooms/ABS.txt',
    ),
]


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['seed']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


ADMIN_USERNAME = 'bu'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'bu'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1428152376803'
