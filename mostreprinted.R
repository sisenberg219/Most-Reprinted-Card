#TO-DO
# Revise Python code for black border
# Add "card_name" column header for column [0]/[1]

setwd("C:/Users/samis/Documents/GitHub/Most-Reprinted-Card")
library(tidyverse)
library(gganimate)
library(gifski)

# loads the data from the CSV file
data <- 
  read.csv("results/results.csv", check.names=FALSE)

# Preprocesses the data (Without Basic Lands)
dataProcessed <- data %>%
  gather(key='year', value="printings", 2:32) %>%
  filter(printings > 0) %>% # removes cards that appear before initial reprint
  filter(card_name != 'Earl of Squirrel') %>% # removes Outlier 
  filter(!card_name %in% c('Mountain', 'Forest', 'Island', 'Swamp', 'Plains'))
write.csv(dataProcessed, "results/processed.csv")


# Preprocesses the data (includes Basic Lands)
# dataProcessed <- data %>%
#   gather(key='year', value="printings", 2:32) %>%
#   filter(printings > 0) %>% # removes cards that appear before initial reprint
#   filter(card_name != 'Earl of Squirrel') %>% # removes Outlier 
# write.csv(dataProcessed, "results/processed.csv")

# Manipulate the Data. Create CSV with only top 10 reprinted Cards
data_manip <- dataProcessed %>%
  group_by(year) %>%
  mutate(rank = rank(-printings, ties.method='first')) %>%
  #filter(printings >= 5) %>%
  filter(rank <= 10) %>%
  #arrange(rank, prev.rank) %>%
  ungroup()
data_manip
write.csv(data_manip, "results/manipulated.csv")

  
plot = ggplot(data_manip, aes(x=rank, y = printings, fill = card_name, 
                            color = card_name)) +
geom_col() +
#geom_tile(aes(y = printings, height = printings, width = 0.9), alpha = 0.8, color = NA) +
geom_text(aes(y = 0, label = card_name), hjust = 1) +
geom_text(aes(y = printings, label = printings, hjust=0)) +
coord_flip(clip = "off", expand = FALSE) +
scale_y_continuous(labels = scales::comma) +
scale_x_reverse() +
guides(color = FALSE, fill = FALSE) +
theme(plot.title = element_text(hjust = 0, size = 22),
      axis.ticks.y = element_blank(), 
      axis.text.y  = element_blank(),
      plot.margin = margin(1,1,1,4, "cm"))
plot

# Animates the plot
anim = plot + transition_states(year, transition_length = 4, state_length = 1) +
  view_follow(fixed_x = TRUE)  +
  ease_aes('cubic-in-out') +
  labs(title = 'Number of Printings Per Year : {closest_state}',
       subtitle  =  "Printed In Black Border Sets",
       caption  = "Excludes printings from Memoribilia Sets")

# Creates the finalized GIF
animate(anim, 200, fps = 60,  width = 1200, height = 1000,
        renderer = gifski_renderer("results/gganim.gif"))

