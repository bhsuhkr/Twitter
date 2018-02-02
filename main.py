with open('point_graph.txt') as fp:
    line = fp.readline()
    sum = [0,0,0,0]
    episode = 0

    while line:
        block1, block2, block3, reward1 = line.split("= ")
        iteration, block4 = block3.split(" ,")

        line = fp.readline() # next line

        block1, block2, block3, reward2 = line.split("= ")

        sum[int(iteration)-1] = int(reward2) - int(reward1)
        line = fp.readline() # next line
        episode += 1

print ("Reward Progress: ",format(sum))