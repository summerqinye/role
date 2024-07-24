# 绘制箱线图
import sys
# sys.path.append("analysis")
from functions import *
import random
import csv
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

if __name__ == "__main__":
	res = readcsv("C:\\Users\\lenovo\\Desktop\\paper\\dt.csv")
	print(res[1])

	envs = ["open", "urban", "indoor", "natural"]
	env_ids = {"open":[1], "urban":[9,10], "indoor":[2,7], "natural":[3,5]}
	sizes = [0,30,30,30,30,50,50,30,31,88,100]
	agents = [0,10,10,10,10,20,20,10,10,100,100]

	fig, axs = plt.subplots(1, 3, figsize=(9, 3))#,sharey=True)
	# fig.suptitle('2x2 ')
	print("& Open & Urban & Indoor & Natural \\\\")

	# Steps
	print("Efficiency", end="")
	d = {}
	for e in envs:
		d[e] = []
		for id in env_ids[e]:
			# s = to_int(get_data(res,"Travel distance (steps)",constraints={"Scene ID":str(id),"Success rate":"True"}))
			s = get_data(res,"Coverage",constraints={"Scene ID":str(id)})
			t = get_data(res,"Completion time (s)",constraints={"Scene ID":str(id)})
			# s = [i/(sizes[id]*sizes[id]/agents[id]) for i in s]
			d[e] += [float(s[i]) / float(t[i]) for i in range(len(s))]
			# d[e] += s
	for e in envs:
		print(" & $%.5f"%np.mean(d[e])+"\pm %.6f$"%np.std(d[e]), end="")
	print("\\\\")

	data = [d[e] for e in envs]
	mp1 = dict(marker='o', markeredgecolor='#000000',markerfacecolor='#000000',markeredgewidth=0, markersize=4)
	bp1 = axs[0].boxplot(data, showmeans = True, meanprops = mp1, widths=0.5, sym='+', patch_artist=True, flierprops = dict(markerfacecolor='#d4d4d4',markeredgecolor="#666666"))
	plt.setp(bp1['boxes'], facecolor='#b2b2b2', linewidth=0)
	axs[0].set_title("(a) Efficiency")
	axs[0].set_ylabel("efficiency factor")
	axs[0].set_xticklabels(["Open","Urban","Indoor","Natural"])

	# Clicks
	print("Human Intervention", end="")
	d = {}
	for e in envs:
		d[e] = []
		for id in env_ids[e]:
			s = get_data(res,"Completion time (s)",constraints={"Scene ID":str(id),"Success rate":"True"})
			s2 = get_data(res,"Clicks (left+right)",constraints={"Scene ID":str(id),"Success rate":"True"})
			d[e] += [int(s2[i])/float(s[i]) for i in range(len(s))]
	for e in envs:
		print(" & $%.3f"%np.mean(d[e])+"\pm %.3f$"%np.std(d[e]), end="")
	print("\\\\")

	data = [d[e] for e in envs]
	mp1 = dict(marker='o', markeredgecolor='#000000',markerfacecolor='#000000',markeredgewidth=0, markersize=4)
	bp1 = axs[1].boxplot(data, showmeans = True, meanprops = mp1, widths=0.5, sym='+', patch_artist=True, flierprops = dict(markerfacecolor='#d4d4d4',markeredgecolor="#666666"))
	plt.setp(bp1['boxes'], facecolor='#b2b2b2', linewidth=0)
	axs[1].set_title("(b) Human Interventions")
	axs[1].set_ylabel("intervention frequency")
	axs[1].set_xticklabels(["Open","Urban","Indoor","Natural"])

	# Coverage
	print("Coverage Rate", end="")
	d = {}
	for e in envs:
		d[e] = []
		for id in env_ids[e]:
			# s = get_data(res,"TLX score",constraints={"Scene ID":str(id),"Success rate":"True"})
			s = get_data(res,"Coverage",constraints={"Scene ID":str(id)})
			# d[e] += [float(s[i]) for i in range(len(s))]
			d[e] += [float(s[i]) for i in range(len(s))]
	for e in envs:
		print(" & $%.5f"%np.mean(d[e])+"\pm %.3f$"%np.std(d[e]), end="")
	print("\\\\")

	data = [d[e] for e in envs]
	mp1 = dict(marker='o', markeredgecolor='#000000', markerfacecolor='#000000',markeredgewidth=0, markersize=4)
	bp1 = axs[2].boxplot(data, showmeans = True, meanprops = mp1, widths=0.5, sym='+', patch_artist=True, flierprops = dict(markerfacecolor='#d4d4d4',markeredgecolor="#666666"))
	plt.setp(bp1['boxes'], facecolor='#b2b2b2', linewidth=0)
	axs[2].set_title("(c) Effectiveness")
	axs[2].set_ylabel("coverage rate")
	axs[2].set_xticklabels(["Open","Urban","Indoor","Natural"])

	fig.tight_layout()
	plt.show()
	# plt.savefig("HSI_results.pdf", bbox_inches='tight')

    # for p in ["Prolific","MTurk"]:
    #     prsint(p)
    #     for target in ["posture","posture_health","armrests","sitting_position","backrest","break","screen_distance","screen_position","keyboard/mouse","eyes","head","neck/shoulders","back","seat/thighs","knees/feet"]:
    #         d = get_data(res,target,constraints={"platform":p})
    #         print("\item "+target.replace("_"," ")+":",get_stats(d))

    # Ergonomics
    # fig, axs = plt.subplots(1,3,figsize=(10, 2.5))
    #
    # i = j = 0
    # for p in ["Prolific","MTurk"]:
    #     for target in ["posture","posture_health","break"]:
    #         s = get_stats(get_data(res,target,constraints={"platform":p}))
    #
    #         if target == "posture":
    #             keys = ["Sitting","Sitting and Standing","Standing","Other"]
    #             labels = ["sitting","sitting/\nstanding","standing","other"]
    #             xlabel = "(a) working posture"
    #             ylim = 135
    #             axs[j].set_xticks(np.array(range(len(labels)))+0.2)
    #             axs[j].set_xticklabels(labels)
    #         elif target == "posture_health":
    #             keys = ["Very unhealthy", "Unhealthy", "Slightly unhealthy","Neutral","Slightly healthy","Healthy","Very healthy"]
    #             labels = keys
    #             xlabel = "(b) self-evaluated overall posture"
    #             ylim = 55
    #             axs[j].set_xticks([0.2,3.2,6.2])
    #             axs[j].set_xticklabels(["very unhealthy","neutral","very healthy"])
    #         elif target == "break":
    #             keys = ["Less than every 30 minutes","Once every 30-60 minutes","Once every 1-2 hours","Once every 2-4 hours","Longer than every 4 hours"]
    #             labels = ["$<$0.5","0.5-1","1-2","2-4","$>$4"]
    #             xlabel = "(c) frequency of breaks (once every x hours)"
    #             ylim = 55
    #             axs[j].set_xticks(np.array(range(len(labels)))+0.2)
    #             axs[j].set_xticklabels(labels)
    #
    #         d = []
    #         for k in keys: d.append(0 if k not in s.keys() else s[k])
    #         axs[j].bar(np.array(range(len(labels)))+(0 if p=="Prolific" else 0.4), d, width=0.4, color="#67a9cf" if p=="Prolific" else "#f1a340", edgecolor="#31749b" if p=="Prolific" else "#be720e")
    #         for k in range(len(labels)):
    #             axs[j].text(k+(0 if p=="Prolific" else 0.4), d[k]+(ylim/50), str(d[k]), ha="center", color="#737373", fontsize=9)
    #         # axs[j].set_xlabel(xlabel, fontsize=11)
    #         axs[j].set_title(xlabel, fontsize=11)
    #         axs[0].set_ylabel("\n\# of workers")
    #         axs[j].set_ylim(0,ylim)
    #         axs[1].legend(["Prolific","MTurk"], ncol=2, edgecolor="#000000",fontsize=10, framealpha=0.5, bbox_to_anchor=(0.9,-0.2))
    #         j += 1
    #     i += 1
    #     j = 0
    # fig.tight_layout()
    # plt.show()
    # # plt.savefig("analysis/fig/ergonomics.pdf",bbox_inches='tight')

    # Sitting
    # fig, axs = plt.subplots(1,3,figsize=(10, 2.5))
    #
    # i = j = 0
    # for p in ["Prolific","MTurk"]:
    #     for target in ["armrests","sitting_position","backrest"]:
    #         s = get_stats(get_data(res,target,constraints={"platform":p}))
    #
    #         if target == "armrests":
    #             keys = ["No armrests","Rarely","Sometimes","Often","Always"]
    #             labels = ["no armrests","rarely","sometimes","often","always"]
    #             xlabel = "(a) use of armrest"
    #             ylim = 65
    #         elif target == "sitting_position":
    #             keys = ["On the front edge of the chair", "In the middle of the chair","To the back of the chair"]
    #             labels = ["front edge", "middle","back"]
    #             xlabel = "(b) sitting position on the chair"
    #             ylim = 85
    #             axs[j].set_xlim(-0.5,3)
    #         elif target == "backrest":
    #             keys = ["No backrest","Sitting upright with the backrest","Leaning on the backrest"]
    #             labels = ["no backrest","sitting upright","leaning"]
    #             xlabel = "(c) use of backrest"
    #             ylim = 85
    #             axs[j].set_xlim(-0.5,3)
    #
    #         d = []
    #         for k in keys: d.append(0 if k not in s.keys() else s[k])
    #         axs[j].bar(np.array(range(len(labels)))+(0 if p=="Prolific" else 0.4), d, width=0.4, color="#67a9cf" if p=="Prolific" else "#f1a340", edgecolor="#31749b" if p=="Prolific" else "#be720e")
    #         for k in range(len(labels)):
    #             axs[j].text(k+(0 if p=="Prolific" else 0.4), d[k]+(ylim/50), str(d[k]), ha="center", color="#737373", fontsize=10)
    #         # axs[j].set_xlabel(xlabel, fontsize=11)
    #         axs[j].set_title(xlabel, fontsize=11)
    #         axs[j].set_xticks(np.array(range(len(labels)))+0.2)
    #         axs[j].set_xticklabels(labels)
    #         axs[0].set_ylabel("\n\# of workers")
    #         axs[j].set_ylim(0,ylim)
    #         axs[1].legend(["Prolific","MTurk"], ncol=2, edgecolor="#000000",fontsize=10, framealpha=0.5, bbox_to_anchor=(0.9,-0.2))
    #         j += 1
    #     i += 1
    #     j = 0
    # fig.tight_layout()
    # plt.show()
    # # plt.savefig("analysis/fig/sitting.pdf",bbox_inches='tight')

    # Devices
    # fig, axs = plt.subplots(1,3,figsize=(10, 2.5))
    #
    # i = j = 0
    # for p in ["Prolific","MTurk"]:
    #     for target in ["screen_distance","screen_position","keyboard/mouse"]:
    #         s = get_stats(get_data(res,target,constraints={"platform":p}))
    #
    #         if target == "screen_distance":
    #             keys = ["Much shorter than an arm's length","Shorter than an arm's length","About an arm's length","Longer than an arm's length","Much longer than an arm's length"]
    #             labels = ["much shorter","","an arm's length","","much longer"]
    #             xlabel = "(a) distance to the screen"
    #             ylim = 95
    #         elif target == "screen_position":
    #             keys = ["Much lower than my eye level", "Lower than my eye level", "At my eye level","Higher than my eye level", "Much higher than my eye level"]
    #             labels = ["much lower","", "At the eye level","","much higher"]
    #             xlabel = "(b) vertical position of the screen"
    #             ylim = 75
    #         elif target == "keyboard/mouse":
    #             keys = ["The height of my keyboard/mouse supports a 90 degree elbow angle","I can easily reach my keyboard/mouse","The position of my keyboard/mouse requires overreaching with the shoulder"]
    #             labels = ["supports a $90^{\circ}$\nelbow angle","easily\nreached","requires\noverreaching"]
    #             xlabel = "(c) the position of keyboard/mouse"
    #             ylim = 155
    #             axs[j].set_xlim(-0.5,3)
    #
    #         d = []
    #         for k in keys: d.append(0 if k not in s.keys() else s[k])
    #         axs[j].bar(np.array(range(len(labels)))+(0 if p=="Prolific" else 0.4), d, width=0.4, color="#67a9cf" if p=="Prolific" else "#f1a340", edgecolor="#31749b" if p=="Prolific" else "#be720e")
    #         for k in range(len(labels)):
    #             axs[j].text(k+(0 if p=="Prolific" else 0.4), d[k]+(ylim/50), str(d[k]), ha="center", color="#737373", fontsize=10)
    #         # axs[j].set_xlabel(xlabel, fontsize=11)
    #         axs[j].set_title(xlabel, fontsize=11)
    #         axs[j].set_xticks(np.array(range(len(labels)))+0.2)
    #         axs[j].set_xticklabels(labels)
    #         axs[0].set_ylabel("\n\# of workers")
    #         axs[j].set_ylim(0,ylim)
    #         axs[1].legend(["Prolific","MTurk"], ncol=2, edgecolor="#000000",fontsize=10, framealpha=0.5, bbox_to_anchor=(0.9,-0.2))
    #         j += 1
    #     i += 1
    #     j = 0
    # fig.tight_layout()
    # plt.show()
    # # plt.savefig("analysis/fig/devices.pdf",bbox_inches='tight')

    # # Body discomfort
    # # fig, axs = plt.subplots(1,2,figsize=(6, 4), gridspec_kw={'width_ratios': [1.5, 2]})
    # fig, axs = plt.subplots(1,2,figsize=(6, 3))
    # data = {}
    # for p in ["Prolific","MTurk"]:
    #     data[p] = []
    #     for target in ["knees/feet","seat/thighs","back","neck/shoulders","head","eyes"]:
    #         data[p].append(get_data(res,target,constraints={"platform":p,"transcribe":True}))
    #         # w,pvalue = scipy.stats.shapiro(data[p][-1])
    #         # print(p,target,w,pvalue)
    #     # h,pvalue = scipy.stats.kruskal(data[p][0],data[p][1],data[p][2],data[p][3],data[p][4],data[p][5])
    #     # print(p,h,pvalue)
    # # body = ["knees/feet","seat/thighs","back","neck/shoulders","head","eyes"]
    # # for i in range(6):
    # #     u,p = scipy.stats.mannwhitneyu(data["Prolific"][i],data["MTurk"][i])
    # #     print(body[i],p)
	#
    # mp1 = dict(marker='o', markeredgecolor='#be720e',markerfacecolor='#be720e',markeredgewidth=0, markersize=4)
    # mp2 = dict(marker='o', markeredgecolor='#31749b',markerfacecolor='#31749b',markeredgewidth=0, markersize=4)
    # bp1 = axs[1].boxplot(data["MTurk"], positions=np.array(range(6)), showmeans = True, meanprops = mp1, widths=0.25, sym='+', vert=False, patch_artist=True, flierprops = dict(markerfacecolor='#f1a340',markeredgecolor="#f1a340"))
    # bp2 = axs[1].boxplot(data["Prolific"], positions=np.array(range(6))+0.3, showmeans = True, meanprops = mp2, widths=0.25, sym='+', vert=False, patch_artist=True, flierprops = dict(markerfacecolor='#67a9cf',markeredgecolor="#67a9cf"))
    # plt.setp(bp1['boxes'], facecolor='#f1a340', linewidth=0)
    # plt.setp(bp2['boxes'], facecolor='#67a9cf', linewidth=0)
    # axs[1].set_xticks([1,4,7])
    # axs[1].set_xticklabels(["very\nuncomfortable","neutral","very\ncomfortable"])
    # axs[1].set_yticks(np.array(range(6))+0.15)
    # axs[1].set_yticklabels(["knees/feet","*seat/thighs","*back","*neck/shoulders","*head","*eyes"])
    # axs[1].legend([bp2["boxes"][0],bp1["boxes"][0]], ["Prolific","MTurk"], loc=9, ncol=2, edgecolor="#000000",fontsize=10, framealpha=0, bbox_to_anchor=(0.5,1.15))
	#
    # axs[0].set_xlim(0, 1)
    # axs[0].set_ylim(0, 1)
	#
    # body = mpimg.imread("analysis/fig/body.png")
    # # imagebox = OffsetImage(body, zoom=0.228)
    # # ab = AnnotationBbox(imagebox, (0.6, 0.43), frameon=False)
    # imagebox = OffsetImage(body, zoom=0.3)
    # ab = AnnotationBbox(imagebox, (0.7, 0.41), frameon=False)
    # img = axs[0].add_artist(ab)
    # axs[0].set_frame_on(False)
    # axs[0].tick_params(left=False, labelleft=False)
    # axs[0].tick_params(bottom=False, labelbottom=False)
	#
    # plt.draw()
    # fig.tight_layout()
    # plt.show()
    # # plt.savefig("analysis/fig/discomfort.pdf",bbox_inches='tight', dpi=300)

    # Spearman
    # fullname = {
    #     "posture_health": "Overall posture",
    #     "break": "Frequency of breaks",
    #     "screen_distance": "Screen distance",
    #     "screen_position": "Screen position",
    #     "armrests": "Use of armrest",
    #     "working_duration": "Working hours"
    # }
    # print()
    # for v1 in ["posture_health","break","screen_distance","screen_position","armrests","working_duration"]:
    #     print("\\textbf{\\emph{"+fullname[v1],end="}} ")
    #     for v2 in ["eyes","head","neck/shoulders","back","seat/thighs","knees/feet"]:
    #         constraints={"transcribe":True}
    #         if v1 == "armrests":
    #             constraints["posture"] = "Sitting"
    #         d1 = get_data(res,v1,constraints)
    #         d2 = get_data(res,v2,constraints)
	#
    #         if v1 == "armrests":
    #             constraints["posture"] = "Sitting and standing"
    #             d1 = d1 + get_data(res,v1,constraints)
    #             d2 = d2 + get_data(res,v2,constraints)
	#
    #         r, p = scipy.stats.spearmanr(d1, d2)
    #         print("& %.3f"%r+" & %.3f"%p,end="* " if p < 0.05 else " ")
    #         # for i in range(len(d1)):
    #         #     d1[i] = d1[i]+ (random.random()-0.5)/2
    #         #     d2[i] = d2[i]+ (random.random()-0.5)/2
    #         # plt.scatter(d1,d2)
    #     print("\\\\")

    # Analysis across Demographic Dimensions: Gender, Country, Age, Income, Experience
