# ComplexDuals

The special euclidean group SE(2) is the set of  all translations and rotations in the plane. 
Rotations in the plane SO(2), is the set of 2D rotations and can be represented by unit complex numbers
Translations in the plane T(2) can be represented by Dual numbers (a + b epsilon)
One would think that simply connecting the two to make complex duals of the form (C1 + C2 epsilon ) would represent SE(2)
However the system cannot accurately represent the transforms because its commutative
So Genki Matsuda, Shizuo Kaji, and Hiroyuki Ochiai in the paper "ANTI-COMMUTATIVE DUAL COMPLEX NUMBERSAND 2D RIGID TRANSFORMATION" https://arxiv.org/pdf/1601.01754.pdf,
developed the anti-commutative dual complex numbers. These can represent rotations, translation and combinations of the two. 

Here the ACDuals are a pure python class which can represent these numbers. You use the @ symbol to apply them to a ACDual that represents a point and use \* to compose them


