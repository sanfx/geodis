# -*- coding: utf-8 -*-


# ISO 3166-1 codes (countries and not sub-divisions)
countries = {
    "AD": "Andorra",
    "AE": "United Arab Emirates",
    "AF": "Afghanistan",
    "AG": "Antigua and Barbuda",
    "AI": "Anguilla",
    "AL": "Albania",
    "AM": "Armenia",
    "AN": "Netherlands Antilles",
    "AO": "Angola",
    "AQ": "Antarctica",
    "AR": "Argentina",
    "AS": "American Samoa",
    "AT": "Austria",
    "AU": "Australia",
    "AW": "Aruba",
    "AX": "Mariehamn",
    "AZ": "Azerbaijan",
    "BA": "Bosnia and Herzegovina",
    "BB": "Barbados",
    "BD": "Bangladesh",
    "BE": "Belgium",
    "BF": "Burkina Faso",
    "BG": "Bulgaria",
    "BH": "Bahrain",
    "BI": "Burundi",
    "BJ": "Benin",
    "BL": "Saint Barthelemy",
    "BM": "Bermuda",
    "BN": "Brunei",
    "BO": "Bolivia",
    "BR": "Brazil",
    "BS": "Bahamas",
    "BT": "Bhutan",
    "BV": "Bouvet Island",
    "BW": "Botswana",
    "BY": "Belarus",
    "BZ": "Belize",
    "CA": "Canada",
    "CC": "Cocos Islands",
    "CD": "Democratic Republic of the Congo",
    "CF": "Central African Republic",
    "CG": "Republic of the Congo",
    "CH": "Switzerland",
    "CI": "Ivory Coast",
    "CK": "Cook Islands",
    "CL": "Chile",
    "CM": "Cameroon",
    "CN": "China",
    "CO": "Colombia",
    "CR": "Costa Rica",
    "CU": "Cuba",
    "CV": "Cape Verde",
    "CW": "Curaçao",
    "CX": "Christmas Island",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DE": "Germany",
    "DJ": "Djibouti",
    "DK": "Denmark",
    "DM": "Dominica",
    "DO": "Dominican Republic",
    "DZ": "Algeria",
    "EC": "Ecuador",
    "EE": "Estonia",
    "EG": "Egypt",
    "EH": "Western Sahara",
    "ER": "Eritrea",
    "ES": "Spain",
    "ET": "Ethiopia",
    "FI": "Finland",
    "FJ": "Fiji",
    "FK": "Falkland Islands",
    "FM": "Micronesia",
    "FO": "Faroe Islands",
    "FR": "France",
    "GA": "Gabon",
    "GB": "United Kingdom",
    "GD": "Grenada",
    "GE": "Georgia",
    "GF": "French Guiana",
    "GG": "Guernsey",
    "GH": "Ghana",
    "GI": "Gibraltar",
    "GL": "Greenland",
    "GM": "Gambia",
    "GN": "Guinea",
    "GP": "Guadeloupe",
    "GQ": "Equatorial Guinea",
    "GR": "Greece",
    "GS": "South Georgia and the South Sandwich Islands",
    "GT": "Guatemala",
    "GU": "Guam",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HK": "Hong Kong",
    "HM": "Heard Island and McDonald Islands",
    "HN": "Honduras",
    "HR": "Croatia",
    "HT": "Haiti",
    "HU": "Hungary",
    "ID": "Indonesia",
    "IE": "Ireland",
    "IL": "Israel",
    "IM": "Isle of Man",
    "IN": "India",
    "IO": "British Indian Ocean Territory",
    "IQ": "Iraq",
    "IR": "Iran",
    "IS": "Iceland",
    "IT": "Italy",
    "JE": "Jersey",
    "JM": "Jamaica",
    "JO": "Jordan",
    "JP": "Japan",
    "KE": "Kenya",
    "KG": "Kyrgyzstan",
    "KH": "Cambodia",
    "KI": "Kiribati",
    "KM": "Comoros",
    "KN": "Saint Kitts and Nevis",
    "KP": "North Korea",
    "KR": "South Korea",
    "XK": "Kosovo",
    "KW": "Kuwait",
    "KY": "Cayman Islands",
    "KZ": "Kazakhstan",
    "LA": "Laos",
    "LB": "Lebanon",
    "LC": "Saint Lucia",
    "LI": "Liechtenstein",
    "LK": "Sri Lanka",
    "LR": "Liberia",
    "LS": "Lesotho",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "LY": "Libya",
    "MA": "Morocco",
    "MC": "Monaco",
    "MD": "Moldova",
    "ME": "Montenegro",
    "MF": "Saint Martin",
    "MG": "Madagascar",
    "MH": "Marshall Islands",
    "MK": "Macedonia",
    "ML": "Mali",
    "MM": "Myanmar",
    "MN": "Mongolia",
    "MO": "Macao",
    "MP": "Northern Mariana Islands",
    "MQ": "Martinique",
    "MR": "Mauritania",
    "MS": "Montserrat",
    "MT": "Malta",
    "MU": "Mauritius",
    "MV": "Maldives",
    "MW": "Malawi",
    "MX": "Mexico",
    "MY": "Malaysia",
    "MZ": "Mozambique",
    "NA": "Namibia",
    "NC": "New Caledonia",
    "NE": "Niger",
    "NF": "Norfolk Island",
    "NG": "Nigeria",
    "NI": "Nicaragua",
    "NL": "Netherlands",
    "NO": "Norway",
    "NP": "Nepal",
    "NR": "Nauru",
    "NU": "Niue",
    "NZ": "New Zealand",
    "OM": "Oman",
    "PA": "Panama",
    "PE": "Peru",
    "PF": "French Polynesia",
    "PG": "Papua New Guinea",
    "PH": "Philippines",
    "PK": "Pakistan",
    "PL": "Poland",
    "PM": "Saint Pierre and Miquelon",
    "PN": "Pitcairn",
    "PR": "Puerto Rico",
    "PS": "Palestinian Territory",
    "PT": "Portugal",
    "PW": "Palau",
    "PY": "Paraguay",
    "QA": "Qatar",
    "RE": "Reunion",
    "RO": "Romania",
    "RS": "Serbia",
    "RU": "Russia",
    "RW": "Rwanda",
    "SA": "Saudi Arabia",
    "SB": "Solomon Islands",
    "SC": "Seychelles",
    "SD": "Sudan",
    "SE": "Sweden",
    "SG": "Singapore",
    "SH": "Saint Helena",
    "SI": "Slovenia",
    "SJ": "Svalbard and Jan Mayen",
    "SK": "Slovakia",
    "SL": "Sierra Leone",
    "SM": "San Marino",
    "SN": "Senegal",
    "SO": "Somalia",
    "SR": "Suriname",
    "SS": "South Sudan",
    "ST": "Sao Tome and Principe",
    "SV": "El Salvador",
    "SX": "Sint Maarten",
    "SY": "Syria",
    "SZ": "Swaziland",
    "TC": "Turks and Caicos Islands",
    "TD": "Chad",
    "TF": "French Southern Territories",
    "TG": "Togo",
    "TH": "Thailand",
    "TJ": "Tajikistan",
    "TK": "Tokelau",
    "TL": "East Timor",
    "TM": "Turkmenistan",
    "TN": "Tunisia",
    "TO": "Tonga",
    "TR": "Turkey",
    "TT": "Trinidad and Tobago",
    "TV": "Tuvalu",
    "TW": "Taiwan",
    "TZ": "Tanzania",
    "UA": "Ukraine",
    "UG": "Uganda",
    #"UM": "United States", This is a subdivision of US (ISO 3166-2) shouldn't be here
    "US": "United States",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VA": "Vatican",
    "VC": "Saint Vincent and the Grenadines",
    "VE": "Venezuela",
    "VG": "British Virgin Islands",
    "VI": "U.S. Virgin Islands",
    "VN": "Vietnam",
    "VU": "Vanuatu",
    "WF": "Wallis and Futuna",
    "WS": "Samoa",
    "YE": "Yemen",
    "YT": "Mayotte",
    "ZA": "South Africa",
    "ZM": "Zambia",
    "ZW": "Zimbabwe",
    "CS": "Serbia and Montenegro"
}

