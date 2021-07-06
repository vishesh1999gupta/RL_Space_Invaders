import pickle
from main_visual import *
# from main import *


# f = open('./weight_data_1.1/gen_108.pickle', "rb")
# data = pickle.load(f)
# score = main_menu(data[8])

# f = open('./weight_data_1.2/gen_98.pickle', "rb")
# data = pickle.load(f)
# score = main_menu(data[22])


# f = open('./weight_data_2.1/gen_121.pickle', "rb")
# data = pickle.load(f)
# main_menu(data[23])

f = open('./weight_data_2.2/gen_101.pickle', "rb")
data = pickle.load(f)
score = main_menu(data[29])






idx = -1
max = -1
# for j in range(75):
# 	score, reward = main_menu(data[j])
# 	print(score)
# 	if max < score:
# 		max = score
# 		idx = j
#
# print(idx)



# For calculation of avg and max scores


# maxValues_1 = []
# avgValues_1 = []
#
# for j in range(150):
# 	print(j)
# 	f = open('./weight_data_penalty/gen_' + str(j) + '.pickle', "rb")
# 	data = pickle.load(f)
# 	scores = []
# 	maxScore = 0
# 	for i in range(0,74):
# 		score, reward = main_menu(data[i])
# 		# print(j,i,score, reward)
# 		maxScore = max(maxScore, score)
# 		scores.append(score)
#
# 	avg = 0
# 	for i in scores:
# 		avg += i
# 	maxValues_1.append(float(maxScore))
# 	avgValues_1.append(avg/75)
#
# print(maxValues_1)
# print(avgValues_1)




# maxValues_2 = []
# avgValues_2 = []

# for j in range(150):
#
# 	f = open('./weight_data_config_2/gen_' + str(j) + '.pickle', "rb")
# 	data = pickle.load(f)
# 	scores = []
# 	maxScore = 0
# 	for i in range(0,74):
# 		score, reward = main_menu(data[i])
# 		maxScore = max(maxScore, score)
# 		scores.append(score)
#
# 	avg = 0
# 	for i in scores:
# 		avg += i
#
# 	print(j,maxScore)
# 	maxValues_2.append(float(maxScore))
# 	avgValues_2.append(avg/75)

def saveWeights(filename, weights):
	with open(filename,'wb') as f:
		pickle.dump(weights, f)


# saveWeights('./NN_uniform/avgValues_1.pickle',avgValues_1)
# saveWeights('./NN_uniform/avgValues_2.pickle',avgValues_2)
# saveWeights('./NN_uniform/maxValues_1.pickle',maxValues_1)
# saveWeights('./NN_uniform/maxValues_2.pickle',maxValues_2)






