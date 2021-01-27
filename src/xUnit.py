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
        self.wasRun = 1

    def setUp(self):
        self.wasRun = False
        self.wasSetup = 1


class TestCaseTest(TestCase):
    def setUp(self):
        self.cut = WasRun("testMethod")

    def testRunning(self):
        self.cut.run()
        assert(self.cut.wasRun)

    def testSetUp(self):
        self.cut.run()
        assert(self.cut.wasSetup)


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
