class ValidateErrors(Exception):
    def __init__(self, text):
        self.text = text

class ValidateIntError(ValidateErrors):
    def __init__(self, text):
        super().__init__(text)

class ValidateStrError(ValidateErrors):
    def __init__(self, text):
        super().__init__(text)

class ValidateFormatStrError(ValidateErrors):
    def __init__(self, text):
        super().__init__(text)

class ValidateFormatIntError(ValidateErrors):
    def __init__(self, text):
        super().__init__(text)

class ValidateFormatFloatError(ValidateErrors):
    def __init__(self, text):
        super().__init__(text)

class ValidateFormatBoolError(ValidateErrors):
    def __init__(self, text):
        super().__init__(text)

class ValidateAgeError(ValidateErrors):
    def __init__(self, text):
        super().__init__(text)

class ValidateNameError(ValidateErrors):
    def __init__(self, text):
        super().__init__(text)


class EmptyNameError(ValidateNameError):
    def __init__(self, text):
        super().__init__(text)


class FormatNameError(ValidateNameError):
    def __init__(self, text):
        super().__init__(text)