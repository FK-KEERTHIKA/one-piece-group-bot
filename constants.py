import os

ROOT_DIR = os.path.dirname(__file__)

REDDIT_USER_URL_PREFIX = 'https://www.reddit.com/user/'
REDDIT_SUBREDDIT_URL_PREFIX = 'https://www.reddit.com/r/'

TG_PARSE_MODE_MARKDOWN = 'MarkdownV2'
TG_DEFAULT_PARSE_MODE = TG_PARSE_MODE_MARKDOWN
TG_MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB
TG_DEFAULT_IMAGE_COMPRESSION_QUALITY = 80
TG_PROFILE_PHOTO_EXTENSION = 'jpg'

TEMP_DIR = os.path.join(ROOT_DIR, 'temp')

# Language code
LANG_CODE_EN = 'en'
DEFAULT_LANG_CODE = LANG_CODE_EN

SCREEN_CODE = 'sc'
PREVIOUS_SCREEN_CODE = 'psc'

# Saved Media
SAVED_MEDIA_NAME_DOC_Q = 'docq'
SAVED_MEDIA_NAME_FIGHT = 'fight'

# Command
STANDARD_SPLIT_CHAR = "|"
COMMAND_PREFIX_ALIASES = ["/", ".", ", ", "!"]

# Bounty poster
BOUNTY_POSTER_EXTENSIION = 'jpg'
BOUNTY_POSTER_ASSETS_PATH = os.path.join(ROOT_DIR, 'assets', 'bounty_poster')
BOUNTY_POSTER_TEMPLATE_PATH = os.path.join(BOUNTY_POSTER_ASSETS_PATH, 'image_components', 'template.png')
BOUNTY_POSTER_NO_PHOTO_PATH = os.path.join(BOUNTY_POSTER_ASSETS_PATH, 'image_components', 'no_photo.jpg')
BOUNTY_POSTER_IMAGE_BOX_START_Y = 239
BOUNTY_POSTER_IMAGE_BOX_H = 461
BOUNTY_POSTER_NAME_FONT_SIZE = 150
BOUNTY_POSTER_NAME_MAX_W = 595
BOUNTY_POSTER_NAME_H = 109
BOUNTY_POSTER_NAME_START_X = 95
BOUNTY_POSTER_NAME_START_Y = 802
BOUNTY_POSTER_NAME_END_Y = 911
BOUNTY_POSTER_NAME_MAX_KERN = 65
BOUNTY_POSTER_NAME_MAX_LENGTH = 16
BOUNTY_POSTER_NAME_SPACE_SUB_MIN_LENGTH = 14
BOUNTY_POSTER_NAME_SPACE_SUB_CHAR = '•'
BOUNTY_POSTER_NAME_TEXTURE_PATH = os.path.join(BOUNTY_POSTER_ASSETS_PATH, 'image_components', 'texture_name.jpg')
BOUNTY_POSTER_NAME_FONT_PATH = os.path.join(BOUNTY_POSTER_ASSETS_PATH, 'fonts', 'PlayfairDisplay-Bold.ttf')
BOUNTY_POSTER_BERRY_FONT_SIZE = 37
BOUNTY_POSTER_BERRY_MAX_W = 522
BOUNTY_POSTER_BERRY_H = 35
BOUNTY_POSTER_BERRY_START_X = 150
BOUNTY_POSTER_BERRY_START_Y = 952
BOUNTY_POSTER_BERRY_END_Y = 987
BOUNTY_POSTER_BERRY_MAX_KERN = 30
BOUNTY_POSTER_BERRY_TEXTURE_PATH = os.path.join(BOUNTY_POSTER_ASSETS_PATH, 'image_components', 'texture_berry.jpg')
BOUNTY_POSTER_BERRY_FONT_PATH = os.path.join(BOUNTY_POSTER_ASSETS_PATH, 'fonts', 'Lilly__.ttf')
BOUNTY_POSTER_COMPONENT_NAME = 1
BOUNTY_POSTER_COMPONENT_BERRY = 2
