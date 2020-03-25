# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError

def shortest_path(graph, source, target):
  # `graph` is an object that provides a get_neighbors(node) method that returns
  # a list of (node, weight) edges. both of your graph implementations should be
  # valid inputs. you may assume that the input graph is connected, and that all
  # edges in the graph have positive edge weights.
  # 
  # `source` and `target` are both nodes in the input graph. you may assume that
  # at least one path exists from the source node to the target node.
  #
  # this method should return a tuple that looks like
  # ([`source`, ..., `target`], `length`), where the first element is a list of
  # nodes representing the shortest path from the source to the target (in
  # order) and the second element is the length of that path
  #
  # NOTE: Please see instructions.txt for additional information about the
  # return value of this method.

  # TODO: YOUR CODE HERE, delete the `raise NotImplementedError`line below once you finish writing your code


  seen = [source]
  shortest = {
    source: 0
  }
  path = {
    source: [source]
  }
  unvisited = [source]

  node = source

  while (node != target):

    unvisited.remove(node)
    for neighbor in graph.get_neighbors(node):
      if neighbor[0] in seen: #if we have seen it then check if we found shorter path or not
        if (shortest[node] + neighbor[1] < shortest[neighbor[0]]):
          shortest[neighbor[0]] = shortest[node] + neighbor[1]
          path[neighbor[0]] = path[node] + [neighbor[0]] #update the shortest path for the node
      else: #havent seen the node before
        shortest[neighbor[0]] = neighbor[1] + shortest[node]
        seen.append(neighbor[0])
        path[neighbor[0]] = path[node]+[neighbor[0]]
        unvisited.append(neighbor[0])

    #choose the minimum unvisted node next

    minVal = shortest[unvisited[0]]
    minNode = unvisited[0]
    for n in unvisited:
      if minVal > shortest[n]:
        minVal = shortest[n]
        minNode = n

    node = minNode

  return (path[target], shortest[target])