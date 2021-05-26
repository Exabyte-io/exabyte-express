import numpy as np

ATOMIC_FORCES_RAW_DATA = [
    [
        -3.9e-07,
        -2.4e-07,
        0.0
    ], [
        3.9e-07,
        2.4e-07,
        0.0
    ]
]

MAGNETIC_MOMENTS_RAW_DATA = [
    [
        0,
        0,
        1.235
    ],
    [
        0,
        0,
        -1.235
    ]
]

EIGENVALUES_AT_KPOINTS = [
    {
        "eigenvalues": [
            {
                "energies": [
                    -5.5990059,
                    6.26931638,
                    6.26931998,
                    6.26934533,
                    8.71135349,
                    8.71135587,
                    8.71135838,
                    9.41550185
                ],
                "occupations": [
                    1.0,
                    0.9999999999990231,
                    0.9999999999990226,
                    0.9999999999990189,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0,
            0,
            0
        ],
        "weight": 0.25
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -3.30219959,
                    -0.66503974,
                    5.06084876,
                    5.0608702,
                    7.69496909,
                    9.49274379,
                    9.49275618,
                    13.89571002
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    2.191035831088034E-113,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.28867514,
            0.20412412,
            -0.49999997
        ],
        "weight": 0.5
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -3.30220019,
                    -0.6650363,
                    5.06084821,
                    5.06086954,
                    7.69496137,
                    9.49273868,
                    9.49275401,
                    13.89571914
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    2.199010455040857E-113,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0,
            -0.61237246,
            0
        ],
        "weight": 0.25
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -1.51073812,
                    -1.51072293,
                    3.41069883,
                    3.41070722,
                    6.91957625,
                    6.91958498,
                    16.14829919,
                    16.1483028
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    4.579502952592552E-11,
                    4.573994582634171E-11,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.28867514,
            -0.40824834,
            -0.49999997
        ],
        "weight": 0.5
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -3.30221054,
                    -0.66501391,
                    5.06085301,
                    5.06085524,
                    7.69495606,
                    9.49273487,
                    9.49273798,
                    13.89571883
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    2.204511701557367E-113,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            -0.57735028,
            0.20412421,
            0
        ],
        "weight": 0.25
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -1.51074222,
                    -1.5107195,
                    3.41069761,
                    3.41071003,
                    6.91957636,
                    6.91958424,
                    16.14830113,
                    16.14830247
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    4.579432877486831E-11,
                    4.574465149035778E-11,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            -0.57735028,
            -0.40824824,
            0
        ],
        "weight": 0.25
    }
]

IBZ_K_POINTS = np.array([
    [
        0.0,
        0.0,
        0.0
    ],
    [
        -4.8471013318887174E-17,
        -4.8471013318887174E-17,
        -0.5000000000000001
    ],
    [
        0.0,
        -0.4999999999999998,
        0.0
    ],
    [
        -4.8471013318887174E-17,
        -0.4999999999999998,
        -0.5000000000000001
    ],
    [
        -0.4999999999999998,
        6.584042720160102E-17,
        0.0
    ],
    [
        -0.4999999999999998,
        -0.4999999999999998,
        0.0
    ]
])

STRESS_TENSOR_RAW_DATA = [
    [
        3,
        0,
        0
    ],
    [
        0,
        3,
        0
    ],
    [
        0,
        0,
        3
    ]
]

SPACE_GROUP_SYMBOL = {
    "value": "Fd-3m",
    "tolerance": 0.3
}

TOTAL_ENERGY_CONTRIBUTIONS_RAW_DATA = {
    "ewald": {
        "name": "ewald",
        "value": 128376.45871064
    },
    "hartree": {
        "name": "hartree",
        "value": -145344.66902862
    },
    "exchangeCorrelation": {
        "name": "exchange_correlation",
        "value": 41.63693035
    }
}

ELEMENTAL_RATIOS_RAW_DATA = {
    "Si": 0.6,
    "Ge": 0.4
}

