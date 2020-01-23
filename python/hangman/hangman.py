# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.guessed_letters = set()
        self.word = word

    def guess(self, char):
        if self.status == STATUS_LOSE:
            raise ValueError("No more guesses, you lost")
        elif self.status == STATUS_WIN:
            raise ValueError("No more guesses, you won")

        if self.status == STATUS_ONGOING:
            self.guessed_letters.add(char)
            print(self.get_masked_word())
            if self.get_masked_word() == self.word:
                self.status = STATUS_WIN
            else:
                self.remaining_guesses -= 1
            print(self.remaining_guesses)
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        print(self.status)
        print(STATUS_LOSE)

    def get_masked_word(self):
        masked_word = ""
        for c in self.word:
            if c in self.guessed_letters:
                masked_word += c
            else:
                masked_word += "_"
        return masked_word

    def get_status(self):
        return self.status
