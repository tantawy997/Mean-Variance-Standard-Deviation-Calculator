import numpy as np


def calculate(matrix):
    if not len(matrix) == 9:
        raise ValueError('list must contain nine numbers')

    ls = np.array(matrix)
    ls_reshape = ls.reshape((3, 3))
    finidings = dict()

    finidings['mean'] = [list(np.mean(ls_reshape, axis=0)), list(
        np.mean(ls_reshape, axis=1)), np.mean(ls)]
    finidings['variance'] = [list(np.var(ls_reshape, axis=0)), list(
        np.var(ls_reshape, axis=1)), np.var(ls)]
    finidings['standard deviation'] = [
        list(np.std(ls_reshape, axis=0)), list(np.std(ls_reshape, axis=1)), np.std(ls)]
    finidings['max'] = [list(np.max(ls_reshape, axis=0)), list(
        np.max(ls_reshape, axis=1)), np.max(ls)]
    finidings['min'] = [list(np.min(ls_reshape, axis=0)), list(
        np.min(ls_reshape, axis=1)), np.min(ls)]
    finidings['sum'] = [list(np.sum(ls_reshape, axis=0)), list(
        np.sum(ls_reshape, axis=1)), np.sum(ls)]

    return finidings
