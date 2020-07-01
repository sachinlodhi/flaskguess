from flask import Flask,redirect,render_template,request
from letter_shuffle import shuffle
from question_generate import quest
from answer import ans
from final_sentence import gen_sen
from setter import transform
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True


q_list = quest() # list of the questions from the pre-defined file
q_list.reverse() # revering the list of question so the popped element would be in increasing order

question=str(q_list.pop()) # popping the element i.e. the question from the list of question for passing in the form

answer = ans() # picking answer from the text file, list type
answer.reverse()
an=str(answer.pop()) #selecting last answer i.e. answer of the first question
sentence = gen_sen(question,an) #this will generate the sentance with right answer

#print(f'Generated Question : {question}')
#print(f'Selected answer words : {an}')
#print(f'Sentence with answer : {sentence}')
choices = shuffle(an)
pre_guess=''
#print(f'Choices are : {choices}')
@app.route('/', methods = ['GET','POST'])
def send():
    global pre_guess
    global question
    global choices
    global sentence
    print(f'Choices are : {choices}')
    t = ''
    #print(f'Picked Question : { question }')
    #print(f'Selected answer words : {an}')
    #print(f'Sentence with answer : {sentence}')

    if request.method == 'POST':
        usr_input = request.form['word']
        usr_input = usr_input.upper() # converting the user input to the uppercase letter for further operations
        print(f'guess is : {usr_input}')


        question = transform(question,sentence,usr_input)
        print(f'question is : {question}')
        print(f'answer is :{sentence}')

        if str(question) == str(sentence):
            return render_template('success.html',ans=sentence)
        else:

            if len(usr_input)==0:
                return render_template('invalid.html', word=usr_input, choice=choices,question=question,hint=an)
            if usr_input in pre_guess: #if already guessed
                return render_template('repeat.html',word = usr_input,choice = choices,question=question,hint=an)
            if usr_input not in choices: # if guessed letter is not in options
                return render_template('invalid.html',word = usr_input,choice = choices,question=question,hint=an)
            if usr_input in choices and usr_input not in an:
                return render_template('wrong.html', word = usr_input,choice = choices,question=question,hint=an)
            if usr_input in an and usr_input not in pre_guess:
                pre_guess += usr_input
                return render_template('correct.html',word = usr_input,choice = choices,question=question,hint=an)

        print(f'Pre_Guess :{pre_guess}')
    print(f'Question is before rendering : {question}')
    return render_template('index.html',question=question,choice=choices,hint=an)
    #return render_template('sample.html',choice=choices)




@app.route('/restart')
def restart():
    global question
    global q_list
    global answer
    global an
    global sentence
    global choices,pre_guess

    try:
            question = str(q_list.pop())  # popping the element i.e. the question from the list of question for passing in the form

            an = str(answer.pop())  # selecting last answer i.e. answer of the first question
            sentence = gen_sen(question, an)  # this will generate the sentance with right answer

            # print(f'Generated Question : {question}')
            # print(f'Selected answer words : {an}')
            # print(f'Sentence with answer : {sentence}')
            choices = shuffle(an)
            pre_guess = ''
            return render_template('index.html', question=question, choice=choices,hint=an)
    except:
        return render_template('complete.html')
if __name__ == '__main__':
    app.run(threaded=True)




'''


                for i in spaces:
                    t += i
                if t == guess:
                    return render_template('success.html', guess = guess)
                else:
                    if usr_input in old_space:
                        print(f'old spaces = {old_space}')
                        return render_template('repeat.html',spaces=spaces,choices=choices,word=usr_input,guess=guess,sep=sep)
                    if usr_input not in choices:
                        return render_template('invalid.html', spaces=spaces, choices=choices, word=usr_input, guess=guess,sep=sep)
                    if usr_input in guess and usr_input not in old_space:
                        return render_template('correct.html',spaces=spaces,choices=choices,word=usr_input,guess=guess,sep=sep)
                    if usr_input in choices and usr_input not in guess:
                        return render_template('wrong.html', spaces=spaces, choices=choices, word=usr_input, guess=guess,sep=sep)



    return render_template('index.html',spaces=spaces,choices=choices,guess=guess,question=question)

@app.route('/restart')
def restart():
    global guess
    global spaces
    global choices
    global q_list
    guess = generator()
    choices = shuffle(guess)
    spaces = ['_' for i in range(len(guess))]
    print(f'current guess {guess}')
    return render_template('index.html',spaces=spaces,choices=choices,guess=guess)


'''


