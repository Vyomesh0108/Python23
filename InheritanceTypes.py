# Different Types of Inheritance.

class Single:
    pass


class Multiple1:
    pass


class Multiple2:
    pass


class Multiple(Multiple1, Multiple2):
    pass


class Multilevel(Single):
    pass


class Hybrid(Multilevel, Multiple):
    pass


class Hierarchical(Hybrid):
    pass


def main():
    single = Single()
    multiple = Multiple()
    multilevel = Multilevel()
    hybrid = Hybrid()
    hierarchical = Hierarchical()

    print(f"Single Inheritance: {single.__class__.__name__}")
    print(f"Multiple Inheritance: {multiple.__class__.__name__}")
    print(f"Multilevel Inheritance: {multilevel.__class__.__name__}")
    print(f"Hybrid Inheritance: {hybrid.__class__.__name__}")
    print(f"Hierarchical Inheritance: {hierarchical.__class__.__name__}")


if __name__ == "__main__":
    main()