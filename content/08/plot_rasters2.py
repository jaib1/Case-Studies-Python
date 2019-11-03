
def plot_rasters2(t, *args):
    """ 
    Plots rasters for each spike train timestamp vector in `*args*` within the time interval `t`
    
    Parameters:
    -----------
        *args (ndarray | list | tuple): spike train timestamp vectors (in s) with 
                                        length == # of timestamps 
        t (ndarray | list | tuple): two numbers specifying a time range (in s)
    
    Returns:
    --------
        fig(figure): a handle to the figure that holds the created rasters
        ax(axes): a handle to the plot that holds the created rasters
        rasters(lines): a handle to the rasters plotted on `ax`
    """
    
    # Create the figure.
    fig, ax = plt.subplots()
    # Plot the spike trains using a comprehension.
    rasters = [ax.plot(args[a], np.zeros_like(args[a])+a, marker='.', linestyle='') \
               for a in range(0, len(args))]
    # Set xlim according to `t` and label x axis.
    ax.set_xlim([t[0], t[1]])
    ax.set_xlabel('Time (s)')
    # Zoom out an y axis and hide y ticks.
    ax.set_ylim([-1, len(args)+1])
    ax.set_yticks([])
    return fig, ax, rasters
