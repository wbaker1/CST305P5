import numpy as np
import matplotlib.pyplot as plt

while True == True:
    rInput = int(input("Enter value for r: "))
    def lorenz(x, y, z, s=10, r=rInput, b=8/3):
        '''
        Given:
        x, y, z: a point of interest in three dimensional space
        s, r, b: parameters defining the lorenz attractor
        Returns:
        x_dot, y_dot, z_dot: values of the lorenz attractor's partial
            derivatives at the point x, y, z
        '''
        x_dot = s*(y - x)
        y_dot = r*x - y - x*z
        z_dot = x*y - b*z
        return x_dot, y_dot, z_dot


    dt = 0.01
    num_steps = 10000

    # Need one more for the initial values
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Set initial values
    xs[0], ys[0], zs[0] = (11.8, 4.4, 2.4)

    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)


    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz - r: " + str(rInput))

    plt.show()


    # time points
    t = np.linspace(0,100,num_steps+1)


    #################################################################
    # plot results for 2D
    plt.plot(t,xs,'b-', label='x(t)')

    # label neccessary info on graph
    plt.title('x(t) [JPG] - r: ' + str(rInput))
    plt.xlabel('t')
    plt.ylabel('X - JPG')
    plt.legend()
    # Display the graph
    plt.show()
    #################################################################

    #################################################################
    # plot results for 2D
    plt.plot(t,ys,'b-', label='y(t)')

    # label neccessary info on graph
    plt.title('y(t) [PNG] - r: ' + str(rInput))
    plt.xlabel('t')
    plt.ylabel('Y - PNG')
    plt.legend()
    # Display the graph
    plt.show()
    #################################################################

    #################################################################
    # plot results for 2D
    plt.plot(t,zs,'b-', label='z(t)')

    # label neccessary info on graph
    plt.title('z(t) [GIF] - r: ' + str(rInput))
    plt.xlabel('t')
    plt.ylabel('Z - GIF')
    plt.legend()
    # Display the graph
    plt.show()
    #################################################################
    userExit = input("Enter y to exit: ")
    if userExit == "y":
        break
    else:
        continue


        