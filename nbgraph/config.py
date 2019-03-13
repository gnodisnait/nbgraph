import decimal

L0 = decimal.Decimal(1e+100)
R0 = decimal.Decimal(1e-200)
cgap = decimal.Decimal(0.0001)
addDim = [512]*2 + [-512]*128
DIM_W2V = 50
INIT_RATIO_W2V = 100
INIT_INC_CATCODE = 10

xalpha = 'alpha/25'
hrate = 0.1
MAXBETA = 0.999
DIM = 100
DECIMAL_PRECISION = 500