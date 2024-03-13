from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 24576599
    API_HASH = "a4e06b7c78866d4f2a61ed55d3dac5d2"
    # the name to display in your alive message
    ALIVE_NAME = "kouroshasli"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://zfnitoac:SJMH1P4BSXQl_0U5x7tRyOXyplNQGOo-@tuffi.db.elephantsql.com/zfnitoac"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOJ0Buys1xDm6rGwA-_rBaK3hPN33_ASbIi30tR2eWkvESo-oadu7owC-gWWnJu5JYuiRYkBhO56AUwBu4BklKjmSheA2Jb1L0Yb-O5BuzUV4N_57ZIoTUgCAlE5uiZQoh0Ae0VMC3S2cWQGjXbu1_Cb5rP__syF9CIy8HmHHB1ffQYDGB0C3lan7OJXAM2axpMK6J_ZtJhswuUigTe_xuor6k2lwlBelV54n56-Mp4V47Bo7HJlrC_qWCqhnWphP57buWtePeRH7Xw69eHKGZ7En1z5lOYHSuQrnfoLlNIICWWn6j1k_Nj0_OT-B-5cznOHo5_zyLtwnNnVMLIsfp7eXavo="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "7028539972:AAHvH6zE002U9xRcwSV_s0Kb_x7t3T2THa4"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002011264154
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
