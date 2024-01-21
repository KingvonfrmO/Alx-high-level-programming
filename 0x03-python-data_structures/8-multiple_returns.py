def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
    else:
        length = len(sentence)
        
        split_sentence= sentence.split(" ")
        first_word = split_sentence[0]
        characters = list(first_word)
        first_character = characters[0]
        
        return(length, first_character)
        