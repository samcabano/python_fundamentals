grid = [[' ', '(', ' '],
        ['/', '=', '('],
        ['\\', '^', '>'],
        ['-', 'Y', 'o'],
        ['/', '^', '<'],
        ['\\', '=', ')'],
        [' ', ')', ' ']]

def picture(plots):
    for b in range(len(plots[0])):
        for a in range(len(plots)):
            print (plots[a][b], end = '')
        print ('')

picture(grid)
