from flask import Flask, request, render_template
from random import randint,choice, sample
from tkinter import *
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)



words1 = ["place", "noun", "verb", "adjective", "plural_noun"]
phrase1 = """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""


words2 = ["adjective_1", "noun_1", "verb", "adverb", "adjective_2", "noun_2"]
phrase2 = """Today I went to the zoo. I saw a(n) {adjective_1} {noun_1} jumping up and down in its tree.
        He {verb} {adverb} through the large tunnel that led to its {adjective_2}
        {noun_2}."""

words3 = ["name", "verb", "number", "animal", "adjective", "emotion"]
phrase3 = """This morning I saw {name} {verb} {number} {animal}. 
         It was very {adjective}, I love {animal} so it made me {emotion}."""

@app.route('/')
def create_story():
    return render_template('index.html')


@app.route('/<story>')
def choose_story(story):
    if story == 'story-1':
        words = ["place", "noun", "verb", "adjective", "plural_noun"]
    elif story == 'story-2':
        words = ["adjective_1", "noun_1", "verb", "adverb", "adjective_2", "noun_2"]
    elif story == 'story-3':
        words = ["name", "verb", "number", "animal", "adjective", "emotion"]
    return render_template('story.html', words=words, story=story)


@app.route('/<story>/madlib')
def display_story(story):
    if story == 'story-1':
        words = ["place", "noun", "verb", "adjective", "plural_noun"]
        phrase = """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
        response = {
            'place': request.args['place'],
            'noun': request.args['noun'],
            'verb': request.args['verb'],
            'adjective': request.args['adjective'],
            'plural_noun': request.args['plural_noun']
        }

    elif story == 'story-2':
        words = ["adjective_1", "noun_1", "verb", "adverb", "adjective_2", "noun_2"]
        phrase = """Today I went to the zoo. I saw a(n) {adjective_1} {noun_1} jumping up and down in its tree.
        He {verb} {adverb} through the large tunnel that led to its {adjective_2}
        {noun_2}."""
        response = {
            'adjective_1': request.args['adjective_1'],
            'noun_1': request.args['noun_1'],
            'verb': request.args['verb'],
            'adverb': request.args['adverb'],
            'adjective_2': request.args['adjective_2'],
            'noun_2': request.args['noun_2'],
        }    
        
    elif story == 'story-3':
        words = ["name", "verb", "number", "animal", "adjective", "emotion"]
        phrase = """This morning I saw {name} {verb} {number} {animal}. 
         It was very {adjective}, I love {animal} so it made me {emotion}."""
        response = {
            'name': request.args['name'],
            'verb': request.args['verb'],
            'number': request.args['number'],
            'animal': request.args['animal'],
            'adjective': request.args['adjective'],
            'emotion': request.args['emotion']
        }

    story1 = Story(words, phrase)
    madlib = story1.generate(response)

    return render_template('mad-lib.html', madlib=madlib)
