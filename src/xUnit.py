# Invoke tearDown afterwards even if testmethod fails
# Run multiple tests
# catch and report errors in setup
class TestCase():
    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result

    def setUp(self):
        pass

    def tearDown(self):
        pass


class TestSuite():
    def __init__(self) -> None:
        self.tests = []

    def add(self, testCase):
        self.tests.append(testCase)


class TestResult:
    def __init__(self) -> None:
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return "{0} run, {1} failed".format(self.runCount, self.errorCount)


class WasRun(TestCase):
    def __init__(self, name) -> None:
        super().__init__(name)

    def testBrokenMethod(self):
        raise Exception

    def testMethod(self):
        self.log += "testMethod "

    def setUp(self):
        self.log = "setup "

    def tearDown(self):
        self.log += "tearDown "


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.log == "setup testMethod tearDown ")

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = suite.run()
        assert("2 run, 1 failed" == result.summary())


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResultFormatting").run()
TestCaseTest("testFailedResult").run()
TestCaseTest("testSuite").run()
