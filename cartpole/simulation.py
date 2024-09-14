import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

import gym
import random

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

import matplotlib.pyplot as plt

# choosing an environment

env = gym.make('CartPole-v1')
states = env.observation_space.shape[0]
actions = env.action_space


def Building_Agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit = 50000, window_length = 1)
    dqn = DQNAgent(model = model, memory = memory, policy = policy, nb_actions = actions, nb_steps_warmup = 10, target_model_update = 1e-2)
    return dqn

def Building_Model(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1,states)))
    model.add(Dense(24, activation = 'relu'))
    model.add(Dense(24, activation = 'relu'))
    model.add(Dense(actions, activation ='linear'))
    return model

scores = []
episodes = 30
for episode in range(1, episodes + 1):
    state = env.reset()
    terminated,truncated = False, False
    score = 0
    while not terminated or truncated:
        env.render()
        action = random.choice([0.1])
        n_state,reward,terminated,truncated,info = env.step(action)
        score += reward
    print('Episode:{} Score:{}'.format(episode,score))
    scores.append(score)

    model = Building_Model(states, actions)
print(model.summary())

plt.plot(range(episodes),scores)
plt.rcParams["figure.figsize"] = (27,8)
plt.show()


