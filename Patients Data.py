import pandas as pd
from faker import Faker

# Initialize Faker generator
fake = Faker()

# Generate random data for 10,000 patients
data = []
for _ in range(10000):
    age_category = fake.random_element(["child", "adult", "senior"])
    email = fake.email()
    address = fake.address()
    data.append((age_category, email, address))

# Create a DataFrame from the generated data
df = pd.DataFrame(data, columns=["age_category", "email", "address"])

# Save the DataFrame to a CSV file
df.to_csv("patients_data.csv", index=False)