countryCodesByName = {
    "Andorra": "AD",
    "United Arab Emirates": "AE",
    "Afghanistan": "AF",
    "Antigua and Barbuda": "AG",
    "Anguilla": "AI",
    "Albania": "AL",
    "Armenia": "AM",
    "Netherlands Antilles": "AN",
    "Angola": "AO",
    "Antarctica": "AQ",
    "Argentina": "AR",
    "American Samoa": "AS",
    "Austria": "AT",
    "Australia": "AU",
    "Aruba": "AW",
    "Mariehamn": "AX",
    "Azerbaijan": "AZ",
    "Bosnia and Herzegovina": "BA",
    "Barbados": "BB",
    "Bangladesh": "BD",
    "Belgium": "BE",
    "Burkina Faso": "BF",
    "Bulgaria": "BG",
    "Bahrain": "BH",
    "Burundi": "BI",
    "Benin": "BJ",
    "Saint Barthélemy": "BL",
    "Saint Barthelemy": "BL",
    "Bermuda": "BM",
    "Brunei": "BN",
    "Bolivia": "BO",
    "Brazil": "BR",
    "Bahamas": "BS",
    "Bhutan": "BT",
    "Bouvet Island": "BV",
    "Botswana": "BW",
    "Belarus": "BY",
    "Belize": "BZ",
    "Canada": "CA",
    "Cocos Islands": "CC",
    "Cocos [Keeling] Islands": "CC",
    "Curaçao": "CW",
    "Curacao": "CW",
    "Democratic Republic of the Congo": "CD",
    "Central African Republic": "CF",
    "Republic of the Congo": "CG",
    "Switzerland": "CH",
    "Ivory Coast": "CI",
    "Cook Islands": "CK",
    "Chile": "CL",
    "Cameroon": "CM",
    "China": "CN",
    "Colombia": "CO",
    "Costa Rica": "CR",
    "Cuba": "CU",
    "Cape Verde": "CV",
    "Christmas Island": "CX",
    "Cyprus": "CY",
    "Czechia": "CZ",
    "Czech Republic": "CZ",
    "Germany": "DE",
    "Djibouti": "DJ",
    "Denmark": "DK",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "Algeria": "DZ",
    "Ecuador": "EC",
    "Estonia": "EE",
    "Egypt": "EG",
    "Western Sahara": "EH",
    "Eritrea": "ER",
    "Spain": "ES",
    "Ethiopia": "ET",
    "Finland": "FI",
    "Fiji": "FJ",
    "Falkland Islands": "FK",
    "Micronesia": "FM",
    "Faroe Islands": "FO",
    "France": "FR",
    "Gabon": "GA",
    "United Kingdom": "GB",
    "Grenada": "GD",
    "Georgia": "GE",
    "French Guiana": "GF",
    "Guernsey": "GG",
    "Ghana": "GH",
    "Gibraltar": "GI",
    "Greenland": "GL",
    "Gambia": "GM",
    "Guinea": "GN",
    "Guadeloupe": "GP",
    "Equatorial Guinea": "GQ",
    "Greece": "GR",
    "South Georgia and the South Sandwich Islands": "GS",
    "Guatemala": "GT",
    "Guam": "GU",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Hong Kong": "HK",
    "Heard Island and McDonald Islands": "HM",
    "Honduras": "HN",
    "Croatia": "HR",
    "Haiti": "HT",
    "Hungary": "HU",
    "Indonesia": "ID",
    "Ireland": "IE",
    "Israel": "IL",
    "Isle of Man": "IM",
    "India": "IN",
    "British Indian Ocean Territory": "IO",
    "Iraq": "IQ",
    "Iran": "IR",
    "Iceland": "IS",
    "Italy": "IT",
    "Jersey": "JE",
    "Jamaica": "JM",
    "Jordan": "JO",
    "Japan": "JP",
    "Kenya": "KE",
    "Kyrgyzstan": "KG",
    "Cambodia": "KH",
    "Kiribati": "KI",
    "Comoros": "KM",
    "Saint Kitts and Nevis": "KN",
    "North Korea": "KP",
    "South Korea": "KR",
    "Kosovo": "XK",
    "Kuwait": "KW",
    "Cayman Islands": "KY",
    "Kazakhstan": "KZ",
    "Laos": "LA",
    "Lebanon": "LB",
    "Saint Lucia": "LC",
    "Liechtenstein": "LI",
    "Sri Lanka": "LK",
    "Liberia": "LR",
    "Lesotho": "LS",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Latvia": "LV",
    "Libya": "LY",
    "Morocco": "MA",
    "Monaco": "MC",
    "Moldova": "MD",
    "Montenegro": "ME",
    "Saint Martin": "MF",
    "Madagascar": "MG",
    "Marshall Islands": "MH",
    "Macedonia": "MK",
    "Mali": "ML",
    "Myanmar": "MM",
    "Myanmar [Burma]": "MM",
    "Mongolia": "MN",
    "Macao": "MO",
    "Northern Mariana Islands": "MP",
    "Martinique": "MQ",
    "Mauritania": "MR",
    "Montserrat": "MS",
    "Malta": "MT",
    "Mauritius": "MU",
    "Maldives": "MV",
    "Malawi": "MW",
    "Mexico": "MX",
    "Malaysia": "MY",
    "Mozambique": "MZ",
    "Namibia": "NA",
    "New Caledonia": "NC",
    "Niger": "NE",
    "Norfolk Island": "NF",
    "Nigeria": "NG",
    "Nicaragua": "NI",
    "Netherlands": "NL",
    "Norway": "NO",
    "Nepal": "NP",
    "Nauru": "NR",
    "Niue": "NU",
    "New Zealand": "NZ",
    "Oman": "OM",
    "Panama": "PA",
    "Peru": "PE",
    "French Polynesia": "PF",
    "Papua New Guinea": "PG",
    "Philippines": "PH",
    "Pakistan": "PK",
    "Poland": "PL",
    "Saint Pierre and Miquelon": "PM",
    "Pitcairn": "PN",
    "Pitcairn Islands": "PN",
    "Puerto Rico": "PR",
    "Palestine": "PS",
    "Palestinian Territory": "PS",
    "Portugal": "PT",
    "Palau": "PW",
    "Paraguay": "PY",
    "Qatar": "QA",
    "Réunion": "RE",
    "Reunion": "RE",
    "Romania": "RO",
    "Serbia": "RS",
    "Russia": "RU",
    "Rwanda": "RW",
    "Saudi Arabia": "SA",
    "Solomon Islands": "SB",
    "Seychelles": "SC",
    "South Sudan": "SS",
    "Sudan": "SD",
    "Sweden": "SE",
    "Singapore": "SG",
    "Saint Helena": "SH",
    "Slovenia": "SI",
    "Svalbard and Jan Mayen": "SJ",
    "Slovakia": "SK",
    "Sierra Leone": "SL",
    "Sint Maarten": "SX",
    "San Marino": "SM",
    "Senegal": "SN",
    "Somalia": "SO",
    "Suriname": "SR",
    "Sao Tome and Principe": "ST",
    "São Tomé and Príncipe": "ST",
    "El Salvador": "SV",
    "Syria": "SY",
    "Swaziland": "SZ",
    "Turks and Caicos Islands": "TC",
    "Chad": "TD",
    "French Southern Territories": "TF",
    "Togo": "TG",
    "Thailand": "TH",
    "Tajikistan": "TJ",
    "Tokelau": "TK",
    "East Timor": "TL",
    "Turkmenistan": "TM",
    "Tunisia": "TN",
    "Tonga": "TO",
    "Turkey": "TR",
    "Trinidad and Tobago": "TT",
    "Tuvalu": "TV",
    "Taiwan": "TW",
    "Tanzania": "TZ",
    "Ukraine": "UA",
    "Uganda": "UG",
    "United States": "US",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Vatican": "VA",
    "Vatican City": "VA",
    "Saint Vincent and the Grenadines": "VC",
    "Venezuela": "VE",
    "British Virgin Islands": "VG",
    "U.S. Virgin Islands": "VI",
    "Vietnam": "VN",
    "Vanuatu": "VU",
    "Wallis and Futuna": "WF",
    "Samoa": "WS",
    "Yemen": "YE",
    "Mayotte": "YT",
    "South Africa": "ZA",
    "Zambia": "ZM",
    "Zimbabwe": "ZW",
    "Serbia and Montenegro": "CS"
}

