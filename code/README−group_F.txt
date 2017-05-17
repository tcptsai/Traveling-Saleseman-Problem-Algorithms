Structure:
code\
  main.py: main function to run with different arguments
  algBnB.py: Branch and Bound algorithm
  algNN.py: Nearest Neighbor Approximation algorithm
  algMA.py: MST Approximation algorithm
  algSA.py: Simulated Annealing algorithm
  algILS.py: Iterated Local Search algorithm
  runCommand.py: script for running commands and generating log file
  README−groupF.txt: this readme file

Execution:
"python main.py -inst <instance> -alg <algorithm> -time <time> -seed <seed>"
  <instance>: DATA/'instance_name'.tsp
    instance_name: 'Cincinnati', 'UKansasState', 'Atlanta', 'Philadelphia', 'Boston',
    'Champaign', 'NYC', 'Denver', 'SanFrancisco', 'UMissouri', 'Toronto', 'Roanoke'
  <algorithm>: 'BnB' for Branch and Bound, 'Heur' for Nearest Neighbor Approximation,
  'MSTApprox' for MST Approximation, 'LS1' for Simulated Annealing, 'LS2' for Iterated Local Search
  <time>: cut-off time in second
  <seed>: random seed id
