users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique_visits = set(users)

stats = {
    'Общее количество': 0,
    'Уникальные посещения': 0,
}

total_count = len(users)
unique_count = len(unique_visits)

stats['Общее количество'] = total_count
stats['Уникальные посещения'] = unique_count

print(stats)
