#Hangman Project
list_of_words= ["Lebron James", "Lionel Messi", 'Cristiana Ronaldo', 'Jazz', 'conceptualize']


    

begin_question= input("would you like to play hangman?")
begin_question = begin_question.lower()
if begin_question=='yes' or begin_question =='yeah' or begin_question =='sure'or begin_question =='ok':



    Playing = True
    import random
    length_of_list= int(len(list_of_words)-1)
    word_number=(random.randint(0, length_of_list))
    word_from_list= list_of_words[word_number]
    word_from_list_length= len(word_from_list)





    while Playing:
        print("I am thinking of a word with length of", " ", word_from_list_length)
        
        
        guess=''
        while guess =='':
            guess = input("take a guess")
        
        
        
    
else:
    print("ok then another time :)")
    






