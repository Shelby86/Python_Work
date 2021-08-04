# 40 Make a csv a dictionary

# Step 1 seperate the fil out by lines.
# Readlines will preserve the \n. Remember to srtip it off later

with open("iris.csv", "r") as iris_file:
    iris_file.readlines()

# Step 2 create a new list to place our new values in. Also trim the headers

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

    # This will store the headers for optional later use
    headers = iris_data[0]

    # This is an empty list to store our values
    irises = []

    # for every line in iris data starting at the second row
    for line in iris_data[1:]:
        pass

    # Step 3

    with open("iris.csv", "r") as iris_file:
        iris_data = iris_file.readlines()

        # The split here tells us to split the values based on commas.
        # this is how we will extract the key value pairs
        headers = iris_data[0].strip().split(",")

        # list to store our values in
        irises = []

        for row in iris_data[1:]:
            iris = row.strip().split(",")
            iris_dict = dict(zip(headers,iris))

            irises.append(iris_dict)

        print(irises)

    # Step 3 long method with an easier to see explination

    with open("iris.csv", "r") as iris_file:
        iris_info = iris_file.readlines()

        headers = iris_info[0].strip()
        irises = []

        for line in iris_info[1:]:
            sepal_length, sepal_width, petal_length, \
            petal_width, species = line.strip().split(",")

            irises.append({
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width,
                "species": species
            })

        print(irises)


# 41 Make a dictionary into a csv

# First create a new file:

# with open("iris_back_to_csv.csv", "r") as new_iris_file:

# Consider what we have here.
# keys and values seperated out by commas
# We can join just the values, using the commas and adding a new line at the end


with open("iris_back_to_csv.csv", "w") as new_iris_file:
    for entry in irises:
        new_iris_file.write(",".join(iris_dict) + "\n")


headers = []

for entry in irises:
    for key in entry.keys():
        headers.append(key)
