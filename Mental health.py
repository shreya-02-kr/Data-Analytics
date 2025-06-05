import pandas as pd
import numpy as np # Used for synthetic data generation
import matplotlib.pyplot as plt


# --- Synthetic Data Generation (for demonstration if you don't have the CSV yet) ---
# In a real project, you would replace this with your actual data loading:
# df = pd.read_csv('/kaggle/input/student-mental-health/Student Mental health.csv')

np.random.seed(42)
data_size = 500

# Simulate common student mental health related features and original column names
data = {
    'Choose your gender': np.random.choice(['Male', 'Female', 'Non-binary'], data_size, p=[0.48, 0.50, 0.02]),
    'Age': np.random.randint(18, 25, data_size),
    'Your current year of Study': np.random.choice(['Year 1', 'Year 2', 'Year 3', 'Year 4'], data_size, p=[0.25, 0.25, 0.25, 0.25]),
    'Do you have Anxiety?': np.random.choice(['Yes', 'No'], data_size, p=[0.4, 0.6]),
    'Do you have Depression?': np.random.choice(['Yes', 'No'], data_size, p=[0.3, 0.7]),
    'Do you have Panic attack?': np.random.choice(['Yes', 'No'], data_size, p=[0.2, 0.8]),
    'What is your CGPA?': np.random.choice(['3.00 - 3.49', '3.50 - 4.00', '2.50 - 2.99', '2.00 - 2.49', 'Less than 2.00'], data_size, p=[0.3, 0.3, 0.2, 0.15, 0.05])
}
df = pd.DataFrame(data)
# --- End of Synthetic Data Generation ---


# Histogram for Age distribution
plt.figure(figsize=(10,10))
plt.hist(df['Age'], color='skyblue', edgecolor='black', bins=7) # Added edgecolor and bins for better visualization
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.show()

# Rename the gender column for easier use
df.rename(columns={'Choose your gender': 'gender'}, inplace=True)

# Pie chart for Gender distribution
plt.figure(figsize=(8,8)) # Adjusted size for pie chart
plt.title("Gender Distribution")
# Added autopct for percentage labels and startangle for orientation
plt.pie(df['gender'].value_counts(),
        explode=(0.025,0.025, 0.025 if 'Non-binary' in df['gender'].unique() else 0), # Adjusted explode for potential 3 categories
        labels=df['gender'].value_counts().index,
        colors=['skyblue','lightcoral','lightgreen'], # Added more colors for potential Non-binary
        autopct='%1.1f%%',
        startangle=90) # Start angle at 90 degrees often looks better
plt.legend(title="Gender") # Added title to legend
plt.axis('equal') # Ensures pie chart is circular
plt.show()

# Count plot for Students studying in particular year by Gender
plt.figure(figsize=(10,7)) # Adjusted height for better readability
sns.countplot(x='Your current year of Study', hue='gender', data=df, palette='viridis') # Using x, hue, data for clarity
plt.title("Students Studying in Particular Year by Gender") # Corrected typo
plt.xlabel("Year of Study")
plt.ylabel("Number of Students")
plt.show()

# Count plot for Anxiety vs. Depression
plt.figure(figsize=(10,7))
sns.countplot(x='Do you have Anxiety?', hue='Do you have Depression?', data=df, palette='magma') # Using x, hue, data for clarity
plt.title("Anxiety Levels vs. Depression Levels") # More descriptive title
plt.xlabel("Do you have Anxiety?")
plt.ylabel("Number of Students")
plt.show()

# Set seaborn theme globally (only needs to be called once)
sns.set_theme(style="darkgrid")

# Count plot for Anxiety by Gender
plt.figure(figsize=(10,7))
ax = sns.countplot(y="Do you have Anxiety?", hue="gender", data=df, palette='pastel')
plt.title("Anxiety by Gender")
plt.xlabel("Number of Students")
plt.ylabel("Do you have Anxiety?")
plt.show()

# Count plot for Depression by Gender
plt.figure(figsize=(10,7))
ax = sns.countplot(y="Do you have Depression?", hue="gender", data=df, palette='pastel')
plt.title("Depression by Gender")
plt.xlabel("Number of Students")
plt.ylabel("Do you have Depression?")
plt.show()

# Count plot for Anxiety by Study Year
plt.figure(figsize=(10,7))
ax = sns.countplot(x="Do you have Anxiety?", hue="Your current year of Study", data=df, palette='coolwarm')
plt.title("Anxiety by Study Year")
plt.xlabel("Do you have Anxiety?")
plt.ylabel("Number of Students")
plt.show()

# Count plot for Depression by Study Year
plt.figure(figsize=(10,7))
ax = sns.countplot(x="Do you have Depression?", hue="Your current year of Study", data=df, palette='coolwarm')
plt.title("Depression by Study Year")
plt.xlabel("Do you have Depression?")
plt.ylabel("Number of Students")
plt.show()

# Count plot for Panic Attack by CGPA
plt.figure(figsize=(10,7))
ax = sns.countplot(x="Do you have Panic attack?", hue="What is your CGPA?", data=df, palette='Spectral')
plt.title("Panic Attack by CGPA")
plt.xlabel("Do you have Panic Attack?")
plt.ylabel("Number of Students")
plt.show()
