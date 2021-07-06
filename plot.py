import pickle
import matplotlib.pyplot as plt

#  For two point NN Genetic Algorithm

f = open('./NN_two_point/avgValues_1.pickle', "rb")
data = pickle.load(f)
avgValues_1 = data

f = open('./NN_two_point/avgValues_2.pickle', "rb")
data = pickle.load(f)
avgValues_2 = data
#
# f = open('./NN_two_point/maxValues_1.pickle', "rb")
# data = pickle.load(f)
# maxValues_1 = data
#
# f = open('./NN_two_point/maxValues_2.pickle', "rb")
# data = pickle.load(f)
# maxValues_2 = data

# For Uniform NN genetic Algorithm

# f = open('./NN_uniform/avgValues_1.pickle', "rb")
# data = pickle.load(f)
# avgValues_1 = data
#
# f = open('./NN_uniform/avgValues_2.pickle', "rb")
# data = pickle.load(f)
# avgValues_2 = data

# f = open('./NN_uniform/maxValues_1.pickle', "rb")
# data = pickle.load(f)
# maxValues_1 = data
#
# f = open('./NN_uniform/maxValues_2.pickle', "rb")
# data = pickle.load(f)
# maxValues_2 = data


# for i in data:
#     avgValues_1.append(i*2)

# def saveWeights(filename, weights):
# 	with open(filename,'wb') as f:
# 		pickle.dump(weights, f)
#
#
# saveWeights('./NN_uniform/avgValues_1.pickle',avgValues_1)
# print(data)

y = []
for i in range(150):
    y.append(i)

# for avg values plot

plt.figure(figsize=(10,5))
plt.plot(y,avgValues_1,label="Config_2")
plt.plot(y,avgValues_2,label="Config_1")
plt.xlabel('Generation')
plt.ylabel('Avg Score')
plt.legend()
plt.show()


# For max values plot

# plt.figure(figsize=(10,5))
# plt.plot(y,maxValues_1,label="Config_2")
# plt.plot(y,maxValues_2,label="Config_1")
# plt.xlabel('Generation')
# plt.ylabel('Max Score')
# plt.legend()
# plt.show()

