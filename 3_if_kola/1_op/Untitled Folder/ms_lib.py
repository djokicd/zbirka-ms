from pylab import *
import matplotlib.ticker as mticker

import matplotlib as mpl
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif"
    })

plt.rc('text.latex', preamble=r'\usepackage[T1,T2A]{fontenc}\usepackage[utf8]{inputenc}\usepackage{cmsrb}\usepackage{amsmath}\usepackage[Symbolsmallscale]{upgreek}\usepackage{icomma}')



# Decimalni zarez
import locale
locale.setlocale(locale.LC_NUMERIC, "sr_RS.utf8")
plt.rcParams['axes.formatter.use_locale'] = True

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 10}

matplotlib.rc('font', **font)

def generate_canvas(w = 1.6, a = 1.618):
    figure (figsize = (a*w, w), dpi = 200)
    minorticks_on()
    grid(b=True, which='major', color='0.45', linestyle='-')
    grid(b=True, which='minor', color='0.75', linestyle='--')


    