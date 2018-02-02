with open('bar_graph_reward.txt') as fp:
    line = fp.readline()
    cnt = 1
    sum = 0
    episode = 0
    while line:
        block1, block2, block3 = line.split(" , ")

        if ("ends" in block2):
            letter, iteration = block3.split("= ")
            sum += int(iteration)
            episode += 1
        line = fp.readline()
        cnt += 1
    averageIter = float(sum / episode)
    print("The average iteration: " + format(averageIter))
