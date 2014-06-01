__author__ = 'Spencer'


from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from analyzer import word_count, print_word_count

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_input_form():
    return render_template('input.html')

@app.route('/facts', methods=['GET'])
def display_facts():
    text = fetch_url_text()
    count = word_count(text)
    return print_word_count(count)

def fetch_url_text():
    pass

if __name__ == '__main__':
    app.run()