struct {
    double xmeas[41], xmv[12];
} pv_;

#define pv pv_

struct {
    int idv[20];
} dvec_;

#define dvec_1 dvec_

struct {
    double setpt[20], deltat;
} ctrlall;

#define ctrlall ctrlall

enum Flag {
    A,
    B, 
    C
} flag;

struct ctrl {
    double gain, taui, errold;
};
struct ctrl ctrl1_;
struct ctrl ctrl2_;
struct ctrl ctrl3_;
struct ctrl ctrl4_;
struct ctrl ctrl5_;
struct ctrl ctrl6_;
struct ctrl ctrl7_;
struct ctrl ctrl8_;
struct ctrl ctrl9_;
struct ctrl ctrl10_;
struct ctrl ctrl11_;
struct ctrl ctrl12_;
struct ctrl ctrl13_;
struct ctrl ctrl14_;
struct ctrl ctrl15_;
struct ctrl ctrl16_;
struct ctrl ctrl17_;
struct ctrl ctrl18_;
struct ctrl ctrl18_;
struct ctrl ctrl19_;
struct ctrl ctrl20_;
struct ctrl ctrl21_;
struct ctrl ctrl22_;

/* Table of constant values */

static int c__9 = 9;
static int c__1 = 1;
static int c__3 = 3;


/*               Tennessee Eastman Process Control Test Problem */

/* 			Original codes written by */

/*                    James J. Downs and Ernest F. Vogel */

/*                  Process and Control Systems Engineering */
/*                        Tennessee Eastman Company */
/*                              P.O. Box 511 */
/*                          Kingsport, Tennessee 37662 */

/* -------------------------------------------------------------------- */

/*  New version is a closed-loop plant-wide control scheme for */
/*  the Tennessee Eastman Process Control Test Problem */

/*  The modifications are by: */

/* 	      Evan L. Russell, Leo H. Chiang and Richard D. Braatz */

/* 		     Large Scale Systems Research Laboratory */
/* 	                Department of Chemical Engineering */
/* 		    University of Illinois at Urbana-Champaign */
/* 	                 600 South Mathews Avenue, Box C-3 */
/* 			      Urbana, Illinois 61801 */
/* 		 	    http://brahms.scs.uiuc.edu */

/* The modified text is Copyright 1998-2002 by The Board of Trustees */
/* of the University of Illinois.  All rights reserved. */

/* Permission hereby granted, free of charge, to any person obtaining a copy */
/* of this software and associated documentation files (the "Software"), to */
/* deal with the Software without restriction, including without limitation */
/* the rights to use, copy, modify, merge, publish, distribute, sublicense, */
/* and/or sell copies of the Software, and to permit persons to whom the */
/* Software is furnished to do so, subject to the following conditions: */
/* 		1. Redistributions of source code must retain the above copyright */
/* 		   notice, this list of conditions and the following disclaimers. */
/* 		2. Redistributions in binary form must reproduce the above */
/* 		   copyright notice, this list of conditions and the following */
/* 		   disclaimers in the documentation and/or other materials */
/* 		   provided with the distribution. */
/* 		3. Neither the names of Large Scale Research Systems Laboratory, */
/* 		   University of Illinois, nor the names of its contributors may */
/* 		   be used to endorse or promote products derived from this */
/* 		   Software without specific prior written permission. */

/* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS */
/* OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, */
/* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL */
/* THE CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR */
/* OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, */
/* ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER */
/* DEALINGS IN THE SOFTWARE. */
/* ---------------------------------------------------------------------- */

/*  Users should cite the original code using the following references: */

/*    J.J. Downs and E.F. Vogel, "A plant-wide industrial process control */
/*    problem." Presented at the AIChE 1990 Annual Meeting, Session on */
/*    Industrial Challenge Problems in Process Control, Paper #24a */
/*    Chicago, Illinois, November 14, 1990. */

/*    J.J. Downs and E.F. Vogel, "A plant-wide industrial process control */
/*    problem," Computers and Chemical Engineering, 17:245-255 (1993). */

/*  Users should cite the modified code using the following references: */

/*    E.L. Russell, L.H. Chiang, and R.D. Braatz. Data-driven Techniques */
/*    for Fault Detection and Diagnosis in Chemical Processes, Springer-Verlag, */
/*    London, 2000. */

/*    L.H. Chiang, E.L. Russell, and R.D. Braatz. Fault Detection and */
/*    Diagnosis in Industrial Systems, Springer-Verlag, London, 2001. */

