'''
suppose all lockers are closed originally. If there are odd number of operations on anyone of them, it will end up with being open.

For 1<=k<=100 and an arbitrary x, if x % k == 0, it must happen that x % (x/k) == 0. Thus, two operations will be performed on x. In order to make the totoally number of operations are odd, for some x, there must be that k == (x/k), thus x = k^2. Now, we can see which locker will end up with being open.
'''
