'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

    Input: asteroids = [5,10,-5]
    Output: [5,10]
    Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output=[]
        for i in asteroids:
            if not output or output[-1]<0 or i>0:
                output.append(i)
                continue
            else:
                while True:
                    if not output:
                        output.append(i) 
                        break
                    elif output[-1]<0:
                        output.append(i)
                        break
                    elif -i<output[-1]:
                        break
                    elif -i==output[-1]:
                        del output[-1]
                        break
                    else:
                        del output[-1]
        return output