/*    L.H. Chiang, E.L. Russell, and R.D. Braatz. "Fault diagnosis in */
/*    chemical processes using Fisher discriminant analysis, discriminant */
/*    partial least squares, and principal component analysis," Chemometrics */
/*    and Intelligent Laboratory Systems, 50:243-252, 2000. */

/*    E.L. Russell, L.H. Chiang, and R.D. Braatz. "Fault detection in */
/*    industrial processes using canonical variate analysis and dynamic */
/*    principal component analysis," Chemometrics and Intelligent Laboratory */
/*    Systems, 51:81-93, 2000. */


/*  Main program for demonstrating application of the modified Tennessee Eastman */
/*  Process Control Test Problem */

/*  5) To ensure the randomness of the measurement noises, the random number */
/*     G in the sub program (teprob.f, line 1187) has to be changed each time before */
/*     running 'temain_mod.f'. */

/*  6) Save the changes in 'temain_mod.f' and 'teprob.f' and compile the program in */
/*      unix by typing */
/*      f77 temain_mod.f teprob.f */

/*  7) Run the program by typing */
/*      a.out */


/* ============================================================================= */


/*  MEASUREMENT AND VALVE COMMON BLOCK */

int main(void)
{
    /* Format strings */
    static char fmt_111[] = "(1x,i6)";

    /* System generated locals */
    int i__1;
    olist o__1;
    cllist cl__1;

    /* Builtin functions */
    int f_open(olist *), s_wsle(cilist *), do_lio(int *, int *, 
	    char *, ftnlen), e_wsle(void), s_wsfe(cilist *), do_fio(int *,
	     char *, ftnlen), e_wsfe(void), f_clos(cllist *);
    /* Subroutine */ int s_stop(char *, ftnlen);

    /* Local variables */
    extern /* Subroutine */ int conshand_(void);
    static int i__, nn;
    static double yp[50], yy[50], time;
    static int test, npts, test1, test3, test4;
    static real sspts;
    extern /* Subroutine */ int teinit_(int *, double *, double *,
	     double *), intgtr_(int *, double *, double *, 
	    double *, double *), output_(void), contrl1_(void), 
	    contrl2_(void), contrl3_(void), contrl4_(void), contrl5_(void), 
	    contrl6_(void), contrl7_(void), contrl8_(void), contrl9_(void), 
	    contrl10_(void), contrl11_(void), contrl13_(void), contrl14_(void)
	    , contrl15_(void), contrl16_(void), contrl17_(void), contrl18_(
	    void), contrl19_(void), contrl20_(void);

    /* Fortran I/O blocks */
    static cilist io___11 = { 0, 6, 0, 0, 0 };
    static cilist io___13 = { 0, 111, 0, fmt_111, 0 };
    static cilist io___14 = { 0, 6, 0, 0, 0 };



/*   DISTURBANCE VECTOR COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */

/*      DOUBLE PRECISION SETPT, GAIN, TAUI, ERROLD, DELTAT */
/*      COMMON/CTRL/ SETPT, GAIN, TAUI, ERROLD, DELTAT */


/*  Local Variables */



/*  Set the number of differential equations (states).  The process has 50 */
/*  states.  If the user wishes to integrate additional states, NN must be */
/*  increased by the number of additional differential equations. */

    nn = 50;

/*  Set the number of points to simulate */

    npts = 172800;

/*  Set the number of pints to simulate in steady state operation */

    sspts = 28800.f;

/*  Integrator Step Size:  1 Second Converted to Hours */

    ctrlall.deltat = 2.7777777777777778e-4f;

/*  Initialize Process */
/*  (Sets TIME to zero) */

    teinit_(&nn, &time, yy, yp);

/*  Set Controller Parameters */
/*  Make a Stripper Level Set Point Change of +15% */

/* C      SETPT = XMEAS(15) + 15.0 */
/* C      GAIN = 2.0 */
/* C      TAUI = 5.0 */
/* C      ERROLD = 0.0 */
    ctrlall.setpt[0] = 3664.f;
    ctrl1_.gain = 1.f;
    ctrl1_.errold = 0.f;
    ctrlall.setpt[1] = 4509.3f;
    ctrl2_.gain = 1.f;
    ctrl2_.errold = 0.f;
    ctrlall.setpt[2] = .25052f;
    ctrl3_.gain = 1.f;
    ctrl3_.errold = 0.f;
    ctrlall.setpt[3] = 9.3477f;
    ctrl4_.gain = 1.f;
    ctrl4_.errold = 0.f;
    ctrlall.setpt[4] = 26.902f;
    ctrl5_.gain = -.083f;
    ctrl5_.taui = 2.7777777777777778e-4f;
    ctrl5_.errold = 0.f;
    ctrlall.setpt[5] = .33712f;
    ctrl6_.gain = 1.22f;
    ctrl6_.errold = 0.f;
    ctrlall.setpt[6] = 50.f;
    ctrl7_.gain = -2.06f;
    ctrl7_.errold = 0.f;
    ctrlall.setpt[7] = 50.f;
    ctrl8_.gain = -1.62f;
    ctrl8_.errold = 0.f;
    ctrlall.setpt[8] = 230.31f;
    ctrl9_.gain = .41f;
    ctrl9_.errold = 0.f;
    ctrlall.setpt[9] = 94.599f;
    ctrl10_.gain = -1.5600000000000001f;
    ctrl10_.taui = .40333333333333332f;
    ctrl10_.errold = 0.f;
    ctrlall.setpt[10] = 22.949f;
    ctrl11_.gain = 1.09f;
    ctrl11_.taui = .72222222222222221f;
    ctrl11_.errold = 0.f;
    ctrlall.setpt[12] = 32.188f;
    ctrl13_.gain = 18.f;
    ctrl13_.taui = .88f;
    ctrl13_.errold = 0.f;
    ctrlall.setpt[13] = 6.882f;
    ctrl14_.gain = 8.3f;
    ctrl14_.taui = .88f;
    ctrl14_.errold = 0.f;
    ctrlall.setpt[14] = 18.776f;
    ctrl15_.gain = 2.37f;
    ctrl15_.taui = 1.4080555555555556f;
    ctrl15_.errold = 0.f;
    ctrlall.setpt[15] = 65.731f;
    ctrl16_.gain = .16899999999999998f;
    ctrl16_.taui = .065555555555555561f;
    ctrl16_.errold = 0.f;
    ctrlall.setpt[16] = 75.f;
    ctrl17_.gain = 1.1099999999999999f;
    ctrl17_.taui = .88f;
    ctrl17_.errold = 0.f;
    ctrlall.setpt[17] = 120.4f;
    ctrl18_.gain = 28.300000000000001f;
    ctrl18_.taui = .27277777777777779f;
    ctrl18_.errold = 0.f;
    ctrlall.setpt[18] = 13.823f;
    ctrl19_.gain = -5.5466666666666669f;
    ctrl19_.taui = 1.76f;
    ctrl19_.errold = 0.f;
    ctrlall.setpt[19] = .8357f;
    ctrl20_.gain = -3.2600000000000002f;
    ctrl20_.taui = 3.4466666666666668f;
    ctrl20_.errold = 0.f;
    ctrlall.setpt[11] = 2633.7f;
    ctrl22_.gain = -5.f;
    ctrl22_.taui = .27777777777777779f;
    ctrl22_.errold = 0.f;

/*    Example Disturbance: */
/*    Change Reactor Cooling */

    pv.xmv[0] = 63.052999999999997f;
    pv.xmv[1] = 53.979999999999997f;
    pv.xmv[2] = 24.643999999999998f;
    pv.xmv[3] = 61.302f;
    pv.xmv[4] = 22.210000000000001f;
    pv.xmv[5] = 40.064f;
    pv.xmv[6] = 38.100000000000001f;
    pv.xmv[7] = 46.533999999999999f;
    pv.xmv[8] = 47.445999999999998f;
    pv.xmv[9] = 41.106000000000002f;
    pv.xmv[10] = 18.114000000000001f;

/* 	SETPT(6)=SETPT(6) + 0.2 */

/*  Set all Disturbance Flags to OFF */

    for (int i = 0; i < 20; i++) {
	    dvec_1.idv[i] = 0;
    }
    o__1.oerr = 0;
    o__1.ounit = 111;
    o__1.ofnmlen = 17;
    o__1.ofnm = "~/TE_data_inc.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 1111;
    o__1.ofnmlen = 17;
    o__1.ofnm = "~/TE_data_mv1.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 1112;
    o__1.ofnmlen = 17;
    o__1.ofnm = "~/TE_data_mv2.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 1113;
    o__1.ofnmlen = 17;
    o__1.ofnm = "~/TE_data_mv3.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2111;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me01.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2112;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me02.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2113;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me03.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2114;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me04.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2115;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me05.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2116;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me06.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2117;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me07.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2118;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me08.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2119;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me09.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2120;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me10.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);
    o__1.oerr = 0;
    o__1.ounit = 2121;
    o__1.ofnmlen = 18;
    o__1.ofnm = "~/TE_data_me11.dat";
    o__1.orl = 0;
    o__1.osta = "new";
    o__1.oacc = 0;
    o__1.ofm = 0;
    o__1.oblnk = 0;
    f_open(&o__1);


/*  Simulation Loop */

    i__1 = npts;
    for (i__ = 1; i__ <= i__1; ++i__) {
	if ((real) i__ >= sspts) {
	    dvec_1.idv[11] = 1;
	}
	test = i__ % 3;
	if (test == 0) {
	    contrl1_();
	    contrl2_();
	    contrl3_();
	    contrl4_();
	    contrl5_();
	    contrl6_();
	    contrl7_();
	    contrl8_();
	    contrl9_();
	    contrl10_();
	    contrl11_();
	    contrl16_();
	    contrl17_();
	    contrl18_();
	}
	test1 = i__ % 360;
	if (test1 == 0) {
	    contrl13_();
	    contrl14_();
	    contrl15_();
	    contrl19_();
	}
	test1 = i__ % 900;
	if (test1 == 0) {
	    contrl20_();
	}
	test3 = i__ % 5000;
	if (test3 == 0) {
	    s_wsle(&io___11);
	    do_lio(&c__9, &c__1, "Simulation time (in seconds) = ", (ftnlen)
		    31);
	    do_lio(&c__3, &c__1, (char *)&i__, (ftnlen)sizeof(int));
	    e_wsle();
	}

	test4 = i__ % 180;
	if (test4 == 0) {
	    output_();
	    s_wsfe(&io___13);
	    do_fio(&c__1, (char *)&i__, (ftnlen)sizeof(int));
	    e_wsfe();
	}

	intgtr_(&nn, &time, &ctrlall.deltat, yy, yp);

	conshand_();

/* L1000: */
    }
    s_wsle(&io___14);
    do_lio(&c__9, &c__1, "Simulation is done. ", (ftnlen)20);
    e_wsle();

    cl__1.cerr = 0;
    cl__1.cunit = 111;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 1111;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 1112;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 1113;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2111;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2112;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2113;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2114;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2115;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2116;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2117;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2118;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2119;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2120;
    cl__1.csta = 0;
    f_clos(&cl__1);
    cl__1.cerr = 0;
    cl__1.cunit = 2121;
    cl__1.csta = 0;
    f_clos(&cl__1);
    s_stop("", (ftnlen)0);
    return 0;
} /* MAIN__ */


