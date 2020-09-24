### efficiently-exploring-systembolaget

What is the most efficient strategy for maximizing pleasure when buying alcohol at Systembolaget? In this repo we plan to implement an epsilon-greedy algorithm for choosing how to explore the rather large state space that is Systembolaget's assortment. We use a [python wrapper](https://github.com/claha/pysystembolaget) for the Systembolaget API to fetch the products available at a given store in a given category and their descriptions. 

### TODO

The actual epsilon-greedy algorithm.

Derive the optimal rule for updating epsilon.

Incorporate some sort of prior?

Continue tweaking **get_products_from_systembolaget.py**, e.g. one could be able to choose some price range.

