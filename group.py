jill = {
    "name": "Jill",
    "age": 26,
    "job": "biologist",
    "connections": [
        {
            "zalinka": "zalinka",
            "connection": "friend"
        },
        {
            "john": "john",
            "connection": "partner"

        }
    ]
}

zalinka = {
    "name": "Zalinka",
    "age": 28,
    "job": "artist",
    "connections": [
        {
            "jill": "jill",
            "connection": "friend"
        },
    ]
}

john = {
    "name": "John",
    "age": 27,
    "job": "writer",
    "connections": [
        {
            "jill": "jill",
            "connection": "partner"
        },
    ]
}

nash = {
    "name": "Nash",
    "age": 34,
    "job": "chef",
    "connections": [
        {
            "john": "john",
            "connection": "counsin"
        },
        {
            "zalinka": "zalinka",
            "connection": "landlord"
        },
    ]
}

my_group = [jill, zalinka, john, nash]

def max_age(group):
    return max(person["age"] for person in group)

def average_connections(group):
    amount=sum(len(person["connections"]) for person in group)
    return amount/len(group)

def max_age_relation(group):
    return max(person["age"] for person in group if(person["connections"]))

def max_age_friend(group):
    new_group=[]
    for person in group:
        for ralation in person["connections"]:
            if(ralation["connection"]=="friend"):
                new_group.append(person)
                break
    
    return max(person["age"] for person in new_group) if(new_group) else None


my_max_age=max_age(my_group)
my_average=average_connections(my_group)
my_max_age_relation=max_age_relation(my_group)
my_max_age_friend=max_age_friend(my_group)

print(my_max_age)
print(my_average)
print(my_max_age_relation)
print(my_max_age_friend)