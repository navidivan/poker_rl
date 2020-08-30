import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 200)

class Poker_decide:
  def __init__(self, num_rounds=4, starting_ronds = [4], debug=False):
    self.debug =debug
    self.deck = [1,2,3,4,5,6,7,8,9]
    self.num_rounds= num_rounds
    self.starting_ronds = starting_ronds

    self.rond = np.random.choice(starting_ronds)

    self.deck_np = np.array(self.deck)
    np.random.shuffle(self.deck_np)
    self.cards = self.deck_np[:2]

    self.com_card = np.array([0]*(self.num_rounds-1))

    self.deck_flop = np.array(self.deck)
    np.random.shuffle(self.deck_flop)

    self.com_card[:self.rond-1] = self.deck_flop[:self.rond-1]

    self.obs= {'cards':self.cards, 'num_rounds': self.num_rounds, 'rond':self.rond, 'com_card':self.com_card}
    # if self.debug: print('flop = ', self.obs['com_card'])
    # if self.debug: print('cards = ', self.obs['cards'])


  def reset_game(self):

    np.random.shuffle(self.deck_np)
    np.random.shuffle(self.deck_flop)
    self.obs['rond'] = np.random.choice(self.starting_ronds)

    self.obs['com_card'] = np.array([0]*(self.num_rounds-1))
    self.obs['com_card'][:self.obs['rond']-1] = self.deck_flop[:self.obs['rond']-1]

    self.obs['cards'] = self.deck_np[:2]
    # if self.debug: print('cards = ', self.obs['cards'])

  def decide(self):
    if self.obs['rond'] < self.obs['num_rounds']:
      self.obs['com_card'][self.obs['rond']-1:] = self.deck_flop[self.obs['rond']-1:self.obs['num_rounds']-1]

    maxp = [0, 0]
    for i in self.obs['com_card']:
        if self.obs['cards'][0] == i:
            maxp[0] = max(maxp[0],i)
        if self.obs['cards'][1] == i:
            maxp[1] = max(maxp[1],i)
    if max(maxp) > 0:
        winner = np.argmax(maxp)
        # if self.debug: print(maxp, 'maxp')
        # if self.debug: print(winner, 'winning with pair of ', max(maxp))
    else:
      winner = np.argmax(self.obs['cards'])
    #   if self.debug: print(winner, 'winning with highcard ', self.obs['cards'][winner])
    # # print('PLAYER {x} WON {y} DOLLARS!'.format(x=winner, y=self.obs['put']), ' counter= ', self.counter)
    # if self.debug: print('flop is: ', self.obs['com_card'])
    # if self.debug: print('PLAYER {x} HAS {xc}, PLAYER {y} HAS {yc}'.format(x=0, xc=self.obs['cards'][0], y=1,yc=self.obs['cards'][1] ))
    # if self.debug: print('PLAYER {x} WON!'.format(x=winner))
    return winner