countryIds = {
    "Rwanda": 49518,
    "Somalia": 51537,
    "Yemen": 69543,
    "Iraq": 99237,
    "Saudi Arabia": 102358,
    "Iran": 130758,
    "Cyprus": 146669,
    "Tanzania": 149590,
    "Syria": 163843,
    "Armenia": 174982,
    "Kenya": 192950,
    "Democratic Republic of the Congo": 203312,
    "Congo": 203312,
    "Djibouti": 223816,
    "Uganda": 226074,
    "Central African Republic": 239880,
    "Seychelles": 241170,
    "Jordan": 248816,
    "Lebanon": 272103,
    "Kuwait": 285570,
    "Oman": 286963,
    "Qatar": 289688,
    "Bahrain": 290291,
    "United Arab Emirates": 290557,
    "Israel": 294640,
    "Turkey": 298795,
    "Ethiopia": 337996,
    "Eritrea": 338010,
    "Egypt": 357994,
    "Sudan": 366755,
    "Greece": 390903,
    "Burundi": 433561,
    "Estonia": 453733,
    "Latvia": 458258,
    "Azerbaijan": 587116,
    "Lithuania": 597427,
    "Georgia": 614540,
    "Moldova": 617790,
    "Belarus": 630336,
    "Finland": 660013,
    "Åland": 661882,
    "Ukraine": 690791,
    "Macedonia": 718075,
    "Hungary": 719819,
    "Bulgaria": 732800,
    "Albania": 783754,
    "Poland": 798544,
    "Romania": 798549,
    "Kosovo": 831053,
    "Zimbabwe": 878675,
    "Zambia": 895949,
    "Comoros": 921929,
    "Malawi": 927384,
    "Lesotho": 932692,
    "Botswana": 933860,
    "Mauritius": 934292,
    "Swaziland": 934841,
    "Réunion": 935317,
    "South Africa": 953987,
    "Mayotte": 1024031,
    "Mozambique": 1036973,
    "Madagascar": 1062947,
    "Afghanistan": 1149361,
    "Pakistan": 1168579,
    "Bangladesh": 1210997,
    "Turkmenistan": 1218197,
    "Tajikistan": 1220409,
    "Sri Lanka": 1227603,
    "Bhutan": 1252634,
    "India": 1269750,
    "Maldives": 1282028,
    "British Indian Ocean Territory": 1282588,
    "Nepal": 1282988,
    "Myanmar": 1327865,
    "Myanmar [Burma]": 1327865,
    "Uzbekistan": 1512440,
    "Kazakhstan": 1522867,
    "Kyrgyzstan": 1527747,
    "French Southern Territories": 1546748,
    "Heard Island and McDonald Islands": 1547314,
    "Cocos [Keeling] Islands": 1547376,
    "Cocos Islands": 1547376,
    "Palau": 1559582,
    "Vietnam": 1562822,
    "Thailand": 1605651,
    "Indonesia": 1643084,
    "Laos": 1655842,
    "Taiwan": 1668284,
    "Philippines": 1694008,
    "Malaysia": 1733045,
    "China": 1814991,
    "Hong Kong": 1819730,
    "Brunei": 1820814,
    "Macao": 1821275,
    "Cambodia": 1831722,
    "South Korea": 1835841,
    "Japan": 1861060,
    "North Korea": 1873107,
    "Singapore": 1880251,
    "Cook Islands": 1899402,
    "East Timor": 1966436,
    "Russia": 2017370,
    "Mongolia": 2029969,
    "Australia": 2077456,
    "Christmas Island": 2078138,
    "Marshall Islands": 2080185,
    "Micronesia": 2081918,
    "Papua New Guinea": 2088628,
    "Solomon Islands": 2103350,
    "Tuvalu": 2110297,
    "Nauru": 2110425,
    "Vanuatu": 2134431,
    "New Caledonia": 2139685,
    "Norfolk Island": 2155115,
    "New Zealand": 2186224,
    "Fiji": 2205218,
    "Libya": 2215636,
    "Cameroon": 2233387,
    "Senegal": 2245662,
    "Republic of the Congo": 2260494,
    "Portugal": 2264397,
    "Liberia": 2275384,
    "Ivory Coast": 2287781,
    "Ghana": 2300660,
    "Equatorial Guinea": 2309096,
    "Nigeria": 2328926,
    "Burkina Faso": 2361809,
    "Togo": 2363686,
    "Guinea-Bissau": 2372248,
    "Mauritania": 2378080,
    "Benin": 2395170,
    "Gabon": 2400553,
    "Sierra Leone": 2403846,
    "Sao Tome and Principe": 2410758,
    "São Tomé and Príncipe": 2410758,
    "Gibraltar": 2411586,
    "Gambia": 2413451,
    "Guinea": 2420477,
    "Chad": 2434508,
    "Niger": 2440476,
    "Mali": 2453866,
    "Western Sahara": 2461445,
    "Tunisia": 2464461,
    "Spain": 2510769,
    "Morocco": 2542007,
    "Malta": 2562770,
    "Algeria": 2589581,
    "Faroe Islands": 2622320,
    "Denmark": 2623032,
    "Iceland": 2629691,
    "United Kingdom": 2635167,
    "Switzerland": 2658434,
    "Sweden": 2661886,
    "Netherlands": 2750405,
    "Austria": 2782113,
    "Belgium": 2802361,
    "Germany": 2921044,
    "Luxembourg": 2960313,
    "Ireland": 2963597,
    "Monaco": 2993457,
    "France": 3017382,
    "Andorra": 3041565,
    "Liechtenstein": 3042058,
    "Jersey": 3042142,
    "Isle of Man": 3042225,
    "Guernsey": 3042362,
    "Slovakia": 3057568,
    "Czechia": 3077311,
    "Czech Republic": 3077311,
    "Norway": 3144096,
    "Vatican": 3164670,
    "Vatican City": 3164670,
    "San Marino": 3168068,
    "Italy": 3175395,
    "Slovenia": 3190538,
    "Montenegro": 3194884,
    "Croatia": 3202326,
    "Bosnia and Herzegovina": 3277605,
    "Angola": 3351879,
    "Namibia": 3355338,
    "Saint Helena": 3370751,
    "Bouvet Island": 3371123,
    "Barbados": 3374084,
    "Cape Verde": 3374766,
    "Guyana": 3378535,
    "French Guiana": 3381670,
    "Suriname": 3382998,
    "Saint Pierre and Miquelon": 3424932,
    "Greenland": 3425505,
    "Paraguay": 3437598,
    "Uruguay": 3439705,
    "Brazil": 3469034,
    "Falkland Islands": 3474414,
    "South Georgia and the South Sandwich Islands": 3474415,
    "Jamaica": 3489940,
    "Dominican Republic": 3508796,
    "Cuba": 3562981,
    "Martinique": 3570311,
    "Bahamas": 3572887,
    "Bermuda": 3573345,
    "Anguilla": 3573511,
    "Trinidad and Tobago": 3573591,
    "Saint Kitts and Nevis": 3575174,
    "Dominica": 3575830,
    "Antigua and Barbuda": 3576396,
    "Saint Lucia": 3576468,
    "Turks and Caicos Islands": 3576916,
    "Aruba": 3577279,
    "British Virgin Islands": 3577718,
    "Saint Vincent and the Grenadines": 3577815,
    "Montserrat": 3578097,
    "Saint Martin": 3578421,
    "Saint Barthélemy": 3578476,
    "Saint Barthelemy": 3578476,
    "Guadeloupe": 3579143,
    "Grenada": 3580239,
    "Cayman Islands": 3580718,
    "Belize": 3582678,
    "El Salvador": 3585968,
    "Guatemala": 3595528,
    "Honduras": 3608932,
    "Nicaragua": 3617476,
    "Costa Rica": 3624060,
    "Venezuela": 3625428,
    "Ecuador": 3658394,
    "Colombia": 3686110,
    "Panama": 3703430,
    "Haiti": 3723988,
    "Argentina": 3865483,
    "Chile": 3895114,
    "Bolivia": 3923057,
    "Peru": 3932488,
    "Mexico": 3996063,
    "French Polynesia": 4030656,
    "Pitcairn": 4030699,
    "Pitcairn Islands": 4030699,
    "Kiribati": 4030945,
    "Tokelau": 4031074,
    "Tonga": 4032283,
    "Wallis and Futuna": 4034749,
    "Samoa": 4034894,
    "Niue": 4036232,
    "Northern Mariana Islands": 4041468,
    "Guam": 4043988,
    "Puerto Rico": 4566966,
    "U.S. Virgin Islands": 4796775,
    "U.S. Minor Outlying Islands": 5854968,
    "American Samoa": 5880801,
    "Canada": 6251999,
    "United States": 6252001,
    "Palestine": 6254930,
    "Palestinian Territory": 6254930,
    "Serbia": 6290252,
    "Antarctica": 6697173,
    "Sint Maarten": 7609695,
    "Curaçao": 7626836,
    "Curacao": 7626836,
    "Bonaire": 7626844,
    "South Sudan": 7909807,
    "Jervis Bay Territory": 8335033,
}

