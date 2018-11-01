import json
from developer_insight.settings import *

class BoardConfig():

    with open(os.path.join(BASE_DIR, 'board/board_list.json')) as f:
        BASE_COFIG = json.load(f)

    BOARD_TABLE = BASE_COFIG["board"]