/* ============================================================================= */

/* C      SUBROUTINE CONTRL */

/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */

/* C      DOUBLE PRECISION XMEAS, XMV */
/* C      COMMON/PV/ XMEAS(41), XMV(12) */

/*   CONTROLLER COMMON BLOCK */

/* C      DOUBLE PRECISION SETPT, GAIN, TAUI, ERROLD, DELTAT */
/* C      COMMON/CTRL/ SETPT, GAIN, TAUI, ERROLD, DELTAT */

/* C      DOUBLE PRECISION ERR, DXMV */

/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

/* C      ERR = SETPT - XMEAS(15) */

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

/* C      DXMV = GAIN * ( ( ERR - ERROLD ) + ERR * DELTAT * 60. / TAUI ) */

/* C      XMV(8) = XMV(8) - DXMV */

/* C      ERROLD = ERR */

/* C      RETURN */
/* C      END */

/* ============================================================================= */
 
/**
 * 1. ctrl1, 1, 5811.f, 1
 * 2. ctrl2, 2, 8354.f, 2
 * 3. ctrl3, 3, 1.017f, 0
 * 4. ctrl4, 4, 15.25f, 3
 * 7. ctrl7, 7, 70.f, 11
 * 8. ctrl8, 8, 70.f, 14
 * 9. ctrl9, 9, 460.f, 18
 */
