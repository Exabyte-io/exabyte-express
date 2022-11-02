from mock import MagicMock
import numpy as np
from tests.unit import UnitTestBase
from express.properties.non_scalar.two_dimensional_plot.averaged_potential_profile import AveragedPotentialProfile


AVG_POTENTIAL = {
    "name": "averaged_potential_profile",
    "xDataArray": [0, 2.0943951, 4.1887902, 6.28318531],
    "yDataSeries": [[0, 0, 0, 0], [1.0, -0.5, -0.5, 1.0]],
    "yAxis": {
        "label": "energy",
        "units": "eV"
    },
    "xAxis": {
        "label": "z coordinate",
        "units": "angstrom"
    },
}


class AveragedPotentialProfileTest(UnitTestBase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def create_mock_data(self, n_points: int = 300):
        """
        Creates mock potential data based on cosine in the range [0, 2*pi].
        Exact minimum is at
          x   = pi
          m_x = -1
        """
        x = np.linspace(0, 2*np.pi, n_points)
        p_x = np.zeros(n_points)  # ignored for now
        m_x = np.cos(x)
        dtype = np.dtype([("x", float), ("p_x", float), ("m_x", float)])
        return np.array(list(zip(x, p_x, m_x)), dtype=dtype)

    def test_averaged_potential(self):
        averaged_potential_data = self.create_mock_data(n_points=4)
        parser = MagicMock()
        parser.attach_mock(MagicMock(return_value=averaged_potential_data), "averaged_potential")
        property_ = AveragedPotentialProfile("averaged_potential_profile", parser)
        self.assertDeepAlmostEqual(property_.serialize_and_validate(), AVG_POTENTIAL, places=6)
