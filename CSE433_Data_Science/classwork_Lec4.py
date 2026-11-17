import pandas as pd
df = pd.read_csv("students_clean.csv")

print(df.groupby("Dept")["CGPA"].mean())


import matplotlib.pyplot as plt
avg = df.groupby("Dept")["CGPA"].mean()
avg.plot(kind="bar")
plt.show()

to_plot = df["CGPA"]
to_plot.plot(
    kind="hist")
plt.show()