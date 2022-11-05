"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


# story1 = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )
# story2 = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Today I went to the zoo. I saw a(n) {adjective-1} {noun-1} jumping up and down in its tree.
#         He {verb} {adverb} through the large tunnel that led to its {adjective-2}
#         {noun-2}."""
# )
# story3 = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """This morning I saw {name} {verb} {number} {animal}. 
#         It was very {adjective}, I love {animal} so it made me {emotion}."""
# )
