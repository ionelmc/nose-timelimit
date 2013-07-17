import logging
logger = logging.getLogger(__name__)
import os
import time
from nose.plugins import Plugin
try:
    from cPickle import dump, load
except ImportError:
    from pickle import dump, load



class TimeLimitPlugin(Plugin):
    name = 'timelimit'
    id_file = None
    score = -200

    def options(self, parser, env):
        """Register commandline options.
        """
        super(TimeLimitPlugin, self).options(parser, env)
        parser.add_option('--timelimit-id-file', action='store', dest='timelimit_id_file',
                          default='.nosetimelimitids', metavar="FILE",
                          help="Store test ids and durations in this file. Default is the file .nosetimelimitids in "
                               "the working directory.")
        parser.add_option('--timelimit-silent', action='store_true', dest='timelimit_silent',
                          default=False, help="Do not output test duration. Default is to show it.")
        parser.add_option('--timelimit', action='store', dest='timelimit', metavar="NUMBER", type="float", default=None,
                          help="Only runs tests that have run in less than NUMBER seconds in the past.")



    def configure(self, options, conf):
        """Configure plugin.
        """
        super(TimeLimitPlugin, self).configure(options, conf)
        self.silent = options.timelimit_silent
        self.id_file = os.path.expanduser(options.timelimit_id_file)
        if not os.path.isabs(self.id_file):
            self.id_file = os.path.join(conf.workingDir, self.id_file)
        self.limit = options.timelimit
        if options.timelimit:
            self.enabled = True

        try:
            with open(self.id_file, 'rb') as fh:
                self.tests = load(fh)
        except (EOFError, IOError) as exc:
            logger.debug('IO error reading %r (%s)', self.id_file, exc)
            self.tests = {}

    def finalize(self, _result):
        """Save new ids file, if needed.
        """
        with open(self.id_file, 'wb') as fh:
            dump(self.tests, fh)

    def setOutputStream(self, stream):
        """Get handle on output stream so the plugin can print id #s
        """
        self.stream = stream

    def writeDuration(self, duration):
        self.stream.write("(%.04f seconds) " % duration)

    def startTest(self, _test):
        self.clock = time.time()

    def addSuccess(self, test):
        self.tests[test.id()] = duration = time.time() - self.clock
        self.writeDuration(duration)

    def addError(self, test, _err):
        self.tests.pop(test.id(), None)
    addFailure = addError

    def prepareTestCase(self, test):
        test_id = test.id()
        duration = self.tests.get(test_id, 0)
        if duration > self.limit:
            def skipper(result):
                result.startTest(test)
                result.addSkip(test, "Last run took %.04f seconds. Too slow !" % duration)
                result.stopTest(test)
            return skipper

__test__ = False
