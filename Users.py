# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:14:00 2019

@author: Lex
"""
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

#print(users)

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


#print(friendship_pairs)

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

#print(friendships)

# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j
    
print(friendships)

def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user)
    for user in users)

num_users = len(users) # length of the users list

avg_connections = total_connections / num_users
#print(avg_connections)


#Create a list(user_id, number_of_freinds)
num_friends_by_id = [(user["id"], number_of_friends(user))
    for user in users]

#print(num_friends_by_id)


num_friends_by_id.sort(
        key=lambda id_and_friends: id_and_friends[1],
        reverse=True)
#print(num_friends_by_id)

from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )
    
#print(friends_of_friends(users[0])) #{3: 2}
print(friends_of_friends(users[3]))

#print(Counter([3,3,5,5,5])) #{5: 3, 3: 2}

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    