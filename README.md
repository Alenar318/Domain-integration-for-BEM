# Domain-integration-for-BEM
This repository reproduces code for the radial basis integration method (RBIM). It contains some subroutines used to generates a meshless quadrature for the integration of tridimensional functions over simple or multi-connected irregular domains.

## Code Structure

- Import the main functions.  
- Read the RBIM quadrature coordinates from an external text file.  
- Read the grid from an external file in **`.mdpa`** format. This file is processed to generate a modified text file that extracts the vertex coordinates and triangle connectivity.  
- Save the vertex coordinates and triangle connectivity so they can be used in another script as needed.  

- Compute the domain integral of a test function analytically by combining **Green's Theorem** and a **geometrical mapping** to be used as a reference value.  

- Build the **augmented radial basis function matrix** and the **integrals vector** to compute the quadrature weights. 
- Compute the integral of the test fuction using the RBIM quadrature in order to check the percentage of error between the two approaches. 
- Save the quadrature weights and point coordinates in a text file so they can be used in another script as needed.  

## Examples

Files for computing the integral of the test function 'f(x,y,z)= 3x^2+y+z' over two tridimensional domains were included 

## Cite this work

If you use this code, please consider citing this work