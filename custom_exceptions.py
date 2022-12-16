"""
this whole module contains the various custom exceptions that i created for each special exception
"""


class brackets_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by brackets"):
        self.message = message
        super().__init__(self.message)


class plus_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by plus"):
        self.message = message
        super().__init__(self.message)


class minus_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by minus"):
        self.message = message
        super().__init__(self.message)


class mul_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by mul"):
        self.message = message
        super().__init__(self.message)


class div_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by div"):
        self.message = message
        super().__init__(self.message)


class pow_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by pow"):
        self.message = message
        super().__init__(self.message)


class mod_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by mod"):
        self.message = message
        super().__init__(self.message)


class max_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by max"):
        self.message = message
        super().__init__(self.message)


class min_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by min"):
        self.message = message
        super().__init__(self.message)


class avg_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by average"):
        self.message = message
        super().__init__(self.message)


class neg_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by negative"):
        self.message = message
        super().__init__(self.message)


class facto_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by factorial"):
        self.message = message
        super().__init__(self.message)


class operand1_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by operand 1"):
        self.message = message
        super().__init__(self.message)


class operand2_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by operand 2"):
        self.message = message
        super().__init__(self.message)


class equation_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by the whole equation not being valid"):
        self.message = message
        super().__init__(self.message)


class complex_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by a complex result from power a calculation"):
        self.message = message
        super().__init__(self.message)


class emptyEq_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by the equation being empty"):
        self.message = message
        super().__init__(self.message)


class emptyBrackets_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by empty brackets"):
        self.message = message
        super().__init__(self.message)


class digitSum_exception(Exception):
    def __init__(self, message="\nan error has occurred, it was caused by digit sum"):
        self.message = message
        super().__init__(self.message)
