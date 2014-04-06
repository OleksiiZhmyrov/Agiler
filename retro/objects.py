
class RetroBoardContainer(object):
    def __init__(self, was_good, need_to_change, action_point, is_active, vote_limit, team, sprint):
        self.was_good = was_good
        self.need_to_change = need_to_change
        self.action_point = action_point
        self.is_active = is_active
        self.vote_limit = vote_limit
        self.team = team
        self.sprint = sprint
