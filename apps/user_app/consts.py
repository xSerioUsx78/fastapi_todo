ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = 'daaa626dfa068882c392e20fd88b9161c5c4a662e4c54d18f9d1d0db7e437cd3'   # should be kept secret
JWT_REFRESH_SECRET_KEY = '8b36ba7835a89514d7a20d2063f67025eba7f1b8303273e0e38fdd4c09736bef'    # should be kept secret