countriesById = {
    49518: "Rwanda",
    51537: "Somalia",
    69543: "Yemen",
    99237: "Iraq",
    102358: "Saudi Arabia",
    130758: "Iran",
    146669: "Cyprus",
    149590: "Tanzania",
    163843: "Syria",
    174982: "Armenia",
    192950: "Kenya",
    203312: "Democratic Republic of the Congo",
    223816: "Djibouti",
    226074: "Uganda",
    239880: "Central African Republic",
    241170: "Seychelles",
    248816: "Jordan",
    272103: "Lebanon",
    285570: "Kuwait",
    286963: "Oman",
    289688: "Qatar",
    290291: "Bahrain",
    290557: "United Arab Emirates",
    294640: "Israel",
    298795: "Turkey",
    337996: "Ethiopia",
    338010: "Eritrea",
    357994: "Egypt",
    366755: "Sudan",
    390903: "Greece",
    433561: "Burundi",
    453733: "Estonia",
    458258: "Latvia",
    587116: "Azerbaijan",
    597427: "Lithuania",
    614540: "Georgia",
    617790: "Moldova",
    630336: "Belarus",
    660013: "Finland",
    661882: "Åland",
    690791: "Ukraine",
    718075: "Macedonia",
    719819: "Hungary",
    732800: "Bulgaria",
    783754: "Albania",
    798544: "Poland",
    798549: "Romania",
    831053: "Kosovo",
    878675: "Zimbabwe",
    895949: "Zambia",
    921929: "Comoros",
    927384: "Malawi",
    932692: "Lesotho",
    933860: "Botswana",
    934292: "Mauritius",
    934841: "Swaziland",
    935317: "Réunion",
    953987: "South Africa",
    1024031: "Mayotte",
    1036973: "Mozambique",
    1062947: "Madagascar",
    1149361: "Afghanistan",
    1168579: "Pakistan",
    1210997: "Bangladesh",
    1218197: "Turkmenistan",
    1220409: "Tajikistan",
    1227603: "Sri Lanka",
    1252634: "Bhutan",
    1269750: "India",
    1282028: "Maldives",
    1282588: "British Indian Ocean Territory",
    1282988: "Nepal",
    1327865: "Myanmar [Burma]",
    1512440: "Uzbekistan",
    1522867: "Kazakhstan",
    1527747: "Kyrgyzstan",
    1546748: "French Southern Territories",
    1547314: "Heard Island and McDonald Islands",
    1547376: "Cocos [Keeling] Islands",
    1559582: "Palau",
    1562822: "Vietnam",
    1605651: "Thailand",
    1643084: "Indonesia",
    1655842: "Laos",
    1668284: "Taiwan",
    1694008: "Philippines",
    1733045: "Malaysia",
    1814991: "China",
    1819730: "Hong Kong",
    1820814: "Brunei",
    1821275: "Macao",
    1831722: "Cambodia",
    1835841: "South Korea",
    1861060: "Japan",
    1873107: "North Korea",
    1880251: "Singapore",
    1899402: "Cook Islands",
    1966436: "East Timor",
    2017370: "Russia",
    2029969: "Mongolia",
    2077456: "Australia",
    2078138: "Christmas Island",
    2080185: "Marshall Islands",
    2081918: "Micronesia",
    2088628: "Papua New Guinea",
    2103350: "Solomon Islands",
    2110297: "Tuvalu",
    2110425: "Nauru",
    2134431: "Vanuatu",
    2139685: "New Caledonia",
    2155115: "Norfolk Island",
    2186224: "New Zealand",
    2205218: "Fiji",
    2215636: "Libya",
    2233387: "Cameroon",
    2245662: "Senegal",
    2260494: "Republic of the Congo",
    2264397: "Portugal",
    2275384: "Liberia",
    2287781: "Ivory Coast",
    2300660: "Ghana",
    2309096: "Equatorial Guinea",
    2328926: "Nigeria",
    2361809: "Burkina Faso",
    2363686: "Togo",
    2372248: "Guinea-Bissau",
    2378080: "Mauritania",
    2395170: "Benin",
    2400553: "Gabon",
    2403846: "Sierra Leone",
    2410758: "São Tomé and Príncipe",
    2411586: "Gibraltar",
    2413451: "Gambia",
    2420477: "Guinea",
    2434508: "Chad",
    2440476: "Niger",
    2453866: "Mali",
    2461445: "Western Sahara",
    2464461: "Tunisia",
    2510769: "Spain",
    2542007: "Morocco",
    2562770: "Malta",
    2589581: "Algeria",
    2622320: "Faroe Islands",
    2623032: "Denmark",
    2629691: "Iceland",
    2635167: "United Kingdom",
    2658434: "Switzerland",
    2661886: "Sweden",
    2750405: "Netherlands",
    2782113: "Austria",
    2802361: "Belgium",
    2921044: "Germany",
    2960313: "Luxembourg",
    2963597: "Ireland",
    2993457: "Monaco",
    3017382: "France",
    3041565: "Andorra",
    3042058: "Liechtenstein",
    3042142: "Jersey",
    3042225: "Isle of Man",
    3042362: "Guernsey",
    3057568: "Slovakia",
    3077311: "Czechia",
    3144096: "Norway",
    3164670: "Vatican City",
    3168068: "San Marino",
    3175395: "Italy",
    3190538: "Slovenia",
    3194884: "Montenegro",
    3202326: "Croatia",
    3277605: "Bosnia and Herzegovina",
    3351879: "Angola",
    3355338: "Namibia",
    3370751: "Saint Helena",
    3371123: "Bouvet Island",
    3374084: "Barbados",
    3374766: "Cape Verde",
    3378535: "Guyana",
    3381670: "French Guiana",
    3382998: "Suriname",
    3424932: "Saint Pierre and Miquelon",
    3425505: "Greenland",
    3437598: "Paraguay",
    3439705: "Uruguay",
    3469034: "Brazil",
    3474414: "Falkland Islands",
    3474415: "South Georgia and the South Sandwich Islands",
    3489940: "Jamaica",
    3508796: "Dominican Republic",
    3562981: "Cuba",
    3570311: "Martinique",
    3572887: "Bahamas",
    3573345: "Bermuda",
    3573511: "Anguilla",
    3573591: "Trinidad and Tobago",
    3575174: "Saint Kitts and Nevis",
    3575830: "Dominica",
    3576396: "Antigua and Barbuda",
    3576468: "Saint Lucia",
    3576916: "Turks and Caicos Islands",
    3577279: "Aruba",
    3577718: "British Virgin Islands",
    3577815: "Saint Vincent and the Grenadines",
    3578097: "Montserrat",
    3578421: "Saint Martin",
    3578476: "Saint Barthélemy",
    3579143: "Guadeloupe",
    3580239: "Grenada",
    3580718: "Cayman Islands",
    3582678: "Belize",
    3585968: "El Salvador",
    3595528: "Guatemala",
    3608932: "Honduras",
    3617476: "Nicaragua",
    3624060: "Costa Rica",
    3625428: "Venezuela",
    3658394: "Ecuador",
    3686110: "Colombia",
    3703430: "Panama",
    3723988: "Haiti",
    3865483: "Argentina",
    3895114: "Chile",
    3923057: "Bolivia",
    3932488: "Peru",
    3996063: "Mexico",
    4030656: "French Polynesia",
    4030699: "Pitcairn Islands",
    4030945: "Kiribati",
    4031074: "Tokelau",
    4032283: "Tonga",
    4034749: "Wallis and Futuna",
    4034894: "Samoa",
    4036232: "Niue",
    4041468: "Northern Mariana Islands",
    4043988: "Guam",
    4566966: "Puerto Rico",
    4796775: "U.S. Virgin Islands",
    5854968: "U.S. Minor Outlying Islands",
    5880801: "American Samoa",
    6251999: "Canada",
    6252001: "United States",
    6254930: "Palestine",
    6290252: "Serbia",
    6697173: "Antarctica",
    7609695: "Sint Maarten",
    7626836: "Curaçao",
    7626844: "Bonaire",
    7909807: "South Sudan",
    8335033: "Jervis Bay Territory",
}

