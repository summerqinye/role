# 绘制箱线图
import sys
# sys.path.append("analysis")
from functions import *
import random
import csv
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

if __name__ == "__main__":
	res = readcsv("C:\\Users\\lenovo\\Desktop\\paper\\random.csv")
	print(res[1])

	envs = ["open", "urban", "indoor", "natural"]
	env_ids = {"open":[1], "urban":[9,10], "indoor":[2,7], "natural":[3,5]}
	sizes = [0, 30, 30, 30, 30, 50, 50, 30, 31, 88, 100]
	agents = [0, 10, 10, 10, 10, 20, 20, 10, 10, 100, 100]

	fig, axs = plt.subplots(1, 1, figsize=(3, 3))#,sharey=True)
	print("& Open & Urban & Indoor & Natural \\\\")

	# coverage
	print("Coverage Rate", end="")
	d = {}
	for e in envs:
		d[e] = []
		for id in env_ids[e]:
			# s = get_data(res,"Coverage",constraints={"Scene ID":str(id),"Success rate":"True"})
			s = get_data(res,"Coverage",constraints={"Scene ID":str(id)})
			d[e] += [float(s[i]) for i in range(len(s))]
			# d[e] += [len(s)/len(t)]
			# d[e] += s
	for e in envs:
		print(" & $%.2f"%np.mean(d[e])+"\pm %.2f$"%np.std(d[e]), end="")
	print("\\\\")

	data = [d[e] for e in envs]
	mp1 = dict(marker='o', markeredgecolor='#000000',markerfacecolor='#000000',markeredgewidth=0, markersize=4)
	bp1 = axs.boxplot(data, showmeans = True, meanprops = mp1, widths=0.5, sym='+', patch_artist=True, flierprops = dict(markerfacecolor='#d4d4d4',markeredgecolor="#666666"))
	plt.setp(bp1['boxes'], facecolor='#b2b2b2', linewidth=0)
	axs.set_title("Effectiveness")
	axs.set_ylabel("coverage rate")
	axs.set_xticklabels(["Open","Urban","Indoor","Natural"])

	fig.tight_layout()
	plt.show()
	# plt.savefig("random_results.pdf", bbox_inches='tight')
