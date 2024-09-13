# Hex to RGB
def rgb2hex(rgb_color):
    r, g, b = rgb_color
    return ('#' + '{:02X}' * 3).format(r, g, b)

# #   0xFDD819-0xE04C4C
# colors = get_multi_colors_by_hsl(hex2rgb(0xFDD819), hex2rgb(0xE04C4C), 100)     # 黄--红
# colors = [(255, 255, 255), ] + colors[:80]   # 信息素为0时，设为白色
# print(colors)
colors = [(255, 255, 255), (253, 216, 25), (252, 213, 25), (252, 211, 26), (252, 209, 26), (251, 207, 27), (251, 205, 27), (251, 203, 28), (250, 201, 28), (250, 199, 29), (250, 197, 29), (249, 195, 30), (249, 193, 30), (249, 191, 31), (248, 189, 32), (248, 187, 32), (248, 186, 33), (247, 184, 33), (247, 182, 34), (247, 180, 34), (246, 178, 35), (246, 176, 35), (246, 174, 36), (246, 173, 36), (245, 171, 37), (245, 169, 37), (245, 167, 38), (244, 166, 38), (244, 164, 39), (244, 162, 40), (243, 160, 40), (243, 159, 41), (243, 157, 41), (242, 155, 42), (242, 154, 42), (242, 152, 43), (242, 151, 43), (241, 149, 44), (241, 147, 44), (241, 146, 45), (240, 144, 45), (240, 143, 46), (240, 141, 46), (239, 140, 47), (239, 138, 47), (239, 137, 48), (239, 135, 48), (238, 134, 49), (238, 132, 49), (238, 131, 50), (237, 130, 51), (237, 128, 51), (237, 127, 52), (237, 125, 52), (236, 124, 53), (236, 123, 53), (236, 121, 54), (235, 120, 54), (235, 119, 55), (235, 117, 55), (234, 116, 56), (234, 115, 56), (234, 114, 57), (234, 112, 57), (233, 111, 58), (233, 110, 58), (233, 109, 59), (232, 108, 59), (232, 106, 60), (232, 105, 60), (232, 104, 61), (231, 103, 61), (231, 102, 62), (231, 101, 62), (231, 100, 63), (230, 99, 63), (230, 97, 64), (230, 96, 64), (229, 95, 65), (229, 94, 65), (229, 93, 66)]


def get_color_by_pheromone(p):
    idx = min(len(colors)-1, int(p * len(colors)))
    return rgb2hex(colors[idx])