int contrl_A(struct ctrl* ctrl_i, int i, double constant, int xmeas_i) {
    // calculate error
    static double err, dxmv;
    err = (ctrlall.setpt[i-1] - pv.xmeas[xmeas_i]) * 100.f / constant;

    // Proportional-Integral controller (velocity form)
    dxmv = ctrl_i->gain * (err - ctrl_i->errold);
    pv.xmv[i-1] += dxmv;
    ctrl_i->errold = err;
    return 0;
}

/**
 * 5. ctrl5, 4, 53.f, 4
 * 10. ctrl10, 10, 150.f, 20
 * 11. ctrl11, 11, 46.f, 16
 */
int contrl_B(struct ctrl* ctrl_i, int i, double constant, int xmeas_i) {
    // calculate error
    static double err, dxmv;
    err = (ctrlall.setpt[i-1] - pv.xmeas[xmeas_i]) * 100.f / constant;

    // Proportional-Integral controller (velocity form)
    dxmv = ctrl_i->gain * (err - ctrl_i->errold + err * ctrlall.deltat * 3.f / ctrl_i->taui);
    pv.xmv[i-1] += dxmv;
    ctrl_i->errold = err;
    return 0;
}

/**
 * 6. ctrl6, 6
 */
int contrl_C(struct ctrl* ctrl_i, int i) {
    static double err, dxmv;
    static double setpoint;
    static double xmeas_high, xmeas_medium, xmeas_low;
    static double xmv_high, xmv_medium, xmv_low;
    int xmeas_i1, xmeas_i2;

    xmeas_i1 = 12;
    xmeas_i2 = 9;

    xmeas_high = 2950;
    xmeas_medium = 2633.7;
    xmeas_low = 2300;

    setpoint = 0.33712;

    xmv_high = 100;
    xmv_medium = 40.06;
    xmv_low = 0;
    
    if (pv.xmeas[xmeas_i1] >= xmeas_high) {
        pv.xmv[i-1] = xmv_high;
        flag = B;
    } else if (flag == B && pv.xmeas[xmeas_i1] >= xmeas_medium) {
	    pv.xmv[i-1] = xmv_high;
    } else if (flag == B && pv.xmeas[xmeas_i1] <= xmeas_medium) {
        pv.xmv[i-1] = xmv_medium;
        ctrlall.setpt[i-1] = setpoint;
        ctrl_i->errold = 0.f;
        flag = A;
    } else if (pv.xmeas[xmeas_i1] <= xmeas_low) {
        pv.xmv[i-1] = xmv_low;
        flag = C;
    } else if (flag = C && pv.xmeas[xmeas_i1] <= xmeas_medium) {
	    pv.xmv[i-1] = 0.f;
    } else if (flag = C && pv.xmeas[xmeas_i1] >= xmeas_medium) {
        pv.xmv[i-1] = xmv_medium;
        ctrlall.setpt[i-1] = setpoint;
        ctrl_i->errold = 0.f;
        flag = A;
    } else {
        flag = A;
        err = (ctrlall.setpt[i-1] - pv.xmeas[xmeas_i2]) * 100.f / 1.f;
        dxmv = ctrl_i->gain * (err - ctrl_i->errold);
        pv.xmv[i-1] += dxmv;
        ctrl_i->errold = err;
    }

    return 0;
}


