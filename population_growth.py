# Use Python to calculate the population growth of Istanbul and print out a short report.

# _You work at the UN in urban planning and are interested in tracking population growth across major metropolitan regions. 
# You are hoping that by looking at historical population numbers that you can predict future growth and help your team make decisions about resourcing_.

# the program that we will write can be used with data from any city, we’ll start by using data from Istanbul and saving our data to variables. 
# Using variables will allow us to swap out the data in the future.

# Istanbul is the largest city in Turkey and the fifth largest city in the world. 
# It has experienced enormous growth over the past 50 years and is one of the world’s 10 fastest growing metropolitan areas. 
# The dataset starts with the population value for the year 1927 and ends with 2017.

# variable city_name and set it equal to "Istanbul, Turkey"

city_name = "Istanbul, Turkey"

pop_1927 =   691000
pop_1950 =   938000
pop_2000 =  8831800
pop_2017 = 15029231


# Print initial scripts division:
print("")
print("Results from scripts:")


# script that allows us to calculate the _annual percentage growth rate_. 
# This is the amount in which the population changes each year during a certain period.

# change in population between 1927 and 2017
# (pop_present - pop_past)
pop_change = pop_2017 - pop_1927
print(pop_change) # 14338231

# we need to calculate the _percentage growth rate_ : the percentage with which a population changes, 
# but doesn’t account for period of time during which the change takes place.
# ((pop_present - pop_past)/pop_past) * 100
percentage_gr = (pop_change/pop_1927) * 100
print(percentage_gr) # 95.4022930381468


# with the percentage growth rate, we can calculate the annual percentage growth: 
# take the result of the variable percentage_gr and divide it by the number of years elapsed. (annual_gr = percentage_gr/time_elapsed)
annual_gr = percentage_gr / (2017-1927)
print (annual_gr) # 1.060025478201631




# Added to function:
def population_growth (year_one, year_two, population_one, population_two):
  pop_change = population_two - population_one
  print("Population change: " + str(pop_change))
  percentage_growth_rate = (pop_change/population_one) * 100
  print("Percentage growth rate: " + str(percentage_growth_rate))
  growth_rate = (((population_two - population_one)/population_one) * 100)/(year_two - year_one)
  print ("Annual percentage growth rate: " + str(growth_rate))
  return growth_rate

print("")
print("Results set one:")
set_one = population_growth(1927,2017,pop_1927, pop_2017)
print(set_one)



# During the second part of the 20th century, Istanbul experience rapid population growth due to the expansion of the city limits 
# and migration to the city from eastern Turkey in the 1980s.
print("")
print("Results set two:")
set_two = population_growth(1950, 2000, pop_1950, pop_2000)
print(set_two)

# _report_ is sentence that explains the change in population from 1927 to 2017, making use of your variables and string interpolation. 
# Be sure to include the variables for the 1927 and 2017 population data, the change of population, and the annual growth rate of population. 
# If you want to challenge yourself, you can also include the results of the rate of change between 1950 and 2000
print("")

report = "The growth of the population of {} between 1927 and 2017 was of {} people, an annual percentage growth rate of  {}, while annual percentage growth between 1950 and 2000 was {}".format(city_name, pop_change, set_one, set_two)

print(report)


# REF: https://www.youtube.com/watch?v=v9h2BirZAcs
