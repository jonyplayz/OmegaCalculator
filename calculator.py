from OmegaCalculator.the_brain import *

def main():

    print("please enter your equation bellow\n")
    eq = input()
    answer = calculate(eq)
    print(f"the answer is: {answer}")


if __name__ == '__main__':
    main()