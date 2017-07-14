import numpy as n
import matplotlib.pyplot as p
fig = p.Figure()
ax=p.axes()


def plot_graph(hash_tags,count):

    x=range(1,len(hash_tags)+1)   # a list of x-coordinates
    y = count                     # A list of y,co-ordinates
    m = n.max(count)              # Max no of count(list)

    # counting total digit's place in Max'
    i=0
    while (m/10)!=0:
        m=m/10
        i=i+1

    m=n.max(count)    # Re-initialize max for further operations

    p.xlim(0,len(hash_tags)+1)   # Limiting the length of x-axis
    p.ylim(0,m+(10**(i-1)))      # Limiting length of y-axis
    p.title("Popularity analysis of hash_tags")  # Title of the plot
    p.xlabel('(Hash_tags)')                      # Label shown along x-axis
    p.ylabel('(No of images shared)*%d' % 10**i) # Label shown along y-axis
    p.xticks(range(1,len(hash_tags)+1),hash_tags)# Setting the ticks of x-axis
    p.yticks(n.linspace(0,m+(10**(i-1)),10))     # Setting ticks of y-axis
    p.plot(x,y,'or')                             # Plot red dots on (x,y) pts
    p.plot(x,y,'green')                          # Plot line along the (x,y) pts

    # Can be thought of as the scale
    p.legend(['red points : No of shares\nPopular hash_tag :"%s"' % hash_tags[count.index(m)]])
    for i,txt in enumerate(count):
        p.annotate(" [%d] "%txt,(x[i],count[i]))  # Marking all (x,y) pts on the plot
    p.show()




