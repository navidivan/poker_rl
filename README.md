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


Results:
more than 2e6 steps, linearly decrease epsilon, lr=1e-6, batch_Szie=512, mem_size=10000
DQLAgent won 94.0 from Call_Any
DQLAgent won 95.5 from Raise_Any
DQLAgent won 81.0 from Random
DQLAgent won 85.9 from Simple_Rational84
