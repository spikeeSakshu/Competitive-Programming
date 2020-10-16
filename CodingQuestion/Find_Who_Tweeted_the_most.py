'''
You will be given a list of tweets
Your program should find the user who has tweeted the most

Note:
    • If multiple users are having same number of tweets, then print all the users in alphabetical order of user names.
    • Use Python 3
    • Follow python coding style guide
    • Only <filename>.py file should be uploaded. Do not upload <filename>.ipnb file

Input format:
    1. Read the input from console.
    2. First line of input should be number of test cases
    3. Remaining lines of input should contain each test case input. 

For each test case input:
    1. First line should contain number of tweets.
    2. Followed by N lines, each containing user name and tweet id separated by a space.

Output format:
Find the user with max number of tweets. Print user name and total number of tweets.


Sample 1:
Input 
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4

Output
sachin 3

Sample 2:
Input 
1
6
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
kohli tweet_id_5
kohli tweet_id_6

Output
kohli 2
sachin 2
sehwag 2

Sample 3:
Input 
2
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
5
dhoni tweet_id_10
dhoni tweet_id_11
kohli tweet_id_12
dhoni tweet_id_13
dhoni tweet_id_14

Output
sachin 2
sehwag 2
dhoni 4
'''


f = open("input.txt", "r")

t = int(f.readline().replace('\n',''))
for i in range(t):
    names = dict()
    counts= dict()
    n = int(f.readline().replace('\n',''))
    for j in range(n):
        temp = f.readline().replace('\n','').split()
        name = temp[0]
        tweet_id = temp[1]
        if name not in names:
            names[name] = 1
            if len(counts)== 0:
                counts[str(1)]= [name]
            else:
                counts[str(1)].append(name)
        else:
            prev_count= names[name]
            new_count= prev_count+1
            names[name] = new_count
            counts[str(prev_count)].remove(name)

            if str(new_count) not in counts.keys():
                counts[str(new_count)]= [name]
            else:
                counts[str(new_count)].append(name)

    max_tweets= max(counts)
    for i in sorted(counts[max_tweets]):
        print(i, max_tweets)