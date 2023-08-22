#!/usr/bin/env python3
class MyString:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.strip()[-1] in [".", "?", "!"]

    def is_question(self):
        return self.value.strip()[-1] == "?"

    def is_exclamation(self):
        return self.value.strip()[-1] == "!"

    def count_sentences(self):
        sentences = self.value.split(".")
        sentences = [s for s in sentences if s]
        return len(sentences)

