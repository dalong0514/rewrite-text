### 05. Neural Nets

OK, so how do our typical models for tasks like image recognition actually work? The most popular—and successful—current approach uses neural nets. Invented—in a form remarkably close to their use today—in the 1940s, neural nets can be thought of as simple idealizations of how brains seem to work.

In human brains there are about 100 billion neurons (nerve cells), each capable of producing an electrical pulse up to perhaps a thousand times a second. The neurons are connected in a complicated net, with each neuron having tree-like branches allowing it to pass electrical signals to perhaps thousands of other neurons. And in a rough approximation, whether any given neuron produces an electrical pulse at a given moment depends on what pulses it's received from other neurons—with different connections contributing with different "weights".

When we "see an image" what's happening is that when photons of light from the image fall on ("photoreceptor") cells at the back of our eyes they produce electrical signals in nerve cells. These nerve cells are connected to other nerve cells, and eventually the signals go through a whole sequence of layers of neurons. And it's in this process that we "recognize" the image, eventually "forming the thought" that we're "seeing a 2" (and maybe in the end doing something like saying the word "two" out loud).

The "black-box" function from the previous section is a "mathematicized" version of such a neural net. It happens to have 11 layers (though only 4 "core layers"):

There's nothing particularly "theoretically derived" about this neural net; it's just something that—back in 1998—was constructed as a piece of engineering, and found to work. (Of course, that's not much different from how we might describe our brains as having been produced through the process of biological evolution.)

OK, but how does a neural net like this "recognize things"? The key is the notion of attractors. Imagine we've got handwritten images of 1's and 2's:

We somehow want all the 1's to "be attracted to one place", and all the 2's to "be attracted to another place". Or, put a different way, if an image is somehow "closer to being a 1" than to being a 2, we want it to end up in the "1 place" and vice versa.

As a straightforward analogy, let's say we have certain positions in the plane, indicated by dots (in a real-life setting they might be positions of coffee shops). Then we might imagine that starting from any point on the plane we'd always want to end up at the closest dot (i.e. we'd always go to the closest coffee shop). We can represent this by dividing the plane into regions ("attractor basins") separated by idealized "watersheds":

We can think of this as implementing a kind of "recognition task" in which we're not doing something like identifying what digit a given image "looks most like"—but rather we're just, quite directly, seeing what dot a given point is closest to. (The "Voronoi diagram" setup we're showing here separates points in 2D Euclidean space; the digit recognition task can be thought of as doing something very similar—but in a 784-dimensional space formed from the gray levels of all the pixels in each image.)

So how do we make a neural net "do a recognition task"? Let's consider this very simple case:

Our goal is to take an "input" corresponding to a position {x,y}—and then to "recognize" it as whichever of the three points it's closest to. Or, in other words, we want the neural net to compute a function of {x,y} like:

So how do we do this with a neural net? Ultimately a neural net is a connected collection of idealized "neurons"—usually arranged in layers—with a simple example being:

Each "neuron" is effectively set up to evaluate a simple numerical function. And to "use" the network, we simply feed numbers (like our coordinates x and y) in at the top, then have neurons on each layer "evaluate their functions" and feed the results forward through the network—eventually producing the final result at the bottom:

In the traditional (biologically inspired) setup each neuron effectively has a certain set of "incoming connections" from the neurons on the previous layer, with each connection being assigned a certain "weight" (which can be a positive or negative number). The value of a given neuron is determined by multiplying the values of "previous neurons" by their corresponding weights, then adding these up and adding a constant—and finally applying a "thresholding" (or "activation") function. In mathematical terms, if a neuron has inputs x = {x1, x2 …} then we compute f[w . x + b], where the weights w and constant b are generally chosen differently for each neuron in the network; the function f is usually the same.

Computing w . x + b is just a matter of matrix multiplication and addition. The "activation function" f introduces nonlinearity (and ultimately is what leads to nontrivial behavior). Various activation functions commonly get used; here we'll just use Ramp (or ReLU):

For each task we want the neural net to perform (or, equivalently, for each overall function we want it to evaluate) we'll have different choices of weights. (And—as we'll discuss later—these weights are normally determined by "training" the neural net using machine learning from examples of the outputs we want.)

Ultimately, every neural net just corresponds to some overall mathematical function—though it may be messy to write out. For the example above, it would be:

The neural net of ChatGPT also just corresponds to a mathematical function like this—but effectively with billions of terms.

But let's go back to individual neurons. Here are some examples of the functions a neuron with two inputs (representing coordinates x and y) can compute with various choices of weights and constants (and Ramp as activation function):

But what about the larger network from above? Well, here's what it computes:

It's not quite "right", but it's close to the "nearest point" function we showed above.

Let's see what happens with some other neural nets. In each case, as we'll explain later, we're using machine learning to find the best choice of weights. Then we're showing here what the neural net with those weights computes:

Bigger networks generally do better at approximating the function we're aiming for. And in the "middle of each attractor basin" we typically get exactly the answer we want. But at the boundaries—where the neural net "has a hard time making up its mind"—things can be messier.

With this simple mathematical-style "recognition task" it's clear what the "right answer" is. But in the problem of recognizing handwritten digits, it's not so clear. What if someone wrote a "2" so badly it looked like a "7", etc.? Still, we can ask how a neural net distinguishes digits—and this gives an indication:

Can we say "mathematically" how the network makes its distinctions? Not really. It's just "doing what the neural net does". But it turns out that that normally seems to agree fairly well with the distinctions we humans make.

Let's take a more elaborate example. Let's say we have images of cats and dogs. And we have a neural net that's been trained to distinguish them. Here's what it might do on some examples:

Now it's even less clear what the "right answer" is. What about a dog dressed in a cat suit? Etc. Whatever input it's given the neural net will generate an answer, and in a way reasonably consistent with how humans might. As I've said above, that's not a fact we can "derive from first principles". It's just something that's empirically been found to be true, at least in certain domains. But it's a key reason why neural nets are useful: that they somehow capture a "human-like" way of doing things.

Show yourself a picture of a cat, and ask "Why is that a cat?". Maybe you'd start saying "Well, I see its pointy ears, etc." But it's not very easy to explain how you recognized the image as a cat. It's just that somehow your brain figured that out. But for a brain there's no way (at least yet) to "go inside" and see how it figured it out. What about for an (artificial) neural net? Well, it's straightforward to see what each "neuron" does when you show a picture of a cat. But even to get a basic visualization is usually very difficult.

In the final net that we used for the "nearest point" problem above there are 17 neurons. In the net for recognizing handwritten digits there are 2190. And in the net we're using to recognize cats and dogs there are 60,650. Normally it would be pretty difficult to visualize what amounts to 60,650-dimensional space. But because this is a network set up to deal with images, many of its layers of neurons are organized into arrays, like the arrays of pixels it's looking at.

And if we take a typical cat image

Cat

then we can represent the states of neurons at the first layer by a collection of derived images—many of which we can readily interpret as being things like "the cat without its background", or "the outline of the cat":

By the 10th layer it's harder to interpret what's going on:

But in general we might say that the neural net is "picking out certain features" (maybe pointy ears are among them), and using these to determine what the image is of. But are those features ones for which we have names—like "pointy ears"? Mostly not.

Are our brains using similar features? Mostly we don't know. But it's notable that the first few layers of a neural net like the one we're showing here seem to pick out aspects of images (like edges of objects) that seem to be similar to ones we know are picked out by the first level of visual processing in brains.

But let's say we want a "theory of cat recognition" in neural nets. We can say: "Look, this particular net does it"—and immediately that gives us some sense of "how hard a problem" it is (and, for example, how many neurons or layers might be needed). But at least as of now we don't have a way to "give a narrative description" of what the network is doing. And maybe that's because it truly is computationally irreducible, and there's no general way to find what it does except by explicitly tracing each step. Or maybe it's just that we haven't "figured out the science", and identified the "natural laws" that allow us to summarize what's going on.

We'll encounter the same kinds of issues when we talk about generating language with ChatGPT. And again it's not clear whether there are ways to "summarize what it's doing". But the richness and detail of language (and our experience with it) may allow us to get further than with images.

### 06. Machine Learning, and the Training of Neural Nets

We've been talking so far about neural nets that "already know" how to do particular tasks. But what makes neural nets so useful (presumably also in brains) is that not only can they in principle do all sorts of tasks, but they can be incrementally "trained from examples" to do those tasks.

When we make a neural net to distinguish cats from dogs we don't effectively have to write a program that (say) explicitly finds whiskers; instead we just show lots of examples of what's a cat and what's a dog, and then have the network "machine learn" from these how to distinguish them.

And the point is that the trained network "generalizes" from the particular examples it's shown. Just as we've seen above, it isn't simply that the network recognizes the particular pixel pattern of an example cat image it was shown; rather it's that the neural net somehow manages to distinguish images on the basis of what we consider to be some kind of "general catness".

So how does neural net training actually work? Essentially what we're always trying to do is to find weights that make the neural net successfully reproduce the examples we've given. And then we're relying on the neural net to "interpolate" (or "generalize") "between" these examples in a "reasonable" way.

Let's look at a problem even simpler than the nearest-point one above. Let's just try to get a neural net to learn the function:

For this task, we'll need a network that has just one input and one output, like:

But what weights, etc. should we be using? With every possible set of weights the neural net will compute some function. And, for example, here's what it does with a few randomly chosen sets of weights:

And, yes, we can plainly see that in none of these cases does it get even close to reproducing the function we want. So how do we find weights that will reproduce the function?

The basic idea is to supply lots of "input → output" examples to "learn from"—and then to try to find weights that will reproduce these examples. Here's the result of doing that with progressively more examples:

At each stage in this "training" the weights in the network are progressively adjusted—and we see that eventually we get a network that successfully reproduces the function we want. So how do we adjust the weights? The basic idea is at each stage to see "how far away we are" from getting the function we want—and then to update the weights in such a way as to get closer.

To find out "how far away we are" we compute what's usually called a "loss function" (or sometimes "cost function"). Here we're using a simple (L2) loss function that's just the sum of the squares of the differences between the values we get, and the true values. And what we see is that as our training process progresses, the loss function progressively decreases (following a certain "learning curve" that's different for different tasks)—until we reach a point where the network (at least to a good approximation) successfully reproduces the function we want:

Alright, so the last essential piece to explain is how the weights are adjusted to reduce the loss function. As we've said, the loss function gives us a "distance" between the values we've got, and the true values. But the "values we've got" are determined at each stage by the current version of neural net—and by the weights in it. But now imagine that the weights are variables—say wi. We want to find out how to adjust the values of these variables to minimize the loss that depends on them.

For example, imagine (in an incredible simplification of typical neural nets used in practice) that we have just two weights w1 and w2. Then we might have a loss that as a function of w1 and w2 looks like this:

Numerical analysis provides a variety of techniques for finding the minimum in cases like this. But a typical approach is just to progressively follow the path of steepest descent from whatever previous w1, w2 we had:

Like water flowing down a mountain, all that's guaranteed is that this procedure will end up at some local minimum of the surface ("a mountain lake"); it might well not reach the ultimate global minimum.

It's not obvious that it would be feasible to find the path of the steepest descent on the "weight landscape". But calculus comes to the rescue. As we mentioned above, one can always think of a neural net as computing a mathematical function—that depends on its inputs, and its weights. But now consider differentiating with respect to these weights. It turns out that the chain rule of calculus in effect lets us "unravel" the operations done by successive layers in the neural net. And the result is that we can—at least in some local approximation—"invert" the operation of the neural net, and progressively find weights that minimize the loss associated with the output.

The picture above shows the kind of minimization we might need to do in the unrealistically simple case of just 2 weights. But it turns out that even with many more weights (ChatGPT uses 175 billion) it's still possible to do the minimization, at least to some level of approximation. And in fact the big breakthrough in "deep learning" that occurred around 2011 was associated with the discovery that in some sense it can be easier to do (at least approximate) minimization when there are lots of weights involved than when there are fairly few.

In other words—somewhat counterintuitively—it can be easier to solve more complicated problems with neural nets than simpler ones. And the rough reason for this seems to be that when one has a lot of "weight variables" one has a high-dimensional space with "lots of different directions" that can lead one to the minimum—whereas with fewer variables it's easier to end up getting stuck in a local minimum ("mountain lake") from which there's no "direction to get out".

It's worth pointing out that in typical cases there are many different collections of weights that will all give neural nets that have pretty much the same performance. And usually in practical neural net training there are lots of random choices made—that lead to "different-but-equivalent solutions", like these:

But each such "different solution" will have at least slightly different behavior. And if we ask, say, for an "extrapolation" outside the region where we gave training examples, we can get dramatically different results:

But which of these is "right"? There's really no way to say. They're all "consistent with the observed data". But they all correspond to different "innate" ways to "think about" what to do "outside the box". And some may seem "more reasonable" to us humans than others.
