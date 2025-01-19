def is_weeknd(day):
    match day:
        case "sunday" | "saturday":
            return True
        case _:
            return False
print(is_weeknd(input("Enter thr Day: ")))