PHONON_DISPERSIONS_RAW_DATA = {
    "frequencies": [
        [
            -6e-06,
            -6.859784
        ],
        [
            -6e-06,
            -6.859784
        ]
    ],
    "qpoints": [
        [
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.05,
            0.05
        ]
    ]
}

PHONON_DOS_RAW_DATA = {
    "total": [
        0.0,
        1.7269000451847205e-08,
        6.90749999421314e-08
    ],
    "frequency": [
        -313.8999938964844,
        -312.8999938964844,
        -311.8999938964844
    ]
}

DOS_RAW_DATA = {
    "energy": [
        -6.005000114440918,
        -5.954999923706055,
        -5.90500020980835
    ],
    "partial": [
        [
            1.6499999980444308E-17,
            1.3080000562020133E-16,
            7.899999954541818E-16
        ]
    ],
    "partial_info": [
        {
            "electronicState": "2py",
            "element": "Si"
        },
        {
            "electronicState": "2px",
            "element": "Si"
        },
        {
            "electronicState": "1s",
            "element": "Si"
        },
        {
            "electronicState": "2pz",
            "element": "Si"
        }
    ],
    "total": [
        0.00012799999967683107,
        0.0010100000072270632,
        0.006130000110715628
    ]
}

HSE_EIGENVALUES_AT_KPOINTS = [
    {
        "eigenvalues": [
            {
                "energies": [
                    -7.4914,
                    5.3112,
                    5.3112,
                    5.3112,
                    9.0299,
                    9.03,
                    9.03,
                    10.0024
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.0,
            0.0,
            0.0
        ],
        "weight": 0.25
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -4.9161,
                    -1.9754,
                    4.1061,
                    4.1061,
                    7.9728,
                    9.8041,
                    9.8041,
                    14.0982
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.5,
            0.0,
            0.0
        ],
        "weight": 0.5
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -2.9288,
                    -2.9288,
                    2.3959,
                    2.3959,
                    7.0191,
                    7.0192,
                    16.9059,
                    16.9059
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.5,
            0.5,
            0.0
        ],
        "weight": 0.25
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -7.4913,
                    5.3138,
                    5.3138,
                    5.3301,
                    9.0302,
                    9.044,
                    9.044,
                    10.1849
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.0,
            0.0,
            0.0
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -7.932,
                    3.9163,
                    4.2722,
                    4.2787,
                    8.6168,
                    9.672,
                    9.7195,
                    10.822
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.1,
            0.0,
            0.1
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -6.9644,
                    2.604,
                    3.7715,
                    3.7717,
                    7.8168,
                    10.3324,
                    11.2318,
                    11.2937
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.2,
            0.0,
            0.2
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -5.7751,
                    0.8774,
                    3.1645,
                    3.1646,
                    7.1761,
                    8.7696,
                    13.1602,
                    13.1908
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.3,
            0.0,
            0.3
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -4.4408,
                    -1.0373,
                    2.6568,
                    2.6568,
                    6.8837,
                    7.6307,
                    15.1777,
                    15.1868
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.4,
            0.0,
            0.4
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -2.9288,
                    -2.9287,
                    2.3959,
                    2.3959,
                    7.0192,
                    7.0192,
                    16.9208,
                    17.0277
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.5,
            0.0,
            0.5
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -2.9129,
                    -2.9128,
                    2.2941,
                    2.2941,
                    7.2376,
                    7.2377,
                    16.4053,
                    16.7348
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.5,
            0.05,
            0.55
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -2.7671,
                    -2.767,
                    2.1427,
                    2.1427,
                    7.8449,
                    7.8453,
                    15.1527,
                    15.2549
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.5,
            0.1,
            0.6
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -2.6725,
                    -2.6722,
                    1.9,
                    1.9001,
                    8.7215,
                    8.7259,
                    13.7766,
                    13.9711
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.5,
            0.15,
            0.65
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -2.5951,
                    -2.595,
                    1.7189,
                    1.719,
                    9.7601,
                    9.7684,
                    12.445,
                    12.5033
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.5,
            0.2,
            0.7
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -2.565,
                    -2.5649,
                    1.6527,
                    1.6527,
                    10.5917,
                    10.6011,
                    11.5213,
                    11.5603
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.5,
            0.25,
            0.75
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -2.7974,
                    -2.3572,
                    1.4828,
                    1.8926,
                    9.9113,
                    10.6632,
                    11.877,
                    11.9237
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.475,
            0.275,
            0.75
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -2.9858,
                    -2.2326,
                    1.3405,
                    2.2252,
                    9.0338,
                    10.6129,
                    12.4356,
                    12.6121
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.45,
            0.3,
            0.75
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -3.1255,
                    -2.169,
                    1.2326,
                    2.5905,
                    8.2736,
                    10.5492,
                    13.0626,
                    13.417
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.425,
            0.325,
            0.75
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -3.2122,
                    -2.1426,
                    1.165,
                    2.8925,
                    7.7374,
                    10.5002,
                    13.6874,
                    14.3407
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.4,
            0.35,
            0.75
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -3.2415,
                    -2.1358,
                    1.142,
                    3.0141,
                    7.5385,
                    10.4847,
                    14.1386,
                    14.6705
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.375,
            0.375,
            0.75
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -4.301,
                    -1.1455,
                    1.1771,
                    3.6549,
                    8.2839,
                    12.36,
                    12.4326,
                    13.4495
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.3,
            0.3,
            0.6
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -5.6321,
                    0.2207,
                    2.0367,
                    4.3266,
                    9.1403,
                    10.9001,
                    10.9735,
                    12.4004
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.225,
            0.225,
            0.45
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -6.8624,
                    1.8869,
                    3.2445,
                    4.7391,
                    9.5687,
                    9.7823,
                    9.8764,
                    12.1208
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.15,
            0.15,
            0.3
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -7.8885,
                    3.5572,
                    4.1971,
                    4.645,
                    9.1335,
                    9.2838,
                    9.3959,
                    11.1464
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.075,
            0.075,
            0.15
        ],
        "weight": 0.0
    },
    {
        "eigenvalues": [
            {
                "energies": [
                    -7.4913,
                    5.3138,
                    5.3138,
                    5.3301,
                    9.0302,
                    9.044,
                    9.044,
                    10.1849
                ],
                "occupations": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "spin": 0.5
            }
        ],
        "kpoint": [
            0.0,
            0.0,
            0.0
        ],
        "weight": 0.0
    }
]

