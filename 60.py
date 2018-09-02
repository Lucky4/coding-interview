if __name__ == '__main__':
    n = input()
    m = input()
    l = 1
    h = m
    mid = -1
    while l < h:
        mid = (l + h + 1) / 2
        tmp = m
        now = mid
        ok = True
        for i in range(n):
            tmp -= now
            if tmp < 0:
                ok = False
                break
            now = (now + 1) / 2
        if not ok:
            h = mid - 1
        else:
            l = mid
    print l