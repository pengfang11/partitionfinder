from basetest import *
import os, shutil

from partfinder import config, analysis_method

class TestAnalysis(PartitionFinderTestCase):

    def load_cfg_and_run(self, name):
        try:
            pth = os.path.join(ANALYSIS_PATH, name)
            cfg = config.Configuration()
            cfg.load_base_path(pth)
            method = analysis_method.choose_method(cfg.search)
            anal = method(cfg, True, False)
            anal.do_analysis(cfg.models, cfg.model_selection)
        finally:
            # Always do this
            shutil.rmtree(cfg.output_path)

# Dymanically add all separate files as tests
# Now we can just add new files
# See here: http://stackoverflow.com/questions/1193909/pythons-unittest-and-dynamic-creation-of-test-cases
analysis_dirs = os.listdir(ANALYSIS_PATH)
for f in analysis_dirs:
    def ch(f):
        return lambda self: self.load_cfg_and_run(f)
    setattr(TestAnalysis, 'test_' + f, ch(f))

if __name__ == '__main__':
    unittest.main()
