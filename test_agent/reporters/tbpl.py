from base import Base
import mozlog


class TBPLLogger(Base):
    def __init__(self, *args, **kwargs):
        Base.__init__(self, *args, **kwargs)
        self.logger = mozlog.getLogger('gaia-unit-tests')

    def on_pass(self, data):
        self.logger.testPass(data['fullTitle'])

    def on_fail(self, data):
        self.logger.testFail(data['fullTitle'])

    def on_suite(self, data):
        self.logger.testStart(data['title'])

    def on_suite_end(self, data):
        self.logger.testEnd(data['title'])

    def on_end(self, data):
        self.logger.info('suite results (pass/fail): %d/%d' %
                         (self.passes, self.failures))
