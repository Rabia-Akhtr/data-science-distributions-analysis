import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from files using pandas
df2020 = pd.read_csv(
    '2020input1.csv',
    sep='\s+',
    header=None,
    names=['Xleft', 'Xright', 'Count']
)
df2024 = pd.read_csv(
    '2024input1.csv',
    sep='\s+',
    header=None,
    names=['Grades']
)

# Calculate mean and standard deviation for 2020 exam
M2020 = (((df2020["Xleft"] + df2020["Xright"]) / 2 * df2020['Count']).sum()) / (df2020['Count'].sum())
SD2020 = np.sqrt(
    np.sum(((((df2020['Xleft'] + df2020['Xright']) / 2) - M2020) ** 2) * df2020['Count']) / np.sum(
        df2020['Count'].sum())
)

# Calculate mean and standard deviation for 2024 exam
M2024 = df2024["Grades"].mean()
SD2024 = df2024["Grades"].std()

# Set figure size
plt.figure(figsize=(10, 6))

# Plot histogram for 2020 exam
plt.hist(
    (df2020["Xleft"] + df2020["Xright"]) / 2,
    bins=len((df2020["Xleft"] + df2020["Xright"]) / 2),
    weights=df2020['Count'],
    alpha=0.5,
    label='2020 Exam Grades',
    color='magenta',
    linewidth=0.5,
    edgecolor='gray'
)

# Plot histogram for 2024 exam
plt.hist(
    df2024["Grades"],
    bins=20,
    alpha=0.5,
    label='2024 Exam Grades',
    color='Chartreuse',
    linewidth=0.5,
    edgecolor='gray'
)

# Count the number of students with grades 70 or higher for calculation of value V
num_students_70_or_higher = (df2024['Grades'] >= 70).sum()
# Total number of students
total_students = len(df2024)

# Calculate the proportion (value V)
V = (proportion_students_70_or_higher) = (num_students_70_or_higher / total_students) 

# Print mean, standard deviation, V value, and student ID text
plt.text(0.02, 0.95, f"Mean (2020): {M2020:.3g}", transform=plt.gca().transAxes, fontsize=10, color='black')
plt.text(0.02, 0.90, f"Mean (2024): {M2024:.3g}", transform=plt.gca().transAxes, fontsize=10, color='black')
plt.text(0.02, 0.85, f"SD (2020):   {SD2020:.3g}", transform=plt.gca().transAxes, fontsize=10, color='black')
plt.text(0.02, 0.80, f"SD (2024):   {SD2024:.3g}", transform=plt.gca().transAxes, fontsize=10, color='black')
plt.text(0.02, 0.75, f"V (2024):    {proportion_students_70_or_higher:.3g}", transform=plt.gca().transAxes, fontsize=10, color='black')
plt.text(0.02, 0.70, "Student ID: 23031641", transform=plt.gca().transAxes, fontsize=10, color='black')

# Axis labels and title
plt.xlabel('Exam Grades', fontsize=14)
plt.ylabel('Number of Students', fontsize=14)
plt.title('Distributions (histograms) for the 2020 and 2024 Exam Grades', fontsize=14)
plt.legend()

# Save the plot as a PNG image
student_id = "23031641"
plt.savefig('23031641.png', dpi=600) 
plt.tight_layout() 

# Show plot
plt.show()
