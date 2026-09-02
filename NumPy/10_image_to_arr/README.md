# Converting Images to Arrays & Sports Analytics with NumPy

This notebook demonstrates two key applications of NumPy:
1. **Image Processing** - Converting digital images to NumPy arrays
2. **Sports Analytics** - Analyzing player statistics using NumPy arrays and matplotlib visualization

---

## Part 1: Image to Array Conversion

### Overview

Digital images are fundamentally arrays of pixel values. This section shows how to load an image file and convert it into a NumPy array for processing.

### Required Libraries

```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  # Python Imaging Library
```

**Installation:**
```bash
pip install pillow  # For PIL image processing
pip install matplotlib  # For visualization
```

---

### Image Fundamentals

#### What is a Digital Image?

A digital image is a 2D grid of pixels, where each pixel contains:
- **RGB Images**: 3 color channels (Red, Green, Blue)
  - Shape: `(height, width, 3)`
  - Each channel value: 0-255
  
- **Grayscale Images**: Single intensity channel
  - Shape: `(height, width)`
  - Values: 0-255 (0=black, 255=white)

- **RGBA Images**: RGB + Alpha (transparency)
  - Shape: `(height, width, 4)`

#### Example Structure

```
RGB Image: (480, 640, 3)
├─ 480 pixels (height)
├─ 640 pixels (width)
└─ 3 channels (Red, Green, Blue)
```

---

### Step-by-Step: Loading an Image

#### Step 1: Import PIL Image
```python
from PIL import Image
```

#### Step 2: Open Image File
```python
image = Image.open(r'C:\Users\Nikhil\NVS Code\NumPy\08_image_to_arr\images.jpg')
image  # Displays the image
```

**Note:** Use raw string `r''` for file paths to avoid issues with backslashes.

**Output:**
- The PIL image object is displayed
- Type: `<class 'PIL.JpegImageFile.JpegImageFile'>`

#### Step 3: Convert to NumPy Array
```python
image_arr = np.asarray(image)
# or
image_arr = np.array(image)
```

**Alternative methods:**
```python
# More explicit, maintains data type
image_arr = np.array(image, dtype=np.uint8)

# If image is a numpy array already
image_arr = np.asarray(image)
```

#### Step 4: Check Array Properties
```python
# Get shape (dimensions)
print(image_arr.shape)  # e.g., (480, 640, 3) for RGB

# Get data type
print(image_arr.dtype)  # e.g., uint8 (8-bit unsigned integer)

# Get total number of pixels
print(image_arr.size)  # height × width × channels

# Get memory usage
print(image_arr.nbytes)  # Total bytes
```

#### Step 5: Display the Array as Image
```python
plt.imshow(image_arr)
plt.show()
```

---

### Complete Image Processing Example

```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load image
image = Image.open('image_path.jpg')

# Convert to array
img_array = np.asarray(image)

# Display image properties
print(f"Shape: {img_array.shape}")
print(f"Data type: {img_array.dtype}")
print(f"Min value: {img_array.min()}")
print(f"Max value: {img_array.max()}")
print(f"Mean intensity: {img_array.mean():.2f}")

# Display the image
plt.figure(figsize=(10, 8))
plt.imshow(img_array)
plt.axis('off')
plt.title('Original Image')
plt.show()

# Example: Grayscale conversion
if len(img_array.shape) == 3:  # If RGB
    gray = np.dot(img_array[...,:3], [0.2989, 0.5870, 0.1140])
    plt.imshow(gray, cmap='gray')
    plt.show()
```

---

### Common Image Processing Operations

#### 1. Accessing Pixel Values
```python
# Get single pixel (RGB values)
pixel = img_array[y, x]  # [R, G, B]

# Get all red channel
red_channel = img_array[:, :, 0]

# Get specific region (cropping)
cropped = img_array[100:300, 200:400]
```

#### 2. Image Manipulation
```python
# Flip image horizontally
flipped = np.fliplr(img_array)

# Flip image vertically
flipped = np.flipud(img_array)

# Rotate 90 degrees
rotated = np.rot90(img_array)

# Brighten image
brightened = np.clip(img_array * 1.2, 0, 255).astype(np.uint8)

# Darken image
darkened = np.clip(img_array * 0.8, 0, 255).astype(np.uint8)
```

