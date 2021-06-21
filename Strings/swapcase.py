def swap_case(sentence):
    final_sentence = ""
    
    for c in sentence:
        if c.isupper():
            final_sentence += c.lower()
        elif c.islower():
            final_sentence += c.upper()
        else:
            final_sentence += c
    return final_sentence
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
