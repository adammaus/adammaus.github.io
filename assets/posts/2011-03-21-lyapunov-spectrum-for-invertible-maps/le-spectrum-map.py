# Program le-spectrum.py calculates the spectrum of LEs for the Henon map
# Adapted from
# http://sprott.physics.wisc.edu/chaos/wolfmap.bas

def derivs(x, xnew, n):
    return tinkerbell(x, xnew, n)

def Henon(x, xnew, n):
    a=1.4
    b=0.3

    #   Nonlinear Henon map equations:
    xnew[1] = 1-a*x[1]*x[1]+b*x[2]
    xnew[2] = x[1]

    #   Linearized Henon map equations:
    xnew[3] = -2*a*x[1]*x[3]+b*x[5]
    xnew[4] = -2*a*x[1]*x[4]+b*x[6]
    xnew[5] = x[3]
    xnew[6] = x[4]

    return [x, xnew]

# Seems to lead to an error after a few thousand iterations
def DelayedLogisticMap(x, xnew, n):
    a=2.27

    #   Nonlinear Delayed Logistic Map equations:
    xnew[1] = a*x[1] - a*x[1]*x[2]
    xnew[2] = x[1]

    #   Linearized Delayed Logistic Map equations:
    xnew[3] = a*x[3]-a*x[3]*x[2] - a*x[1]*x[5]
    xnew[4] = a*x[4]-a*x[4]*x[2] - a*x[1]*x[6]
    xnew[5] = x[3]
    xnew[6] = x[4]

    return [x, xnew]

def burger(x, xnew, n):
    a = .75
    b = 1.75

    # Nonlinear
    xnew[1] = a*x[1] - x[2]**2
    xnew[2] = b*x[2] + x[1]*x[2]

    # Linearized
    xnew[3] = a*x[3] - 2 * x[2]*x[5]
    xnew[4] = a*x[4] - 2 * x[2]*x[6]
    xnew[5] = x[2]*x[3] + b*x[5] + x[1]*x[5]
    xnew[6] = x[2]*x[4] + b*x[6] + x[1]*x[6]

    return [x, xnew]

def tinkerbell(x, xnew, n):
    a =  0.9
    b = -0.6
    c =  2.0
    d =  0.5

    # Nonlinear
    xnew[1] = x[1]**2 - x[2]**2 + a*x[1] + b*x[2]   # x
    xnew[2] = 2*x[1]*x[2] + c * x[1] + d * x[2]     # y

    # Linearized
    # To linearize these equations
    # Find the jacobian of the system
    # Then multiply the Jn by the 1 x 2 vector [delta x; delta y] to get
    # a 1 x 2 vector [delta x+1; delta y+1]
    # xnew[3] = delta x(n + 1), xnew[5] = delta y(n+1)
    xnew[3] = 2 * x[1] * x[3] + a * x[3] - 2 * x[2] * x[5] + b * x[5] # delta x
    xnew[4] = 2 * x[1] * x[4] + a * x[4] - 2 * x[2] * x[6] + b * x[6] # delta x
    xnew[5] = 2 * x[2] * x[3] + c * x[3] + 2 * x[1] * x[5] + d * x[5] # delta y
    xnew[6] = 2 * x[2] * x[4] + c * x[4] + 2 * x[1] * x[6] + d * x[6] # delta y

    return [x, xnew]

n=2                 #   number of variables in nonlinear map
nn=n*(n+1)          #   total number of variables (nonlinear + linear)
m = 0

x = []
xnew = []

v = []
ltot = []

znorm = []
gsc = []

i = 0
while i <= nn:
    x.append(0)
    xnew.append(0)
    v.append(0)

    i = i + 1

i = 0
while i <= n:
    ltot.append(0)
    znorm.append(0)
    gsc.append(0)

    i = i + 1

irate=10            #   integration steps per reorthonormalization
io= 1000            #   number of iterations between printouts
cmax = 100000       #   number of iterations to perform

#   initial conditions for nonlinear maps
#   must be within the basin of attraction
i = 1
while i <= n:
    v[i] = 0.001
    i = i + 1

i = n+1
while i <= nn:       #   initial conditions for linearized maps
    v[i]=0           #   Don't mess with these; they are problem independent!
    i = i + 1

i = 1
while i <= n:
    v[(n+1)*i]=1
    ltot[i]=0
    i = i + 1

print(v)

t=0
w = 0
while (w < cmax):
    j = 1
    while j <= irate:
        i = 1
        while i <= nn:
            x[i]=v[i]
            i = i + 1

        [x, xnew] = derivs(x, xnew, n)

        i = 1
        while i <= nn:
            v[i]=xnew[i]
            i = i + 1

        t = t + 1
        j = j + 1

    #construct new orthonormal basis by gram-schmidt:
    znorm[1]=0    #normalize first vector

    j = 1
    while j <= n:
        znorm[1]=znorm[1]+v[n*j+1]**2
        j = j + 1

    znorm[1] = math.sqrt(znorm[1])

    j = 1
    while j <= n:
        v[n*j+1]=v[n*j+1]/znorm[1]
        j = j + 1

    # generate new orthonormal set:
    j = 2
    while j <= n:
        k = 1
        while k <= j-1:
            gsc[k]=0
            l = 1
            while l <= n:
                gsc[k]=gsc[k]+v[n*l+j]*v[n*l+k]
                l = l + 1
            k = k + 1

        k = 1
        while k <= n:    #construct a new vector
            l = 1
            while l <= j-1:
                v[n*k+j]=v[n*k+j]-gsc[l]*v[n*k+l]
                l = l + 1
            k = k + 1

        znorm[j]=0       #calculate the vector's norm

        k = 1
        while k <= n:    #construct a new vector
            znorm[j]=znorm[j]+v[n*k+j]**2
            k = k + 1

        znorm[j]=math.sqrt(znorm[j])

        k = 1
        while k <= n:    #normalize the new vector
            v[n*k+j] = v[n*k+j] / znorm[j]
            k = k + 1

        j = j + 1

    k = 1
    while k <= n:    #update running vector magnitudes
        if znorm[k] > 0:
            ltot[k] = ltot[k] + math.log(znorm[k])
        k = k + 1

    m = m + 1
    if m % io == 0:  #normalize exponent and print every io iterations
        print("\tLEs =")

        lsum=0
        kmax=0
        k = 1
        while k <= n:
            le = ltot[k] / t
            lsum = lsum + le
            if lsum > 0:
                lsum0 = lsum
                kmax = k

            print(le)
            k = k + 1

        if ltot[1]>0:
            dky = kmax - t * lsum0 / float(ltot[kmax+1])

        else:
            dky = 0

        print("  Kaplan-Yorke dimension =", dky)
    w = w + 1