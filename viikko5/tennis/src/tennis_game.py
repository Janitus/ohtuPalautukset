class TennisGame:
    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]
    SCORE_END_GAME = 3

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.is_tie():
            return self.score_when_tie()
        elif self.is_end_game():
            return self.score_when_end_game()
        else:
            return self.normal_score()

    def is_tie(self):
        return self.player1_score == self.player2_score

    def score_when_tie(self):
        if self.player1_score < 3:
            return f"{self.SCORES[self.player1_score]}-All"
        else:
            return "Deuce"

    def is_end_game(self):
        return self.player1_score > self.SCORE_END_GAME or self.player2_score > self.SCORE_END_GAME

    def score_when_end_game(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def normal_score(self):
        return f"{self.SCORES[self.player1_score]}-{self.SCORES[self.player2_score]}"