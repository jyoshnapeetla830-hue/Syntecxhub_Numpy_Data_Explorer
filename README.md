# NumPy Data Explorer Task 1

A simple Python script that demonstrates NumPy fundamentals using `syntecxhub task1.py`.

## File

- `syntecxhub task1.py` - main script that runs NumPy examples.

## Requirements

- Python 3.x
- NumPy

Install NumPy with:

```powershell
pip install numpy
```

## What the script does

The script covers the following NumPy topics:

- Array creation
  - 1D array
  - 2D array
  - arrays of zeros and ones
- Indexing and slicing
  - single element access
  - slices from 1D and 2D arrays
- Mathematical operations
  - addition, subtraction, multiplication, division
- Statistical operations
  - mean, median, standard deviation, sum
- Reshaping arrays
  - reshape a 1D array into a 2D array
- Broadcasting
  - add a scalar to an array
- Save and load NumPy arrays
  - `np.save` and `np.load`
- Performance comparison
  - Python list addition vs NumPy array addition

## Script structure

The code follows these steps:

1. Import `numpy` and `time`
2. Create example arrays
3. Print array values and shapes
4. Show indexing and slicing results
5. Perform arithmetic operations on arrays
6. Compute statistics over a sample array
7. Reshape a 1D array into a 3x4 array
8. Demonstrate broadcasting with a scalar addition
9. Save the array to `my_array.npy` and load it back
10. Compare runtime for Python list addition and NumPy vectorized addition

## How to run

From the same folder as the script, run:

```powershell
python "syntecxhub task1.py"
```

## Output

The script prints:

- 1D and 2D arrays
- zeros and ones arrays
- indexing and slicing examples
- arithmetic operation results
- computed statistics: mean, median, std, sum
- reshaped array
- loaded array from disk
- comparison timing for list vs NumPy addition

## Notes

- The script saves `my_array.npy` in the current folder.
- This example is for learning NumPy, not a production application.
