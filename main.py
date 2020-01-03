from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask,redirect,render_template,request
from word_guess import generator
from setter import let_set
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

guess = generator()
spaces = ['_' for i in range(len(guess))]
@app.route('/send', methods = ['GET','POST'])
def send():
    global guess
    global  spaces
    t = ''
    print(f'temp : {guess}')
    print(f'spaces : {spaces}')
    if request.method == 'POST':
        word = request.form['word']
        print(f'age is : {word}')

        if t == guess:
            return render_template('success.html',word=word)
        else:
            spaces=let_set(guess,spaces,word)

            for i in spaces:
                t += i
            if t == guess:
                return render_template('success.html', guess=guess)
            else:
                if word in spaces:
                    return render_template('repeat.html',spaces=spaces)
                else:
                    return render_template('try.html', spaces=spaces)
    return render_template('index.html',spaces=spaces)
if __name__ == '__main__':
    app.run()
