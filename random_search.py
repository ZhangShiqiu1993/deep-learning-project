from gym import wrappers
import gym
import numpy as np
import matplotlib.pyplot as plt

def get_action(s, w):
    return 1 if s.dot(w) > 0 else 0

def play_one_episode(env, params, show = False):
    observation = env.reset()
    done = False
    t = 0

    while not done and t < 200:
        if show:
            env.render()
        t += 1
        action = get_action(observation, params)
        observation, reward, done, info = env.step(action)
        if done:
            break
    return t

def play_multiple_episodes(env, T, params, show = False):
    episode_lengths = np.empty(T)
    for i in range(T):
        episode_lengths[i] = play_one_episode(env, params, show)

    avg_length = episode_lengths.mean()
    print("avg length: ", avg_length)
    return avg_length

def random_search(env):
    episode_lengths = []
    best = 0
    params = None
    for t in range(100):
        new_params = np.random.random(4) * 2 - 1
        avg_length = play_multiple_episodes(env, 100, new_params)
        episode_lengths.append(avg_length)

        if avg_length > best:
            params = new_params
            best = avg_length
    return episode_lengths, params

def main():
    env = gym.make('CartPole-v0')
    episode_lengths, params = random_search(env)
    plt.plot(episode_lengths)
    plt.show()

    print("***Final run with final weights**")
    env = wrappers.Monitor(env, 'videos')
    play_multiple_episodes(env, 100, params, False)

if __name__ == '__main__':
    main()
