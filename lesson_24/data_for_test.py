test_cases = [
    {"sort_by": "brand", "limit": 2},
    {"sort_by": "year", "limit": 3},
    {"sort_by": "engine_volume", "limit": 4},
    {"sort_by": "price", "limit": 5},
    {"sort_by": "", "limit": 10},
    {"sort_by": "year", "limit": 0},
    {"sort_by": "year", "limit": 26},
    {"sort_by": "nonexistent_field", "limit": 5},   # баг? має бути 400?
    {},
    {"sort_by": "price"},
    {"limit": 5},
]