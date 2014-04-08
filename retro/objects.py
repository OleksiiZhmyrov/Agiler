from model_choices import STICKER_TYPE_GOOD, STICKER_TYPE_CHANGE, STICKER_TYPE_ACTION


class BoardContainer(object):
    def __init__(self, board):
        self.was_good = board.stickers.all().filter(type=STICKER_TYPE_GOOD)
        self.need_to_change = board.stickers.all().filter(type=STICKER_TYPE_CHANGE)
        self.action_point = board.stickers.all().filter(type=STICKER_TYPE_ACTION)
        self.is_active = board.isActive
        self.vote_limit = board.voteLimit
        self.team = board.team
        self.sprint = board.sprint
