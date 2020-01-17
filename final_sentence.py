def gen_sen(question,answer):
        answer = answer.replace(" ","") # removing space between the words of answers
        final_sentence = ''
        t = [i for i in answer]
        t.reverse()
        for i in question:

            if i == "_":
                final_sentence+=str(t.pop()) # filling the blanks
            else:
                final_sentence+=i # making the question

        return final_sentence