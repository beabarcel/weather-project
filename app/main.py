from services.cities_loader import load_cities


def run():
    load_cities("data/cities15000.txt")


if __name__ == "__main__":
    run()