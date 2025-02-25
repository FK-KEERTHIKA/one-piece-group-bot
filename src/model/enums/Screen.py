from enum import StrEnum


class Screen(StrEnum):
    UNKNOWN = "0"

    GRP_USER_STATUS = "G1"
    GRP_DOC_Q_GAME = "G2"
    GRP_CHANGE_REGION = "G3"
    GRP_FIGHT = "G4"
    GRP_GAME = "G5"
    GRP_GAME_SELECTION = "G6"
    GRP_GAME_OPPONENT_CONFIRMATION = "G7"
    GRP_ROCK_PAPER_SCISSORS_GAME = "G8"
    GRP_RUSSIAN_ROULETTE_GAME = "G9"
    GRP_PREDICTION_BET = "G10"
    GRP_PREDICTION_BET_REMOVE = "G11"
    GRP_PREDICTION_BET_STATUS = "G12"
    GRP_CREW_JOIN = "G13"
    GRP_CREW_INVITE = "G14"
    GRP_SILENCE = "G15"
    GRP_SILENCE_END = "G16"
    GRP_SPEAK = "G17"
    GRP_BOUNTY_GIFT = "G18"
    GRP_DEVIL_FRUIT_COLLECT = "G19"  # Deprecated
    GRP_SETTINGS = "G20"
    GRP_DEVIL_FRUIT_SELL = "G21"
    GRP_BOUNTY_LOAN = "G22"
    GRP_PLUNDER = "G23"
    GRP_DAILY_REWARD = "G24"
    GRP_DAILY_REWARD_PRIZE = "G25"

    PVT_START = "P1"
    PVT_SETTINGS = "P2"
    PVT_SETTINGS_LOCATION_UPDATE = "P3"  # Deprecated
    PVT_USER_STATUS = "P4"
    PVT_CREW = "P5"
    PVT_CREW_CREATE_OR_EDIT = "P6"
    PVT_CREW_LEAVE = "P7"
    PVT_CREW_DISBAND = "P8"
    PVT_CREW_MEMBER = "P9"
    PVT_CREW_MEMBER_DETAIL_REMOVE = "P10"
    PVT_SETTINGS_NOTIFICATIONS = "P11"
    PVT_SETTINGS_NOTIFICATIONS_TYPE = "P12"
    PVT_SETTINGS_NOTIFICATIONS_TYPE_EDIT = "P13"
    PVT_LOGS = "P14"
    PVT_LOGS_TYPE = "P15"
    PVT_LOGS_TYPE_DETAIL = "P16"
    PVT_PREDICTION = "P17"
    PVT_PREDICTION_DETAIL = "P18"
    PVT_PREDICTION_DETAIL_PLACE_BET = "P19"
    PVT_PREDICTION_DETAIL_PLACE_BET_SEND_AMOUNT = "P20"
    PVT_PREDICTION_DETAIL_REMOVE_BET = "P21"
    PVT_PREDICTION_DETAIL_REMOVE_BET_CONFIRM = "P22"
    PVT_DEVIL_FRUIT = "P23"
    PVT_DEVIL_FRUIT_DETAIL = "P24"
    PVT_DEVIL_FRUIT_DETAIL_EAT = "P25"
    PVT_DEVIL_FRUIT_DETAIL_SELL = "P26"
    PVT_DEVIL_FRUIT_DETAIL_DISCARD = "P27"
    PVT_GAME_GUESS_INPUT = "P28"
    PVT_LOGS_TYPE_STATS = "P29"
    PVT_SETTINGS_TIMEZONE = "P30"
    PVT_BOUNTY_LOAN = "P31"
    PVT_BOUNTY_LOAN_DETAIL = "P32"
    PVT_BOUNTY_LOAN_DETAIL_PAY = "P33"
    PVT_BOUNTY_LOAN_DETAIL_FORGIVE = "P34"
    PVT_PREDICTION_CREATE = "P35"
    PVT_PREDICTION_DETAIL_SEND_TO_GROUP = "P36"
    PVT_PREDICTION_DETAIL_SET_RESULT = "P37"
    PVT_CREW_MEMBER_DETAIL = "P38"
    PVT_CREW_ABILITY = "P39"
    PVT_CREW_ABILITY_ACTIVATE = "P40"
    PVT_CREW_ABILITY_ACTIVATE_CONFIRM = "P41"
    PVT_CREW_MEMBER_DETAIL_FIRST_MATE_PROMOTE = "P42"
    PVT_CREW_MEMBER_DETAIL_FIRST_MATE_DEMOTE = "P43"
    PVT_CREW_MODIFY = "P44"
    PVT_CREW_POWERUP = "P45"
    PVT_CREW_LEVEL = "P46"
    PVT_CREW_LEVEL_UP = "P47"
    PVT_CREW_SEARCH = "P48"
    PVT_CREW_SEARCH_DETAIL = "P49"
    PVT_CREW_SEARCH_DETAIL_JOIN = "P50"
    PVT_CREW_JOIN_REQUEST_RECEIVED = "P51"
    PVT_CREW_MEMBER_DETAIL_POST_BAIL = "P52"
    PVT_CREW_DAVY_BACK_FIGHT_REQUEST = "P53"
    PVT_CREW_DAVY_BACK_FIGHT_REQUEST_RECEIVED = "P54"
    PVT_CREW_DAVY_BACK_FIGHT = "P55"
    PVT_CREW_DAVY_BACK_FIGHT_DETAIL = "P56"
    PVT_CREW_DAVY_BACK_FIGHT_DETAIL_PARTICIPANTS_SELECT = "P57"
    PVT_CREW_DAVY_BACK_FIGHT_DETAIL_PARTICIPANTS_VIEW = "P58"
    PVT_CREW_DAVY_BACK_FIGHT_DETAIL_CONSCRIPT_OPPONENT = "P59"
    PVT_CREW_MODIFY_DAVY_BACK_FIGHT_DEFAULT_PARTICIPANTS = "P60"
    PVT_DEVIL_FRUIT_SHOP = "P61"
    PVT_DEVIL_FRUIT_SHOP_DETAIL = "P62"
    PVT_DEVIL_FRUIT_SHOP_DETAIL_REMOVE = "P63"
    PVT_DEVIL_FRUIT_SHOP_DETAIL_BUY = "P64"
    PVT_CREW_MEMBER_DETAIL_CAPTAIN_PROMOTE = "P65"


