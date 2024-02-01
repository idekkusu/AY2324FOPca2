A = [28, 34, 27, 28]
B = [18, 19, 24, 26]
C = [22, 23, 22, 32]
D = [33, 30, 30, 26]
import scipy.stats as stats

# Perform one-way ANOVA
F, p = stats.f_oneway(A, B, C, D)

print("F-value: ", F)
print("p-value: ", p)
