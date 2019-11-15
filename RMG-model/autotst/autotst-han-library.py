#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "sp0",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u1 p1 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90867,0.00573133,8.30176e-05,-1.90464e-07,1.27575e-10,24255.8,8.93979], Tmin=(10,'K'), Tmax=(519.336,'K')),
            NASAPolynomial(coeffs=[4.60119,0.019672,-1.2918e-05,4.15107e-09,-5.11772e-13,23924,3.55004], Tmin=(519.336,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (201.647,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 1,
    label = "sp1",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {11,S}
4  N u0 p1 c0 {1,S} {2,S} {5,S}
5  N u0 p1 c0 {4,S} {7,S} {8,S}
6  N u0 p1 c0 {1,S} {9,S} {10,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81824,0.0127238,0.000162037,-4.29662e-07,3.34596e-10,21340.7,10.5734], Tmin=(10,'K'), Tmax=(442.88,'K')),
            NASAPolynomial(coeffs=[4.55787,0.036859,-2.40761e-05,7.60041e-09,-9.17367e-13,20973,4.19564], Tmin=(442.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (177.421,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 2,
    label = "sp2",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,D} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u0 p2 c0 {1,D}
5 N u1 p2 c-1 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8948,0.00706787,8.17335e-05,-2.11748e-07,1.56769e-10,39009.6,10.0594], Tmin=(10,'K'), Tmax=(475.479,'K')),
            NASAPolynomial(coeffs=[4.78719,0.0183472,-1.31158e-05,4.33678e-09,-5.36245e-13,38712.3,4.18442], Tmin=(475.479,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (324.325,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 3,
    label = "sp3",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92947,0.00598499,8.57166e-05,-2.54169e-07,2.38314e-10,26288.5,9.44943], Tmin=(10,'K'), Tmax=(332.625,'K')),
            NASAPolynomial(coeffs=[3.19279,0.0214175,-1.35216e-05,4.14396e-09,-4.89115e-13,26301.2,11.646], Tmin=(332.625,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (218.587,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 4,
    label = "sp4",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {3,D}
2 O u0 p3 c-1 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03014,-0.00192172,1.57933e-05,-1.87729e-08,7.1058e-12,5204.3,5.85505], Tmin=(10,'K'), Tmax=(831.639,'K')),
            NASAPolynomial(coeffs=[2.96996,0.00605899,-3.79847e-06,1.09869e-09,-1.20232e-13,5280.99,10.1753], Tmin=(831.639,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (43.2788,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 5,
    label = "sp5",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,D} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95513,0.00269641,4.87838e-05,-1.00861e-07,6.19633e-11,20287.4,8.6229], Tmin=(10,'K'), Tmax=(549.181,'K')),
            NASAPolynomial(coeffs=[3.73876,0.0142058,-9.78395e-06,3.17163e-09,-3.882e-13,20161.4,8.17325], Tmin=(549.181,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (168.662,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 6,
    label = "sp6",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,S} {6,D}
4 O u0 p2 c0 {2,S} {7,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8489,0.0116957,8.7501e-05,-2.69991e-07,2.33881e-10,16204.7,9.51649], Tmin=(10,'K'), Tmax=(407.529,'K')),
            NASAPolynomial(coeffs=[4.65345,0.0216422,-1.47854e-05,4.77417e-09,-5.83119e-13,15990.9,4.53929], Tmin=(407.529,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (134.735,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 7,
    label = "sp7",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {6,S}
2 O u0 p3 c-1 {5,S}
3 O u0 p2 c0 {5,D}
4 O u0 p2 c0 {6,D}
5 N u0 p0 c+1 {1,S} {2,S} {3,D}
6 N u0 p1 c0 {1,S} {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71715,0.03077,-5.62817e-05,7.8946e-08,-5.07555e-11,6554.66,10.7229], Tmin=(10,'K'), Tmax=(367.323,'K')),
            NASAPolynomial(coeffs=[4.62884,0.0208421,-1.57401e-05,5.36588e-09,-6.76951e-13,6487.68,7.23762], Tmin=(367.323,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (54.5201,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 8,
    label = "sp8",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03041,-0.00235534,3.36665e-05,-4.82382e-08,2.31733e-11,-5187.63,4.78781], Tmin=(10,'K'), Tmax=(575.929,'K')),
            NASAPolynomial(coeffs=[2.22466,0.0115079,-5.88258e-06,1.52666e-09,-1.58382e-13,-5001.55,12.3129], Tmin=(575.929,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-43.13,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 9,
    label = "sp9",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 N u0 p1 c0 {1,S} {4,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92662,0.00554874,4.84543e-05,-1.63925e-07,1.51689e-10,26248.2,7.23457], Tmin=(10,'K'), Tmax=(396.097,'K')),
            NASAPolynomial(coeffs=[4.85041,0.00799164,-5.37608e-06,1.70724e-09,-2.07066e-13,26082.7,2.46764], Tmin=(396.097,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (218.244,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 10,
    label = "sp10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  N u0 p1 c0 {1,S} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {8,D} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87594,0.0110074,6.71121e-05,-1.36857e-07,8.60574e-11,-45931.6,9.49612], Tmin=(10,'K'), Tmax=(412.454,'K')),
            NASAPolynomial(coeffs=[1.36479,0.0353609,-2.14567e-05,6.30197e-09,-7.15762e-13,-45724.4,19.387], Tmin=(412.454,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-381.905,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 11,
    label = "sp11",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02121,-0.00137827,3.11305e-05,-3.61302e-08,1.36009e-11,-24845.3,5.05106], Tmin=(10,'K'), Tmax=(693.442,'K')),
            NASAPolynomial(coeffs=[0.826531,0.0170506,-8.73537e-06,2.19821e-09,-2.17951e-13,-24402.3,19.2939], Tmin=(693.442,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-206.57,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 12,
    label = "sp12",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {5,S}
2  N u0 p1 c0 {1,S} {4,S} {6,S}
3  N u0 p1 c0 {1,S} {7,S} {8,S}
4  N u0 p1 c0 {2,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9499,0.00310087,9.98092e-05,-1.91764e-07,1.16934e-10,34521.1,8.52612], Tmin=(10,'K'), Tmax=(502.215,'K')),
            NASAPolynomial(coeffs=[1.34531,0.0335609,-2.01852e-05,6.042e-09,-7.07358e-13,34660.2,18.0781], Tmin=(502.215,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (287.009,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 13,
    label = "sp13",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05304,-0.00460318,4.98303e-05,-8.20295e-08,4.59227e-11,26626.4,5.25444], Tmin=(10,'K'), Tmax=(514.102,'K')),
            NASAPolynomial(coeffs=[2.34637,0.0116193,-6.09098e-06,1.6245e-09,-1.73026e-13,26763,11.9743], Tmin=(514.102,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (221.385,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 14,
    label = "sp14",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 N u0 p2 c-1 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08126,-0.00540497,4.23117e-05,-5.11936e-08,2.01322e-11,15370.2,6.45057], Tmin=(10,'K'), Tmax=(782.331,'K')),
            NASAPolynomial(coeffs=[1.35043,0.0148271,-8.50102e-06,2.3503e-09,-2.51577e-13,15605.6,17.7287], Tmin=(782.331,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (127.813,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 15,
    label = "sp15",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {7,S}
3 N u1 p1 c0 {1,S} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96063,0.00250194,8.17043e-05,-1.62663e-07,1.03e-10,-11437.8,9.22334], Tmin=(10,'K'), Tmax=(479.988,'K')),
            NASAPolynomial(coeffs=[1.91816,0.0267215,-1.64796e-05,4.95247e-09,-5.76167e-13,-11324.6,16.7141], Tmin=(479.988,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-95.1089,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 16,
    label = "sp16",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02905,-0.00171431,1.02164e-05,-1.02522e-08,3.36031e-12,845.158,4.66116], Tmin=(10,'K'), Tmax=(933.741,'K')),
            NASAPolynomial(coeffs=[3.02733,0.00428315,-2.15917e-06,5.40642e-10,-5.33264e-14,957.846,9.02691], Tmin=(933.741,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (7.03482,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 17,
    label = "sp17",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00372,-0.000186539,3.18681e-06,-2.19173e-09,4.54452e-13,44984.3,0.592882], Tmin=(10,'K'), Tmax=(906.903,'K')),
            NASAPolynomial(coeffs=[3.25962,0.00260784,-6.28613e-07,2.01874e-11,8.12304e-15,45139.3,4.22058], Tmin=(906.903,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (374.021,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 18,
    label = "sp18",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u1 p1 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50531,-0.000279995,5.61216e-07,1.50602e-09,-1.34656e-12,11006.1,4.72766], Tmin=(10,'K'), Tmax=(727.497,'K')),
            NASAPolynomial(coeffs=[2.93031,0.00157053,-5.51196e-07,4.83157e-11,5.61617e-15,11124.5,7.55723], Tmin=(727.497,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.5122,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 19,
    label = "sp19",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {5,S}
4 N u0 p1 c0 {1,S} {8,D}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {4,D}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84547,0.0101957,0.000131293,-3.28318e-07,2.37487e-10,24871.2,10.1594], Tmin=(10,'K'), Tmax=(483.879,'K')),
            NASAPolynomial(coeffs=[5.10796,0.0293637,-1.98995e-05,6.42744e-09,-7.87991e-13,24402.4,1.40384], Tmin=(483.879,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (206.759,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 20,
    label = "sp20",
    molecule = 
"""
1 O u0 p3 c-1 {4,S}
2 O u0 p2 c0 {5,D}
3 O u0 p2 c0 {4,D}
4 N u0 p0 c+1 {1,S} {3,D} {5,S}
5 C u0 p0 c0 {2,D} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88365,0.0111017,1.79579e-05,-3.85863e-08,1.94952e-11,-15248.3,9.38715], Tmin=(10,'K'), Tmax=(714.476,'K')),
            NASAPolynomial(coeffs=[4.17478,0.0171198,-1.07331e-05,3.16695e-09,-3.56862e-13,-15485.1,6.71442], Tmin=(714.476,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-126.792,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 21,
    label = "sp21",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,D} {4,S} {5,S}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u1 p2 c0 {1,S}
5 O u0 p3 c-1 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94919,0.00293013,6.33523e-05,-1.20494e-07,6.86465e-11,12080.7,9.70657], Tmin=(10,'K'), Tmax=(579.595,'K')),
            NASAPolynomial(coeffs=[2.96574,0.0215052,-1.52275e-05,4.98134e-09,-6.11041e-13,11996.7,12.2067], Tmin=(579.595,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (100.423,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 22,
    label = "sp22",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {5,S} {6,S}
2 N u0 p2 c-1 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91208,0.00564164,8.33826e-05,-1.95214e-07,1.34433e-10,24652.1,9.171], Tmin=(10,'K'), Tmax=(501.018,'K')),
            NASAPolynomial(coeffs=[4.34828,0.0200001,-1.30192e-05,4.13399e-09,-5.03587e-13,24384.4,5.1334], Tmin=(501.018,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (204.946,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 23,
    label = "sp23",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10102,-0.00679999,4.96161e-05,-6.14618e-08,2.47004e-11,39357.8,6.48312], Tmin=(10,'K'), Tmax=(778.36,'K')),
            NASAPolynomial(coeffs=[1.39329,0.0154203,-9.21048e-06,2.63179e-09,-2.88687e-13,39527.7,17.2518], Tmin=(778.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (327.261,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 24,
    label = "sp24",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 O u0 p3 c-1 {1,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05983,-0.0036807,2.63459e-05,-2.91427e-08,1.03749e-11,-3633.66,5.62859], Tmin=(10,'K'), Tmax=(871.75,'K')),
            NASAPolynomial(coeffs=[1.91505,0.0106917,-6.18098e-06,1.69447e-09,-1.78474e-13,-3431.89,14.6941], Tmin=(871.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-30.1958,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 25,
    label = "sp25",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10242,-0.00693494,5.16364e-05,-6.17061e-08,2.43243e-11,6017.34,3.21987], Tmin=(10,'K'), Tmax=(759.078,'K')),
            NASAPolynomial(coeffs=[0.490933,0.0180921,-9.66806e-06,2.54148e-09,-2.62694e-13,6392.87,18.5098], Tmin=(759.078,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (50.0528,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 26,
    label = "sp26",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49863,8.10799e-05,-2.55729e-07,1.22397e-11,3.06213e-13,-444.075,-4.29116], Tmin=(10,'K'), Tmax=(610.591,'K')),
            NASAPolynomial(coeffs=[3.68699,-0.000782705,9.56901e-07,-3.18866e-10,3.52533e-14,-473.978,-5.16347], Tmin=(610.591,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-3.69273,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 27,
    label = "sp27",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49685,0.000185054,-1.00604e-06,1.58683e-09,-6.18788e-13,4289.04,1.47312], Tmin=(10,'K'), Tmax=(981.579,'K')),
            NASAPolynomial(coeffs=[3.44928,-0.000288198,7.36613e-07,-2.89136e-10,3.53523e-14,4330.52,1.86546], Tmin=(981.579,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.6601,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 28,
    label = "sp28",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03138,-0.00190329,8.07556e-06,3.98804e-09,-8.29327e-12,24981.4,3.42235], Tmin=(10,'K'), Tmax=(599.191,'K')),
            NASAPolynomial(coeffs=[1.53277,0.00883506,-3.93271e-06,7.99738e-10,-5.83487e-14,25387.5,15.087], Tmin=(599.191,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (207.718,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 29,
    label = "sp29",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,S} {6,S}
3 O u1 p2 c0 {4,S}
4 N u0 p1 c0 {1,S} {2,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91531,0.00585958,7.16283e-05,-1.86465e-07,1.41732e-10,-8812.71,9.19827], Tmin=(10,'K'), Tmax=(454.781,'K')),
            NASAPolynomial(coeffs=[4.2804,0.0168242,-1.12919e-05,3.62713e-09,-4.41953e-13,-8992.51,6.11292], Tmin=(454.781,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.2832,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 30,
    label = "sp30",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  N u0 p0 c+1 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p3 c-1 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79369,0.0218444,7.14884e-06,-1.96803e-08,7.76045e-12,-44429,9.68382], Tmin=(10,'K'), Tmax=(990.518,'K')),
            NASAPolynomial(coeffs=[4.5375,0.0274984,-1.45243e-05,3.731e-09,-3.7559e-13,-45001.1,3.95853], Tmin=(990.518,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-369.401,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 31,
    label = "sp31",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 N u0 p1 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p3 c-1 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94203,0.0069142,4.43662e-06,-8.15671e-09,2.95365e-12,9518.89,6.55472], Tmin=(10,'K'), Tmax=(1029.83,'K')),
            NASAPolynomial(coeffs=[4.03132,0.0100163,-5.10519e-06,1.2722e-09,-1.2474e-13,9317.62,5.23342], Tmin=(1029.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (79.149,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 32,
    label = "sp32",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95334,0.00309543,7.47678e-05,-1.64622e-07,1.13593e-10,-23856.7,8.06877], Tmin=(10,'K'), Tmax=(459.213,'K')),
            NASAPolynomial(coeffs=[2.84447,0.0213842,-1.31607e-05,3.95272e-09,-4.5984e-13,-23845.9,11.5647], Tmin=(459.213,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-198.364,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 33,
    label = "sp33",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00627,-0.000314294,1.21228e-06,1.4947e-09,-1.36594e-12,22575.6,0.598446], Tmin=(10,'K'), Tmax=(786.46,'K')),
            NASAPolynomial(coeffs=[3.25219,0.00187325,1.82773e-07,-2.96661e-10,5.03469e-14,22745.1,4.37928], Tmin=(786.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (187.706,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 34,
    label = "sp34",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,S} {5,D}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u0 p3 c-1 {1,S}
5 N u1 p1 c0 {1,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87245,0.00900814,8.51853e-05,-2.4479e-07,1.96584e-10,37727.1,10.1036], Tmin=(10,'K'), Tmax=(446.29,'K')),
            NASAPolynomial(coeffs=[5.19848,0.017615,-1.26168e-05,4.18969e-09,-5.20615e-13,37404.7,2.48976], Tmin=(446.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (313.67,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 35,
    label = "sp35",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93691,0.0052666,-8.58294e-06,1.62317e-08,-1.00651e-11,6465.9,4.95305], Tmin=(10,'K'), Tmax=(630.866,'K')),
            NASAPolynomial(coeffs=[3.09252,0.00676891,-2.99711e-06,6.51318e-10,-5.58809e-14,6649.08,9.24526], Tmin=(630.866,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (53.757,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 36,
    label = "sp36",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01388,-0.000821535,4.65091e-06,-4.71206e-11,-2.51144e-12,4549.91,4.13336], Tmin=(10,'K'), Tmax=(627.753,'K')),
            NASAPolynomial(coeffs=[2.73851,0.0046603,-2.12821e-06,4.40901e-10,-3.30386e-14,4762.14,10.1075], Tmin=(627.753,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (37.8353,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 37,
    label = "sp37",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53581,-0.00347894,3.85413e-05,-6.93024e-08,4.08312e-11,-48328.5,5.37917], Tmin=(10,'K'), Tmax=(533.365,'K')),
            NASAPolynomial(coeffs=[2.75585,0.00712913,-4.67508e-06,1.44258e-09,-1.69173e-13,-48313,8.01727], Tmin=(533.365,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-401.828,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 38,
    label = "sp38",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u1 p0 c+1 {1,S} {4,D}
4 N u0 p2 c-1 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39551,0.0605281,-0.000257339,4.88393e-07,-3.33666e-10,467.625,10.5263], Tmin=(10,'K'), Tmax=(446.011,'K')),
            NASAPolynomial(coeffs=[7.06723,0.00623164,-2.87167e-06,6.20365e-10,-5.0338e-14,352.622,-1.84059], Tmin=(446.011,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (3.87576,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 39,
    label = "sp39",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {8,S}
2 O u0 p3 c-1 {4,S}
3 O u0 p2 c0 {4,D}
4 N u0 p0 c+1 {2,S} {3,D} {5,S}
5 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86213,0.013447,2.65019e-05,-5.01456e-08,2.3951e-11,-28886.1,9.47188], Tmin=(10,'K'), Tmax=(725.039,'K')),
            NASAPolynomial(coeffs=[3.39318,0.0246915,-1.46722e-05,4.18239e-09,-4.60379e-13,-29045.6,10.0143], Tmin=(725.039,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-240.183,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 40,
    label = "sp40",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92726,0.00449052,8.64753e-05,-1.81731e-07,1.15567e-10,10404.4,8.41935], Tmin=(10,'K'), Tmax=(524.002,'K')),
            NASAPolynomial(coeffs=[3.36177,0.0244383,-1.53722e-05,4.77286e-09,-5.73836e-13,10249,8.73438], Tmin=(524.002,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (86.483,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 41,
    label = "sp41",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 O u1 p2 c0 {1,S}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97503,0.00139309,3.27177e-05,-5.91586e-08,3.19146e-11,12494.6,7.87979], Tmin=(10,'K'), Tmax=(607.357,'K')),
            NASAPolynomial(coeffs=[3.21427,0.0123869,-9.21122e-06,3.08513e-09,-3.82766e-13,12476.6,10.2622], Tmin=(607.357,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (103.874,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 42,
    label = "sp42",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02131,-0.00149006,2.85433e-05,-3.63578e-08,1.51891e-11,630.779,5.39026], Tmin=(10,'K'), Tmax=(620.664,'K')),
            NASAPolynomial(coeffs=[1.74026,0.0132111,-6.98721e-06,1.80734e-09,-1.84095e-13,913.923,15.3069], Tmin=(620.664,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.24835,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 43,
    label = "sp43",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98421,0.00102842,3.88118e-05,-7.6626e-08,4.97507e-11,7535.86,7.37236], Tmin=(10,'K'), Tmax=(394.321,'K')),
            NASAPolynomial(coeffs=[2.77533,0.0132911,-7.83487e-06,2.23717e-09,-2.47968e-13,7631.19,12.0795], Tmin=(394.321,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (62.6525,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 44,
    label = "sp44",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p3 c-1 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80738,0.0198584,-3.86972e-05,9.49541e-08,-8.53356e-11,20798.5,10.0678], Tmin=(10,'K'), Tmax=(413.952,'K')),
            NASAPolynomial(coeffs=[2.80204,0.0211204,-1.26413e-05,3.66342e-09,-4.11107e-13,20954.2,14.9061], Tmin=(413.952,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (172.923,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 45,
    label = "sp45",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80736,0.0198615,-3.87234e-05,9.5025e-08,-8.53983e-11,20798.3,10.0748], Tmin=(10,'K'), Tmax=(413.935,'K')),
            NASAPolynomial(coeffs=[2.80196,0.0211206,-1.26414e-05,3.66345e-09,-4.1111e-13,20954,14.9136], Tmin=(413.935,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (172.921,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 46,
    label = "sp46",
    molecule = 
"""
multiplicity 3
1 N u1 p0 c+1 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u1 p1 c0 {2,S} {8,S}
4 N u0 p2 c-1 {1,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94056,0.00367523,8.40231e-05,-1.7105e-07,1.07242e-10,67341.3,8.87233], Tmin=(10,'K'), Tmax=(516.664,'K')),
            NASAPolynomial(coeffs=[2.72311,0.0256152,-1.60063e-05,4.9018e-09,-5.8117e-13,67300.1,12.3254], Tmin=(516.664,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (559.888,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 47,
    label = "sp47",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9839,0.00659214,4.82439e-06,-7.802e-09,2.58573e-12,17684.9,7.43113], Tmin=(10,'K'), Tmax=(1155.11,'K')),
            NASAPolynomial(coeffs=[4.80036,0.00858061,-4.01149e-06,9.06916e-10,-8.03076e-14,17175,1.98378], Tmin=(1155.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (147.058,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 48,
    label = "sp48",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97486,0.00132631,4.32701e-05,-6.37888e-08,3.03293e-11,-20691.2,7.09928], Tmin=(10,'K'), Tmax=(543.912,'K')),
            NASAPolynomial(coeffs=[1.29636,0.0210244,-1.10536e-05,2.7954e-09,-2.75094e-13,-20399.9,18.3904], Tmin=(543.912,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-172.05,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 49,
    label = "sp49",
    molecule = 
"""
1 N u0 p0 c+1 {3,S} {4,D} {5,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 N u0 p2 c-1 {1,S} {2,S}
4 N u0 p1 c0 {1,D} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10496,-0.0106133,0.000147865,-2.81756e-07,1.75497e-10,45939.2,8.16915], Tmin=(10,'K'), Tmax=(507.887,'K')),
            NASAPolynomial(coeffs=[1.68825,0.0267293,-1.64974e-05,4.97069e-09,-5.78188e-13,45948.6,15.8663], Tmin=(507.887,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (381.949,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 50,
    label = "sp51",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {3,S} {4,S}
2 N u0 p2 c-1 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05304,-0.00460301,4.98305e-05,-8.20318e-08,4.59252e-11,26626.4,5.25444], Tmin=(10,'K'), Tmax=(514.084,'K')),
            NASAPolynomial(coeffs=[2.34642,0.0116192,-6.09089e-06,1.62447e-09,-1.73023e-13,26763,11.9741], Tmin=(514.084,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (221.385,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 51,
    label = "sp52",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 O u0 p3 c-1 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95479,0.00286756,7.1155e-05,-1.47487e-07,9.52594e-11,-24482.9,8.07557], Tmin=(10,'K'), Tmax=(492.76,'K')),
            NASAPolynomial(coeffs=[2.75683,0.0216152,-1.33816e-05,4.04529e-09,-4.73726e-13,-24474.4,11.8956], Tmin=(492.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-203.574,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 52,
    label = "sp53",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 O u1 p2 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03014,-0.00192175,1.57933e-05,-1.87728e-08,7.10572e-12,5204.3,5.85508], Tmin=(10,'K'), Tmax=(831.649,'K')),
            NASAPolynomial(coeffs=[2.96998,0.00605894,-3.79842e-06,1.09867e-09,-1.20229e-13,5280.98,10.1752], Tmin=(831.649,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (43.2788,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 53,
    label = "sp54",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {3,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03028,-0.00293956,7.51984e-05,-1.30773e-07,7.46169e-11,-48452.5,6.35819], Tmin=(10,'K'), Tmax=(523.531,'K')),
            NASAPolynomial(coeffs=[1.66171,0.021397,-1.24071e-05,3.54971e-09,-3.96628e-13,-48290,15.4357], Tmin=(523.531,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-402.862,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 54,
    label = "sp55",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,29269.9,4.09089], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,29269.9,4.09089], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (243.363,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 55,
    label = "sp56",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05688,-0.00445882,5.03934e-05,-7.23169e-08,3.49359e-11,11883,4.24408], Tmin=(10,'K'), Tmax=(582.706,'K')),
            NASAPolynomial(coeffs=[1.49102,0.0157069,-8.08693e-06,2.10632e-09,-2.18939e-13,12138.7,14.8653], Tmin=(582.706,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (98.8055,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 56,
    label = "sp57",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01515,-0.00084465,2.71567e-06,3.13571e-09,-3.77835e-12,13841.6,3.73823], Tmin=(10,'K'), Tmax=(674.766,'K')),
            NASAPolynomial(coeffs=[2.54728,0.00452337,-1.80703e-06,2.82696e-10,-8.72927e-15,14115.6,10.8048], Tmin=(674.766,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.092,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 57,
    label = "sp58",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00474,-0.000240355,9.48148e-07,1.28423e-09,-1.11758e-12,-28362.6,-0.117025], Tmin=(10,'K'), Tmax=(774.343,'K')),
            NASAPolynomial(coeffs=[3.50635,0.00114759,5.58031e-07,-3.58784e-10,5.17665e-14,-28249.9,2.38964], Tmin=(774.343,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-235.819,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 58,
    label = "sp59",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {9,S}
2  N u0 p1 c0 {1,S} {4,S} {10,S}
3  N u0 p1 c0 {1,S} {5,S} {11,S}
4  N u0 p1 c0 {2,S} {6,S} {12,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {5,S} {13,S}
8  O u0 p2 c0 {6,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40639,0.056494,-4.10942e-05,1.43374e-08,-1.81638e-12,37460.8,13.7525], Tmin=(10,'K'), Tmax=(1210.27,'K')),
            NASAPolynomial(coeffs=[12.4347,0.0316121,-1.63997e-05,4.11895e-09,-4.0468e-13,34912.4,-33.0269], Tmin=(1210.27,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (311.431,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 59,
    label = "sp60",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97024,0.00173296,4.77457e-05,-8.69504e-08,4.90906e-11,-12036.1,6.81994], Tmin=(10,'K'), Tmax=(562.056,'K')),
            NASAPolynomial(coeffs=[2.75584,0.0170035,-1.06963e-05,3.34969e-09,-4.0662e-13,-12004.2,11.0477], Tmin=(562.056,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-100.086,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 60,
    label = "sp61",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {7,S}
2 N u0 p0 c+1 {1,S} {4,D} {6,S}
3 O u0 p2 c0 {1,S} {5,S}
4 N u0 p1 c0 {2,D} {8,S}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 O u0 p3 c-1 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78696,0.0173587,9.62661e-05,-2.93632e-07,2.49174e-10,24142.2,10.5403], Tmin=(10,'K'), Tmax=(410.432,'K')),
            NASAPolynomial(coeffs=[4.3076,0.0308364,-2.07911e-05,6.63275e-09,-8.02222e-13,23943.2,6.58866], Tmin=(410.432,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (200.729,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 61,
    label = "sp62",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98821,0.00066617,2.7538e-05,-4.40464e-08,2.28871e-11,-3102.11,5.10394], Tmin=(10,'K'), Tmax=(497.281,'K')),
            NASAPolynomial(coeffs=[2.57029,0.0120625,-6.81044e-06,1.9652e-09,-2.25996e-13,-2960.98,10.9552], Tmin=(497.281,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-25.7984,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 62,
    label = "sp63",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98557,0.00081614,2.39113e-05,-4.16647e-08,2.2422e-11,-15845.3,5.00016], Tmin=(10,'K'), Tmax=(585.9,'K')),
            NASAPolynomial(coeffs=[3.22459,0.00927084,-6.07878e-06,1.95446e-09,-2.41511e-13,-15812.1,7.78719], Tmin=(585.9,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-131.752,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 63,
    label = "sp64",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {6,S}
2 N u0 p1 c0 {1,S} {4,S} {7,S}
3 O u0 p2 c0 {1,S} {5,S}
4 N u0 p1 c0 {2,S} {8,D}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {4,D}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74452,0.0219328,6.46753e-05,-2.15479e-07,1.83318e-10,26092.5,10.8391], Tmin=(10,'K'), Tmax=(418.732,'K')),
            NASAPolynomial(coeffs=[4.42589,0.0305678,-2.0506e-05,6.50861e-09,-7.83785e-13,25902.7,6.55969], Tmin=(418.732,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (216.941,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 64,
    label = "sp65",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  N u0 p0 c+1 {3,S} {5,S} {9,D}
3  N u0 p2 c-1 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6007,0.0347162,6.138e-06,-5.02014e-08,3.2224e-11,-7439.18,11.3288], Tmin=(10,'K'), Tmax=(634.482,'K')),
            NASAPolynomial(coeffs=[5.11114,0.0359991,-2.24403e-05,6.66761e-09,-7.59638e-13,-7848.34,3.01507], Tmin=(634.482,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.9014,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 65,
    label = "sp66",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u1 p1 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2601,0.0800008,-0.000440643,9.88288e-07,-7.73052e-10,1015.81,12.4793], Tmin=(10,'K'), Tmax=(406.255,'K')),
            NASAPolynomial(coeffs=[6.34073,0.00541748,-1.87445e-06,1.44996e-10,2.40375e-14,1130.67,4.88635], Tmin=(406.255,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (8.42248,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (99.7737,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 66,
    label = "sp67",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.507,-0.000405655,1.23223e-06,1.57366e-09,-2.02163e-12,-1252.36,4.69557], Tmin=(10,'K'), Tmax=(633.969,'K')),
            NASAPolynomial(coeffs=[2.87702,0.00206506,-1.05487e-06,2.36436e-10,-1.85731e-14,-1142.25,7.68611], Tmin=(633.969,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-10.4099,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 67,
    label = "sp68",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 N u2 p1 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03145,-0.00208283,1.38518e-05,-1.64262e-08,6.39762e-12,23881.9,4.89883], Tmin=(10,'K'), Tmax=(793.019,'K')),
            NASAPolynomial(coeffs=[3.19168,0.0043187,-2.35309e-06,6.40517e-10,-6.83096e-14,23947,8.32615], Tmin=(793.019,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (198.573,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 68,
    label = "sp69",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u0 p1 c0 {2,S} {4,S} {7,S}
4 N u0 p1 c0 {1,S} {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14115,-0.0102611,0.000100061,-1.37596e-07,6.10887e-11,67314.1,7.95342], Tmin=(10,'K'), Tmax=(705.727,'K')),
            NASAPolynomial(coeffs=[-0.182616,0.0297995,-1.81462e-05,5.29836e-09,-5.93604e-13,67537,24.5619], Tmin=(705.727,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (559.701,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 69,
    label = "sp70",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97549,0.00145082,6.29809e-05,-1.0761e-07,5.98527e-11,-24822.3,7.00875], Tmin=(10,'K'), Tmax=(463.471,'K')),
            NASAPolynomial(coeffs=[1.18424,0.0255265,-1.48924e-05,4.33793e-09,-4.9697e-13,-24563.4,18.3301], Tmin=(463.471,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-206.396,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 70,
    label = "sp71",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {5,S} {13,S}
3  O u0 p2 c0 {6,S} {12,S}
4  N u0 p1 c0 {1,S} {5,S} {11,S}
5  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7175,0.0344367,-2.82128e-06,-1.33476e-08,5.52134e-12,-49089.5,10.8137], Tmin=(10,'K'), Tmax=(1129.5,'K')),
            NASAPolynomial(coeffs=[7.58732,0.032657,-1.62944e-05,3.95187e-09,-3.76545e-13,-50724.3,-11.6944], Tmin=(1129.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-408.14,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 71,
    label = "sp72",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01913,-0.00112477,6.88054e-06,-1.26951e-09,-2.21548e-12,-4861.34,0.274982], Tmin=(10,'K'), Tmax=(654.712,'K')),
            NASAPolynomial(coeffs=[2.40706,0.00563581,-1.53269e-06,9.23261e-11,1.57259e-14,-4584.06,7.87496], Tmin=(654.712,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.4124,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 72,
    label = "sp73",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  N u0 p0 c+1 {3,D} {5,S} {9,S}
3  N u0 p1 c0 {1,S} {2,D}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p3 c-1 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62855,0.0321833,2.39169e-05,-9.05838e-08,6.15523e-11,-7360.29,11.2846], Tmin=(10,'K'), Tmax=(552.506,'K')),
            NASAPolynomial(coeffs=[4.56292,0.0376343,-2.40464e-05,7.30658e-09,-8.48475e-13,-7649.99,5.64385], Tmin=(552.506,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.2405,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 73,
    label = "sp74",
    molecule = 
"""
multiplicity 3
1 N u1 p1 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02405,-0.00144034,9.54912e-06,-9.64149e-09,3.18486e-12,20336.2,4.71931], Tmin=(10,'K'), Tmax=(905.188,'K')),
            NASAPolynomial(coeffs=[3.00353,0.00434083,-2.138e-06,5.17849e-10,-4.96041e-14,20468.9,9.25333], Tmin=(905.188,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (169.091,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 74,
    label = "sp75",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {3,S} {5,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p2 c-1 {1,S} {6,S}
4 O u0 p2 c0 {2,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9089,0.00656704,8.57739e-05,-2.27903e-07,1.80776e-10,29404.3,9.43343], Tmin=(10,'K'), Tmax=(426.245,'K')),
            NASAPolynomial(coeffs=[3.88688,0.0207606,-1.33957e-05,4.18723e-09,-5.01434e-13,29279.1,8.03044], Tmin=(426.245,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (244.478,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 75,
    label = "sp76",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04166,-0.00250279,1.15444e-05,3.4541e-09,-9.37978e-12,-9324.7,-0.432707], Tmin=(10,'K'), Tmax=(613.213,'K')),
            NASAPolynomial(coeffs=[0.694826,0.0117175,-4.62257e-06,7.8966e-10,-4.15934e-14,-8771.13,15.2439], Tmin=(613.213,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-77.5149,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 76,
    label = "sp77",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,S} {5,D}
2 N u0 p2 c-1 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u1 p2 c0 {1,S}
5 O u0 p2 c0 {1,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94912,0.00293332,6.33245e-05,-1.20419e-07,6.85853e-11,12080.7,9.70671], Tmin=(10,'K'), Tmax=(579.813,'K')),
            NASAPolynomial(coeffs=[2.96758,0.0214998,-1.52222e-05,4.97921e-09,-6.10742e-13,11996.2,12.1973], Tmin=(579.813,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (100.423,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 77,
    label = "sp78",
    molecule = 
"""
multiplicity 3
1 N u2 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49651,0.000235417,-1.43097e-06,2.53132e-09,-1.12358e-12,42441.9,1.81122], Tmin=(10,'K'), Tmax=(878.954,'K')),
            NASAPolynomial(coeffs=[3.31981,5.15759e-05,5.68853e-07,-2.64365e-10,3.53385e-14,42511.1,2.85802], Tmin=(878.954,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (352.881,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 78,
    label = "sp79",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {8,S}
2 O u0 p2 c0 {3,S} {9,S}
3 N u0 p1 c0 {2,S} {4,S} {7,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95154,0.00301781,9.15665e-05,-1.79265e-07,1.10846e-10,-28896.9,8.54114], Tmin=(10,'K'), Tmax=(499.489,'K')),
            NASAPolynomial(coeffs=[1.73812,0.0302066,-1.8502e-05,5.57368e-09,-6.52169e-13,-28793.8,16.5014], Tmin=(499.489,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-240.277,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 79,
    label = "sp80",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u1 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04712,-0.00340059,2.75856e-05,-3.60946e-08,1.56723e-11,10979.2,5.05723], Tmin=(10,'K'), Tmax=(692.94,'K')),
            NASAPolynomial(coeffs=[2.57443,0.00823098,-4.36964e-06,1.16872e-09,-1.23779e-13,11108.1,11.0796], Tmin=(692.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.2936,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 80,
    label = "sp81",
    molecule = 
"""
1 N u0 p0 c+1 {3,D} {4,S} {5,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 N u0 p1 c0 {1,D} {2,S}
4 N u0 p2 c-1 {1,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97597,0.00154152,7.59757e-05,-1.44252e-07,8.97139e-11,47786.8,8.05092], Tmin=(10,'K'), Tmax=(413.129,'K')),
            NASAPolynomial(coeffs=[1.3491,0.0269827,-1.64236e-05,4.89625e-09,-5.67083e-13,48003.8,18.4011], Tmin=(413.129,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (397.316,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 81,
    label = "sp82",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {6,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,D} {5,S}
4 O u0 p2 c0 {2,S} {8,S}
5 N u0 p1 c0 {3,S} {7,D}
6 O u0 p3 c-1 {1,S}
7 O u0 p2 c0 {5,D}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55138,0.040537,-4.47972e-05,2.58787e-08,-6.1088e-12,35641.1,11.3435], Tmin=(10,'K'), Tmax=(977.949,'K')),
            NASAPolynomial(coeffs=[8.77818,0.0191585,-1.20065e-05,3.52544e-09,-3.94504e-13,34618.8,-13.7562], Tmin=(977.949,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (296.291,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 82,
    label = "sp83",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u1 p1 c0 {1,S} {6,S}
4 O u0 p2 c0 {2,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93085,0.0041429,7.49526e-05,-1.54086e-07,9.4416e-11,28220.6,8.90015], Tmin=(10,'K'), Tmax=(551.735,'K')),
            NASAPolynomial(coeffs=[3.69308,0.0213867,-1.41222e-05,4.52774e-09,-5.5573e-13,28010.7,7.76512], Tmin=(551.735,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (234.614,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 83,
    label = "sp84",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,25472.6,-0.461279], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,25472.6,-0.461279], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (211.791,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 84,
    label = "sp85",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  N u0 p1 c0 {1,S} {6,S} {7,S}
6  N u0 p1 c0 {2,S} {5,S} {8,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84376,0.0101763,0.000142738,-3.43273e-07,2.41487e-10,11921.7,10.7821], Tmin=(10,'K'), Tmax=(491.612,'K')),
            NASAPolynomial(coeffs=[4.65541,0.0340223,-2.29294e-05,7.37798e-09,-9.01002e-13,11473.9,3.70026], Tmin=(491.612,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.0868,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 85,
    label = "sp86",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u1 p0 c+1 {1,S} {4,D}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90162,0.00824235,4.54489e-05,-1.90624e-07,2.04745e-10,18674,8.64584], Tmin=(10,'K'), Tmax=(349.473,'K')),
            NASAPolynomial(coeffs=[4.84872,0.00886217,-6.40066e-06,2.12101e-09,-2.6309e-13,18537.9,4.07106], Tmin=(349.473,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (155.276,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 86,
    label = "sp87",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 N u0 p1 c0 {1,D} {5,S}
3 O u0 p3 c-1 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08108,-0.00552806,4.41924e-05,-5.50285e-08,2.23241e-11,18196.8,6.40014], Tmin=(10,'K'), Tmax=(757.328,'K')),
            NASAPolynomial(coeffs=[1.43457,0.0147627,-8.49972e-06,2.36206e-09,-2.54262e-13,18416.7,17.2372], Tmin=(757.328,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.314,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 87,
    label = "sp89",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  N u0 p0 c+1 {3,D} {4,S} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p3 c-1 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73871,0.0325937,-1.27753e-05,-1.37947e-09,1.48136e-12,-44770.2,10.5455], Tmin=(10,'K'), Tmax=(1283.91,'K')),
            NASAPolynomial(coeffs=[9.6498,0.0223482,-1.03508e-05,2.31809e-09,-2.03724e-13,-46961.5,-22.0719], Tmin=(1283.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-372.242,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 88,
    label = "sp90",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {5,S}
3 N u1 p0 c+1 {1,D} {4,S}
4 O u0 p3 c-1 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95512,0.00269693,4.8781e-05,-1.00855e-07,6.19582e-11,20287.4,8.62293], Tmin=(10,'K'), Tmax=(549.2,'K')),
            NASAPolynomial(coeffs=[3.73901,0.0142051,-9.78323e-06,3.17135e-09,-3.8816e-13,20161.3,8.17204], Tmin=(549.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (168.662,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 89,
    label = "sp91",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 N u0 p1 c0 {1,D} {5,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06934,-0.00503397,4.37168e-05,-5.8824e-08,2.5864e-11,8851.01,7.16964], Tmin=(10,'K'), Tmax=(699.648,'K')),
            NASAPolynomial(coeffs=[1.94593,0.01301,-7.62643e-06,2.16031e-09,-2.36832e-13,9003.63,15.6227], Tmin=(699.648,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (73.6018,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (99.7737,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 90,
    label = "sp92",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  N u0 p1 c0 {3,S} {4,S} {7,S}
3  N u0 p1 c0 {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97079,0.00200828,0.000109474,-2.26086e-07,1.54654e-10,-11582.5,8.60636], Tmin=(10,'K'), Tmax=(373.562,'K')),
            NASAPolynomial(coeffs=[0.940826,0.0344407,-2.07082e-05,6.15688e-09,-7.14462e-13,-11356.1,20.2418], Tmin=(373.562,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.3018,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 91,
    label = "sp93",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97413,0.00145195,4.27514e-05,-7.45458e-08,3.96654e-11,22585.3,8.40654], Tmin=(10,'K'), Tmax=(592.236,'K')),
            NASAPolynomial(coeffs=[2.46612,0.0174346,-1.24126e-05,4.08009e-09,-5.0226e-13,22662.3,14.0335], Tmin=(592.236,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (187.773,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 92,
    label = "sp94",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {6,D}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p2 c-1 {1,S} {5,S}
4 O u0 p2 c0 {2,S} {8,S}
5 N u0 p1 c0 {3,S} {7,D}
6 O u0 p2 c0 {1,D}
7 O u0 p2 c0 {5,D}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55145,0.0405398,-4.48089e-05,2.58934e-08,-6.11453e-12,35641,11.3436], Tmin=(10,'K'), Tmax=(977.551,'K')),
            NASAPolynomial(coeffs=[8.77453,0.0191677,-1.20146e-05,3.52839e-09,-3.9489e-13,34619.8,-13.7362], Tmin=(977.551,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (296.29,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 93,
    label = "sp95",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {5,S}
4 N u0 p1 c0 {1,D} {8,S}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u0 p3 c-1 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81274,0.0137969,0.00013062,-3.79085e-07,3.1425e-10,24827,10.3508], Tmin=(10,'K'), Tmax=(423.547,'K')),
            NASAPolynomial(coeffs=[4.92897,0.0298282,-2.02647e-05,6.53685e-09,-7.98563e-13,24494.1,3.11081], Tmin=(423.547,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (206.418,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 94,
    label = "sp96",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70406,0.0379206,0.000160281,-2.62987e-06,6.99142e-09,9136.04,8.91232], Tmin=(10,'K'), Tmax=(164.989,'K')),
            NASAPolynomial(coeffs=[7.43778,0.00142917,8.34464e-07,-7.73527e-10,1.43743e-13,8939.3,-4.60157], Tmin=(164.989,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.6913,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 95,
    label = "sp97",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,T}
2 O u0 p3 c-1 {1,S}
3 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5349,-0.00369429,4.35277e-05,-8.39812e-08,5.30944e-11,10466.2,5.99721], Tmin=(10,'K'), Tmax=(500.362,'K')),
            NASAPolynomial(coeffs=[2.84549,0.00711248,-4.74426e-06,1.48621e-09,-1.76488e-13,10468.9,8.1834], Tmin=(500.362,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (87.0179,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 96,
    label = "sp98",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05877,-0.00383205,5.41147e-05,-6.35653e-08,2.43381e-11,-10683,3.53467], Tmin=(10,'K'), Tmax=(733.479,'K')),
            NASAPolynomial(coeffs=[-0.971593,0.0264859,-1.37869e-05,3.51375e-09,-3.53005e-13,-10022.7,25.715], Tmin=(733.479,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-88.8096,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 97,
    label = "sp99",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95269,0.00280299,4.93274e-05,-1.00947e-07,6.0989e-11,-352.977,7.93874], Tmin=(10,'K'), Tmax=(562.573,'K')),
            NASAPolynomial(coeffs=[3.84494,0.0143086,-9.98485e-06,3.27246e-09,-4.04395e-13,-510.798,6.88617], Tmin=(562.573,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-2.95344,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 98,
    label = "sp100",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {4,S} {5,S}
2  N u0 p1 c0 {1,S} {3,S} {6,S}
3  N u0 p1 c0 {2,S} {9,S} {10,S}
4  N u0 p1 c0 {1,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {5,S} {13,S}
8  O u0 p2 c0 {6,S} {14,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68367,0.0228916,0.000225437,-6.45716e-07,5.27498e-10,33968.5,12.6012], Tmin=(10,'K'), Tmax=(431.624,'K')),
            NASAPolynomial(coeffs=[5.94908,0.0496699,-3.36463e-05,1.08807e-08,-1.33345e-12,33327.9,-1.57963], Tmin=(431.624,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (282.415,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 99,
    label = "sp101",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03195,-0.0019507,9.19476e-06,2.64697e-09,-7.9253e-12,-13508.5,3.46232], Tmin=(10,'K'), Tmax=(594.429,'K')),
            NASAPolynomial(coeffs=[1.44648,0.00944934,-4.43694e-06,9.60407e-10,-7.68335e-14,-13095.2,15.4822], Tmin=(594.429,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-112.305,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 100,
    label = "sp102",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p0 c+1 {1,D} {4,D}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15476,0.0229155,-3.90264e-05,3.25671e-08,-1.02558e-11,32103.7,6.9997], Tmin=(10,'K'), Tmax=(939.04,'K')),
            NASAPolynomial(coeffs=[5.49499,0.00705944,-4.29381e-06,1.23216e-09,-1.35993e-13,31923.8,-2.76123], Tmin=(939.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (266.856,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (87.302,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 101,
    label = "sp103",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05926,-0.00492254,4.7777e-05,-7.62514e-08,3.95569e-11,-8684.42,6.45292], Tmin=(10,'K'), Tmax=(612.836,'K')),
            NASAPolynomial(coeffs=[2.90268,0.00989456,-6.27952e-06,1.90553e-09,-2.20887e-13,-8679.15,10.3529], Tmin=(612.836,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-72.2057,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 102,
    label = "sp104",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 N u0 p2 c-1 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5349,-0.00369423,4.35265e-05,-8.39776e-08,5.30912e-11,10466.2,5.99721], Tmin=(10,'K'), Tmax=(500.37,'K')),
            NASAPolynomial(coeffs=[2.84547,0.00711249,-4.74427e-06,1.48621e-09,-1.76487e-13,10468.9,8.18349], Tmin=(500.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (87.0179,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 103,
    label = "sp105",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96335,0.00225205,5.23103e-05,-1.05151e-07,6.53147e-11,998.878,6.9251], Tmin=(10,'K'), Tmax=(521.307,'K')),
            NASAPolynomial(coeffs=[3.2006,0.0159439,-9.64252e-06,2.92278e-09,-3.46785e-13,971.884,9.08643], Tmin=(521.307,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (8.29299,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 104,
    label = "sp106",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50341,-0.000166215,3.06591e-08,1.44541e-09,-9.49914e-13,486.598,3.08248], Tmin=(10,'K'), Tmax=(806.459,'K')),
            NASAPolynomial(coeffs=[3.10794,0.00079002,1.21868e-07,-1.7567e-10,3.17702e-14,583.075,5.108], Tmin=(806.459,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (4.04703,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 105,
    label = "sp107",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 N u0 p1 c0 {1,S} {5,D}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91401,0.0101113,2.22044e-07,-5.92223e-09,2.50312e-12,1132.18,7.94586], Tmin=(10,'K'), Tmax=(1047.5,'K')),
            NASAPolynomial(coeffs=[5.06758,0.00984306,-5.3177e-06,1.37358e-09,-1.37903e-13,663.547,1.24369], Tmin=(1047.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (9.41882,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 106,
    label = "sp108",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,S} {5,D}
2 N u1 p1 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u0 p3 c-1 {1,S}
5 O u0 p2 c0 {1,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94923,0.00292853,6.33638e-05,-1.20524e-07,6.86713e-11,12080.6,9.70652], Tmin=(10,'K'), Tmax=(579.497,'K')),
            NASAPolynomial(coeffs=[2.9647,0.021508,-1.52301e-05,4.98234e-09,-6.11177e-13,11996.9,12.212], Tmin=(579.497,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (100.422,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 107,
    label = "sp109",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  N u0 p1 c0 {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7352,0.0238585,2.48453e-05,-5.54887e-08,2.71688e-11,-46887.9,10.4539], Tmin=(10,'K'), Tmax=(723.991,'K')),
            NASAPolynomial(coeffs=[3.33661,0.03607,-2.11928e-05,6.00005e-09,-6.57713e-13,-47092.5,10.4365], Tmin=(723.991,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-389.874,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 108,
    label = "sp110",
    molecule = 
"""
multiplicity 2
1 N u0 p2 c-1 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u1 p0 c+1 {1,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94183,0.0038901,5.48071e-05,-1.35181e-07,9.81896e-11,20261.5,8.32455], Tmin=(10,'K'), Tmax=(472.152,'K')),
            NASAPolynomial(coeffs=[4.1051,0.0132239,-8.8928e-06,2.8356e-09,-3.43198e-13,20126.6,6.3944], Tmin=(472.152,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (168.453,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 109,
    label = "sp111",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,D}
3 O u0 p2 c0 {5,D}
4 N u0 p1 c0 {1,S} {2,D}
5 N u0 p1 c0 {1,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85416,0.0117459,7.00289e-05,-2.72759e-07,2.75087e-10,12519.3,8.23187], Tmin=(10,'K'), Tmax=(371.133,'K')),
            NASAPolynomial(coeffs=[5.4281,0.0131058,-9.52472e-06,3.17278e-09,-3.95115e-13,12276.3,0.498483], Tmin=(371.133,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (104.105,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 110,
    label = "sp112",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 N u0 p0 c+1 {1,D} {5,D}
3 O u0 p3 c-1 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93709,0.0109257,-2.63642e-06,-2.62965e-09,1.26082e-12,2634.7,8.07735], Tmin=(10,'K'), Tmax=(1187.45,'K')),
            NASAPolynomial(coeffs=[6.02886,0.00789147,-3.87164e-06,9.09169e-10,-8.32637e-14,1855.07,-3.5646], Tmin=(1187.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (21.9185,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 111,
    label = "sp113",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {7,S}
3 N u0 p1 c0 {1,S} {6,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.977,0.00166296,7.96851e-05,-1.79147e-07,1.33654e-10,-12252.4,8.30541], Tmin=(10,'K'), Tmax=(341.922,'K')),
            NASAPolynomial(coeffs=[2.14357,0.0231121,-1.44142e-05,4.33004e-09,-5.00784e-13,-12127.1,15.183], Tmin=(341.922,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-101.869,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 112,
    label = "sp114",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08329,-0.00764723,8.76947e-05,-1.5467e-07,8.76733e-11,-16109.8,8.16937], Tmin=(10,'K'), Tmax=(572.385,'K')),
            NASAPolynomial(coeffs=[2.81855,0.0154965,-1.04446e-05,3.29857e-09,-3.93229e-13,-16199.3,11.5183], Tmin=(572.385,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.952,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 113,
    label = "sp115",
    molecule = 
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {4,S} {6,S}
3 N u1 p1 c0 {1,S} {7,S}
4 N u1 p1 c0 {2,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94012,0.00361986,8.2107e-05,-1.62692e-07,9.88028e-11,66589.7,9.40694], Tmin=(10,'K'), Tmax=(536.03,'K')),
            NASAPolynomial(coeffs=[2.72882,0.025709,-1.62251e-05,5.02397e-09,-6.01564e-13,66532.1,12.7466], Tmin=(536.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (553.637,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 114,
    label = "sp116",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98343,0.00104816,1.02441e-05,-1.76479e-08,1.08084e-11,16905,0.220458], Tmin=(10,'K'), Tmax=(401.791,'K')),
            NASAPolynomial(coeffs=[3.7039,0.00383109,-1.45855e-07,-4.07845e-10,8.09442e-14,16927.5,1.31413], Tmin=(401.791,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (140.548,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 115,
    label = "sp117",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u0 p1 c0 {1,S} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95036,0.0032532,6.36308e-05,-1.43282e-07,9.87115e-11,10979.4,8.14592], Tmin=(10,'K'), Tmax=(476.144,'K')),
            NASAPolynomial(coeffs=[3.39926,0.0174245,-1.1072e-05,3.39862e-09,-4.01294e-13,10923.7,9.25992], Tmin=(476.144,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.2781,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 116,
    label = "sp118",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9734,0.00122556,7.67021e-05,-1.08223e-07,4.9346e-11,-13346.9,6.77947], Tmin=(10,'K'), Tmax=(568.01,'K')),
            NASAPolynomial(coeffs=[-1.21534,0.0377652,-1.97916e-05,5.03021e-09,-5.00403e-13,-12757.4,28.8773], Tmin=(568.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-110.989,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 117,
    label = "sp119",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99342,0.00039847,1.91287e-05,-3.31776e-08,1.89386e-11,-16115.2,3.82298], Tmin=(10,'K'), Tmax=(449.574,'K')),
            NASAPolynomial(coeffs=[3.2082,0.00737187,-4.09484e-06,1.19631e-09,-1.40477e-13,-16044.5,6.98491], Tmin=(449.574,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.992,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 118,
    label = "sp120",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {5,S} {6,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93252,0.00421929,8.60962e-05,-1.81674e-07,1.17047e-10,18202.6,8.41076], Tmin=(10,'K'), Tmax=(511.432,'K')),
            NASAPolynomial(coeffs=[3.14276,0.0245837,-1.52428e-05,4.66627e-09,-5.54908e-13,18097.8,9.87734], Tmin=(511.432,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.325,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 119,
    label = "sp121",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91846,0.00832208,-1.11362e-06,2.43105e-08,-2.78314e-11,13440.2,5.87478], Tmin=(10,'K'), Tmax=(504.395,'K')),
            NASAPolynomial(coeffs=[1.34338,0.0201011,-1.04421e-05,2.67125e-09,-2.69678e-13,13809.9,17.6255], Tmin=(504.395,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (111.75,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 120,
    label = "sp122",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u1 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04127,-0.00333996,3.20734e-05,-5.08062e-08,2.5569e-11,42814.9,6.23153], Tmin=(10,'K'), Tmax=(651.824,'K')),
            NASAPolynomial(coeffs=[3.50932,0.0062378,-4.49595e-06,1.45539e-09,-1.74594e-13,42750.1,7.54139], Tmin=(651.824,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (355.984,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 121,
    label = "sp123",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,S} {5,D}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u1 p2 c0 {1,S}
5 N u0 p2 c-1 {1,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8948,0.00706856,8.17338e-05,-2.11758e-07,1.56783e-10,39009.6,10.0595], Tmin=(10,'K'), Tmax=(475.46,'K')),
            NASAPolynomial(coeffs=[4.78715,0.0183473,-1.31159e-05,4.33682e-09,-5.36249e-13,38712.4,4.18486], Tmin=(475.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (324.325,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 122,
    label = "sp124",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94199,0.00691276,4.44396e-06,-8.1673e-09,2.95831e-12,9518.93,6.5548], Tmin=(10,'K'), Tmax=(1029.31,'K')),
            NASAPolynomial(coeffs=[4.02927,0.0100207,-5.10865e-06,1.27336e-09,-1.24883e-13,9318.35,5.24413], Tmin=(1029.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (79.1493,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 123,
    label = "sp125",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {5,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,D} {6,S}
4 O u0 p2 c0 {2,S} {7,S}
5 H u0 p0 c0 {1,S}
6 O u0 p3 c-1 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9027,0.00616161,8.9616e-05,-2.07216e-07,1.39916e-10,14519.3,9.26518], Tmin=(10,'K'), Tmax=(512.378,'K')),
            NASAPolynomial(coeffs=[4.4249,0.0220058,-1.50871e-05,4.89558e-09,-6.00918e-13,14204.2,4.54332], Tmin=(512.378,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.692,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

entry(
    index = 124,
    label = "sp126",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u1 p1 c0 {1,S} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96325,0.00254241,4.74394e-05,-1.14398e-07,8.50641e-11,18258.7,7.53167], Tmin=(10,'K'), Tmax=(438.989,'K')),
            NASAPolynomial(coeffs=[3.59804,0.0122574,-7.58074e-06,2.30196e-09,-2.70443e-13,18229.3,8.29196], Tmin=(438.989,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.809,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16
""",
)

