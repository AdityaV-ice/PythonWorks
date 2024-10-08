import numpy as np
inputNeurons=2
hiddenlayerNeurons=2
outputNeurons=2

input=np.random.randint(1,10,size=(1,inputNeurons))
output=np.array([1.0,0.0])

hidden_weights=np.random.normal(scale=0.5,size=(inputNeurons,hiddenlayerNeurons))
output_weights=np.random.normal(scale=0.5,size=(hiddenlayerNeurons,outputNeurons))

def sigmoid(layer):
    return 1/(1+np.exp(-layer))

def gradient(layer):
    return layer*1-layer

for i in range(5):
    L1in=np.dot(input,hidden_weights)
    L1out=sigmoid(L1in)

    L2in=np.dot(L1out,output_weights)
    L2out=sigmoid(L2in)

    error=(L2out-output)
    gradient_L2=gradient(L2out)
    error_terms_L2=error*gradient_L2

    error=np.dot(error_terms_L2,output_weights.T)
    gradient_L1=gradient(L1out)
    error_terms_L1=error*gradient_L1

    gradient_output_weights=np.dot(L1out.T,error_terms_L2)
    gradient_hidden_weights=np.dot(input.T,error_terms_L1)

    hidden_weights=hidden_weights-0.1*gradient_hidden_weights
    output_weights=output_weights-0.1*gradient_output_weights

    print("*****************")
    print("<iteration>:",i,"<error>:",error)
    print("               <output>:",L2out)
