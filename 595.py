#595
select name,population,area 
from World
where population > 25000000 or area > 3000000 



# union solution (supposed to be faster but it took longer for me)
select name, population, area
from World
where area > 3000000 

union

select name, population, area
from World
where population > 25000000
