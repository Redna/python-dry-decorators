import logging

from python_dry_decorators.example import another


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)20s :: %(levelname)-8s :: %(name)s :: %(message)s', level=logging.DEBUG)
    print(f"finished {another(dict(demo= 5), call_count=5)}")

    print("next one")

    print(f"finished {another(dict(demo= 5), call_count=3)}")