#### 3. Channel Operations
```python
# Extract individual channels
r_channel = img_array[:, :, 0]  # Red
g_channel = img_array[:, :, 1]  # Green
b_channel = img_array[:, :, 2]  # Blue

# Create different colored versions
red_only = img_array.copy()
red_only[:, :, 1] = 0  # Remove green
red_only[:, :, 2] = 0  # Remove blue

# Channel swapping
bgr_to_rgb = img_array[:, :, ::-1]  # Reverse channels
```

---

## Part 2: Sports Analytics - Proof of Concept (POC)

### Overview

This section demonstrates practical data analysis using cricket player statistics from multiple seasons. It shows how to:
- Structure multi-dimensional sports data
- Perform array operations (division, rounding)
- Create professional visualizations
- Analyze player performance trends

---

### Dataset Structure

#### Players (10 cricket players)
```python
Players = ["Sachin", "Rahul", "Smith", "Sami", "Pollard", 
           "Morris", "Samson", "Dhoni", "Kohli", "Sky"]
```

#### Seasons (10 years)
```python
Seasons = ["2015", "2016", "2017", "2018", "2019", "2020", 
           "2021", "2022", "2023", "2024"]
```

#### Data Points per Player
- **Salary**: Annual salary in each season
- **Games**: Number of games played
- **Points**: Total points scored

#### Data Structure
```
Arrays shape: (10 players, 10 seasons)

Example - Sachin's data:
Salary: [15946875, 17718750, 19490625, ...]
Games:  [80, 77, 82, ...]
Points: [2832, 2430, 2323, ...]
```

---

### Data Organization

#### Using NumPy Arrays
```python
# Create individual player data
Sachin_Salary = [15946875, 17718750, 19490625, ...]
Rahul_Salary = [12000000, 12744189, 13488377, ...]
# ... (continue for all players)

# Combine into a matrix (10 players × 10 seasons)
Salary = np.array([Sachin_Salary, Rahul_Salary, Smith_Salary, 
                    Sami_Salary, Pollard_Salary, Morris_Salary, 
                    Samson_Salary, Dhoni_Salary, Kohli_Salary, Sky_Salary])

Games = np.array([Sachin_G, Rahul_G, Smith_G, ...])
Points = np.array([Sachin_PTS, Rahul_PTS, Smith_PTS, ...])
```

#### Using Dictionary for Mapping
```python
# Map player names to row indices
Pdict = {
    "Sachin": 0, "Rahul": 1, "Smith": 2, "Sami": 3, 
    "Pollard": 4, "Morris": 5, "Samson": 6, "Dhoni": 7, 
    "Kohli": 8, "Sky": 9
}

# Map seasons to column indices
Sdict = {
    "2015": 0, "2016": 1, "2017": 2, "2018": 3, "2019": 4,
    "2020": 5, "2021": 6, "2022": 7, "2023": 8, "2024": 9
}

# Access data easily
sachin_salary_2020 = Salary[Pdict["Sachin"], Sdict["2020"]]
```

---

### Array Operations

#### 1. Division Operations
```python
# Integer division (floor division)
salary_per_game_floor = Salary // Games
# Result: Salary divided by Games, rounded down to nearest integer

# Float division
salary_per_game_float = Salary / Games
# Result: Exact decimal division

# Rounding to specific decimals
salary_per_game_rounded = np.round(Salary / Games)
# Result: Salary per game rounded to nearest integer
```

**Example Output:**
```
Sachin's salary per game over seasons:
[199336, 230114, 237690, 259055, 315402, 
 302515, 435939, 357042, 5075633, 671428]
```

#### 2. Accessing Data
```python
# Get entire row (player's data across all seasons)
sachin_salary = Salary[0]  # All of Sachin's salaries

# Get entire column (all players' salary in one season)
salary_2024 = Salary[:, 9]  # All players' 2024 salary

# Get specific element
rahul_2019_salary = Salary[Pdict["Rahul"], Sdict["2019"]]
```

