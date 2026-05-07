# CS-130 Final: Methodology 

Robert Sheehan

Dr. Chris Bopp

Introduction To Programming in Python

May 7th, 2026


## Data Soruces

This data was collected was collected from [CORGIS](https://corgis-edu.github.io/corgis/csv/)

- Cars CSV File was downloaded from [this](https://corgis-edu.github.io/corgis/csv/cars/) link
   - By Austin Cory Bart
   - The dataset contains information about cars and how much fuel that they use.
 
  Focus:
  - More specifically, this analysis was more focused on the `Driveline`(4WD, AWD, FWD, RWD) of the cars and how this relates to `City MPG`, `Highway MPG` and `Horsepower`


## Data Preparation/Cleaning

Column Renaming:

- To make the names of the respective colums more readble and easier to work with, I changed them.
  - Specifically I created a dictonnary called column_renaming with the old names as the keys, and the new names as the value.
  - Then I used the `.rename` function to push these names into the .csv file, effectivly renaming the columns.
 
Outlier Removal: 

- I then checked to see if thier were any outliers in my data that didnt make sense in the scope of the column
  -For example a 2011 Chevy was listed as getting 223 miles per gallon on the highway
  - I also checked the other categories of `City_mpg` and `Horsepower` and found no extreme outliers
  
- Then I use `.loc` to list the cars that had over 100 mpg to further confirm this outlier.

- Once that was complete, I used the `.drop` function to drop/remove the row with the outlier
  - This was then moved to a new, clean data set named `cars_clean`

String Replacement: 

- Using the `.replace ` fucntion I coverted the strings found in the Driveline column to easier to work with strings
  - For example, "Front-wheel drive" was converted to "FWD"
  - This was done agian using a dictonary with the previous strings as the key and the new strings as the values

New Column Creation:

- To calcualte the gap between the highway mpg and the city mpg, I created a new column that holds `Highway_mpg - City_mpg'
  - This gap is then used to calculate the addtional number of miles a driveline would get on the highway to see if thier is an advantage

- To find the avergae mpg of the car, not just the city and highway, I created a column that held this data called `avg_mpg`
  - To do so I took the coulmn `City_mpg` added it to `Highway_mpg` then divided by 2

- I then used the `groupby` and `map` functions to calculate the average MPG for each driveline type and add it as a new colum to the DataFrame
  
- The `groupby` and `map` functions were also used to calculate the average MPG gap for each driveline type and add it as a new column

## Assumptions 

- Driver Behavior
  - While analyzing this data I assumed that the behavior of the drivers was reativley uniform among the diffrent driveline types. This would mean that mpg is all calculated under the same standard of the cars themselves, rather than the assumption that 4WD owners drive more aggressivley than FWD owners.

- Fuel Type
  - I assumed that every vehicle is running on Gasoline, which is supported by the data, but also the right octane level. Some cars take a more premium feul, so I am assuming that this data is based on all of the vehicles running on its ideal fuel type for best performance.
 
- Modifications
  - I assumed that every car is stock, from the factory, and has not undergone any modifications. This would play a diffrence as modifications can play a heavy role in the horsepower and fuel consumption.
 
- 4WD vs. AWD
  - I assume that the author of this dataset took into account the diffrences between these drivelines. It is very common to get these two confused or even beleive there is no diffrence between them. However, there is a clear mechanical diffrence between the two drivelines that has effects on how the car operates.
 
- Age of the Car
  - I assume that the year that the car was made has little effect on the MPG of both city and highway. This assumtion may or may not be correct beucase of the advancements of technology over the years. However since this dataset only has cars made from 2009-2011, I assume that this would have minimal effect on the information.
 

## Limitations 

- Height, Length, and Width
  - When I fist started anaylzing this data, I assumed that this represented the height, weight, and length of the exterior of the car in inches. I was initally trying to draw a connection between the volume of the car its respective average MPG. I wanted to see if bigger cars typically offered less MPG. However, when looking at these columns, the data was super inconsistent. For example, when I looked at the height, length, and width of a 2009 Audi A3 the dimensions did not match anything on the car. This was checked in multiple diffrent forms of measurment including inches, centimeters, and feet. This is very misleading and the dimensions dont line up with any other car, which made the analysis of all of these columns very difficult/impossible. It would have helped for these to be labled or even removed.
 

