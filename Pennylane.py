'''import pennylane as qml
import jax.numpy as jnp
import jax

# Set number of wires
num_wires = 28

# Set a random seed
key = jax.random.PRNGKey(0)

dev = qml.device("lightning.gpu",wires = num_wires)



'''
import pennylane as qml
import numpy as np
import jaxlib

dev1 = qml.device("lightning.qubit", wires = 1)

def circuit(params) :
    qml.RX(params[0],wires = 0)
    qml.RX(params[1],wires = 0)
    return qml.expval(qml.PauliZ(0))

