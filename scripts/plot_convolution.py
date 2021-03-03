#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Remi Flamary <remi.flamary@polytechnique.edu>
#
# License: MIT License

#%%

import numpy as np
import pylab as pl
import scipy as sp

path='../imgs/sig_conv/'

#%%

T=1

ns=600
t=np.linspace(-1,5,ns)

x=lambda x: 1.0*(x>=0)
h=lambda x: 1.0*(x>=0)*np.exp(-x)


#%% plot the signals For figures analog convolution fig:convolution

pl.figure(1,(8,5))
pl.clf()
pl.subplot(2,1,1)
pl.plot(t,x(t),label='x(t)')
pl.legend()
pl.title('Signals $x(t)$ and $h(t)$')
#pl.xticks((-1,0,1,2,3,4,5),(-1,0,1,"",3,4,5))
pl.subplot(2,1,2)
pl.plot(t,h(t),'--',c='C1',label='h(t)')
pl.legend(loc='upper left')
    
pl.savefig(path+'signals.pdf',bbox_inches='tight')

#%% plot the signals and output figures analog convolution fig:convolution

y=np.convolve(x(t),h(t))[100:700]
y/=y.max()


ns2=100
taus=np.linspace(-1,5,ns2)

tau=1

pl.figure(1,(8,5))
pl.clf()
pl.subplot(2,1,1)
pl.plot(t,x(t),label='x(t)')
pl.plot(t,h(t),'--',c='C1',label='h(t)')
pl.legend()
pl.title('Signals $x(t)$ and $h(t)$')
#pl.xticks((-1,0,1,2,3,4,5),(-1,0,1,"",3,4,5))
pl.subplot(2,1,2)
pl.plot(t,y,c='C2',label='$x(t)*h(t)$')
pl.fill(t,h(tau-t)*x(t),c='C4',alpha=0.5,label='$x(\\tau)h(t-\\tau)$')
pl.legend(loc='upper left')
# for n in range(51):

#     pl.figure(1,(5,4))
#     pl.clf()
#     pl.plot(t,x,label='$x(t)$')
#     pl.plot(t,get_series(n),label='$x_{{{}}}(t)$'.format(n))
#     pl.xlim((0,5))
#     pl.ylim((-.2,1.2))
#     pl.legend(loc='lower right')
#     pl.title('Square wave and Fourier series')
    
pl.savefig(path+'signals_conv.pdf',bbox_inches='tight')
#     pl.savefig('../imgs/fourier_series/fourier_series_{:02d}.png'.format(n),bbox_inches='tight')

#%%  save png to create the movie for convolution

y=np.convolve(x(t),h(t))[100:700]
y/=y.max()


ns2=100
taus=np.linspace(-1,5,ns2)

tau=1


for i,tau in enumerate(taus):

    pl.figure(2,(8,5))
    pl.clf()
    pl.subplot(2,1,1)
    pl.plot(t,x(t),label='$x(\\tau)$')
    pl.plot(t,h(tau-t),'--',c='C1',label='$h(t-\\tau)$')
    pl.fill(t,h(tau-t)*x(t),c='C4',alpha=0.5,label='$x(\\tau)h(t-\\tau)$')
    
    xlim=pl.xlim()
    ylim=pl.ylim()
    pl.xticks(pl.xticks()[0],['' for i in pl.xticks()[0]])
    pl.xlim(xlim)
    pl.xlabel('$\\tau$')
    pl.legend()
    pl.title('Signals $x(\\tau)$, $h(t-\\tau)$ and product')
    
    #pl.xticks((-1,0,1,2,3,4,5),(-1,0,1,"",3,4,5))
    pl.subplot(2,1,2)
    pl.plot(t[:int((tau+1)/6*ns)],y[:int((tau+1)/6*ns)],c='C2',label='$x(t)*h(t)$')
    pl.plot([tau,tau],ylim,'k',label='$t$')
    pl.xlim(xlim)
    pl.ylim(ylim)
    pl.xlabel('t')
    pl.legend(loc='upper left')
    
    pl.savefig(path+'/conv_demo/conv_{:03d}.png'.format(i),bbox_inches='tight')



#%% 50 shades of discrete convolution with scipy.signal.convolve

import scipy.signal
import scipy.ndimage

n1=32
n2=8

x=np.exp(-np.arange(n1)/5)
h=np.ones(n2)
#h[-1]=0


pl.figure(3,(12,2))
pl.clf()
pl.subplot(1,2,1)
pl.plot(x,'-+',label='x[n], N=32')
pl.plot(h,'-x',label='h[n], M=8')
pl.xlim((-1.5,40))
pl.legend()
pl.title('Finite signals')

pl.subplot(1,2,2)
pl.plot(sp.signal.convolve(x,h,mode='full'),'-+',color='C2',label="mode='full'")
pl.plot(sp.signal.convolve(x,h,mode='valid'),'-x',color='C3',label="mode='valid'")
pl.plot(sp.signal.convolve(x,h,mode='same'),'-',marker='.',color='C4',label="mode='same'")
pl.legend()
pl.xlim((-1.5,40))
pl.title('Convolution $x*h[n]$ with scipy.signal.convolve')

#pl.savefig('../imgs/conv_scipy_signal.pdf',bbox_inches='tight')


#%% 50 shades of discrete convolution with scipy.ndimage.convolve

import scipy.signal
import scipy.ndimage

n1=32
n2=8

x=np.exp(-np.arange(n1)/5)
h=np.ones(n2)
#h[-1]=0


pl.figure(3,(12,2))
pl.clf()
pl.subplot(1,2,1)
pl.plot(x,'-+',label='x[n], N=32')
pl.plot(h,'-x',label='h[n], M=8')
pl.legend()
pl.title('Finite signals')

pl.subplot(1,2,2)
pl.plot(sp.ndimage.convolve(x,h,mode='reflect',origin=-n2//2),'-+',color='C2',label="mode='reflect'")
pl.plot(sp.ndimage.convolve(x,h,mode='nearest',origin=-n2//2),'-x',color='C3',label="mode='nearest'")
pl.plot(sp.ndimage.convolve(x,h,mode='mirror',origin=-n2//2),'-',marker='.',color='C4',label="mode='mirror'")
pl.plot(sp.ndimage.convolve(x,h,mode='wrap',origin=-n2//2),'-',marker='.',color='C6',label="mode='wrap'")
pl.legend()
pl.title('Convolution $x*h[n]$ with scipy.ndimage.convolve')

#pl.savefig('../imgs/conv_scipy_ndimage.pdf',bbox_inches='tight')
