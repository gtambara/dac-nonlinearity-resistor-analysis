# dac-nonlinearity-resistor-analysis
When working with converters, precision is important, and it's known that commercial resistors tend to vary in their resistors values. This code is a tool to analise how adequate the chosen tolerance is to your project, based on hte Monte Carlo simulation.

This code works on the r2r topology, and all you have to do is define the value of vref (the voltage reference, or maximum value); rep (number of simulations done); tol (the commercial tolerance for the resistors); rep (the number of repetitions on the random number simulation); and nl_req (non-linearity requirement for approval or failure of tests).

The result is a graph like the one below.

![]()
