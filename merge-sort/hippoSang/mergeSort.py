def merge_sorted_seq(left_seq, right_seq):
    result = []
    while left_seq and right_seq:
        if left_seq[-1] > right_seq[-1]:
            result.append(left_seq.pop())
        else:
            result.append(right_seq.pop())
    if left_seq:
        result += left_seq[::-1]
    else:
        result += right_seq[::-1]
    return result[::-1]


def merge_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    elif len(sequence) == 2:
        if sequence[0] <= sequence[1]:
            return sequence
        else:
            return sequence[::-1]
    else:
        split_index = int(len(sequence)/2)+1
        return merge_sorted_seq(merge_sort(sequence[:split_index]), merge_sort(sequence[split_index:]))


if __name__ == "__main__":
    seq = [1, 9, 4, 7, 10, 10000, 747, 9320, 90]
    sorted_seq = merge_sort(sequence=seq)
    print(sorted_seq)
