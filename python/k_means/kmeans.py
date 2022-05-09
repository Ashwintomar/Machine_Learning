from random import randint
from math import sqrt
from statistics import mean


def clustering(x, y, cluster1x, cluster1y, cluster2x, cluster2y, cluster3x, cluster3y):

    cluster1_x = []
    cluster1_y = []
    cluster2_x = []
    cluster2_y = []
    cluster3_x = []
    cluster3_y = []

    for i in range(len(x)):
        eucC1 = sqrt((x[i]-cluster1x)**2+(y[i]-cluster1y)**2)
        eucC2 = sqrt((x[i]-cluster2x)**2+(y[i]-cluster2y)**2)
        eucC3 = sqrt((x[i]-cluster3x)**2+(y[i]-cluster3y)**2)
        if(min(eucC1, eucC2, eucC3) == eucC1):
            cluster1_x.append(x[i])
            cluster1_y.append(y[i])

            continue
        elif(min(eucC1, eucC2, eucC3) == eucC2):
            cluster2_x.append(x[i])
            cluster2_y.append(y[i])

            continue
        elif(min(eucC1, eucC2, eucC3) == eucC3):
            cluster3_x.append(x[i])
            cluster3_y.append(y[i])

            continue

    cluster1x_mean = mean(cluster1_x)
    cluster1y_mean = mean(cluster1_y)
    cluster2x_mean = mean(cluster2_x)
    cluster2y_mean = mean(cluster2_y)
    cluster3x_mean = mean(cluster3_x)
    cluster3y_mean = mean(cluster3_y)

    cluster1x = cluster1x_mean
    cluster1y = cluster1y_mean
    cluster2x = cluster2x_mean
    cluster2y = cluster2y_mean
    cluster3x = cluster3x_mean
    cluster3y = cluster3y_mean
    return cluster1x, cluster1y, cluster2x, cluster2y, cluster3x, cluster3y

    # for i in range(0, 100):

    #     min_dist1 = abs(data[i]-cluster1)
    #     min_dist2 = abs(data[i]-cluster2)
    #     min_dist3 = abs(data[i]-cluster3)
    #     if(min(min_dist1, min_dist2, min_dist3) == min_dist1):
    #         cluster1_data.append(data[i])
    #         continue
    #     elif(min(min_dist1, min_dist2, min_dist3) == min_dist2):
    #         cluster2_data.append(data[i])
    #         continue
    #     elif(min(min_dist1, min_dist2, min_dist3) == min_dist3):
    #         cluster3_data.append(data[i])
    #         continue

    # cluster1_mean = sum(cluster1_data)/len(cluster1_data)
    # cluster2_mean = sum(cluster2_data)/len(cluster2_data)
    # cluster3_mean = sum(cluster3_data)/len(cluster3_data)

    # cluster1 = cluster1_mean
    # cluster2 = cluster2_mean
    # cluster3 = cluster3_mean
    # return cluster1, cluster2, cluster3


x = [1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 9]
y = [8, 4, 7, 8, 9, 7, 8, 3, 4, 5, 2, 4, 5, 6, 2, 3, 4, 5, 3, 4]
ctr = 0
# data = []
# for i in range(0, 100):
#     data.append((randint(0, 100)+randint(0, 100))/2)
cluster1x = randint(1, 3)
cluster1y = randint(1, 3)
cluster2x = randint(1, 6)
cluster2y = randint(1, 6)
cluster3x = randint(1, 10)
cluster3y = randint(1, 10)

clusterx_prev1 = 0
clusterx_prev2 = 0
clusterx_prev3 = 0
clustery_prev1 = 0
clustery_prev2 = 0
clustery_prev3 = 0
ctr = 0
while(clusterx_prev1 != cluster1x and clusterx_prev2 != cluster2x and clusterx_prev3 != cluster3x and clustery_prev1 != cluster1y and clustery_prev2 != cluster2y and clustery_prev3 != cluster3y):

    clusterx_prev1 = cluster1x
    clusterx_prev2 = cluster2x
    clusterx_prev3 = cluster3x
    clustery_prev1 = cluster1y
    clustery_prev2 = cluster2y
    clustery_prev3 = cluster3y
    cluster1x, cluster1y, cluster2x, cluster2y, cluster3x, cluster3y = clustering(
        x, y, cluster1x, cluster1y, cluster2x, cluster2y, cluster3x, cluster3y)
    print("Iteration : ", ctr+1, "\nC1 :", cluster1x, ",", cluster1y, "\nC2 :", cluster2x, ",",
          cluster2y, "\nC3 :", cluster3x, ",", cluster3y)
    ctr = ctr+1

# print("C1 :", cluster1x,",", cluster1y, "C2 :", cluster2x,",",
#       cluster2y, "C3 :", cluster3x,",",cluster3y)