/* ============================================================================= */

/* Subroutine */ int contrl13_(void)
{
    static double err13, dxmv;


/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */



/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

    err13 = (ctrlall.setpt[12] - pv.xmeas[22]) * 100.f / 100.f;

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

    dxmv = ctrl13_1.gain13 * (err13 - ctrl13_1.errold13 + err13 * 
	    ctrlall.deltat * 360.f / ctrl13_1.taui13);

    ctrlall.setpt[2] += dxmv * 1.017f / 100.f;

    ctrl13_1.errold13 = err13;

    return 0;
} /* contrl13_ */


/* ============================================================================= */

/* Subroutine */ int contrl14_(void)
{
    static double err14, dxmv;


/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */



/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

    err14 = (ctrlall.setpt[13] - pv.xmeas[25]) * 100.f / 100.f;

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

    dxmv = ctrl14_1.gain14 * (err14 - ctrl14_1.errold14 + err14 * 
	    ctrlall.deltat * 360.f / ctrl14_1.taui14);

    ctrlall.setpt[0] += dxmv * 5811.f / 100.f;

    ctrl14_1.errold14 = err14;

    return 0;
} /* contrl14_ */


/* ============================================================================= */

/* Subroutine */ int contrl15_(void)
{
    static double err15, dxmv;


/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */



/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

    err15 = (ctrlall.setpt[14] - pv.xmeas[26]) * 100.f / 100.f;

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

    dxmv = ctrl15_1.gain15 * (err15 - ctrl15_1.errold15 + err15 * 
	    ctrlall.deltat * 360.f / ctrl15_1.taui15);

    ctrlall.setpt[1] += dxmv * 8354.f / 100.f;

    ctrl15_1.errold15 = err15;

    return 0;
} /* contrl15_ */


