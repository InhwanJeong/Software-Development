class WasRun:
    def __init__(self, name) -> None:
        self.was_run = None
    
    def test_method(self):
        self.was_run = 1


if __name__ == '__main__':
    test = WasRun('test_method')
    print(test.was_run)
    test.test_method()
    print(test.was_run)