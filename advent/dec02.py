from io import StringIO

import pandas as pd

from util import aocio


day_input = aocio.get_day(2)

day_io = StringIO(day_input)

df = pd.DataFrame(day_io, columns=['raw'])
# add one so these are 1-INDEXED - to match the points for your thrown symbol
df['opponent'] = df['raw'].apply(lambda x: ord(x[0]) - ord('A'))
df['played'] = df['raw'].apply(lambda x: ord(x[2]) - ord('X'))

# you win if played - opponent == 1 (for 2, 3) or if played - opponent = -2
# which works with modulo? because negative numbers? mod(played-opponent, 3)

# you tie if played - opponet == 0, and lose if played - opponet == -1 (or 2)

# so the formula is mod(played - opponent, 3) * 3 + 3 - except we're shifted a bit
# because this results in a loss of 2. So we have to rotate it, by adding one:
# mod(played - opponent + 1, 3) * 3

df['result'] = df['played'] - df['opponent']
df['result'] = (df['result'] + 1) % 3 * 3


# get the total:
df['total'] = df['result'] + df['played'] + 1  # add one for every row for the played shift

# print(df)
print(f"total {sum(df['total'])}")


# PART 2

# (I should have assumed this would all be zero-indexed, lol - updating now)

# so column 2 now depicts the required result
# translating this into points is easy: (played) * 3

df['result 2'] = df['played'] * 3

# but to figure out what you played:
# 1 = lose, 2 = draw, 3 = win
# so 1 means shift one down, 2 means keep the same, and 3 means shift one up
# mod 3 ofc

df['played 2'] = (df['opponent'] + df['played'] - 1) % 3 + 1
df['total 2'] = (df['played 2'] + df['result 2'])

print(df)
print(f"total 2 {sum(df['total 2'])}")
