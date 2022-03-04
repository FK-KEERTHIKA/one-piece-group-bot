import datetime

from peewee import MySQLDatabase
from telegram import Update
from telegram.ext import CallbackContext

import constants as c
import resources.Environment as Env
from resources.Database import Database
from src.chat.group.screens.screen_bounty import manage as manage_screen_show_bounty
from src.chat.group.screens.screen_doc_q_game import manage as manage_screen_doc_q_game
from src.model.User import User
from src.model.enums.GroupScreen import GroupScreen
from src.model.error.GroupChatError import GroupChatError
from src.model.pojo.Keyboard import Keyboard, get_keyboard_from_callback_query
from src.service.bounty_service import get_message_belly
from src.service.message_service import full_message_send, is_command


def init() -> MySQLDatabase:
    """
    Initializes the group chat manager
    :return: Database connection
    :rtype: MySQLDatabase
    """
    db_obj = Database()
    db = db_obj.get_db()

    return db


def end(db: MySQLDatabase) -> None:
    """
    Ends the group chat manager
    :param db: Database connection
    :type db: MySQLDatabase
    :return: None
    :rtype: None
    """
    db.close()


def update_group_user(update: Update) -> User:
    """
    Creates a new user or updates an existing user
    :param update: Telegram update
    :return: User object
    """

    # Insert or update user
    user = User.get_or_none(User.tg_user_id == update.effective_user.id)
    if user is None:
        user = User()
        user.tg_user_id = update.effective_user.id

    user.tg_first_name = update.effective_user.first_name
    user.bounty += get_message_belly(update)
    user.last_message_date = datetime.datetime.now()
    user.save()

    return user


def manage(update: Update, context: CallbackContext) -> None:
    """
    Main function for the group chat manager
    :param update: Telegram update
    :type update: Update
    :param context: Telegram context
    :type context: CallbackContext
    :return: None
    :rtype: None
    """
    # Initialize
    db = init()
    screen = GroupScreen.SCREEN_UNKNOWN

    # Insert or update user, with message count
    try:
        # Ignore self bot messages or from linked channel
        if update.effective_user.is_bot or update.message.sender_chat.id == int(Env.OPD_CHANNEL_ID.get()):
            return
    except AttributeError:
        pass

    # Text message
    if update.message is not None and update.message.text is not None and is_command(update.message.text):
        # Remove command prefix
        command_message = update.message.text[1:].lower()

        # Bounty command
        if command_message == c.COMMAND_GRP_BOUNTY:
            screen = GroupScreen.SCREEN_BOUNTY

        # Doc Q Game
        if command_message == c.COMMAND_GRP_DOC_Q_GAME:
            screen = GroupScreen.SCREEN_DOC_Q_GAME

    # Screen still unknown, get from callback query
    if screen == GroupScreen.SCREEN_UNKNOWN:
        if update.callback_query is not None and update.callback_query.data is not None:  # Callback query
            keyboard: Keyboard = get_keyboard_from_callback_query(update.callback_query)
            if keyboard is not None:
                screen = keyboard.screen

    user = update_group_user(update)

    dispatch_screens(update, context, user, screen)

    # End
    end(db)


def dispatch_screens(update: Update, context: CallbackContext, user: User, screen: GroupScreen) -> None:
    keyboard = None
    if update.callback_query is not None:
        keyboard = get_keyboard_from_callback_query(update.callback_query)

    match screen:
        case GroupScreen.SCREEN_BOUNTY:  # Bounty screen
            manage_screen_show_bounty(update, context)

        case GroupScreen.SCREEN_DOC_Q_GAME:  # Doc Q Game screen
            manage_screen_doc_q_game(update, context, user, keyboard)

        case _:  # Unknown screen
            if update.callback_query is not None:
                ot_text = GroupChatError.UNRECOGNIZED_SCREEN.build()
                full_message_send(context, ot_text, update, new_message=True)
