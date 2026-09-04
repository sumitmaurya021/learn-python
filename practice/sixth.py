riya_friends = {"Aman", "Sneha", "Kabir", "Priya"}
aman_friends = {"Sneha", "Rohan", "Kabir", "Vikas"}

common = riya_friends & aman_friends
only_riya = riya_friends - aman_friends
only_aman = aman_friends - riya_friends
all_friends = riya_friends | aman_friends

print(f"Common friends : {common}")
print(f"Riya's unique friends : {only_riya}")
print(f"Aman's unique friends : {only_aman}")
print(f"All friends : {all_friends}")