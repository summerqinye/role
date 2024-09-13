# Boxplot
import sys
sys.path.append("analysis")
from functions import *

import random
import csv
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

if __name__ == "__main__":
	res = readcsv("C:\\Users\\lenovo\\Desktop\\paper\\opportunistic.csv")
	res1 = readcsv("C:\\Users\\lenovo\\Desktop\\paper\\algorithmic.csv")
	res2 = readcsv("C:\\Users\\lenovo\\Desktop\\paper\\collaborative.csv")

	print(res[1])

	envs = ["open", "urban", "indoor", "natural"]
	sense = ["opp", "alg", "col"]
	sense_id = {"opp":res, "alg":res1, "col":res2}
	env_ids = {"open":[1], "urban":[9,10], "indoor":[2,7], "natural":[3,5]}
	#sizes = [0,30,30,30,30,50,50,30,31,88,100]
	#agents = [0,10,10,10,10,20,20,10,10,100,100]

	# fig, axs = plt.subplots(2, 2, figsize=(6, 6),gridspec_kw={'hspace': 0.3, 'wspace': 0.17},sharey=True)
	fig, axs = plt.subplots(2, 2, figsize=(6, 6), gridspec_kw={'hspace': 0.3, 'wspace': 0.2})
	# plt.ylim(-0.1, 1.8)
	# fig.suptitle('2x2')
	# plt.show()
	print("& Open & Urban & Indoor & Natural \\\\")


	# Efficiency
	print("open", end="")
	d = {}
	for s in sense:
		d[s] = []
		for id in env_ids["open"]:
			# s = to_int(get_data(res,"Travel distance (steps)",constraints={"Scene ID":str(id),"Success rate":"True"}))
			c = get_data(sense_id[s],"coverage",constraints={"Scene ID":str(id)})
			# t = get_data(sense_id[s],"Duration",constraints={"Scene ID":str(id)})
			# s = [i/(sizes[id]*sizes[id]/agents[id]) for i in s]
			d[s] += [float(c[i]) for i in range(len(c))]
			# d[e] += s
	# for e in envs:
	# 	print(" & $%.3f"%np.mean(d[e])+"\pm %.3f$"%np.std(d[e]), end="")
	# print("\\\\")

	data = [d[s] for s in sense]
	mp1 = dict(marker='o', markeredgecolor='#000000',markerfacecolor='#000000',markeredgewidth=0, markersize=4)
	bp1 = axs[0,0].boxplot(data, showmeans = True, meanprops = mp1, widths=0.5, sym='+', patch_artist=True, flierprops = dict(markerfacecolor='#d4d4d4',markeredgecolor="#666666"))
	plt.setp(bp1['boxes'], facecolor='#b2b2b2', linewidth=0)
	# axs[0,0].set_ylim(-0.1, 1.8)
	axs[0,0].set_title("(a) Open")
	axs[0,0].set_ylabel("coverage rate (%)")
	axs[0,0].set_xticklabels(["Opp","Alg","Col"])
	# plt.show()

	print("urban", end="")
	d = {}
	for s in sense:
		d[s] = []
		for id in env_ids["urban"]:
			# s = to_int(get_data(res,"Travel distance (steps)",constraints={"Scene ID":str(id),"Success rate":"True"}))
			c = get_data(sense_id[s], "coverage", constraints={"Scene ID": str(id)})
			# t = get_data(sense_id[s], "Duration", constraints={"Scene ID": str(id)})
			# s = [i/(sizes[id]*sizes[id]/agents[id]) for i in s]
			d[s] += [float(c[i])  for i in range(len(c))]
	# d[e] += s
	# for e in envs:
	# 	print(" & $%.3f"%np.mean(d[e])+"\pm %.3f$"%np.std(d[e]), end="")
	# print("\\\\")

	data = [d[s] for s in sense]
	mp1 = dict(marker='o', markeredgecolor='#000000', markerfacecolor='#000000', markeredgewidth=0, markersize=4)
	bp1 = axs[0, 1].boxplot(data, showmeans=True, meanprops=mp1, widths=0.5, sym='+', patch_artist=True,
							flierprops=dict(markerfacecolor='#d4d4d4', markeredgecolor="#666666"))
	plt.setp(bp1['boxes'], facecolor='#b2b2b2', linewidth=0)
	axs[0, 1].set_title("(b) Urban")
	# axs[0, 1].set_ylim(-0.1, 1.8)
	# axs[0, 1].set_ylabel("coverage speed (% / s)")
	axs[0, 1].set_xticklabels(["Opp", "Alg", "Col"])
	# plt.show()

	print("indoor", end="")
	d = {}
	for s in sense:
		d[s] = []
		for id in env_ids["indoor"]:
			# s = to_int(get_data(res,"Travel distance (steps)",constraints={"Scene ID":str(id),"Success rate":"True"}))
			c = get_data(sense_id[s], "coverage", constraints={"Scene ID": str(id)})
			# t = get_data(sense_id[s], "Duration", constraints={"Scene ID": str(id)})
			# s = [i/(sizes[id]*sizes[id]/agents[id]) for i in s]
			d[s] += [float(c[i])  for i in range(len(c))]
	# d[e] += s
	# for e in envs:
	# 	print(" & $%.3f"%np.mean(d[e])+"\pm %.3f$"%np.std(d[e]), end="")
	# print("\\\\")

	data = [d[s] for s in sense]
	mp1 = dict(marker='o', markeredgecolor='#000000', markerfacecolor='#000000', markeredgewidth=0, markersize=4)
	bp1 = axs[1, 0].boxplot(data, showmeans=True, meanprops=mp1, widths=0.5, sym='+', patch_artist=True,
							flierprops=dict(markerfacecolor='#d4d4d4', markeredgecolor="#666666"))
	plt.setp(bp1['boxes'], facecolor='#b2b2b2', linewidth=0)
	# axs[1,0].set_ylim(-0.1, 1.8)
	axs[1, 0].set_title("(c) Indoor")
	axs[1, 0].set_ylabel("coverage rate (%)")
	axs[1, 0].set_xticklabels(["Opp", "Alg", "Col"])
	# plt.show()

	print("natural", end="")
	d = {}
	for s in sense:
		d[s] = []
		for id in env_ids["natural"]:
			# s = to_int(get_data(res,"Travel distance (steps)",constraints={"Scene ID":str(id),"Success rate":"True"}))
			c = get_data(sense_id[s], "coverage", constraints={"Scene ID": str(id)})
			# t = get_data(sense_id[s], "Duration", constraints={"Scene ID": str(id)})
			# s = [i/(sizes[id]*sizes[id]/agents[id]) for i in s]
			d[s] += [float(c[i])  for i in range(len(c))]
	# d[e] += s
	# for e in envs:
	# 	print(" & $%.3f"%np.mean(d[e])+"\pm %.3f$"%np.std(d[e]), end="")
	# print("\\\\")

	data = [d[s] for s in sense]
	mp1 = dict(marker='o', markeredgecolor='#000000', markerfacecolor='#000000', markeredgewidth=0, markersize=4)
	bp1 = axs[1, 1].boxplot(data, showmeans=True, meanprops=mp1, widths=0.5, sym='+', patch_artist=True,
							flierprops=dict(markerfacecolor='#d4d4d4', markeredgecolor="#666666"))
	plt.setp(bp1['boxes'], facecolor='#b2b2b2', linewidth=0)
	# axs[1,1].set_ylim(-0.1, 1.8)
	axs[1, 1].set_title("(d) Natural")
	# axs[1, 0].set_ylabel("coverage speed (% / s)")
	axs[1, 1].set_xticklabels(["Opp", "Alg", "Col"])
	fig.tight_layout()
	# plt.show()
	plt.savefig("4zitu1.pdf", bbox_inches='tight')

	phic Dimensions: Gender, Country, Age, Income, Experience
