# testing-kademlia

Install and run
```bash
docker build -t /kademlia github.com/h3dema/kademlia.docker
docker run -w /kademlia -it kademlia
```

# Running an example

vamos abrir 3 conexões docker para simular uma rede com 3 nós.
2 nós serão servidores (s1 e s2) e 1 nó fará as pesquisas (q).

temos que modificar o arquivo examples/server.tac para que os nós servidores saibam um do outro.
assim em s1 colocamos o endereco ip de s2 e vice-versa.

o programa populate.py que fornecemos acrescenta 50 valores (key,value) no hash distribuído.

``` bash
python populate.py --server=172.167.0.1
```

agora podemos utilizar o programa query.py para solicitar um valor baseado na chave.

``` bash
python examples/query.py 172.17.0.60 8468 1
```


# Source and documentation

The source is find [here](https://github.com/bmuller/kademlia).
The documentation is [in the readthedocs](http://kademlia.readthedocs.io/en/latest/index.html).
