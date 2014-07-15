import random
import sys

"""
Longest Monotonic Subsequence in 2D
There is a hypothesis floating around that SAT score is a strong indicator
of GPA. Your task is to provide the strongest counter example for this
hypothesis. Given a data set of (sat, gpa) for the final year of a group
of students, devise an algorithm to construct the longest sequence of
(sati, gpai) of students with progressively better SAT scores, and
progressively worse gpa’s, i.e. sat1 < sat2 < … < satk and gpa1 >
gpa2 > … > gpak ( Assume SAT scores and gpa’s are unique )
"""

def longestIncBinarySearch(X):
   """Finding a longest sequence using a Binary Search. O(nlogn)
   http://en.wikipedia.org/wiki/Longest_increasing_subsequence """
   L = 0
   P = [0] * len(X)
   M = [0] * (len(X) + 1)
   for i in range(len(X)):
      lo = 1
      hi = L
      while lo <= hi:
         mid = (lo+hi)/2
         if X[M[mid]][1] > X[i][1]:
            lo = mid+1
         else:
            hi = mid-1
      newL = lo
      P[i] = M[newL-1]
      if newL > L:
         M[newL] = i
         L = newL
      elif X[i][1] > X[M[newL]][1]:
         M[newL] = i
# Reconstruct the longest increasing subsequence
   S = [0] * L
   k = M[L]
   for i in reversed(range(L)):
      S[i] = X[k]
      k = P[k]
   return S

def main():
   numscore = 10
   sat = [random.randint(600,2400) for r in range(numscore)]
   gpa = [round(random.uniform(0,4.0), 2) for r in range(numscore)]
   scores = sorted(zip(sat,gpa))
   hypo = longestIncBinarySearch(scores)
   print 'scores', scores
   print 'anti-hypothesis', hypo

if __name__ == "__main__":
   main()
