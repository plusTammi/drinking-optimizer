import numpy as np
import matplotlib.pylab as plb

class alcohol_level:
	def __init__(self,weight,time_start=0,time_end=60*24):
		self.weight=weight
		self.time=np.linspace(time_start,time_end,time_end-time_start+1)
		self.burn=-((self.time/60.0)*self.weight*0.1)
		self.drinks=np.zeros(self.time.shape)
	
	def add_drink(self,grams,time):
		self.drinks[self.time>time]+=grams
		
	def plot_level(self):
		to_plot=self.burn+self.drinks-self.burn[self.drinks[self.drinks==0].shape[0]]
		to_plot[:self.drinks[self.drinks==0].shape[0]]=0
		to_plot[to_plot<0]=0
		plb.plot(self.time,to_plot)
		plb.show()

