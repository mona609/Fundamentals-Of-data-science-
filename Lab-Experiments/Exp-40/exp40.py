import pandas as pd
import matplotlib.pyplot as plt

players = pd.read_csv("players.csv")

# Top 5 players by goals scored
print("Top 5 players by goals scored:")
print(players.nlargest(5, "goals")[["name", "position", "goals"]].to_string(index=False))

# Top 5 players by weekly salary
print("\nTop 5 highest paid players:")
print(players.nlargest(5, "weekly_salary")[["name", "position", "weekly_salary"]].to_string(index=False))

# Average age and players above the average age
average_age = players["age"].mean()
print(f"\nAverage age of the players: {average_age:.2f}")

older = players[players["age"] > average_age]
print("Players above the average age:")
for name, age in zip(older["name"], older["age"]):
    print(f"  {name} ({age})")

# Distribution of players by position
position_counts = players["position"].value_counts()

plt.figure(figsize=(7, 4))
plt.bar(position_counts.index, position_counts.values, color="seagreen")
plt.title("Number of Players in Each Position")
plt.xlabel("Position")
plt.ylabel("Number of players")
plt.show()
