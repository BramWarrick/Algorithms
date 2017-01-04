# Question 3 - Udacity specs
# Given an undirected graph G, find the minimum spanning tree within G. A
# minimum spanning tree connects all vertices in a graph with the smallest
# possible total weight of edges. Your function should take in and return
# an adjacency list structured like this:

# {'A': [('B', 2)],
# 'B': [('A', 2), ('C', 5)],
# 'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition
# should be question3(G)


from operator import itemgetter


def question3(G):
    edges, vertices = question3_load_edges(G)

    # Sort edges ascending by weight, placed into list
    # http://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
    edges_sorted = sorted(edges, key=itemgetter(0))
    return question3_connect_vertices(edges_sorted, vertices)


def question3_load_edges(G):
    edges = []
    vertices = {}
    # Receive vertices and edges
    for start_v in G:
        # Seed vertex into itself as entry in dictionary
        vertices[start_v] = [start_v]
        for edge in G[start_v]:
            stop_v = edge[0]
            weight = edge[1]
            edges.append([weight, start_v, stop_v])
    return edges, vertices


def question3_connect_vertices(edges_sorted, vertices):
    mst = {}
    for edge in edges_sorted:
        start_v, stop_v, weight = edge[1], edge[2], edge[0]
        if start_v not in vertices[stop_v] and stop_v not in vertices[start_v]:
            # Create edge for both vertices, if not present default with []
            mst.setdefault(start_v, []).append((stop_v, str(weight)))
            mst.setdefault(stop_v, []).append((start_v, str(weight)))
            # Update list of connected vertices for each vertex
            vertices[start_v], vertices[stop_v] = question3_concat_list(
                vertices[start_v], vertices[stop_v])
    return mst


def question3_concat_list(list1, list2):
    result = list1 + list(set(list2) - set(list1))
    return result, result


print "Question 3 Tests"
print question3({'A': [('B', 2)],
                 'B': [('A', 2), ('C', 5)],
                 'C': [('B', 5)]})
print "Expected output 1:"
print "{'A': [('B', '2')], 'C': [('B', '5')], 'B': [('A', '2'), ('C', '5')]}"
print "Actual output 1:"
print question3({'A': [('B', 2)],
                 'B': [('A', 2), ('C', 5), ('D', 1)],
                 'C': [('B', 5), ('D', 2)],
                 'D': [('C', 2), ('B', 1)]})
print "Expected output 2:"
"{'A': [('B', '2')], 'C': [('D', '2')], 'B': [('D', '1'), ('A', '2')], 'D': [('B', '1'), ('C', '2')]}"
print "Actual output 2:"
print "Actual output 3:"
print question3({'A': [('B', 2)],
                 'B': [('A', 2), ('C', 5), ('D', 5)],
                 'C': [('B', 5), ('D', 2)],
                 'D': [('C', 2), ('B', 5)]})
print "Expected output 3:"
print "{'A': [('B', '2')], 'C': [('D', '2'), ('B', '5')], 'B': [('A', '2'), ('C', '5')], 'D': [('C', '2')]}"
print "Actual output 4:"
print question3({})
print "Expected output 4:"
print "{}"
print "Actual output 5:"
print question3({'A': [('B', 2)],
                 'B': [('A', 2), ('C', 5), ('D', 5)],
                 'C': [('B', 5), ('D', 2)],
                 'D': [('C', 2), ('B', 5)],
                 'E': []})
print "Expected output 5:"
print "{'A': [('B', '2')], 'C': [('D', '2'), ('B', '5')], 'B': [('A', '2'), ('C', '5')], 'D': [('C', '2')]}"
print "Actual output 6:"
print question3({'A': [('B', 2)],
                 'B': [('A', 2), ('C', 5), ('D', 5)],
                 'C': [('B', 5), ('D', 2)],
                 'D': [('C', 2), ('B', 5)],
                 'E': [('F', 10)],
                 'F': [('E', 10)]})
print "Expected output 6:"
print "{'A': [('B', '2')], 'C': [('D', '2'), ('B', '5')], 'B': [('A', '2'), ('C', '5')], 'E': [('F', '10')], 'D': [('C', '2')], 'F': [('E', '10')]}"

# Question 3 Commentary

# Efficiency:
# Tree (build): O(2n), simplifying to O(n) - where n is the number of edges
# The above is 2n because each edge is stated twice in the adjacency list.

# Find MST (worst): O(2n) - where n is the number of edges
# Find MST (best): O(v-1) - where v is the number of vertices

# Efficiency Design:
# By sorting the edges based on weight, I avoided a lot of the overhead of a
# vertex radiating style of solution I initially favored. The math became
# cleaner and the comparisons are intuitive. I'm assuming smaller graphs
# or sufficient memory to accomomodate this process, but it didn't seem
# unreasonable based on the spec.

# Process:
# At first I considered radiating out from an arbitrary vertex, tracking the
# total "cost" of reaching another vertex. Ultimately it seemed if the shortest
# path is always preferred, then sorting the edges could be a more direct
# solution.

# The function imports all edges and vertices and then sorts the edges
# ascending by weight.

# Evaluations:
# Each vertex is given an key value entry in the vertices dictionary. Each
# vertex has, as a list, all vertices that are linked to it at that point
# in the algorithm's process.

# As the algorithm evaluates each edge, it looks at each of the vertices on
# the edge. If both vertices do not reflect a connection to the other vertex,
# then a new edge is added to the MST and the vertices are updated to reflect
# their connection. This update takes the full list of connected vertices for
# A and the full list of connected vertices for B, concatenates them without
# duplicates and passes that updated list into each on the dictionary.

# Addt'l Note:
# This function can work even when there are >1 /different/ graphs submitted,
# or an unconnected vertex - it will always only return vertices: [edges] when
# there is a connection. The edges for multiple graphs can be returned as long
# as each graph has connected vertices.
