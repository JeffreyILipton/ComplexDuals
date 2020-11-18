from math import *

class ACDual:
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual

    def __toDual(self,other):
        if isinstance(other, ACDual): return other
        return ACDual(other,0)
        
    def __add__(self, other1):
        other = self.__toDual(other1)
        return ACDual(self.real + other.real,
                          self.dual + other.dual)
    __radd__ = __add__

    def __sub__(self, other1):
        other = self.__toDual(other1)
        return ACDual(self.real - other.real,
                          self.dual - other.dual)

    def __rsub__(self, other1):
        other = self.__toDual(other1)
        return ACDual(other, 0) - self
		
    def __truediv__(self, other1):
        other = self.__toDual(other1)
        return ACDual(self.real/other.real,
                          (self.dual*other.real - self.real*other.dual)/(other.real**2))

    def __rtruediv__(self, other1):
        other = self.__toDual(other1)
        return other/self

    def __pow__(self, other):
        return ACDual(self.real**other,
                          self.dual * other * self.real**(other - 1))

    def involution(self):
        return ACDual(self.real.conjugate(),self.dual)
    
    def __mul__(self, other1):
        other = self.__toDual(other1)
        return ACDual(self.real * other.real,
                      self.dual * other.real.conjugate() + self.real * other.dual)
    __rmul__ = __mul__
    
    def mag(self):
        return np.sqrt(self.real*self.real.conjugate())
    
    def __matmul__(self,other):
        return self*other*self.involution()
    
    def __rmatmul(self,other):
        return other*self*other.involution()
    
    def __repr__(self):
        return repr(self.real) + ' + ' + repr(self.dual) + '*'+'\u03B5'
        

def cdToPt(cd):
    C = cd.dual
    return np.array([C.real,C.imag])

def ptToCd(pt):
    C = pt[0]+pt[1]*complex('j')
    return ACDual(complex(1.0),C)

def CDRotateAngle(theta):
    c = cos(theta/2)
    s = sin(theta/2)
    return ACDual(c+s*complex('j'),0)

def CDTranslate(D):
    return ACDual(complex(1.0),D[0]/2+D[1]/2*complex('j'))
	
def CDRotateAroundPoint(theta,D):
    d = np.array(D)
    T = CDTranslate(d)
    Tinv = CDTranslate(-d)
    R = CDRotateAngle(theta)
    return T*R*Tinv