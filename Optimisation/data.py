
from datetime import datetime

# jeu de données permettant de tester la solution
flights = {
    "BER_LHR": [
        {
            "max_departure_time": datetime(2010, 7, 26, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 26, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 7, 27, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 27, 17, 0, 0),
        }
    ],
    "BIO_LHR": [
        {
            "max_departure_time": datetime(2010, 7, 26, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 26, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 7, 27, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 27, 17, 0, 0),
        }
    ],
    "CDG_LHR": [
        {
            "max_departure_time": datetime(2010, 7, 26, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 26, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 7, 27, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 27, 17, 0, 0),
        }
    ],
    "JFK_LHR": [
        {
            "max_departure_time": datetime(2010, 7, 26, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 27, 17, 0, 0),
        },
        {
            "max_departure_time": datetime(2010, 7, 27, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 27, 17, 0, 0),
        }
    ],
    "LYS_LHR": [
        {
            "max_departure_time": datetime(2010, 7, 26, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 26, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 7, 27, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 27, 17, 0, 0),
        }
    ],
    "MAN_LHR": [
        {
            "max_departure_time": datetime(2010, 7, 26, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 26, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 7, 27, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 27, 17, 0, 0),
        }
    ],
    "MRS_LHR": [
        {
            "max_departure_time": datetime(2010, 7, 26, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 26, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 7, 27, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 27, 17, 0, 0),
        }
    ],
    "MXP_LHR": [
        {
            "max_departure_time": datetime(2010, 7, 26, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 26, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 7, 27, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 27, 17, 0, 0),
        }
    ],
    "TUN_LHR": [
        {
            "max_departure_time": datetime(2010, 7, 26, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 26, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 7, 27, 0, 0, 0),
            "max_arrival_time": datetime(2010, 7, 27, 17, 0, 0),
        }
    ]
}

flights_return = {
    "LHR_BER": [
        {
            "max_departure_time": datetime(2010, 8, 3, 15, 0, 0),
            "max_arrival_time": datetime(2010, 8, 3, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 8, 4, 0, 0, 0),
            "max_arrival_time": datetime(2010, 8, 4, 23, 59, 0),
        }
    ],
    "LHR_BIO": [
        {
            "max_departure_time": datetime(2010, 8, 3, 15, 0, 0),
            "max_arrival_time": datetime(2010, 8, 3, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 8, 4, 0, 0, 0),
            "max_arrival_time": datetime(2010, 8, 4, 23, 59, 0),
        }
    ],
    "LHR_CDG": [
        {
            "max_departure_time": datetime(2010, 8, 3, 15, 0, 0),
            "max_arrival_time": datetime(2010, 8, 3, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 8, 4, 0, 0, 0),
            "max_arrival_time": datetime(2010, 8, 4, 23, 59, 0),
        }
    ],
    "LHR_JFK": [
        {
            "max_departure_time": datetime(2010, 8, 3, 15, 0, 0),
            "max_arrival_time": datetime(2010, 8, 3, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 8, 4, 0, 0, 0),
            "max_arrival_time": datetime(2010, 8, 4, 23, 59, 0),
        }
    ],
    "LHR_LYS": [
        {
            "max_departure_time": datetime(2010, 8, 3, 15, 0, 0),
            "max_arrival_time": datetime(2010, 8, 3, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 8, 4, 0, 0, 0),
            "max_arrival_time": datetime(2010, 8, 4, 23, 59, 0),
        }
    ],
    "LHR_MAN": [
        {
            "max_departure_time": datetime(2010, 8, 3, 15, 0, 0),
            "max_arrival_time": datetime(2010, 8, 3, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 8, 4, 0, 0, 0),
            "max_arrival_time": datetime(2010, 8, 4, 23, 59, 0),
        }
    ],
    "LHR_MRS": [
        {
            "max_departure_time": datetime(2010, 8, 3, 15, 0, 0),
            "max_arrival_time": datetime(2010, 8, 3, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 8, 4, 0, 0, 0),
            "max_arrival_time": datetime(2010, 8, 4, 23, 59, 0),
        }
    ],
    "LHR_MXP": [
        {
            "max_departure_time": datetime(2010, 8, 3, 15, 0, 0),
            "max_arrival_time": datetime(2010, 8, 3, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 8, 4, 0, 0, 0),
            "max_arrival_time": datetime(2010, 8, 4, 23, 59, 0),
        }
    ],
    "LHR_TUN": [
        {
            "max_departure_time": datetime(2010, 8, 3, 15, 0, 0),
            "max_arrival_time": datetime(2010, 8, 3, 23, 59, 0),
        },
        {
            "max_departure_time": datetime(2010, 8, 4, 0, 0, 0),
            "max_arrival_time": datetime(2010, 8, 4, 23, 59, 0),
        }
    ]
}