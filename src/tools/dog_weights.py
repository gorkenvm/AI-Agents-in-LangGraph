def average_dog_weight(name: str) -> str:
    """Return the average weight for a given dog breed."""
    name = name.lower()
    if "scottish terrier" in name:
        return "Scottish Terriers average 20 lbs"
    elif "border collie" in name:
        return "Border Collies average 37 lbs"
    elif "toy poodle" in name:
        return "Toy Poodles average 7 lbs"
    else:
        return "An average dog weighs 50 lbs"
