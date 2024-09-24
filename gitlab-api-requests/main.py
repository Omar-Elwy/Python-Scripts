import requests
response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_projects = response.json() # this returns a list of Dic

# print the whole objects list
# to know which keys in Dic we want to print out in our for loop
print(my_projects)
print(type(my_projects))

# print just the names and urls
for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['http_url_to_repo']}\n")

