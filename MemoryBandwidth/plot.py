import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

# Curve 1 data (size, bandwidth)
data_str_2 = """
2,1108.602173
4,1172.187256
8,1110.842163
12,1146.279785
16,1158.844482
24,1166.714355
32,1124.244995
48,1137.033691
64,1181.000732
96,1096.003418
128,1099.511597
192,644.045044
256,616.318176
512,611.383240
600,635.114685
768,640.447327
1024,633.359253
1536,656.336487
2048,614.664368
3072,640.462036
4096,623.588745
5120,629.337646
6144,600.658081
8192,574.097534
10240,436.340759
12288,375.767456
16384,269.488159
24567,247.133591
32768,239.357285
65536,217.811340
98304,186.961792
131072,178.956970
262144,138.939499
393216,125.621292
524288,128.615906
1048576,122.647644
1572864,114.324379
2097152,113.342369
3145728,116.251572
"""

# Curve 2 data (size, bandwidth)
data_str_1 = """
2,1757.344116
4,1773.882690
8,1764.866211
12,1741.570679
16,1719.778320
24,1746.180542
32,1740.651611
48,1749.421753
64,1755.006592
96,1591.955444
128,1610.612793
192,958.878235
256,965.613281
512,977.054199
600,977.053223
768,978.220642
1024,982.876892
1536,991.131165
2048,984.049805
3072,958.905701
4096,933.900024
5120,875.460754
6144,837.140503
8192,844.046814
10240,860.839294
12288,814.954895
16384,781.643311
24567,708.534546
32768,645.758606
65536,567.538696
98304,511.377045
131072,479.438202
262144,339.076355
393216,297.290070
524288,280.869781
1048576,254.909958
1572864,250.462448
2097152,247.414856
3145728,242.418335
"""

# Parse data for curve 1
sizes_1 = []
bw_1 = []
for line in data_str_1.strip().split('\n'):
    s, b = line.split(',')
    sizes_1.append(int(s))
    bw_1.append(float(b))

# Parse data for curve 2
sizes_2 = []
bw_2 = []
for line in data_str_2.strip().split('\n'):
    s, b = line.split(',')
    sizes_2.append(int(s))
    bw_2.append(float(b))

x_indices = range(len(sizes_1))

plt.figure(figsize=(10, 6))

plt.plot(x_indices, bw_1, marker='s', linestyle='--', color='red', label='M4 Pro')
plt.plot(x_indices, bw_2, marker='o', linestyle='-', color='blue', label='M1 MAX')


plt.title('CPU Memory Read Bandwidth (All Cores)', fontsize=16, fontweight='bold')
plt.xlabel('Block Size (KB)', fontsize=12)
plt.ylabel('Bandwidth (GB/s)', fontsize=12)
plt.grid(True)
plt.legend()

plt.xticks(x_indices, sizes_1, rotation=90)

# Determine global min and max
y_min = min(min(bw_1), min(bw_2))
y_max = max(max(bw_1), max(bw_2))

# Determine individual min values
y_min_1 = min(bw_1)
y_min_2 = min(bw_2)

# Add some margin
data_range = y_max - y_min
margin = 0.05 * data_range
plt.ylim(y_min - margin, y_max + margin)

# Use a scalar formatter to avoid scientific notation
ax = plt.gca()
formatter = ScalarFormatter()
formatter.set_scientific(False)
formatter.set_useOffset(False)
ax.yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.draw()

# Get the current ticks
current_ticks = ax.get_yticks()

# Protected ticks: global min, global max, and individual minima
protected_ticks = {y_min, y_max, y_min_1, y_min_2}

# Ensure all protected ticks are included
for pt in protected_ticks:
    if pt not in current_ticks:
        current_ticks = np.append(current_ticks, pt)

# Sort ticks
current_ticks = np.sort(current_ticks)

# Use a relative threshold based on data range
relative_threshold = 0.1 * data_range

filtered_ticks = []
for t in current_ticks:
    # Always keep protected ticks
    if t in protected_ticks:
        filtered_ticks.append(t)
    else:
        # Only keep intermediate ticks if they are not too close to min/max
        if (t > y_min + relative_threshold) and (t < y_max - relative_threshold):
            filtered_ticks.append(t)

ax.set_yticks(filtered_ticks)

plt.draw()
plt.show()