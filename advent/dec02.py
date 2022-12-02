from io import StringIO

import pandas as pd

from util import aocio


day_input = aocio.get_day(2)

day_io = StringIO(day_input)

df = pd.DataFrame(day_io, columns=['raw'])
# add one so these are 1-INDEXED - to match the points for your thrown symbol
df['opponent'] = df['raw'].apply(lambda x: ord(x[0]) - ord('A') + 1)
df['played'] = df['raw'].apply(lambda x: ord(x[2]) - ord('X') + 1)

# you win if played - opponent == 1 (for 2, 3) or if played - opponent = -2
# which works with modulo? because negative numbers? mod(played-opponent, 3)

# you tie if played - opponet == 0, and lose if played - opponet == -1 (or 2)

# so the formula is mod(played - opponent, 3) * 3 + 3 - except we're shifted a bit
# because this results in a loss of 2. whereas if you drop the "+1s" (or subtract 1) then it looks like
# mod(played - opponent + 1, 3) * 3

df['result'] = df['played'] - df['opponent']
df['result'] = df['result'].add(1).mod(3).mul(3)


# get the total:
df['total'] = df['result'] + df['played']

print(df)
print(f"total {sum(df['total'])}")
