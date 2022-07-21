class Wordle:

    def __init__(self, word):
        self.word = word.upper()
        self.attempts_left = 5
    
    def guess_made(self):
        self.attempts_left -= 1

    def position_check(self, player_input, expected):
        result = {}
        # Implementation could be changed to a list of tuples instead?
        # e.g. For "ERUPT", attempt is "ERASE":
        # [("E", 2), ("R", 2), ("A", 0), ("S", 0), ("E", 1)]
        # Note: Tried this. Quite tedious when it comes to accessing values directly.

        """
        For ref: 
        Green (Word present and in correct position) = 2
        Yellow (Word present, not in correct position) = 1
        Grey (Word not present) = 0
        """

        for i in range(len(player_input)):
            if player_input[i] in expected and player_input[i] == expected[i]:
                result[player_input[i]] = 2
            elif player_input[i] in expected:
                result[player_input[i]] = 1
            else:
                result[player_input[i]] = 0
        
        return result 
