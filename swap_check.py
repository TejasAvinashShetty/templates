# from two_qubit_plot import
# from hu import Hi
from parameters import omega1,omega2,tmax
from scipy.optimize import minimize
from numpy.random import random, random_sample
from matplotlib.pyplot import plot, figure, xlabel, ylabel, title
from matplotlib.pyplot import show, savefig
from numpy import arange, linspace, sqrt, sin, cos
from qutip.qip.gates import swap
from qutip.tensor import tensor
from qutip.operators import identity, sigmax, sigmaz
# filename = 'sc-' + datetime.date.today().strftime("%d-%B") + '-' + datetime.datetime.now().strftime("%H-%M") + '-PM'

from datetime import date
from datetime import datetime# now

# Identity in the qubit
Q = identity(2)



W = (omega1 + omega2)/2
deltaa = (omega1 - omega2)/2
T = tmax # 7

def fidelity_twoqubit_anal(W, deltaa, T, g):
    f = 0.5*sqrt((cos(sqrt(W**2 + g**2)*T))**2 + ((g**2)/(deltaa**2 + g**2))*(sin((sqrt(deltaa**2 + g**2))*T))**2)
    return f

def u_W_deltaa_T_g(W, deltaa, T, g):
    omega1 = W + deltaa
    omega2 = W - deltaa

    # build the bare hamiltonian
    H0 = (omega1/2)*tensor(sigmaz(), Q) + (omega2/2)*tensor(Q, sigmaz())

    # build the interaction hamiltonians
    Hi = tensor(sigmax(), sigmax())
    # print(g)
    H = H0 + g*Hi

    U = (-1j*H*T).expm()
    return U

def fid_U_targ_U(U_target,U):
    # stuff inside the trace with normalization
    uu = ((U_target.dag())*U)/(2*2)
    # taking the trace
    f = uu.tr()
    # absolute value of the trace
    fi = abs(f)
    return fi

success_amt = []
n_trials = 100
opt_repeat = 5 #50
fid_check = []
g_check = []
for p in range(n_trials):
    # g_target = random_sample()
    # U_target = u_W_deltaa_T_g(W, deltaa, T, g_target)
    U_target = swap()
    fid_this_repeat = []
    g_this_repeat = []
    for q in range(opt_repeat):

        g0 = random(1) # random_sample()
        def one_minus_fid_Utarg_Uofg(nelder_g):
            nelder_g_num = nelder_g[0]

            U_nelder = u_W_deltaa_T_g(W, deltaa, T, nelder_g_num)
            fi = 1 - fid_U_targ_U(U_target,U_nelder)
            return fi


        optim = minimize(one_minus_fid_Utarg_Uofg, g0, method='SLSQP', tol=1e-6)
        g_optim_arr = optim.x
        g_optim = g_optim_arr[0]
        print('g_optim',g_optim)
        g_this_repeat.append(g_optim)
        # print('g_actual',g_target)
        # g_ratio = g_optim/g_target
        U_nelder_opt = u_W_deltaa_T_g(W, deltaa, T, g_optim)
        fid_this_repeat.append(fid_U_targ_U(U_target,U_nelder_opt))

    fid_this_run = max(fid_this_repeat)
    fid_check.append(fid_this_run)
    # success_amt.append(g_ratio)

trial_vec = arange(n_trials)
'''plot(trial_vec, success_amt)
xlabel('Number of Trials ')
ylabel('Capacity of optimizer')
title('Checking how well the optimizer works')
#show()
'''
plot(trial_vec, fid_check,'k.--')
xlabel('Number of Trials ')
ylabel('fidelity')
title('Fidelity for trials')
# filename = 'sc-' + datetime.date.today().strftime("%d-%B") + '-' + datetime.datetime.now().strftime("%H-%M") + '-PM'

filename = 'sc-' + date.today().strftime("%d-%B") + '-' + datetime.now().strftime("%H-%M") + '-PM'
savefig(filename)

show()