/* ============================================================================= */

/* Subroutine */ int contrl16_(void)
{
    static double err16, dxmv;


/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */



/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

    err16 = (ctrlall.setpt[15] - pv.xmeas[17]) * 100.f / 130.f;

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

    dxmv = ctrl16_1.gain16 * (err16 - ctrl16_1.errold16 + err16 * 
	    ctrlall.deltat * 3.f / ctrl16_1.taui16);

    ctrlall.setpt[8] += dxmv * 460.f / 100.f;

    ctrl16_1.errold16 = err16;

    return 0;
} /* contrl16_ */


/* ============================================================================= */

/* Subroutine */ int contrl17_(void)
{
    static double err17, dxmv;


/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */



/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

    err17 = (ctrlall.setpt[16] - pv.xmeas[7]) * 100.f / 50.f;

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

    dxmv = ctrl17_1.gain17 * (err17 - ctrl17_1.errold17 + err17 * 
	    ctrlall.deltat * 3.f / ctrl17_1.taui17);

    ctrlall.setpt[3] += dxmv * 15.25f / 100.f;

    ctrl17_1.errold17 = err17;

    return 0;
} /* contrl17_ */


/* ============================================================================= */

/* Subroutine */ int contrl18_(void)
{
    static double err18, dxmv;


/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */



/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

    err18 = (ctrlall.setpt[17] - pv.xmeas[8]) * 100.f / 150.f;

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

    dxmv = ctrl18_1.gain18 * (err18 - ctrl18_1.errold18 + err18 * 
	    ctrlall.deltat * 3.f / ctrl18_1.taui18);

    ctrlall.setpt[9] += dxmv * 150.f / 100.f;

    ctrl18_1.errold18 = err18;

    return 0;
} /* contrl18_ */


/* ============================================================================= */

/* Subroutine */ int contrl19_(void)
{
    static double err19, dxmv;


/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */



/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

    err19 = (ctrlall.setpt[18] - pv.xmeas[29]) * 100.f / 26.f;
/*      PRINT *, 'ERROLD19= ', ERROLD19 */

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

    dxmv = ctrl19_1.gain19 * (err19 - ctrl19_1.errold19 + err19 * 
	    ctrlall.deltat * 360.f / ctrl19_1.taui19);

    ctrlall.setpt[5] += dxmv * 1.f / 100.f;
/*      PRINT *, 'SETPT(6)= ', SETPT(6) */

    ctrl19_1.errold19 = err19;

    return 0;
} /* contrl19_ */


/* ============================================================================= */

/* Subroutine */ int contrl20_(void)
{
    static double err20, dxmv;


/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */



/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

    err20 = (ctrlall.setpt[19] - pv.xmeas[37]) * 100.f / 1.6f;

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

    dxmv = ctrl20_1.gain20 * (err20 - ctrl20_1.errold20 + err20 * 
	    ctrlall.deltat * 900.f / ctrl20_1.taui20);

    ctrlall.setpt[15] += dxmv * 130.f / 100.f;

    ctrl20_1.errold20 = err20;

    return 0;
} /* contrl20_ */


/* ============================================================================= */

/* Subroutine */ int contrl22_(void)
{
    static double err22, dxmv;


/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */



/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

    err22 = ctrlall.setpt[11] - pv.xmeas[12];

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

    dxmv = ctrl22_1.gain22 * (err22 - ctrl22_1.errold22 + err22 * 
	    ctrlall.deltat * 3.f / ctrl22_1.taui22);

    pv.xmv[5] += dxmv;

    ctrl22_1.errold22 = err22;

    return 0;
} /* contrl22_ */


/* ============================================================================= */

