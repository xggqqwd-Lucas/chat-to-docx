# Signal processing and deep learning

A sample technical note for document conversion.

## Conversion request

Export the following note to Word, preserving headings, equations, tables, and code.

## Technical note

### 1. From time domain to frequency domain

Let $x[n]$ be a sampled sequence of length N. Its discrete Fourier transform is:

$$
X[k]=\sum_{n=0}^{N-1}x[n]\exp\left(-\mathrm{i}\frac{2\pi kn}{N}\right)
$$

The index k ranges from 0 to N-1, and i is the imaginary unit. An FFT is an algorithm for computing the discrete Fourier transform.

### 2. Continuous wavelet transform

\[
W_x(a,b)=\frac{1}{\sqrt{|a|}}\int_{-\infty}^{\infty}x(t)\psi^{*}\left(\frac{t-b}{a}\right)\,\mathrm{d}t
\]

a is a nonzero scale parameter, b is the translation parameter, and the asterisk denotes complex conjugation. A discrete implementation also requires sampling, scale selection, and boundary handling.

### 3. Input normalization

$$
z[n]=\frac{x[n]-\mu_{\mathrm{train}}}{\sigma_{\mathrm{train}}+\varepsilon}
$$

Compute the mean and standard deviation from the training set. Use the same statistics for validation and testing. Epsilon is a small positive constant.

### 4. Classification loss

For a batch of B samples and C classes, the cross-entropy loss is:

$$
\mathcal{L}=-\frac{1}{B}\sum_{j=1}^{B}\sum_{c=1}^{C}y_{j,c}\log p_{j,c}
$$

| Step | Input | Output |
|---|---|---|
| Fourier transform | Time-domain samples | Complex spectrum |
| Wavelet analysis | Signal and scale parameters | Multiscale coefficients |
| Classification | Preprocessed signal | Class probabilities |

- Equations should remain editable in Word.
- Formula strings inside code blocks should remain code.

```python
# FFT of a four-sample sequence.
import numpy as np
signal = np.array([0.0, 1.0, 0.0, -1.0])
spectrum = np.fft.fft(signal)
formula_as_code = r"\frac{x-\mu}{\sigma}"
```

## Expected output

Five equation objects: one inline equation and four display equations. The code string is not an equation object. Preserve the headings, table, list, and code block, and check for five `m:oMath` objects in the DOCX.