BAND_STRUCTURE = {
    "name": "band_structure",
    "spin": [
        0.5,
        0.5,
        0.5,
        0.5,
        0.5,
        0.5,
        0.5,
        0.5
    ],
    "xAxis": {
        "label": "kpoints",
        "units": "crystal"
    },
    "xDataArray": [
        [
            0,
            0,
            0
        ],
        [
            0.28867514,
            0.20412412,
            -0.49999997
        ],
        [
            0,
            -0.61237246,
            0
        ],
        [
            0.28867514,
            -0.40824834,
            -0.49999997
        ],
        [
            -0.57735028,
            0.20412421,
            0
        ],
        [
            -0.57735028,
            -0.40824824,
            0
        ]
    ],
    "yAxis": {
        "label": "energy",
        "units": "eV"
    },
    "yDataSeries": [
        [
            -5.5990059,
            -3.30219959,
            -3.30220019,
            -1.51073812,
            -3.30221054,
            -1.51074222
        ],
        [
            6.26931638,
            -0.66503974,
            -0.6650363,
            -1.51072293,
            -0.66501391,
            -1.5107195
        ],
        [
            6.26931998,
            5.06084876,
            5.06084821,
            3.41069883,
            5.06085301,
            3.41069761
        ],
        [
            6.26934533,
            5.0608702,
            5.06086954,
            3.41070722,
            5.06085524,
            3.41071003
        ],
        [
            8.71135349,
            7.69496909,
            7.69496137,
            6.91957625,
            7.69495606,
            6.91957636
        ],
        [
            8.71135587,
            9.49274379,
            9.49273868,
            6.91958498,
            9.49273487,
            6.91958424
        ],
        [
            8.71135838,
            9.49275618,
            9.49275401,
            16.14829919,
            9.49273798,
            16.14830113
        ],
        [
            9.41550185,
            13.89571002,
            13.89571914,
            16.1483028,
            13.89571883,
            16.14830247
        ]
    ]
}

