"""
Script for running commands and generating log file by CSE6140 fall 2016 Group F
"""

from subprocess import call

alg = ['LS1', 'LS2']

time = 60

seed_from = 1
seed_to = 10

instances = [
'Cincinnati',
'UKansasState',
'Atlanta',
'Philadelphia',
'Boston',
'Champaign',
'NYC',
'Denver',
'SanFrancisco',
'UMissouri',
'Toronto',
'Roanoke'
]

fw = open('output.log', 'w')
fw.close()

for a in alg:
    for i in instances:
        fw = open('output.log', 'a')
        fw.write(a + " " + i + '\n')
        fw.close()
        for j in range(seed_from, seed_to + 1):
            print a, i, str(j)
            call(['python', 'main.py', '-inst', 'DATA/' + i + '.tsp', '-alg', a, '-seed', str(j), '-time', str(time)])
        fw = open('output.log', 'a')
        fw.write('\n')
        fw.close()