ONLY_BY_CAPTAIN = [
    Screen.PVT_CREW_MEMBER_DETAIL_FIRST_MATE_PROMOTE,
    Screen.PVT_CREW_MEMBER_DETAIL_FIRST_MATE_DEMOTE,
    Screen.PVT_CREW_MEMBER_DETAIL_CAPTAIN_PROMOTE,
    Screen.PVT_CREW_DAVY_BACK_FIGHT_DETAIL_CONSCRIPT_OPPONENT,
    Screen.PVT_CREW_DISBAND,
]

ONLY_BY_CAPTAIN_OR_FIRST_MATE = [
    Screen.PVT_CREW_ABILITY_ACTIVATE,
    Screen.PVT_CREW_ABILITY_ACTIVATE_CONFIRM,
    Screen.PVT_CREW_LEVEL_UP,
    Screen.PVT_CREW_MODIFY_DAVY_BACK_FIGHT_DEFAULT_PARTICIPANTS,
]

ALLOW_WHILE_ARRESTED = [
    Screen.PVT_SETTINGS,
    Screen.PVT_SETTINGS_NOTIFICATIONS,
    Screen.PVT_SETTINGS_NOTIFICATIONS_TYPE,
    Screen.PVT_SETTINGS_NOTIFICATIONS_TYPE_EDIT,
]

ALLOW_WHILE_ARRESTED_TEMPORARY = [
    Screen.PVT_CREW,
    Screen.PVT_CREW_MEMBER,
    Screen.PVT_CREW_MEMBER_DETAIL,
    Screen.PVT_CREW_MEMBER_DETAIL_POST_BAIL,
    Screen.PVT_BOUNTY_LOAN,
    Screen.PVT_BOUNTY_LOAN_DETAIL,
    Screen.GRP_DAILY_REWARD_PRIZE,
]

ALLOW_DEEPLINK = [
    Screen.PVT_PREDICTION_DETAIL,
    Screen.PVT_GAME_GUESS_INPUT,
    Screen.PVT_LOGS_TYPE_DETAIL,
    Screen.PVT_DEVIL_FRUIT_DETAIL,
    Screen.PVT_SETTINGS_TIMEZONE,
    Screen.PVT_BOUNTY_LOAN_DETAIL,
    Screen.PVT_CREW_SEARCH_DETAIL,
    Screen.PVT_CREW_DAVY_BACK_FIGHT_DETAIL,
    Screen.PVT_CREW_MODIFY,
    Screen.PVT_DEVIL_FRUIT_SHOP_DETAIL,
    Screen.PVT_CREW_SEARCH,
]

DEPRECATED = [
    Screen.PVT_SETTINGS_LOCATION_UPDATE,
    Screen.GRP_DEVIL_FRUIT_COLLECT,
]

ALLOW_SEARCH_INPUT = [Screen.PVT_CREW_SEARCH]

HAS_CONTEXT_FILTER = [Screen.PVT_CREW_SEARCH]
