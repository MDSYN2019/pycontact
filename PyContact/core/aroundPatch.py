'''
    Authors: Maximilian Scheurer, Peter Rodenkirch
    Date created: Nov 2016
    Python Version: 2.7
    Version: 0.1a
    Status: Development
    Patch for MDAnalysis AroundSelection to make it faster
'''
# from ctypes import cdll
# import ctypes

from MDAnalysis.core.Selection import *
import numpy as np
# from numpy.ctypeslib import ndpointer

from ..cy_modules import cy_gridsearch

# aroundLibrary = cdll.LoadLibrary('./shared/libgridsearch.so')

class AroundSelection(DistanceSelection):
    token = 'around'
    precedence = 1

    def __init__(self, parser, tokens):
        # self.findw = aroundLibrary.find_within
        # find_within(const float *xyz, int *flgs, const int *others, int num, float r)
        # self.findw.argtypes = [ndpointer(ctypes.c_float, flags="C_CONTIGUOUS"), ndpointer(ctypes.c_int, flags="C_CONTIGUOUS"), ndpointer(ctypes.c_int, flags="C_CONTIGUOUS"), ctypes.c_int,\
        #  ctypes.c_float]

        super(AroundSelection, self).__init__()
        self.cutoff = float(tokens.popleft())
        self.sel = parser.parse_expression(self.precedence)

    def _apply_KDTree(self, group):
        """KDTree based selection is about 7x faster than distmat
        for typical problems.
        Limitations: always ignores periodicity
        """

        # NOTE: Max' custom version of around search
        custom = 1
        sel = self.sel.apply(group)
        # All atoms in group that aren't in sel
        sys = group[~np.in1d(group.indices, sel.indices)]
        if custom:
            # print("custom KD tree running")

            # print sel.indices
            syspos = sys.positions
            selpos = sel.positions

            # coords = np.reshape(syspos, (1, np.size(syspos,0) * 3))
            # print "coord ", coords.size/3

            sys_ones = np.ones(np.size(syspos, 0), dtype=np.int32)
            sys_zeros = np.zeros(np.size(syspos, 0), dtype=np.int32)

            sel_ones = np.ones(np.size(selpos, 0), dtype=np.int32)
            sel_zeros = np.zeros(np.size(selpos, 0), dtype=np.int32)

            all_positions = np.concatenate((syspos, selpos), axis=0)
            flgs = np.concatenate((sys_ones, sel_zeros), axis=0)
            others = np.concatenate((sys_zeros, sel_ones), axis=0)

            atom_number = flgs.size
            # self.findw.restype = ndpointer(ctypes.c_int,shape=(atom_number,))
            result = cy_gridsearch.cy_find_within(all_positions, flgs, others, atom_number, self.cutoff)

            real_result = result[0:np.size(syspos,0)]
            found_indices = np.where(real_result!=0)[0]
            unique_idx = np.unique(found_indices)
            return unique(sys[unique_idx.astype(np.int32)])
        else:
            kdtree = KDTree(dim=3, bucket_size=10)
            kdtree.set_coords(sys.positions)
            found_indices = []
            for atom in sel.positions:
                kdtree.search(atom, self.cutoff)
                found_indices.append(kdtree.get_indices())
            # These are the indices from SYS that were seen when
            # probing with SEL
            unique_idx = np.unique(np.concatenate(found_indices))
            return unique(sys[unique_idx.astype(np.int32)])


    def _apply_distmat(self, group):
        # print "custom distmat running"
        sel = self.sel.apply(group)
        sys = group[~np.in1d(group.indices, sel.indices)]

        box = group.dimensions if self.periodic else None
        dist = distances.distance_array(
            sys.positions, sel.positions, box)

        mask = (dist <= self.cutoff).any(axis=1)

        return unique(sys[mask])
