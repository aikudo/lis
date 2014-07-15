import random
"""
First attempt using a common dynamic algorithm with n^2.
"""

def printsolution(scores, prev, index):
   if prev[index] != -1:
      printsolution(scores, prev, prev[index])
   print 'score', scores[index]

def longestIncDP(scores):
   longest = 1
   bestend  = 0
   DP = [1] * len(scores)
   prev = [-1] * len(scores)
   for i in range(len(scores)):
      for j in range(i):
         if scores[j][1] > scores[i][1] and DP[j] + 1 > DP[i]:
            DP[i] = DP[j] + 1
            prev[i] = j
      if DP[i] > longest:
         bestend = i
         longest = DP[i]
   #print 'longest distance', DP
   #print 'previous indexes', prev
   printsolution(scores, prev, bestend)

def main():
   numscore = 10
   sat = [random.randint(600,2400) for r in range(numscore)]
   gpa = [round(random.uniform(0,4.0), 2) for r in range(numscore)]
   scores = sorted(zip(sat,gpa))
   print 'input scores', scores
   #scores = [random.randint(0,100) for r in range(numScore)]
   #scores = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
   longestIncDP(scores)


if __name__ == "__main__":
   main()
