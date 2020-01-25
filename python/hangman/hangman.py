# Game status categories
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.letters_found = list()
        self.word = word

    def guess(self, char):
        """Handling of guesses from the player."""
        if self.status == STATUS_LOSE:
            raise ValueError("No more guesses, you lost")
        elif self.status == STATUS_WIN:
            raise ValueError("No more guesses, you have already won")
        elif self.status == STATUS_ONGOING:
            if char in self.letters_found or char not in self.word:
                # Handling of an incorrect guess.
                self.remaining_guesses -= 1
                if self.remaining_guesses < 0:
                    self.status = STATUS_LOSE
            else:
                # Handling of a correct guess.
                self.letters_found.append(char)
                if self.get_masked_word() == self.word:
                    self.status = STATUS_WIN

    def get_masked_word(self):
        """Get the word to be guessed with not guessed letters being masked."""
        masked_word = ""
        for c in self.word:
            if c in self.letters_found:
                masked_word += c
            else:
                masked_word += "_"
        return masked_word

    def get_status(self):
        """Get the current game status."""
        return self.status
