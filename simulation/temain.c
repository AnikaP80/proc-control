/* temain.f -- translated by f2c (version 20200916).
   You must link the resulting object file with libf2c:
	on Microsoft Windows system, link with libf2c.lib;
	on Linux or Unix systems, link with .../path/to/libf2c.a -lm
	or, if you install libf2c.a in a standard place, with -lf2c -lm
	-- in that order, at the end of the command line, as in
		cc *.o -lf2c -lm
	Source for libf2c is in /netlib/f2c/libf2c.zip, e.g.,

		http://www.netlib.org/f2c/libf2c.zip
*/

#include "f2c.h"

/* Common Block Declarations */

struct {
    doublereal xmeas[41], xmv[12];
} pv_;

#define pv_1 pv_

struct {
    integer idv[20];
} dvec_;

#define dvec_1 dvec_

struct {
    doublereal setpt, gain, taui, errold, deltat;
} ctrl_;

#define ctrl_1 ctrl_

/* Table of constant values */

static integer c__1 = 1;

/*               Tennessee Eastman Process Control Test Problem */

/*                    James J. Downs and Ernest F. Vogel */

/*                  Process and Control Systems Engineering */
/*                        Tennessee Eastman Company */
/*                              P.O. Box 511 */
/*                          Kingsport, TN  37662 */


/*  Reference: */
/*    "A Plant-Wide Industrial Process Control Problem" */
/*    Presented at the AIChE 1990 Annual Meeting */
/*    Industrial Challenge Problems in Process Control, Paper #24a */
/*    Chicago, Illinois, November 14, 1990 */

/*    "A Plant-Wide Industrial Process Control Problem" */
/*    Computers and Chemical Engineering, Vol. 17, No. 3, pp. 245-255 */
/*    (1993). */


/*  Main program for demonstrating application of the Tennessee Eastman */
/*  Process Control Test Problem */


/* ============================================================================= */


/*  MEASUREMENT AND VALVE COMMON BLOCK */

/* Main program */ int MAIN__(void)
{
    /* System generated locals */
    integer i__1;

    /* Builtin functions */
    /* Subroutine */ int s_stop(char *, ftnlen);

    /* Local variables */
    static integer i__, nn;
    static doublereal yp[50], yy[50], time;
    static integer npts;
    extern /* Subroutine */ int teinit_(integer *, doublereal *, doublereal *,
	     doublereal *), contrl_(void), intgtr_(integer *, doublereal *, 
	    doublereal *, doublereal *, doublereal *), output_(void);


/*   DISTURBANCE VECTOR COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */


/*  Local Variables */



/*  Set the number of differential equations (states).  The process has 50 */
/*  states.  If the user wishes to integrate additional states, NN must be */
/*  increased by the number of additional differential equations. */

    nn = 50;

/*  Set the number of points to simulate */

    npts = 1000;

/*  Integrator Step Size:  1 Second Converted to Hours */

    ctrl_1.deltat = 2.7777777777777778e-4f;

/*  Initialize Process */
/*  (Sets TIME to zero) */

    teinit_(&nn, &time, yy, yp);

/*  Set Controller Parameters */
/*  Make a Stripper Level Set Point Change of +15% */

    ctrl_1.setpt = pv_1.xmeas[14] + 15.f;
    ctrl_1.gain = 2.f;
    ctrl_1.taui = 5.f;
    ctrl_1.errold = 0.f;

/*  Example Disturbance: */
/*    Change Reactor Cooling */

    pv_1.xmv[9] = 38.f;

/*  Set all Disturbance Flags to OFF */

    for (i__ = 1; i__ <= 20; ++i__) {
	dvec_1.idv[i__ - 1] = 0;
/* L100: */
    }

/*  Simulation Loop */

    i__1 = npts;
    for (i__ = 1; i__ <= i__1; ++i__) {

	contrl_();

	output_();

	intgtr_(&nn, &time, &ctrl_1.deltat, yy, yp);

/* L1000: */
    }

    s_stop("", (ftnlen)0);
    return 0;
} /* MAIN__ */


/* ============================================================================= */

/* Subroutine */ int contrl_(void)
{
    static doublereal err, dxmv;


/*  Discrete control algorithms */


/*   MEASUREMENT AND VALVE COMMON BLOCK */


/*   CONTROLLER COMMON BLOCK */



/*  Example PI Controller: */
/*    Stripper Level Controller */

/*    Calculate Error */

    err = ctrl_1.setpt - pv_1.xmeas[14];

/*    Proportional-Integral Controller (Velocity Form) */
/*         GAIN = Controller Gain */
/*         TAUI = Reset Time (min) */

    dxmv = ctrl_1.gain * (err - ctrl_1.errold + err * ctrl_1.deltat * 60.f / 
	    ctrl_1.taui);

    pv_1.xmv[7] -= dxmv;

    ctrl_1.errold = err;

    return 0;
} /* contrl_ */


/* ============================================================================= */

/* Subroutine */ int output_(void)
{
    /* Format strings */
    static char fmt_100[] = "(1x,\002Reac Temp = \002,f6.2,2x,\002Stripper L"
	    "ev = \002,f6.2,2x,\002Sripper Underflow = \002,f6.2)";

    /* Builtin functions */
    integer s_wsfe(cilist *), do_fio(integer *, char *, ftnlen), e_wsfe(void);

    /* Fortran I/O blocks */
    static cilist io___9 = { 0, 6, 0, fmt_100, 0 };




/*   MEASUREMENT AND VALVE COMMON BLOCK */


    s_wsfe(&io___9);
    do_fio(&c__1, (char *)&pv_1.xmeas[8], (ftnlen)sizeof(doublereal));
    do_fio(&c__1, (char *)&pv_1.xmeas[14], (ftnlen)sizeof(doublereal));
    do_fio(&c__1, (char *)&pv_1.xmv[7], (ftnlen)sizeof(doublereal));
    e_wsfe();

    return 0;
} /* output_ */


/* ============================================================================= */

/* Subroutine */ int intgtr_(integer *nn, doublereal *time, doublereal *
	deltat, doublereal *yy, doublereal *yp)
{
    /* System generated locals */
    integer i__1;

    /* Local variables */
    static integer i__;
    extern /* Subroutine */ int tefunc_(integer *, doublereal *, doublereal *,
	     doublereal *);


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

