#Search in 2D Matrix 👉 Matrix sorted → search target

def search_matrix(mat, target):
    if not mat:
        return False

    r, c = 0, len(mat[0])-1

    while r < len(mat) and c >= 0:
        if mat[r][c] == target:
            return True
        elif mat[r][c] > target:
            c -= 1
        else:
            r += 1

    return False