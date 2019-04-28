'''
2 神秘的女孩
现有两幅相似图像的数据（矩阵形式存储于1.xlsx, 2.xlsx），之所以相似，是因为记录了同一场景，差别在于其中一个场景中出现了一位神秘的女孩。
(1) 请仅根据两份数据，经过分析，判断神秘的女孩在哪一个图像内。请说明自己判断的依据，及分析过程。
(2) 根据两份数据，对图像进行可视化，验证自己的判断。
(3) 请从你的直觉上为两幅图像的相似性打分（0~1之间，完全不像为0，完全一样为1），计算两幅图像的相关系数，你觉得计算出来的结果与你的主观评价是否相近。
'''

import xlrd
import numpy as np
from PIL import Image

def excel2matix(path):
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    datamatrix = np.zeros((nrows, ncols))
    for x in range(ncols):
        cols = table.col_values(x)
        cols1 = np.matrix(cols)
        datamatrix[:, x] = cols1  # 把数据进行存储
    return datamatrix

# 将数组转为图片
def Matrix2Image(data):
    image = Image.fromarray(data)
    return image


# 计算直方图
def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    hist = sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)
    return hist


# 计算相似度
def calc_similar(li, ri):
    calc_sim = hist_similar(li.histogram(), ri.histogram())
    return calc_sim

if __name__ == '__main__':
    # 获取图像
    excel1 = 'C:\\Users\Andy Sun\Desktop\Task\实验一\\1.xlsx'
    excel2 = 'C:\\Users\Andy Sun\Desktop\Task\实验一\\2.xlsx'
    matix1 = excel2matix(excel1)
    matix2 = excel2matix(excel2)
    image1 = Matrix2Image(matix1)
    image2 = Matrix2Image(matix2)
    image1.show()
    image2.show()
    # 计算相似度
    print("图片间的相似度为： ", calc_similar(image1, image2))

