UECM3033 Assignment #2 Report
========================================================

- Prepared by: ** Low Kok Chung**
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/LowKokChung/UECM3033_assign1](https://github.com/your_github_id/UECM3033_assign1)

Explain your selection criteria here.

If A is strictly diagonally dominant matrix, 

  then it will be solved by SOR
  
else 

  A will be solved by using LU factorisation.

Explain how you implement your `task1.py` here.

Matrix A is classified as strictly diagonally dominant matrix when (2* diagonal element > sum of row) for all rows.

In python: 

`	try:
        np.linalg.cholesky(A)

If the result is true, then A is a strictly diagonally dominant Matrix

Matrix A will be classified as strictly positive definite matrix when  np.linalg.cholesky(A) comes out the solution without any error.

If any error received, then it will be solved by LU.

else no error received, then it will continue with its progress by checking positive diagonal element and positive eigenvalue.
If all above condition satisfies, then we solve it by SOR, else, solve it by LU.

---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (Handsome.jpg)

![Handsome.jpg](Handsome.jpg)

How many non zero element in $\Sigma$?

For a $M \times N$ sized image, the number of zero in $\Sigma$ will be $(N \times M - N)$ 

Put here your lower and better resolution pictures.

The image with lower resolution
![Handsome_lower_resolution.jpg](Handsome_lower_resoultion.ipg)

The image with better resolution
![Handsome_better_resolution.jpg](Handsome_better_resolution.jpg)

Explain how you generate these pictures from `task2.py`.

First, calculate a new $\Sigma_n$ with $n$ number of eigenvector used, 30 for lower resolution and 200 for better resolution.
Both picture is then obtained by computing the matrix by U $\Sigma_n$ V for each color layer, then merge together to become an image.

What is a sparse matrix?

Sparse matrix is the matrix with high percentage of zero entries.


-----------------------------------

<sup>last modified: 11.3.2016</sup>
