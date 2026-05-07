# CS-130 Final: Methodology 

Robert Sheehan

Dr. Chris Bopp

Introduction To Programming in Python

May 7th, 2026


## Data Soruces

This data was collected from [CORGIS](https://corgis-edu.github.io/corgis/csv/)

- Cars CSV File was downloaded from [this](https://corgis-edu.github.io/corgis/csv/cars/) link
   - By Austin Cory Bart
   - The dataset contains information about cars and how much fuel that they use.
 
  Focus:
  - More specifically, this analysis was more focused on the `Driveline`(4WD, AWD, FWD, RWD) of the cars and how this relates to `City MPG`, `Highway MPG` and `Horsepower`


## Data Preparation/Cleaning

__Column Renaming:__

- To make the names of the respective colums more readble and easier to work with, I changed them.
  - Specifically I created a dictionary called column_renaming with the old names as the keys, and the new names as the value.
  - Then I used the `.rename` function to push these names into the .csv file, effectively renaming the columns.
 
__Outlier Removal:__

- I then checked to see if there were any outliers in my data that didnt make sense in the scope of the column
  - For example a 2011 Chevy was listed as getting 223 miles per gallon on the highway
  - I also checked the other categories of `City_mpg` and `Horsepower` and found no extreme outliers
  
- Then I use `.loc` to list the cars that had over 100 mpg to further confirm this outlier.

- Once that was complete, I used the `.drop` function to drop/remove the row with the outlier
  - This was then moved to a new, clean data set named `cars_clean`

__String Replacement:__

- Using the `.replace ` function I coverted the strings found in the Driveline column to easier to work with strings
  - For example, "Front-wheel drive" was converted to "FWD"
  - This was done again using a dictonary with the previous strings as the key and the new strings as the values

__New Column Creation:__

- To calculate the gap between the highway mpg and the city mpg, I created a new column that holds `Highway_mpg - City_mpg`
  - This gap is then used to calculate the additional number of miles a driveline would get on the highway to see if thier is an advantage

- To find the average mpg of the car, not just the city and highway, I created a column that held this data called `avg_mpg`
  - To do so I took the coulmn `City_mpg` added it to `Highway_mpg` then divided by 2

- I then used the `groupby` and `map` functions to calculate the average MPG for each driveline type and add it as a new column to the DataFrame
  
- The `groupby` and `map` functions were also used to calculate the average MPG gap for each driveline type and add it as a new column


__Graphic Creation:__

- To create the graphics I imported `seaborn` and `matplotlib` and used thier built in functions
  - Seaborn was something that I researched and found to be able to change the color of the dots on the scatterplot based on the driveline
 

## Assumptions 

__Driver Behavior__

  - While analyzing this data I assumed that the behavior of the drivers was relatively uniform among the diffrent driveline types. This would mean that mpg is all calculated under the same standard of the cars themselves, rather than the assumption that 4WD owners drive more aggressively than FWD owners.

__Fuel Type__

  - I assumed that every vehicle is running on Gasoline, which is supported by the data, but also the right octane level. Some cars take a more premium fuel, so I am assuming that this data is based on all of the vehicles running on its ideal fuel type for best performance.
 
__Modifications__

  - I assumed that every car is stock, from the factory, and has not undergone any modifications. This would play a difference as modifications can play a heavy role in the horsepower and fuel consumption.
 
__4WD vs. AWD__

  - I assume that the author of this dataset took into account the differences between these drivelines. It is very common to get these two confused or even believe there is no difference between them. However, there is a clear mechanical difference between the two drivelines that has effects on how the car operates.
 
__Age of the Car__

  - I assume that the year that the car was made has little effect on the MPG of both city and highway. This assumtion may or may not be correct because of the advancements of technology over the years. However since this dataset only has cars made from 2009-2011, I assume that this would have minimal effect on the information.
 

## Limitations 

__Height, Length, and Width__

  - When I first started analyzing this data, I assumed that this represented the height, weight, and length of the exterior of the car in inches. I was initially trying to draw a connection between the volume of the car its respective average MPG. I wanted to see if bigger cars typically offered less MPG. However, when looking at these columns, the data was super inconsistent. For example, when I looked at the height, length, and width of a 2009 Audi A3 the dimensions did not match anything on the car. This was checked in multiple diffrent forms of measurement including inches, centimeters, and feet. This is very misleading and the dimensions dont line up with any other car, which made the analysis of all of these columns very difficult/impossible. It would have helped for these to be labeled or even removed.

__Weight__

   - There is no column for the weight of the respective cars. I feel that this is a huge limitation in the fact that this can play a large role in the MPG. The drop in MPG could be simply the fact that AWD vehicles typically weigh several hundred pounds more than a FWD car. So, there is no way to tell if this calculation is based off of the mechanical drag of spinning four wheels, or just the weight. 

