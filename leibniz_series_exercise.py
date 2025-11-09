def approximate_pi(n_terms):
     total= 0
     for i in range(n_terms):
         total+=((-1)**i/(2*i+1))
     pi_value = 4* total
     return pi_value      
     return approximate_pi
approximate_pi(1000)     