#### Utility functions to deal with country ids, codes and names ###

def getCountryNameById(id):
    """
    Return the official ISO name of a country by its internal numeric id
    """
    return countriesById.get(int(id or 0))

def getCountryCodeById(id):
    """
    Get the ISO country code (e.g. US, GB)  by its internal numeric id
    """
    return getCountryCodeByName(getCountryNameById(id))


def getCountryCodeByName(name):
    """
    Get the ISO Country code of a country by its official name. *** CASE SENSITIVE ***
    """
    return countryCodesByName.get(_str(name))

def getCountryNameByCode(code):
    """
    Get the official ISO name of a country by its ISO code. Case  - INsensitive -
    """
    return countries.get(str(code).upper())

def getCountryIdByName(name):
    """
    Get the internal numeric country id by its name (case SENSITIVE)
    """
    return countryIds.get(_str(name))

def getCountryIdByCode(code):
    """
    Get the internal numeric country id by its ISO code (case insensitive)
    """
    return getCountryIdByName(getCountryNameByCode(code))


def _str(s):
    """
    Convert to utf-8 encoded string for every possible type
    @param s: anything that can be converted to a string
    @return:
    """

    return s.encode('utf-8', 'replace') if isinstance(s, unicode) else (str(s) if not isinstance(s, str) else s)
