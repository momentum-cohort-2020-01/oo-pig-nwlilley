Game
Responsibilities
 - randomly decide which player goes first
 - hosts a round, in which each player gets a single turn
  - 
 - keep Player and CpuPlayer total
    - if total equals or exceeds 100, declare winner
 - end turn, start another


Player
Responsibilities
- roll die 
- choose to play or hold
  - 'while' player continues to choose to (r)oll, roll die and add roll value into list
  - when player  chooses to (h)old, stop and total the values in the list
  - if player rolls 1, replace score value with 0
- collect and show round score
- collect and show total score


CpuPlayer
Responsibilities
- roll die 
- holds until they roll a total of 20 points
- collect and show round score
- collect and show total score

Die
Responsibilities
- contains 6 numbers, 1 - 6
- randomly produce number in its range

