
'''
truth table
player1 player2 result
rock    paper   player1 win
paper   rock    player2 win
scissor rock    player2 win
rock    scissor player1 win
paper   scissor player2 win
scissor paper   player1 win
scissor scissor tie
paper   paper   tie
rock    rock    tie
'''
print "player1 one choose either rock or paper or scissor"
a= raw_input()
print "player2 one choose either rock or paper or scissor"
b= raw_input()
if (a=='rock' and b=='rock'):
    print 'player1? '+a
    print 'player2? '+b
    print 'tie'
elif(a=='paper' and b=='paper'):
    print 'player1? '+a
    print 'player2? '+b
    print 'tie'
elif(a=='paper' and b=='paper'):
    print 'player1? '+a
    print 'player2? '+b
    print 'tie'
elif(a=='paper' and b=='rock'):
    print 'player1? '+a
    print 'player2? '+b
    print 'player1 wins'
elif(a=='rock' and b=='scissor'):
    print 'player1? '+a
    print 'player2? '+b
    print 'player1 wins'
elif(a=='scissor' and b=='paper'):
    print 'player1? '+a
    print 'player2? '+b
    print 'player1 wins'
elif(a=='rock' and b=='paper'):
    print 'player1? '+a
    print 'player2? '+b
    print 'player2 wins'
elif(a=='scissor' and b=='rock'):
    print 'player1? '+a
    print 'player2? '+b
    print 'player2 wins'
elif(a=='paper' and b=='scissor'):
    print 'player1? '+a
    print 'player2? '+b
    print 'player2 wins'
else:
    print 'make sure the spelling of rock or paper or scissor is correct and that they are all in small'
