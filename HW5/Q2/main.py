import time
import random
import matplotlib.pyplot as plt
# Build a hybrid method to see the how large k is

def merge_sort(li):
    # time complexity should be O(nlogn)
    if len(li) > 1:
        # find the mid point of the list
        mid = len(li) // 2
        # split the list into equal halves
        l_li = li[ : mid]
        r_li = li[mid : ]
        # sort the left & right halves
        merge_sort(l_li)
        merge_sort(r_li)
        i = j = k = 0
        # combine the left & right lists into a sorted one
        while i < len(l_li) and j < len(r_li):
            if l_li[i] <= r_li[j]:
                li[k] = l_li[i]
                i += 1
            else:
                li[k] = r_li[j]
                j += 1
            k += 1
        # make sure every element has been stored
        while i < len(l_li):
            li[k] = l_li[i]
            k += 1
            i += 1
        while j < len(r_li):
            li[k] = r_li[j]
            j += 1
            k += 1

def insertion_sort(li):
    # time comlexity should be O(n^2)
    if len(li) > 1:
        for i in range(1, len(li)):
            curr_val = li[i]
            j = i - 1
            while j >= 0 and curr_val < li[j]:
                li[j + 1] = li[j]
                j -= 1
            li[j + 1] = curr_val

def tim_sort(li, k):
    if len(li) > k:
        # if the length of li is larger than threshold of k
        # we use merge sort
        mid = len(li) // 2
        # split the list into equal halves
        l_li = li[ : mid]
        r_li = li[mid : ]
        tim_sort(l_li, k=k)
        tim_sort(r_li, k=k)
        i = j = l = 0
        # combine the left & right lists into a sorted one
        while i < len(l_li) and j < len(r_li):
            if l_li[i] <= r_li[j]:
                li[l] = l_li[i]
                i += 1
            else:
                li[l] = r_li[j]
                j += 1
            l += 1
        # make sure every element has been stored
        while i < len(l_li):
            li[l] = l_li[i]
            l += 1
            i += 1
        while j < len(r_li):
            li[l] = r_li[j]
            j += 1
            l += 1
    else:
        # or if the length of li is smaller than k
        # we use insertion sort
        insertion_sort(li)




def time_eff_comp(li, epoch=1000, k=40):
    # compare the running time of different sorting algorithms
    # n indicates the length of the shuffled list we expect to test
    # epoch indicates the times of loop we wish to repeat
    merge_sort_t = 0
    insertion_sort_t = 0
    tim_sort_t = 0
    for _ in range(epoch):
        li_merge = li[:]
        li_insert = li[:]
        li_tim = li[:]
        # merge sort
        start_t = time.time()
        merge_sort(li_merge)
        merge_sort_t += time.time() - start_t
        # insertion sort
        start_t = time.time()
        insertion_sort(li_insert)
        insertion_sort_t += time.time() - start_t
        # hybrid sort
        start_t = time.time()
        tim_sort(li_tim, k=k)
        tim_sort_t += time.time() - start_t

    return merge_sort_t / epoch, insertion_sort_t / epoch, tim_sort_t / epoch


if __name__ == "__main__":
    test_size = [200, 500, 800, 1200]
    th_list = [10 * k for k in range(1, 11)]
    for n in test_size:
        merge_sort_t = []
        insertion_sort_t = []
        tim_sort_t = []
        li = list(map(int, range(n)))
        random.shuffle(li)
        for k in th_list:
            if n < 100:
                mst, ist, tst = time_eff_comp(li, epoch=100000, k=k)
            elif n < 1000:
                mst, ist, tst = time_eff_comp(li, epoch=100, k=k)
            elif n < 10000:
                mst, ist, tst = time_eff_comp(li, epoch=10, k=k)
            else:
                mst, ist, tst = time_eff_comp(li, epoch=1, k=k)    
            merge_sort_t.append(mst)
            insertion_sort_t.append(ist)        
            tim_sort_t.append(tst)
        plt.figure()
        plt.plot(th_list, merge_sort_t, 's-', color='r', label='merge sort')
        plt.plot(th_list, insertion_sort_t, 'o-', color='b', label='insertion sort')
        plt.plot(th_list, tim_sort_t, 'x-', color='g', label='hybrid sort')
        plt.xlabel("k")
        plt.ylabel("running time")
        plt.title("running time of each sort algorithms under n = {}".format(n))
        plt.legend(loc="best")
        fig_name = "./Q2/" + str(n) + ".pdf"
        plt.savefig(fig_name, dpi=300, bbox_inches='tight')

