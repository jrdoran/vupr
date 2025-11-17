import matplotlib.pyplot as plt

# --- Initial ratings test  ---
team1 = {"Ra": 5.000, "Rb": 4.000}
team2 = {"Rc": 4.500, "Rd": 4.500}

# --- Constants ---
SCALE = 0.10
CURVE = 2.0
CRF   = 0.0

# --- Game outcomes (Team1_won?) ---
games = [
    {"game_num": 1, "team1_won": False},
    {"game_num": 2, "team1_won": True},
    {"game_num": 3, "team1_won": False},
]

def print_constants(scale, curve, crf):
    print("\n=== CONSTANTS ===")
    print(f"SCALE = {scale}")
    print(f"CURVE = {curve}")
    print(f"CRF   = {crf}")
    print("=================\n")

def combined_rating(r1, r2, crf):
    avg = (r1 + r2) / 2.0
    if crf == 0:
        return avg
    weakest = min(r1, r2)
    return avg - (avg - weakest) * (crf / 100)

def rating_delta(team1, team2, crf, scale, curve):
    F = combined_rating(team1["Ra"], team1["Rb"], crf)
    G = combined_rating(team2["Rc"], team2["Rd"], crf)
    exponent = curve * (F - G)
    return abs(scale / (1 + 10 ** exponent))

def apply_game(team1, team2, crf, scale, curve, team1_won):
    delta = rating_delta(team1, team2, crf, scale, curve)

    n1 = team1.copy()
    n2 = team2.copy()

    if team1_won:
        n1["Ra"] += delta
        n1["Rb"] += delta
        n2["Rc"] -= delta
        n2["Rd"] -= delta
    else:
        n1["Ra"] -= delta
        n1["Rb"] -= delta
        n2["Rc"] += delta
        n2["Rd"] += delta

    return n1, n2, delta

def plot_rating_trajectory(game_labels, ra_vals, rb_vals, rc_vals, rd_vals):
    plt.figure(figsize=(10, 5))
    plt.plot(game_labels, ra_vals, marker="o", label="Ra")
    plt.plot(game_labels, rb_vals, marker="o", label="Rb")
    plt.plot(game_labels, rc_vals, marker="o", label="Rc")
    plt.plot(game_labels, rd_vals, marker="o", label="Rd")

    plt.title("Rating Trajectory", fontweight="bold")
    plt.xlabel("Game #")
    plt.ylabel("Rating")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()


########
# MAIN #
###### #

# --- PRINT CONSTANTS BEFORE ANYTHING ELSE ---
print_constants(SCALE, CURVE, CRF)

# --- Track ratings over time ---
game_labels = ["Before"]
ra_vals = [team1["Ra"]]
rb_vals = [team1["Rb"]]
rc_vals = [team2["Rc"]]
rd_vals = [team2["Rd"]]


# --- Run the sequence with horizontal-friendly output ---
for g in games:
    game = g["game_num"]
    team1_won = g["team1_won"]

    print(f"\n=== Game {game} ===") 

    print(f"Before | "
          f"T1: Ra={team1['Ra']:.3f}, Rb={team1['Rb']:.3f}   "
          f"T2: Rc={team2['Rc']:.3f}, Rd={team2['Rd']:.3f}")

    new_team1, new_team2, delta = apply_game(team1, team2, CRF, SCALE, CURVE, team1_won)

    print(f"Winner | {'Team 1' if team1_won else 'Team 2'}")
    print(f"Delta  | {delta:.3f}")

    print(f"After  | "
          f"T1: Ra={new_team1['Ra']:.3f}, Rb={new_team1['Rb']:.3f}   "
          f"T2: Rc={new_team2['Rc']:.3f}, Rd={new_team2['Rd']:.3f}")

    # Record post-game ratings
    # build the arrays used for plotting
    game_labels.append(f"G{game}")
    ra_vals.append(new_team1["Ra"])
    rb_vals.append(new_team1["Rb"])
    rc_vals.append(new_team2["Rc"])
    rd_vals.append(new_team2["Rd"])

    team1, team2 = new_team1, new_team2

# --- Plot at the end ---
plot_rating_trajectory(game_labels, ra_vals, rb_vals, rc_vals, rd_vals)
