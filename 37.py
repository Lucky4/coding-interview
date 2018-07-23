def get_most_gold(n, w, g, p):
    pre_result = [0] * (w+1)
    result = [0] * (w+1)

    for i in range(1, w+1):
        if i < p[0]:
            pre_result[i] = 0
        else:
            pre_result[i] = g[0]
    # print pre_result[1:] 

    for j in range(1, n):
        for k in range(1, w+1):
            if k < p[j]:
                result[k] = pre_result[k]
            else:
                result[k] = max(pre_result[k], pre_result[k-p[j]] + g[j])
        # print result[1:]
        pre_result = result[:]
    
    return result.pop()

print get_most_gold(5, 10, [400, 500, 200, 300, 350], [5, 5, 3, 4, 3])
