#!usr/bin/env python
# encoding:utf-8

'''
__Author__:沂水寒城
功能：求解列表中元素的排列和组合问题
'''

from itertools import product
from itertools import combinations
import itertools
import pprint

def test_func1(*num_list):
    '''
    生成排列
    列表中元素不允许重复出现
    排列数计算为：n！，其中n为num_list列表中元素个数
    '''
    tmp_list = itertools.permutations(num_list)
    res_list = []
    for one in tmp_list:
        res_list.append(one)
    pprint.pprint(res_list)
    print('元素不允许重复出现排列总数为:', len(res_list))

#这个功能是一样的
def test_func11(num_list):
    '''
    生成排列
    列表中元素可以重复出现
    排列总数计算为：(n*n*n...*n)，一共n个n相乘
    '''
    num = len(num_list)
    res_list = list(product(num_list, repeat=num))
    print(res_list)
    print('元素可以重复出现排列总数为:', len(res_list))

#自己选择次数
def test_func11_add_num(num_list, num=5):
    '''
    生成排列
    列表中元素可以重复出现
    排列总数计算为：(n*n*n...*n)，一共n个n相乘
    '''
    # num = len(num_list)
    res_list = list(product(num_list, repeat=num))
    print(res_list)
    print('元素可以重复出现排列总数为:', len(res_list))


def test_func2(num_list):
    '''
    生成组合,不限元素个数
    列表中元素不允许重复出现
    组合数计算为：2^n，其中n为num_list列表中元素个数
    '''
    res_list = []
    for i in range(len(num_list) + 1):
        res_list += list(combinations(num_list, i))
    print(res_list)
    print('元素不允许重复出现组合总数为:', len(res_list))


def test_func22(num_list):
    '''
    生成组合,不限元素个数
    列表中元素可以重复出现
    '''
    res_list = []
    num_list1 = [str(i) for i in num_list]
    for i in range(0, len(num_list) + 1):
        res_list += [''.join(x) for x in itertools.product(*[num_list1] * i)]
    print(res_list)
    print('元素可以重复出现组合总数为:', len(res_list))

def generate_five_list(all_candiante_nms, INFERENCE_TH_TEST):
    if len(INFERENCE_TH_TEST) == 5:
        with open("./resut_remove_first_low_0.5.txt", "a+") as f:
            f.write(str(INFERENCE_TH_TEST))
            f.write('\n')
        return

    for values in all_candiante_nms:
        if len(INFERENCE_TH_TEST) == 0 and values < 0.5:
            continue
        INFERENCE_TH_TEST.append(values)
        generate_five_list(all_candiante_nms, INFERENCE_TH_TEST)
        INFERENCE_TH_TEST.pop()

#实现排列中10个取5个
def permutations_10_chose_5(num_list, num=2):
    '''
    生成排列
    列表中元素不允许重复出现
    排列数计算为：n！，其中n为num_list列表中元素个数
    '''
    tmp_list = itertools.permutations(num_list, r=5)
    res_list = []
    for one in tmp_list:
        res_list.append(one)
    pprint.pprint(res_list)
    print('元素不允许重复出现排列总数为:', len(res_list))

if __name__ == '__main__':
    # num_list = [1, 2, 3, 4]
    # num_list = [0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7,0.8,0.9]

    # test_func1(num_list)
    # print('-------------------------------------')
    # test_func11(num_list)
    # print('-------------------------------------')
    # test_func2(num_list)
    # print('-------------------------------------')
    # test_func22(num_list)

    #思路：低层阈值要高一点，高层可以低一点
    level_one = [0.5, 0.6, 0.7, 0.8]
    level_two = [0.4, 0.5, 0.6, 0.7]
    level_three = [0.3, 0.4, 0.5, 0.6]
    level_four = [0.2, 0.3, 0.4, 0.5]
    level_five = [0.1, 0.2, 0.3, 0.4]

    all_nms_list = list(itertools.product(level_one, level_two, level_three, level_four, level_five))
    begin = 0
    for i in range(3):
        end = begin + len(all_nms_list) // 3
        for nms_list in all_nms_list[begin:end]:
            with open("./small_nms_list_" + str(i) + "_.txt", "a+") as f:
                f.write(str(nms_list) + '\n')
        begin = end

    # test_func11(all_candiante_nms, num=5)
    # generate_five_list(all_candiante_nms, INFERENCE_TH_TEST)
