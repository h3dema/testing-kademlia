# testing-kademlia

Install and run
```bash
docker build -t /kademlia github.com/h3dema/kademlia.docker
docker run -w /kademlia -it kademlia
```

# Running an example

We need to open 3 docker containers to simulate a network with 3 nodes: 
* two nodes will be servers (*s1* and *s2*) and 
* one node will do the search (*q*) and populate the hash table.

We have to modify the examples/server.tac file so that the server nodes know each other. 
In *s1* file we put the *s2*'s ip address, and vice versa.
Suppose that our addresses are 172.167.0.1, 172.167.0.2 and 172.167.0.3 corresponding to *s1*, *s2*, and *q*.

The populate.py program we provide inside /kademlia directory adds 50 (key, value) pairs in the distributed hash.

``` bash
python populate.py --server=172.167.0.1
```

Then we can query one of these keys.
We can now use the query.py program to request a value based on the key.
For example, let's query the key = 1.

``` bash
python examples/query.py 172.17.0.60 8468 1
```


# Source and documentation

The source is find [here](https://github.com/bmuller/kademlia).
The documentation is [in the readthedocs](http://kademlia.readthedocs.io/en/latest/index.html).
