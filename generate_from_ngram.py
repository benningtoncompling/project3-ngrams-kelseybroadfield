#!/usr/bin/python3
#
# Comp Ling PROJECT #3 Part 2
# May 2019
# Author: Kelsey Broadfield kelseybroadfield@bennington.edu
#

import sys
import random

input_file = sys.argv[1]
output_file = sys.argv[2]


total = 0
uni_sentence = []
lines = []
with open(output_file, 'w', encoding='utf8') as sentence_output:
    with open(input_file, 'r', encoding='utf8') as input_text:
        my_lines = input_text.read().splitlines()
        for y in my_lines:
            lines.append(y)

    #print(lines)
    # create my dictionaries
    uni_dict = {}
    bi_dict = {}
    tri_dict = {}

    in_unigrams = False

    for y in lines:
        #print(y)
        if "-grams" in y:
            in_unigrams = True
            continue
        current_line = y.split()
        if len(current_line) == 4 and in_unigrams == True:
            uni_dict[current_line[3]] = float(current_line[1])
        if len(current_line) == 5 and in_unigrams == True:
            if current_line[3] not in bi_dict:
                bi_dict[current_line[3]] = {}
            if current_line[4] not in bi_dict[current_line[3]]:
                bi_dict[current_line[3]][current_line[4]] = float(current_line[1])
        if len(current_line) == 6 and in_unigrams == True:
            first_phrase = current_line[3] + ' ' + current_line[4]
            if first_phrase not in tri_dict:
                tri_dict[first_phrase] = {}
            if current_line[5] not in tri_dict[first_phrase]:
                tri_dict[first_phrase][current_line[5]] = float(current_line[1])


    #print(uni_dict)
    #print(bi_dict)
    #print(tri_dict)


    # UNIGRAMS
    sentence_output.write('UNIGRAM SENTENCES:' + '\n')
    for i in range(5):
        my_sentence = '<s>'
        tip_word = ''
        while tip_word != '</s>':
            tipper = random.random()
            total = 0
            for word, prob in uni_dict.items():
                current = prob
                total += current
                if total > tipper:
                    tip_word = str(word)
                    my_sentence = my_sentence + tip_word + ' '
                    break
        sentence_output.write(my_sentence + '\n')

    sentence_output.write('BIGRAM SENTENCES:' + '\n')

    # BIGRAMS
    for i in range(5):
        my_sentence = '<s>'
        tip_word = '<s>'
        while tip_word != '</s>':
            tipper = random.random()
            total = 0
            for word, prob in bi_dict[tip_word].items():
                current = prob
                total += current
                if total > tipper:
                    tip_word = str(word)
                    my_sentence = my_sentence + tip_word + ' '
                    break
        sentence_output.write(my_sentence + '\n')

    sentence_output.write('TRIGRAM SENTENCES:' + '\n')
    # TRIGRAMS
    for i in range(5):
        my_sentence = ['<s>']
        tipper = random.random()
        total = 0
        for word, prob in bi_dict['<s>'].items():
            current = prob
            total += current
            if total > tipper:
                tip_word = str(word)
                my_sentence.append(tip_word)
                break

        tip_word = '<s>'
        while tip_word != '</s>':
            look_up = ' '.join(my_sentence[-2:])
            tipper = random.random()
            total = 0
            for first_phrase, dic in tri_dict[look_up].items():
                current = dic
                total += current
                if total > tipper:
                    tip_word = str(first_phrase)
                    my_sentence.append(tip_word)
                    break
        new_sentence = str(' '.join(my_sentence))
        sentence_output.write(new_sentence + '\n')