HSE_BAND_STRUCTURE = {
    "name": "band_structure",
    "spin": [
        0.5,
        0.5,
        0.5,
        0.5,
        0.5,
        0.5,
        0.5,
        0.5
    ],
    "xAxis": {
        "label": "kpoints",
        "units": "crystal"
    },
    "xDataArray": [
        [
            0.0,
            0.0,
            0.0
        ],
        [
            0.1,
            0.0,
            0.1
        ],
        [
            0.2,
            0.0,
            0.2
        ],
        [
            0.3,
            0.0,
            0.3
        ],
        [
            0.4,
            0.0,
            0.4
        ],
        [
            0.5,
            0.0,
            0.5
        ],
        [
            0.5,
            0.05,
            0.55
        ],
        [
            0.5,
            0.1,
            0.6
        ],
        [
            0.5,
            0.15,
            0.65
        ],
        [
            0.5,
            0.2,
            0.7
        ],
        [
            0.5,
            0.25,
            0.75
        ],
        [
            0.475,
            0.275,
            0.75
        ],
        [
            0.45,
            0.3,
            0.75
        ],
        [
            0.425,
            0.325,
            0.75
        ],
        [
            0.4,
            0.35,
            0.75
        ],
        [
            0.375,
            0.375,
            0.75
        ],
        [
            0.3,
            0.3,
            0.6
        ],
        [
            0.225,
            0.225,
            0.45
        ],
        [
            0.15,
            0.15,
            0.3
        ],
        [
            0.075,
            0.075,
            0.15
        ],
        [
            0.0,
            0.0,
            0.0
        ]
    ],
    "yAxis": {
        "label": "energy",
        "units": "eV"
    },
    "yDataSeries": [
        [
            -7.4913,
            -7.932,
            -6.9644,
            -5.7751,
            -4.4408,
            -2.9288,
            -2.9129,
            -2.7671,
            -2.6725,
            -2.5951,
            -2.565,
            -2.7974,
            -2.9858,
            -3.1255,
            -3.2122,
            -3.2415,
            -4.301,
            -5.6321,
            -6.8624,
            -7.8885,
            -7.4913
        ],
        [
            5.3138,
            3.9163,
            2.604,
            0.8774,
            -1.0373,
            -2.9287,
            -2.9128,
            -2.767,
            -2.6722,
            -2.595,
            -2.5649,
            -2.3572,
            -2.2326,
            -2.169,
            -2.1426,
            -2.1358,
            -1.1455,
            0.2207,
            1.8869,
            3.5572,
            5.3138
        ],
        [
            5.3138,
            4.2722,
            3.7715,
            3.1645,
            2.6568,
            2.3959,
            2.2941,
            2.1427,
            1.9,
            1.7189,
            1.6527,
            1.4828,
            1.3405,
            1.2326,
            1.165,
            1.142,
            1.1771,
            2.0367,
            3.2445,
            4.1971,
            5.3138
        ],
        [
            5.3301,
            4.2787,
            3.7717,
            3.1646,
            2.6568,
            2.3959,
            2.2941,
            2.1427,
            1.9001,
            1.719,
            1.6527,
            1.8926,
            2.2252,
            2.5905,
            2.8925,
            3.0141,
            3.6549,
            4.3266,
            4.7391,
            4.645,
            5.3301
        ],
        [
            9.0302,
            8.6168,
            7.8168,
            7.1761,
            6.8837,
            7.0192,
            7.2376,
            7.8449,
            8.7215,
            9.7601,
            10.5917,
            9.9113,
            9.0338,
            8.2736,
            7.7374,
            7.5385,
            8.2839,
            9.1403,
            9.5687,
            9.1335,
            9.0302
        ],
        [
            9.044,
            9.672,
            10.3324,
            8.7696,
            7.6307,
            7.0192,
            7.2377,
            7.8453,
            8.7259,
            9.7684,
            10.6011,
            10.6632,
            10.6129,
            10.5492,
            10.5002,
            10.4847,
            12.36,
            10.9001,
            9.7823,
            9.2838,
            9.044
        ],
        [
            9.044,
            9.7195,
            11.2318,
            13.1602,
            15.1777,
            16.9208,
            16.4053,
            15.1527,
            13.7766,
            12.445,
            11.5213,
            11.877,
            12.4356,
            13.0626,
            13.6874,
            14.1386,
            12.4326,
            10.9735,
            9.8764,
            9.3959,
            9.044
        ],
        [
            10.1849,
            10.822,
            11.2937,
            13.1908,
            15.1868,
            17.0277,
            16.7348,
            15.2549,
            13.9711,
            12.5033,
            11.5603,
            11.9237,
            12.6121,
            13.417,
            14.3407,
            14.6705,
            13.4495,
            12.4004,
            12.1208,
            11.1464,
            10.1849
        ]
    ]
}

