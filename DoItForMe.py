courses = [{"name":"example1", "minAge":12, "maxAge":16},
           {"name":"example2", "minAge":10, "maxAge":13},
           {"name":"example3", "minAge":13, "maxAge":15}]

people = [{"name":"person1", "age":14, "avCourses":[]},
          {"name":"person2", "age":11, "avCourses":[]},]

for person in people:
    for course in courses:
        if course["minAge"] <= person["age"] <= course["maxAge"]:
            person["avCourses"].append(course)
    print(person["name"], "can go to these courses:")
    for course in person["avCourses"]:
        print(course["name"])
    print()
