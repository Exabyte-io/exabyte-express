from tests.fixtures.nwchem.references import *
from tests.integration import IntegrationTestBase
from express.parsers.apps.nwchem.parser import NwchemParser


class TestNwchemParser(IntegrationTestBase):
    def setUp(self):
        super(TestNwchemParser, self).setUp()
        self.parser = NwchemParser(work_dir=self.workDir, stdout_file=self.stdoutFile)

    def tearDown(self):
        super(TestNwchemParser, self).setUp()

    def test_nwchem_total_energy(self):
        print("TOTAL_ENERGY={}".format(TOTAL_ENERGY))
        print("total_energy={}".format(self.parser.total_energy()))
        #self.assertAlmostEqual(self.parser.total_energy(), TOTAL_ENERGY, places=2)

    def test_nwchem_total_energy_contributions(self):
        self.assertDeepAlmostEqual(self.parser.total_energy_contributions(), TOTAL_ENERGY_CONTRIBUTION, places=2)