#### 3. Statistical Operations
```python
# Total salary across seasons
total_salary = np.sum(Salary[0])  # Sachin's total

# Average salary
avg_salary = np.mean(Salary[0])  # Sachin's average

# Maximum salary in a season
max_salary = np.max(Salary[0])

# Minimum salary
min_salary = np.min(Salary[0])

# Standard deviation
salary_std = np.std(Salary[0])
```

---

### Data Visualization with Matplotlib

#### Basic Plotting

```python
import matplotlib.pyplot as plt

# Simple line plot
plt.plot(Salary[0])  # Sachin's salary trend
plt.show()
```

---

#### Line Style Options

```python
# Different line styles (ls parameter)
plt.plot(Salary[0], ls='-')    # Solid line (default)
plt.plot(Salary[0], ls='--')   # Dashed line
plt.plot(Salary[0], ls=':')    # Dotted line
plt.plot(Salary[0], ls='-.')   # Dash-dot line

# Line style abbreviations
# '-'   : solid line
# '--'  : dashed line
# ':'   : dotted line
# '-.'  : dash-dot line
```

---

#### Color Options

```python
# Named colors
plt.plot(Salary[0], c='red')      # 'r' abbreviation
plt.plot(Salary[0], c='blue')     # 'b' abbreviation
plt.plot(Salary[0], c='green')    # 'g' abbreviation
plt.plot(Salary[0], c='black')    # 'k' abbreviation

# RGB tuples
plt.plot(Salary[0], c=(1.0, 0.5, 0))  # Orange (R, G, B)
```

---

#### Marker Options

```python
# Different marker styles (marker parameter)
plt.plot(Salary[0], marker='o')   # Circle marker
plt.plot(Salary[0], marker='d')   # Diamond marker
plt.plot(Salary[0], marker='s')   # Square marker
plt.plot(Salary[0], marker='^')   # Triangle marker
plt.plot(Salary[0], marker='*')   # Star marker
plt.plot(Salary[0], marker='+')   # Plus marker
plt.plot(Salary[0], marker='x')   # X marker
```

---

#### Marker Size

```python
# Marker size (ms parameter)
plt.plot(Salary[0], marker='d', ms=10)   # Large markers
plt.plot(Salary[0], marker='d', ms=5)    # Small markers
plt.plot(Salary[0], marker='d', ms=7)    # Medium markers
```

---

#### Complete Plot Example

```python
import warnings
warnings.filterwarnings('ignore')  # Suppress warnings
import matplotlib.pyplot as plt

# Plot multiple players' salary trends
plt.figure(figsize=(12, 6))

# Sachin's data
plt.plot(Salary[0], ls='--', c='green', marker='d', ms=7, 
         label='Sachin')

# Rahul's data
plt.plot(Salary[1], ls=':', c='blue', marker='o', ms=7, 
         label='Rahul')

# Customization
plt.xlabel('Seasons (2015-2024)')
plt.ylabel('Salary (in rupees)')
plt.title('Player Salary Trends Over Seasons')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

#### Advanced Visualization Combinations

```python
# Plot with styling
plt.plot(Salary[0], ls='-', c='r')           # Solid red
plt.plot(Salary[0], ls='--', c='red')        # Dashed red
plt.plot(Salary[0], ls='-.', c='red')        # Dash-dot red
plt.plot(Salary[0], ls=':', c='green')       # Dotted green

# Plot with markers and colors
plt.plot(Salary[0], ls='--', c='green', marker='d', ms=10)
plt.plot(Salary[0], ls='--', c='blue', marker='o', ms=7)

