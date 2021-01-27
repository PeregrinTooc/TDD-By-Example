# Invoke tearDown afterwards even if testmethod fails
# catch and report errors in setup
# Create TestSuite from a TestCase class
class TestCase():
    def __init__(self, name) -> None:
        self.name = name

    def run(self, result):
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

    def run(self, result):
        for testCase in self.tests:
            testCase.run(result)


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
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert(test.log == "setup testMethod tearDown ")

    def testResult(self):
        test = WasRun("testMethod")
        self.result = TestResult()
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())


suite = TestSuite()
result = TestResult()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))
suite.run(result)
print(result.summary())
