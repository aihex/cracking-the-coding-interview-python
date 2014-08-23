'''
If we drop the first egg every ten floors from the 10th floor, and if the egg breaks at the 10th floor. We drop the other egg from 1 - 10. If the first one breaks at the 100th floor, we drop the second egg from 91 to 100. In this way, if the larger N, more number of test.

I can try to make them as balanced as possbile. If the first egg breaks at the 1th trail, we use x trails to find N, the total number of trails is (x+1). If the first egg breaks at the ith trail, we basically want the numder of dropping the second egg plus i to equal to (x+1). The number of trail for the second egg is (x+i-i).

Then we can get (x) + (x-1) + (x-2) ... + (x-(x-1)) - (x-x) >= 100
(x+1)*x / 2 >= 100, min(x) = 14
'''
