import time
import random
import matplotlib.pyplot as plt
# Compare the time efficiency of merge sort and insertion sort

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


def time_eff_comp(li, epoch=1000):
    # compare the running time of different sorting algorithms
    # n indicates the length of the shuffled list we expect to test
    # epoch indicates the times of loop we wish to repeat
    merge_sort_t = 0
    insertion_sort_t = 0
    for _ in range(epoch):
        li_merge = li[:]
        li_insert = li[:]
        # merge sort
        start_t = time.time()
        merge_sort(li_merge)
        merge_sort_t += time.time() - start_t
        # insertion sort
        start_t = time.time()
        insertion_sort(li_insert)
        insertion_sort_t += time.time() - start_t

    return merge_sort_t / epoch, insertion_sort_t / epoch


if __name__ == "__main__":
    merge_sort_t = []
    insertion_sort_t = []
    test_size = [10, 50, 100, 500] + [1000 * k for k in range(1, 10)] + [10000]
    # test_size = [10 * k for k in range(1, 10)] + [100 * k for k in range(1, 11)]
    # test_size = [10 * k for k in range(1, 11)]
    for n in test_size:
        li = list(map(int, range(n)))
        random.shuffle(li)
        if n < 100:
            mst, ist = time_eff_comp(li, epoch=100000)
        elif n < 1000:
            mst, ist = time_eff_comp(li, epoch=100)
        elif n < 10000:
            mst, ist = time_eff_comp(li, epoch=10)
        else:
            mst, ist = time_eff_comp(li, epoch=1)    
        merge_sort_t.append(mst)
        insertion_sort_t.append(ist)        
    plt.plot(test_size, merge_sort_t, 's-', color='r', label='merge sort')
    plt.plot(test_size, insertion_sort_t, 'o-', color='b', label='insertion sort')
    plt.xlabel("size of list")
    plt.ylabel("running time")
    plt.legend(loc="best")
    fig_name = "./Q1/" + str(test_size[0]) + "_" + str(test_size[-1]) + ".pdf"
    plt.savefig(fig_name, dpi=300, bbox_inches='tight')