def crowdedGroup(scores, subject, marklimit):
    my_list = []
    for i in range(len(scores)):
        my_list.append([])
        for j in range(len(scores)):
            if marklimit >= scores[i][subject] - scores[j][subject] >= 0:
                my_list[i].append(scores[j]['SeqNo'])
    max_ = []
    group = []
    for i in range(2):
        for k in sorted(my_list):
            if not i:
                if len(k) > len(max_):
                    max_ = k
            else:
                if len(max_) == len(k):
                    if k in group:
                        continue
                    else:
                        group.append(k)

    return group