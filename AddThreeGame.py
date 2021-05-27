# Author: Conor Smith
# Date: 5/26/21
# Description: Add 3 game, allows two players to play a game in which they alternately choose numbers from 1-9. They
# may not choose a number that has already been selected by either player. If at any point exactly three of the player's
# numbers sum to exactly 15, then that player has won.

class AddThreeGame:
    """Initializes members"""
    def __int__(self):
        self._first = []
        self._second = []
        self._current_state = "unfinished"
        self._played = []
        self._turn = turn

    def get_current_state(self):
        return self._current_state

    def get_turn(self):
        return self._turn

    def make_move(self, player, num_1):
        """makes sure a number selection is valid adds valid selections to each players lists, keeps track of total selections"""
        if num_1 < 1 or num_1 > 9:
            return False
        if num_1 in self._played:
            return False
        if self._played == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self._current_state = "draw"

        if player == "first":
            self._first = self._first + num_1
            self._played.append(num_1)
        elif player == "second":
            self._second = self._second + num_1
            self._played.append(num_1)

        if self._first == 15:
            self._current_state = "First wins!"
        elif self._second == 15:
            self._current_state = "Second wins!"




    current_state = game.get_current_state()
    if curent_state == "unfinished":
        print("Next player's turn.")
    elif current_state == "draw":
        print("all possible numbers were chosen with no winner")
    elif current_state == "first_won":
        print("First wins!")
    elif current_state == "second_won":
        print("Second player wins!")

#game = AddThreeGame()
#game.make_move("first", 2)
#game.make_move("second", 5)
#result = game.make_move("first", 7)
#state = game.get_current_state()