import plot_rasters2

def test_plot_rasters2():
	fig, ax, rasters = plot_rasters2(t, ts_dark, ts_light)
	# Get individual rasters for dark and light conditions.
	r_dark = rasters[0][0]
	r_light = rasters[1][0]
	# `assert` that the number of points plotted matches the number of timestamps for each condition.
	assert r_light.get_ydata().size == ts_light.size and r_dark.get_ydata().size == ts_dark.size