class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = {}
        losses = {}

        for winner, loser in matches:
            wins[winner] = wins.get(winner, 0) + 1
            losses[loser] = losses.get(loser, 0) + 1

        no_losses = [player for player in wins if player not in losses]
        one_loss = [player for player in losses if losses[player] == 1]

        no_losses.sort()
        one_loss.sort()
        return [no_losses, one_loss]
            