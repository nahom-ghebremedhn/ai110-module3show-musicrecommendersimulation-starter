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

    # Taste profile: an upbeat pop listener who prefers produced (non-acoustic) songs
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)
    print_recommendations(user_prefs, recommendations)


MAX_SCORE = 5.0
WIDTH = 60


def print_recommendations(user_prefs: dict, recommendations: list) -> None:
    """Prints the ranked recommendations as a readable terminal report."""
    acoustic = "acoustic" if user_prefs["likes_acoustic"] else "produced"
    print()
    print("=" * WIDTH)
    print(" TOP RECOMMENDATIONS".center(WIDTH))
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
