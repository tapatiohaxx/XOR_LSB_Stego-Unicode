
# README for XOR_LSB_Stego

## Overview
XOR_LSB_Stego is a Python-based implementation of a novel image steganography technique described in the accompanying paper. This technique enhances the security of the Least Significant Bit (LSB) replacement method by introducing an XOR operation with the 7th bit of RGB components before embedding the data in the 8th bit. This README provides instructions on installation, usage, and understanding the underlying method.

## Installation

### Requirements
- Python 3.x
- Dependencies listed in `requirements.txt`

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/JustinPack/XOR_LSB_Stego-Unicode.git
   ```
2. Navigate to the cloned directory:
   ```
   cd XOR_LSB_Stego-Unicode
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Basic Command
To use the XOR_LSB_Stego tool, just run the script:
```
python xorsteg.py
```

### Example Usage

#### Embedding Data
<img src="Examples/embedding_example.png" width="300" />

#### Extracting Data
<img src="Examples/extraction_example.png" width="300" />


## Methodology

### Abstract from the Paper
The paper proposes a highly secure data hiding technique in the spatial domain of image steganography. It involves an XOR operation with the 7th bit of each RGB component, followed by embedding the output in the 8th bit. This approach ensures no trace of the original message in the cover object without using an external key. The method shows high PSNR (55.90 dB) and low MSE, indicating enhanced imperceptibility and security compared to other techniques.

### Key Concepts
- **Least Significant Bit (LSB) Replacement**: A popular method in image steganography for its simplicity and effectiveness.
- **XOR Operation**: Enhances security by manipulating the 7th bit of RGB components before data embedding.
- **PSNR and MSE Analysis**: Used to evaluate the quality and security of the steganographic technique.

## Contribution
Feel free to contribute to this project by submitting pull requests or opening issues for bugs and feature requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Special Thanks
I'd like to give a very special thanks to [JustinPack][https://github.com/JustinPack] for helping to develop tunctional extraction and embedding logic. Also, I'd like to thank [Mark Tolonen][https://stackoverflow.com/users/235698/mark-tolonen] for giving the hint for solving a longstanding issue with embedding and extracting Unicode characters.

