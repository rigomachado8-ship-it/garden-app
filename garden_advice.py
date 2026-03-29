"""
Garden Advice Program
Provides gardening advice based on the user's chosen season and plant type.
"""


def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."


def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Run the garden advice program."""
    season = input("Enter the season: ").strip().lower()
    plant_type = input("Enter the plant type: ").strip().lower()

    advice = get_season_advice(season) + "\n" + get_plant_advice(plant_type)
    print("\nGardening Advice:")
    print(advice)


if __name__ == "__main__":
    main()