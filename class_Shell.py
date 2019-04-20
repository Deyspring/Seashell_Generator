class Shell: 

	def __init__(self, i, D, alpha_, beta, phi, mu, omega, A, a, b, L, P, W1, W2, N):
		self.i = i
    	self.D = D
    	self.alpha_ = alpha_
    	self.beta = beta
    	self.phi = phi 
    	self.mu = mu
    	self.omega = omega
    	self.A = A
    	self.a = a
    	self.b = b
    	self.L = L 
    	self.P = P
    	self.W1 = W1
    	self.W2 = W2
    	self.N = N 


    def generateSpiral(self):
    """Generates spiral points """

    spiral_matrix=[]

    while self.i < n: 

        theta = float(map(i, 0, n, 0, turns))
        rad = float(exp(theta * cos(self.alpha_) / sin(self.alpha_)))
    
        x = float(self.A * rad * sin(self.beta) * cos(theta) * D)
        y = float(self.A * rad * sin(self.beta) * sin(theta))
        z = float(-self.A * rad * cos(self.beta))
  
        spiral_i = PVector(x,y,z)
        
        spiral_matrix.append(spiral_i) 

        i = i + 1  #for some reason i += 1 does not work here. It may be a processing thing. 

    return spiral_matrix


    def generateSpline(self):
    """Generates spline around a spiral point """

    spline_matrix =[]
    j = 0 

    while j < m: 
        s = float(map(j, 0, m, 0, TWO_PI)) 
        r2 = float(pow( pow(cos(self.s)/a,2) + pow(sin(self.s)/b,2), -0.5 ))
        
        # add surface manipulations
        surfrad = float(0)
        if (W1==0 or W2==0 or N==0):
            surfrad = 0
        else: 
            lt = float((TWO_PI / self.N) * ( self.N*theta / TWO_PI - int(self.N*theta / TWO_PI) ))
            surfrad = self.L * exp( -( pow(2*(self.s-self.P)/self.W1, 2) + pow(2*lt/self.W2, 2) ) ) 

        r2 += surfrad
        
        x = cos(s + self.phi) * cos(theta + self.omega) * r2 * rad * self.D   # here  rad - 1 closes the opening of the curve at the origin
        y = cos(s + self.phi) * sin(theta + self.omega) * r2 * rad
        z = sin(s + self.phi)                      * r2 * rad
        
        # adjust orientation of the spline so shell doesn't flatten out to a ribbon?
        x -= sin(self.mu) * sin(self.s + self.phi) * sin(theta + self.omega) * r2
        y += sin(self.mu) * sin(self.s + self.phi) * cos(theta + self.omega) * r2
        z *= cos(self.mu)
        
        
        spline = PVector(x,y,z)
        spline_matrix.append(spline)   

        j = j+ 1 

        return spline_matrix
 
 	def mesh(self):
    	return  zip(spiral_matrix, spline_matrix) 
    
    