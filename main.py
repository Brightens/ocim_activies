from utils.classtest import car_class
#from utils.sample_func import apply_discount


case_rule = "lower"

def clean_name(name: str):
    """
    Removes whitespace & lowercase name.
    """
    cleaned = name.strip()
    if case_rule == "lower":
        cleaned = cleaned.lower()
        print(f"Cleaned Name: {cleaned}")
        cleaned = cleaned.count("a")
        print(f"How many a's: {cleaned}")

if __name__ == "__main__":
    # car_1 = car_class("toyota", "camry", 1500)
    # car_2 = car_class("nissan", "terra", 1500)
    # car_3 = car_class("byd", "seagull", 1500)

    clean_name(" MariA ")
