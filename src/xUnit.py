# Invoke tearDown afterwards
# Invoke tearDown afterwards even if testmethod fails
# Run multiple tests
# Report collected results
class TestCase():
    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

    def setUp(self):
        pass


class WasRun(TestCase):
    def __init__(self, name) -> None:
        super().__init__(name)

    def testMethod(self):
        self.log += "testMethod "

    def setUp(self):
        self.log = "setup "


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        self.cut = WasRun("testMethod")
        self.cut.run()
        assert(self.cut.log.count("setup testMethod ") == 1)


TestCaseTest("testTemplateMethod").run()