INCHIS = {
    "Si2": "InChI=1S/Si2/c1-2",
    "H2O": "InChI=1S/H2O.2H2/h1H2;2*1H"
    "C6H6": "InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H"
}

SI = {
    "_id": "",
    "basis": {
        "coordinates": [
            {
                "id": 1,
                "value": [
                    0.0,
                    0.0,
                    0.0
                ]
            },
            {
                "id": 2,
                "value": [
                    0.25,
                    0.25,
                    0.25
                ]
            }
        ],
        "elements": [
            {
                "id": 1,
                "value": "Si"
            },
            {
                "id": 2,
                "value": "Si"
            }
        ],
        "units": "crystal"
    },
    "creator": {
        "_id": "",
        "cls": "User",
        "slug": ""
    },
    "derivedProperties": [
        {
            "name": "volume",
            "units": "angstrom^3",
            "value": 40.88909038874689
        },
        {
            "name": "density",
            "units": "g/cm^3",
            "value": 2.2811497523923894
        },
        {
            "name": "symmetry",
            "spaceGroupSymbol": "Fd-3m",
            "tolerance": {
                "units": "angstrom",
                "value": 0.3
            }
        },
        {
            "element": "Si",
            "name": "elemental_ratio",
            "value": 1
        },
        {
            "degree": 0,
            "name": "p-norm",
            "value": 1
        },
        {
            "degree": 2,
            "name": "p-norm",
            "value": 1
        },
        {
            "degree": 3,
            "name": "p-norm",
            "value": 1
        },
        {
            "degree": 5,
            "name": "p-norm",
            "value": 1
        },
        {
            "degree": 7,
            "name": "p-norm",
            "value": 1
        },
        {
            "degree": 10,
            "name": "p-norm",
            "value": 1
        }
    ],
    "exabyteId": "",
    "formula": "Si",
    "hash": "",
    "lattice": {
        "a": 3.867,
        "alpha": 60,
        "b": 3.867,
        "beta": 60,
        "c": 3.867,
        "gamma": 59.99999,
        "type": "FCC",
        "units": {
            "angle": "degree",
            "length": "angstrom"
        }
    },
    "name": "material",
    "owner": {
        "_id": "",
        "cls": "Account",
        "slug": ""
    },
    "schemaVersion": "0.2.0",
    "unitCellFormula": "Si2"
}
