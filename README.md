# Rankings-to-Bracket
Brute force count how many different rankings lead to the exact same single elimination bracket

For example, 2^2=4 contestants, if A plays B and C plays D, and A and C both win, and then A wins in the finals, a bracket fails to differentiate between the best-to-worst rankings A/B/C/D, A/C/B/D, and A/C/D/B, so we want to return 3. 