/* Subroutine */ int output_(void)
{
    /* Format strings */
    static char fmt_100[] = "(1x,e13.5,2x,e13.5,2x,e13.5,2x,e13.5)";
    static char fmt_300[] = "(1x,e13.5)";

    /* Builtin functions */
    int s_wsfe(cilist *), do_fio(int *, char *, ftnlen), e_wsfe(void);

    /* Fortran I/O blocks */
    static cilist io___55 = { 0, 1111, 0, fmt_100, 0 };
    static cilist io___56 = { 0, 1112, 0, fmt_100, 0 };
    static cilist io___57 = { 0, 1113, 0, fmt_100, 0 };
    static cilist io___58 = { 0, 2111, 0, fmt_100, 0 };
    static cilist io___59 = { 0, 2112, 0, fmt_100, 0 };
    static cilist io___60 = { 0, 2113, 0, fmt_100, 0 };
    static cilist io___61 = { 0, 2114, 0, fmt_100, 0 };
    static cilist io___62 = { 0, 2115, 0, fmt_100, 0 };
    static cilist io___63 = { 0, 2116, 0, fmt_100, 0 };
    static cilist io___64 = { 0, 2117, 0, fmt_100, 0 };
    static cilist io___65 = { 0, 2118, 0, fmt_100, 0 };
    static cilist io___66 = { 0, 2119, 0, fmt_100, 0 };
    static cilist io___67 = { 0, 2120, 0, fmt_100, 0 };
    static cilist io___68 = { 0, 2121, 0, fmt_300, 0 };




/*   MEASUREMENT AND VALVE COMMON BLOCK */


    s_wsfe(&io___55);
    do_fio(&c__1, (char *)&pv.xmv[0], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmv[1], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmv[2], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmv[3], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___56);
    do_fio(&c__1, (char *)&pv.xmv[4], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmv[5], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmv[6], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmv[7], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___57);
    do_fio(&c__1, (char *)&pv.xmv[8], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmv[9], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmv[10], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmv[11], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___58);
    do_fio(&c__1, (char *)&pv.xmeas[0], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[1], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[2], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[3], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___59);
    do_fio(&c__1, (char *)&pv.xmeas[4], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[5], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[6], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[7], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___60);
    do_fio(&c__1, (char *)&pv.xmeas[8], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[9], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[10], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[11], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___61);
    do_fio(&c__1, (char *)&pv.xmeas[12], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[13], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[14], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[15], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___62);
    do_fio(&c__1, (char *)&pv.xmeas[16], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[17], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[18], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[19], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___63);
    do_fio(&c__1, (char *)&pv.xmeas[20], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[21], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[22], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[23], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___64);
    do_fio(&c__1, (char *)&pv.xmeas[24], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[25], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[26], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[27], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___65);
    do_fio(&c__1, (char *)&pv.xmeas[28], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[29], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[30], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[31], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___66);
    do_fio(&c__1, (char *)&pv.xmeas[32], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[33], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[34], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[35], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___67);
    do_fio(&c__1, (char *)&pv.xmeas[36], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[37], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[38], (ftnlen)sizeof(double));
    do_fio(&c__1, (char *)&pv.xmeas[39], (ftnlen)sizeof(double));
    e_wsfe();
    s_wsfe(&io___68);
    do_fio(&c__1, (char *)&pv.xmeas[40], (ftnlen)sizeof(double));
    e_wsfe();
/* L200: */

    return 0;
} /* output_ */


/* ============================================================================= */

/* Subroutine */ int intgtr_(int *nn, double *time, double *
	deltat, double *yy, double *yp)
{
    /* System generated locals */
    int i__1;

    /* Local variables */
    static int i__;
    extern /* Subroutine */ int tefunc_(int *, double *, double *,
	     double *);


/*  Euler Integration Algorithm */




    /* Parameter adjustments */
    --yp;
    --yy;

    /* Function Body */
    tefunc_(nn, time, &yy[1], &yp[1]);

    *time += *deltat;

    i__1 = *nn;
    for (i__ = 1; i__ <= i__1; ++i__) {

	yy[i__] += yp[i__] * *deltat;

/* L100: */
    }

    return 0;
} /* intgtr_ */


/* ============================================================================= */

/* Subroutine */ int conshand_(void)
{
    /*  Euler Integration Algorithm */
    for (int i = 0; i <= 11; i++) {
        if (pv.xmv[i] <= 0.f) {
            pv.xmv[i] = 0.f;
        }
        if (pv.xmv[i] >= 100.f) {
            pv.xmv[i] = 100.f;
        }
    }

    return 0;
} /* conshand_ */

