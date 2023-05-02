# %%
import pandas as pd
import numpy as np

from scipy import stats
import math

from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('Pizza.csv')
df = df.fillna(0)

# %%
df.head()


# %%
df = df.loc[(df['Pos'] == 'FW') & (df['90s'] > 10)]
df.head()

# %%
df = df.drop(['Pos'], axis=1).reset_index()
df.head()

# %%
params = list(df.columns)
params

# %%
params = params[2:]
params.remove('Dist')
params.remove('PK')
params.remove('PKatt')
params

# %%
# The player needs to be spelled exactly the same way as it is in the data. Accents and everything.

player = df.loc[df['Player'] == 'Matías Cóccaro'].reset_index()
player = list(player.loc[0])
print(player)

# %%
df.Player.values

# %%
print(len(player), print(len(params)))
player = player[6:]
print(len(player), print(len(params)))

player


# %%
print(len(player), print(len(params)))

# %%
values = []
for x in range(len(params)):
    score = stats.percentileofscore(df[params[x]], player[x])


# %%
round(stats.percentileofscore(df[params[0]], player[0]))

# %%
for n, i in enumerate(player):
    if i == 100:
        player[n] = 99

# %%
font_normal = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                          'Roboto%5Bwdth,wght%5D.ttf')
font_italic = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                          'Roboto-Italic%5Bwdth,wght%5D.ttf')
font_bold = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                        'RobotoSlab%5Bwght%5D.ttf')

# %%
baker = PyPizza(
    params=params,                  # list of parameters
    straight_line_color="#000000",  # color for straight lines
    straight_line_lw=1,             # linewidth for straight lines
    last_circle_lw=1,               # linewidth of last circle
    other_circle_lw=1,              # linewidth for other circles
    other_circle_ls="-."
)


# %%


# %%
# plot pizza
fig, ax = baker.make_pizza(
    player,              # list of values
    figsize=(8, 8),      # adjust figsize according to your need
    param_location=110,  # where the parameters will be added
    kwargs_slices=dict(
        facecolor="#6CABDD", edgecolor="#000000",
        zorder=2, linewidth=1
    ),                   # values to be used when plotting slices
    kwargs_params=dict(
        color="#000000", fontsize=12,
        va="center", alpha=.5
    ),                   # values to be used when adding parameter
    kwargs_values=dict(
        color="#000000", fontsize=12,
        zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="#6CABDD",
            boxstyle="round,pad=0.2", lw=1
        )
    )                    # values to be used when adding parameter-values
)

# add title
fig.text(
    0.515, 0.97, "João Cancelo - Manchester City", size=18,
    ha="center", color="#000000"
)

# add subtitle
fig.text(
    0.515, 0.942,
    "Per 90 Percentile Rank vs Premier League Defenders | 2020-21",
    size=15,
    ha="center", color="#000000"
)

# add credits
notes = 'Players only with more than 15 90s'
CREDIT_1 = "data: statsbomb via fbref"
CREDIT_2 = "inspired by: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"

fig.text(
    0.99, 0.005, f"{notes}\n{CREDIT_1}\n{CREDIT_2}", size=9,
    color="#000000",
    ha="right"
)

plt.savefig('pizza.png', dpi=500, bbox_inches='tight')
