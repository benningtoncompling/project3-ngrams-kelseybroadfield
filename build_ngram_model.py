#!/usr/bin/python3
#
# Comp Ling PROJECT #3
# April 2019
# Author: Kelsey Broadfield kelseybroadfield@bennington.edu
#

import nltk
from nltk import ngrams
import math


# for input file, add <s> and </s> tags to the sentences and make them lower case
with open('dickens_training.txt', 'r+', encoding="utf8") as dickens_txt:
    fixed_text = []
    for lines in dickens_txt.readlines():
        lowered = lines.lower()
        these_lines = ['<s>'] + lowered.split() + ['</s>']
        fixed_text.append(these_lines)
# print(fixed_text)


# UNIGRAMS:
unigram_dict = {}
uni_tokens = 0
for line in fixed_text:
    for word in line:
        uni_tokens += 1
        if word in unigram_dict:
            unigram_dict[word] += 1
        else:
            unigram_dict[word] = 1
# print(unigram_dict)


# COUNT:
# Number of Unigram TYPES
uni_types = len(unigram_dict)
# Number of Unigram TOKENS
print(uni_tokens)


# BIGRAMS
bigrams = []
for lines in fixed_text:
    my_bigrams = list(nltk.bigrams(lines))
    bigrams += my_bigrams


bigrams_dict = {}
bi_tokens = 0
for x in bigrams:
    if x[0] not in bigrams_dict:
        bigrams_dict[x[0]] = {}
    if x[1] not in bigrams_dict[x[0]]:
        bigrams_dict[x[0]][x[1]] = 1
    else:
        bigrams_dict[x[0]][x[1]] += 1
    bi_tokens += 1
# print(bigrams_dict)

# COUNT:
# Number of Bigram TYPES
# found this idea on stack overflow bc what I tried below absolutely didn't work
# having a hard time wrapping my head around adding within the nested dictionary thing
bi_types = sum(len(x) for x in bigrams_dict.values())

# Failed Attempts at counting
#for x in bigrams_dict.values():
    #length = len(x)
    #bi_type_count += sum(length)
#print(bi_type_count)

#for x in bigrams_dict:
    #for y in x:
        #number = len(x)
        #bi_type_count += number
#print(bi_type_count)

# Number of Bigram TOKENS
print(bi_tokens)

# TRIGRAMS
trigrams = []
for lines in fixed_text:
    my_trigrams = ngrams(lines, 3)
    trigrams += my_trigrams

trigrams_dict = {}
tri_tokens = 0
for word in trigrams:
        tri_tokens += 1
        phrase1 = word[0] + " " + word[1]
        if phrase1 not in trigrams_dict:
            trigrams_dict[phrase1] = {}
        if word[2] not in trigrams_dict[phrase1]:
            trigrams_dict[phrase1][word[2]] = 1
        else:
            trigrams_dict[phrase1][word[2]] += 1
# print(trigrams_dict)

# COUNT:
# Number of Trigram TYPES
tri_types = sum(len(x) for x in trigrams_dict.values())
# Number of Trigram TOKENS
print(tri_tokens)


# function for unigram probability
def uni_divider(unigram_freq, total):
    return unigram_freq / total


# function for bigram probability
def bi_divider(unigram, bigram_freq):
    number = int(unigram_dict[unigram])
    return bigram_freq / number


# function for trigram probability
def tri_divider(bigram, unigram_freq):
    count = 0
    for k, v in trigrams_dict[bigram].items():
        count += v
    return unigram_freq / count


with open('dickens_output.txt', 'w+', encoding="utf8") as out_file:
    out_file.write('\data\ ' + '\n') 'ngram 1: type=' + str(uni_types) + ' ' + 'token=' + str(uni_tokens))
    out_file.write('ngram 2: type=' + str(bi_types) + ' ' + 'token=' + str(bi_tokens))
    out_file.write('ngram 3: type=' + str(tri_types) + ' ' + 'token=' + str(tri_tokens) + '\n')
    out_file.write("\1-grams")
    for a, b in unigram_dict.items():
        count = b
        prob = uni_divider(b, uni_tokens)
        log_prob = math.log(prob, 10)
        actual_gram = a
        print(count, prob, log_prob, actual_gram, file=out_file)
    out_file.write('\n')
    out_file.write('\2-grams')
    counter = 0
    for a, b in bigrams_dict.items():
        for k, v in b.items():
            counter = v
            prob = bi_divider(a, counter)
            log_prob = math.log(prob, 10)
            actual_gram = a
            print(counter, prob, log_prob, actual_gram, k, file=out_file)
    out_file.write('\n')
    out_file.write('\3-grams')
    counter1 = 0
    for a, b in trigrams_dict.items():
        for k, v in b.items():
            counter1 = v
            prob = tri_divider(a, counter1)
            log_prob = math.log(prob, 10)
            actual_gram = a
            print(counter1, prob, log_prob, actual_gram, k, file=out_file)
    out_file.close()



