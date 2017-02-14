import numpy as np
from matplotlib import pyplot as plt

import plotly.graph_objs as go

def generate_z(n, d):
    return np.random.uniform(low=-1.0, high=1.0, size=(n, d))

def generate_y(n):
    y = np.zeros((n, 10))
    y[range(n),[i%10 for i in range(n)]] = 1
    return y

def square_plot(data):
    """Take an array of shape (n, height, width) or (n, height, width , 3)
       and visualize each (height, width) thing in a grid of size approx. sqrt(n) by sqrt(n)"""

    if type(data) == list:
	    data = np.concatenate(data)
    # normalize data for display
    data = (data - data.min()) / (data.max() - data.min())

    # force the number of filters to be square
    n = int(np.ceil(np.sqrt(data.shape[0])))

    padding = (((0, n ** 2 - data.shape[0]) ,
                (0, 1), (0, 1))  # add some space between filters
               + ((0, 0),) * (data.ndim - 3))  # don't pad the last dimension (if there is one)
    data = np.pad(data , padding, mode='constant' , constant_values=1)  # pad with ones (white)

    # tilethe filters into an image
    data = data.reshape((n , n) + data.shape[1:]).transpose((0 , 2 , 1 , 3) + tuple(range(4 , data.ndim + 1)))

    data = data.reshape((n * data.shape[1] , n * data.shape[3]) + data.shape[4:])

    plt.figure(figsize=(17, 17))
    plt.imshow(data[:,:,0], cmap='gray')
    plt.axis('off')

def interactive_plot(data1, data2, data1_name='data1', data2_name='data2'):

	# Create traces
	trace0 = go.Scatter(
	    y = data1,
	    mode = 'lines+markers',
	    name = data1_name
	)
	trace1 = go.Scatter(
	    y = data2,
	    mode = 'lines+markers',
	    name = data2_name
	)
	data = [trace0, trace1]
	return data