# Multiple players
plt.plot(Salary[0])   # Sachin
plt.plot(Salary[1])   # Rahul
plt.plot(Salary[7])   # Dhoni
plt.plot(Salary[8])   # Kohli
```

---

### Plot Parameters Reference

| Parameter | Purpose | Examples |
|-----------|---------|----------|
| **ls** | Line style | '-', '--', ':', '-.' |
| **c** | Color | 'r', 'blue', 'green', 'black' |
| **marker** | Point marker | 'o', 'd', 's', '^', '*', '+', 'x' |
| **ms** | Marker size | 5, 7, 10, 15 |
| **linewidth** | Line thickness | 1, 2, 3 |
| **alpha** | Transparency | 0.0 to 1.0 |
| **label** | Legend label | 'Player Name' |

---

## Practical Applications

### Image Processing
1. **Image Classification** - Convert images to arrays for ML models
2. **Image Enhancement** - Adjust brightness, contrast, filters
3. **Computer Vision** - Object detection, facial recognition
4. **Photo Editing** - Crop, resize, rotate, apply effects

### Sports Analytics
1. **Performance Tracking** - Monitor player statistics over time
2. **Trend Analysis** - Identify performance patterns
3. **Benchmarking** - Compare players' performance
4. **Predictive Analytics** - Forecast future performance
5. **Decision Making** - Salary negotiations, team composition
6. **Data Visualization** - Create insights from visual representations

---

## Common Issues & Solutions

### Image Loading Issues

```python
# Issue: File not found
# Solution: Use raw string for paths
image = Image.open(r'C:\path\to\image.jpg')  # Use r'' for Windows paths

# Issue: Wrong image format
# Solution: Check supported formats (JPEG, PNG, GIF, BMP, etc.)
# PIL supports most common formats

# Issue: Image has wrong color channel order
# Solution: PIL uses RGB by default, OpenCV uses BGR
# To convert BGR to RGB: image_rgb = image_bgr[:, :, ::-1]
```

### Array Conversion Issues

```python
# Issue: Array values out of expected range
# Solution: Check data type and normalize if needed
print(image_arr.dtype)  # Should be uint8 for images
print(image_arr.min(), image_arr.max())  # Should be 0-255

# Issue: Shape mismatch in operations
# Solution: Ensure broadcasting compatibility
# Use arr.shape to check dimensions before operations
```

### Plotting Issues

```python
# Issue: Warnings about deprecated parameters
# Solution: Filter warnings
import warnings
warnings.filterwarnings('ignore')

# Issue: Plot not displaying
# Solution: Always call plt.show()
plt.plot(data)
plt.show()  # Required to display

# Issue: Multiple plots overlapping
# Solution: Create new figure or clear previous plot
plt.figure()  # New figure
plt.plot(data)
```

---

## Summary

### Key Concepts

1. **Image as Array**: Digital images are 2D/3D arrays of pixel values
2. **PIL Library**: Python Imaging Library for image I/O
3. **NumPy Conversion**: `np.asarray()` converts images to NumPy arrays
4. **Data Structures**: Use 2D arrays for tabular sports data
5. **Array Operations**: Vectorized operations on sports statistics
6. **Visualization**: Matplotlib for plotting trends and comparisons

### Workflow

```
Image File → PIL Load → NumPy Array → Processing → Visualization
                                          ↓
                          Sports Data → NumPy Array → Analysis → Plots
```

### Key Functions

| Function | Purpose |
|----------|---------|
| `Image.open()` | Load image file |
| `np.asarray()` | Convert to NumPy array |
| `np.array()` | Create/convert to array |
| `plt.imshow()` | Display image |
| `plt.plot()` | Create line plots |
| `plt.show()` | Display plot |

---

## Practice Exercises

1. Load an image and print its shape, dtype, and memory usage
2. Extract and display individual color channels (R, G, B)
3. Create a grayscale version of an RGB image
4. Plot salary trends for multiple players on the same graph
5. Calculate and visualize average salary per game
6. Find the player with highest total salary and highest average points
7. Create a plot comparing two players' performance metrics
8. Resize an image array by downsampling
9. Apply brightness adjustment to an image
10. Create a heatmap of player performance across seasons

---

## References

- [PIL/Pillow Documentation](https://pillow.readthedocs.io/)
- [NumPy Array Documentation](https://numpy.org/doc/stable/reference/arrays.html)
- [Matplotlib Pyplot Tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [Image Processing with NumPy](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)

---

## Author Notes

This notebook demonstrates:
- Real-world application of NumPy with image processing
- Practical sports analytics workflow
- Professional data visualization techniques
- Integration of multiple libraries (PIL, NumPy, Matplotlib)

These skills are essential for data science, computer vision, and sports analytics projects.
