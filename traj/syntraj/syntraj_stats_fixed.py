# Calculate the mean, median, and standard deviation of T, P, qv, and qi for a given set of simulation trajs
# This function fixes the number of elements per bin.
def syntraj_stats_fixed( alt_ICON, t_ICON, p_ICON, qv_ICON, qi_ICON, indx, bins_sim  ):
    import numpy as np
    import random
    n = bins_sim.shape[0]

    # Store 4 variables and 3 statistics over <n> levels for 625 trajectories
    stats = np.empty((4, 3, n, alt_ICON.shape[1]))
    stats[:] = np.nan

    # Read in the number of in-situ measurements in each bin
    basedir = '/work/bb1018/b380873/tropic_vis/'
    Stratoclim_temp_len = np.load(basedir + 'output/Stratoclim_temp_len.npy')
    Stratoclim_qv_len = np.load(basedir + 'output/Stratoclim_qv_len.npy')

    for i in np.arange(alt_ICON.shape[1]):
        if i%100 == 0:
           print(i)
        t_list = [ [] for k in np.arange(n) ]
        p_list = [ [] for k in np.arange(n) ]
        qv_list = [ [] for k in np.arange(n) ]
        qi_list = [ [] for k in np.arange(n) ]

        # Group values for this trajectory into bins.
        for elem_idx, group_idx in enumerate( indx[:,i] ):
            t_list[int(group_idx)-1].append( t_ICON[elem_idx, i].item() )
            p_list[int(group_idx)-1].append( p_ICON[elem_idx, i].item() )
            qv_list[int(group_idx)-1].append( qv_ICON[elem_idx, i].item() )
            qi_list[int(group_idx)-1].append( qi_ICON[elem_idx, i].item() )

        # Only retain the corresponding number of elements from the measurements
        # We do this calculation only for n-1 bins as the last bin contains the whole "upper-level" trajectory set (z ~ 22 km)
        t_list_fixed = [ [] for k in np.arange(n) ]
        p_list_fixed = [ [] for k in np.arange(n) ]
        qv_list_fixed = [ [] for k in np.arange(n) ]
        qi_list_fixed = [ [] for k in np.arange(n) ]

        for j in np.arange(n):
            if( (len(t_list[j]) >= Stratoclim_temp_len[j]) & (len(p_list[j]) >= Stratoclim_temp_len[j]) ):
               t_list_fixed[j] = random.sample( t_list[j], Stratoclim_temp_len[j] )
               p_list_fixed[j] = random.sample( p_list[j], Stratoclim_temp_len[j] )
            if( (len(qv_list[j]) >= Stratoclim_qv_len[j]) & (len(qi_list[j]) >= Stratoclim_qv_len[j]) ):
               qv_list_fixed[j] = random.sample( qv_list[j], Stratoclim_qv_len[j] )
               qi_list_fixed[j] = random.sample( qi_list[j], Stratoclim_qv_len[j] )

            if t_list_fixed[j]:
                stats[0, 0, j, i] = np.nanmean( t_list_fixed[j] )
                stats[0, 1, j, i] = np.nanmedian( t_list_fixed[j] )
                stats[0, 2, j, i] = np.nanstd( t_list_fixed[j] )
            if p_list_fixed[j]:
                stats[1, 0, j, i] = np.nanmean( p_list_fixed[j] )
                stats[1, 1, j, i] = np.nanmedian( p_list_fixed[j] )
                stats[1, 2, j, i] = np.nanstd( p_list_fixed[j] )
            if qv_list_fixed[j]:
                stats[2, 0, j, i] = np.nanmean( qv_list_fixed[j] )
                stats[2, 1, j, i] = np.nanmedian( qv_list_fixed[j] )
                stats[2, 2, j, i] = np.nanstd( qv_list_fixed[j] )
            if qi_list_fixed[j]:
                stats[3, 0, j, i] = np.nanmean( qi_list_fixed[j] )
                stats[3, 1, j, i] = np.nanmedian( qi_list_fixed[j] )
                stats[3, 2, j, i] = np.nanstd( qi_list_fixed[j] )

    return stats
