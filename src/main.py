"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, user_prefs in PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(name, user_prefs, recommendations)


# Distinct taste profiles used to test the recommender
PROFILES = {
    # Upbeat pop listener who prefers produced (non-acoustic) songs
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False,
    },
    # Low-key study music: mellow, acoustic-leaning lofi
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "likes_acoustic": True,
    },
    # Loud, driving rock with heavy production
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.9,
        "likes_acoustic": False,
    },
    # --- Adversarial / edge-case profiles (system evaluation) ---
    # Mood that no song in the catalog has, paired with high energy
    "Sad Gym Rat": {
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.9,
        "likes_acoustic": False,
    },
    # Extra whitespace / casing in preferences
    "Whitespace Pop": {
        "favorite_genre": " Pop ",
        "favorite_mood": "HAPPY",
        "target_energy": 0.8,
        "likes_acoustic": False,
    },
    # Energy outside the 0-1 range
    "Overdrive": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 1.5,
        "likes_acoustic": True,
    },
    # Genre whose only song contradicts every other preference
    "Contradictory Classical": {
        "favorite_genre": "classical",
        "favorite_mood": "chill",
        "target_energy": 0.95,
        "likes_acoustic": False,
    },
    # Genre with a single song in the catalog
    "Acoustic Metal": {
        "favorite_genre": "metal",
        "favorite_mood": "angry",
        "target_energy": 0.97,
        "likes_acoustic": True,
    },
    # Close cousin of "pop" that only matches exactly
    "Indie Pop Fan": {
        "favorite_genre": "indie pop",
        "favorite_mood": "happy",
        "target_energy": 0.76,
        "likes_acoustic": False,
    },
    # No genre or mood given
    "No Preferences": {
        "favorite_genre": "",
        "favorite_mood": "",
        "target_energy": 0.5,
        "likes_acoustic": False,
    },
}


MAX_SCORE = 5.0
WIDTH = 60


def print_recommendations(name: str, user_prefs: dict, recommendations: list) -> None:
    """Prints the ranked recommendations as a readable terminal report."""
    acoustic = "acoustic" if user_prefs["likes_acoustic"] else "produced"
    print()
    print("=" * WIDTH)
    print(f" TOP RECOMMENDATIONS: {name}".center(WIDTH))
    print("=" * WIDTH)
    print(
        f" Profile: {user_prefs['favorite_genre']} | {user_prefs['favorite_mood']} | "
        f"energy {user_prefs['target_energy']:.2f} | {acoustic}"
    )
    print("-" * WIDTH)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f" #{rank}  {song['title']}  by {song['artist']}")
        print(f"     Score: {score:.2f} / {MAX_SCORE:.2f}")
        print("     Why:")
        for reason in explanation.split(", "):
            print(f"       - {reason}")
        print("-" * WIDTH)


if __name__ == "__main__":
    main()
