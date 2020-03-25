### diffing.py
- In DNA sequencing; given two strands of DNA, there are many sequences of mutations (insertions, deletions, etc.) which would have transformed one to the other; we would like to find the most probable. We know that certain mutations are more likely than other, and these probabilities are reflected in the cost table(the pair with higher likelihood has a lower cost).
- Here we solve a more general version. We would like to align two strings, s and t, in a way to produce a minimum-cost alignment. To produce an alignment on two strings s and t, we insert the special character ‘-’ some number of times into each string to produce align s and align t so that:
  - align_s and align_t have the same length, and
  - There is no i such that align s[i] and align t[i] are both ‘-’.
- The cost of an alignment is given by a cost function, which we will call cost. The cost of an alignment is the sum over all i of cost(align s[i], align t[i]). The cost of aligning a letter with itself is always 0.
- The minimum-cost alignment between string s = ‘acb’ and t = ‘baa’ is given by:
  - align_s: -acb 
  - align_t: ba-a


### respacing.py

- The respacing problem is to put spaces back into a string that has lost them, given a dictionary. 
- For example, given the string “itwasthebestoftimes” and an English dictionary, we would like to reconstruct the original sentence: “it was the best of times”.
