def split_and_join(sentence):
    updated_sentence = sentence.split(" ")
    updated_sentence = "-".join(updated_sentence)
    return updated_sentence
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
