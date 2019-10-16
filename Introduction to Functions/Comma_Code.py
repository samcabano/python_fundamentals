spam = ['apples', 'bananas', 'tofu', 'cats']

def sentence(values):
    for i in range(len(values)-1):
        print (values[i], ', ', sep='', end='')
    print ('and', values[-1])

sentence(spam)
