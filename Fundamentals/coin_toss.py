import random
def toss_coin():
    count_head = 0
    count_tail = 0  
    for i in range (0, 5000):
        random_num = random.randint(0,100)
        if random_num >= 50:
            count_head += 1
            print ("Attemp #" + str(i) + ": Throwing a coin... It's a head... Got " + str(count_head) + " head(s) so far and " + str(count_tail) +" tail(s) so far")
        if random_num < 50:
            count_tail += 1
            print ("Attemp #" + str(i) + ": Throwing a coin... It's a tail... Got " + str(count_head) + " head(s) so far and " + str(count_tail ) + " tail(s) so far")

toss_coin()

