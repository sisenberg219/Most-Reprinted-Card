setwd("C:/Users/samis/Documents/GitHub/Most-Reprinted-Card")
library(tidyverse)
library(readr)
library(dplyr)
library(data.table)
library(gganimate)
test <- 
  read.csv("results/2007.csv")
temp <- 
  list.files(path = "results", pattern = "*.csv") 

# Imports all CSVs into memory
data_path <- "results/"
files_df <- paste0(data_path, list.files(path = data_path, pattern = "*.csv")) %>% 
  lapply(FUN=function(f) { 
  fread(f) })

# Create Dataframe with the results from the CSV
df <- data.frame(Card_Name=c(test$X[1:20]), 
                 Reprint_Amount=c(test$Reprint.Amount[1:20]))
d2f <- data.frame(Card_name=c(files_df[[1]]$x[1:20]),
                  Reprint_Amount=c(files_df[[1]]$Reprint.Amount[1:20])
