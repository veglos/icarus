# 2026-10-13

* By Claude's instructions, I'm writing the Karpathy's Value python class without looking at the video or the github code. I can't remember what _prev was, but I do remember _op.
* _prev was the set of previous nodes. had troubles trying to work with python sets.

# 2026-10-14

* I got stuck understanding what grad means, and why even need to derivate.

# 2026-10-18

* I understand now! After many conversations with claude and watching some youtube videos I think I finally get it. The function d = a*b + c is a very simple toy function in order to understand how to calculate the sensitivity of the inputs. For example, how sensitive is the output d if we change the input a by a tiny amount (say, 0.0001) while keeping the inputs b and c fixed. This is the rate of change of d according to a, also known as the partial derivative of d with respect to a, or ∂d/∂a. Then, we also want ∂d/∂b and ∂d/∂c.

In english, if we nudge a by a very small amount, 0.000001, what is the rate of change of d? That is all. 

In a neural network, d is the loss value (result of the loss function -how off the output is from the expected result-), and a,b and c play the role of the weights (to be seen later). The derivative tells us which way to nudge the weights in order to reduce the loss, and thus train the model.

# 2026-10-28

After watching Karpathy's video completely, claude told me to write the rest of the Value class by memory. I managed most of it, googling derivatives, except that I forgot that the tanh was imported from the math library.
