def find_common_participants(team1: str, team2: str, separator: str = ",") -> list:
    members1 = team1.split(separator)
    members2 = team2.split(separator)

    common_members = set(members1).intersection(members2)
    common_members = sorted(common_members)

    return common_members


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
