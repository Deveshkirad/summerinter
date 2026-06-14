#7) Using "Customizing Matplotlib Visualizations" discussed in Numpy session4 notes plot graph to compare your at least 2 semester result
import matplotlib.pyplot as plt

sem2_subjects = ["Maths2", "Python", "COS", "OS", "CHEMISTRY"]

sem2 = [75, 80, 70, 72, 78]

sem3_subjects=["DMLA", "DBMS", "CN", "AI", "TC"]

sem3 = [82, 85, 79, 80, 88]

plt.figure(figsize=(8,5))

plt.plot(sem2_subjects, sem2,
         marker='o',
         linestyle='--',
         linewidth=2,
         label='Semester 1')

plt.plot(sem3_subjects, sem3,
         marker='s',
         linestyle='-',
         linewidth=2,
         label='Semester 2')

plt.title("Semester Result Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()

plt.show()