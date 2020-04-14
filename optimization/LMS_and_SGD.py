import numpy as np
import matplotlib.pyplot as plt

def SGD(step_size=0.01, epoch=2048, batch_size=32): # SGD algorithm
    u, w1, w2, e, v = init_variables(epoch)
    index = 0
    total_e = np.zeros(epoch)
    for n in range(epoch):
        if batch_size * index == epoch:
            index = 0
        sum1, sum2, error = 0, 0, 0
        for i in range(index*batch_size, (index+1)*batch_size):
            u[i] = (0.99 * u[i-1]) + (-0.99 * u[i-2]) + v[i]
            y = w1[n-1] * u[i-1] + w2[n-1] * u[i-2] # estimated signal
            e[i] = u[i] - y
            error += e[i]
            sum1 += u[i-1] * e[i]
            sum2 += u[i-2] * e[i]
        index += 1

        total_e[n] = error / batch_size
        expect1 = sum1 / batch_size
        expect2 = sum2 / batch_size
        w1[n] = w1[n-1] + step_size * expect1
        w2[n] = w2[n-1] + step_size * expect2
    plot_result(w1, w2, total_e, "SGD")

def LMS(step_size=0.01, epoch=2048): # LMS algorithm
    u, w1, w2, e, v = init_variables(epoch)
    for n in range(epoch):
        u[n] = (0.99 * u[n-1]) + (-0.99 * u[n-2]) + v[n]
        y = w1[n-1] * u[n-1] + w2[n-1] * u[n-2]
        e[n] = u[n] - y
        w1[n] = w1[n-1] + step_size * u[n-1] * e[n]
        w2[n] = w2[n-1] + step_size * u[n-2] * e[n]
    plot_input(u)
    plot_result(w1, w2, e, "LMS")

def init_variables(epoch): # create and initialize variables
    u = np.zeros(epoch)  # input, desired signals
    w1 = np.zeros(epoch) # weight1
    w2 = np.zeros(epoch) # weight2
    e = np.zeros(epoch)  # error
    v = np.random.normal(0, 0.5**0.5, epoch) # white Gaussian noise
    return u, w1, w2, e, v

def plot_input(u): # plot input signals
    params = {'legend.fontsize': '16',
              'figure.figsize': (20, 10),
              'axes.labelsize': '16',
              'axes.titlesize': '16',
              'xtick.labelsize': '16',
              'ytick.labelsize': '16',
              'axes.grid': True}
    plt.rcParams.update(params)

    # plot inputs
    plt.plot(u)
    plt.xlabel('n')
    plt.ylabel('u[n]')
    plt.title('input signals')
    plt.savefig('input')
    plt.show()

def plot_result(w1, w2, e, algorithm): # plot results
    # plot weights
    plt.plot(w1)
    plt.plot(w2)
    plt.xlabel('Iteration time n')
    plt.ylabel('w1 & w2')
    plt.title(algorithm)
    plt.legend(['w1', 'w2'])
    plt.savefig(algorithm + '_weights')
    plt.show()

    # plot error(loss)
    plt.plot(abs(e))
    plt.xlabel('Iteration time n')
    plt.ylabel('error')
    plt.title(algorithm)
    plt.savefig(algorithm + '_error')
    plt.show()

if __name__ == "__main__":
    LMS()
    SGD()