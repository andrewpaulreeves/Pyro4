import Pyro

proxy=Pyro.core.Proxy("PYRONAME:example.embedded.server")
print("5*11=%d" % proxy.multiply(5,11))
print("'x'*10=%s" % proxy.multiply('x',10))
