# poker_rl
a CONV based NLH poker RL agent and ENV

This is a work in progress, currently working on version 5.1

Descriptions:
mod_agents: implementations of different hard-coded poker agents

mod_automated_training: code for finding optimal learning rate and setup self-play

mod_comp_test: benchmarks for testing the trained agent

mod_DQN_Conv: the Conv agent, implemented with a memory object and different learning algorithms such as Proximal Policy Optimization (PPO, works best), TRPO, Vanila Policy Gradient, Deep Q learning, ... .

mod_fe: Feature Engineering of the input signal for faster training

mod_memory: Implementation of the memory object and memory generators

mod_poker_5: The Env

mod_poker_decide: Implementation of a no-action environment used for pre training the weights of the Conv net

mod_step_function: Testing the agent versus human player
