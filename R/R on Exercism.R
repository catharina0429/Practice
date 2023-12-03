# Exercisem ####

## Hello world ====
hello_world <- function() {
  "Hello, World!"
}

## Two per ====
two_fer <- function(input) {
  if (missing(input) == TRUE)
    print("One for you, one for me.")
  else
    paste0("One for ", input, ", one for me.")
}
two_fer()
two_fer("Alice")

## Leap ====
# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

# leap <- function(year) {
#   if ((year %% 4 == 0 )|(year %% 400 == 0))
#     TRUE
#   else
#     FALSE
# }

leap <- function(year) {
  if ((year %% 4 == 0 && year %% 100 != 0) || year %% 400 == 0) {
    return(TRUE)
  } else {
    return(FALSE)
  }
}
leap(1990) # FALSE
leap(2000) # TRUE
leap(1996) # TRUE
leap(1997) # FALSE
leap(2024) # TRUE

## Darts ====
score <- function(x, y) {
  dist <- sqrt((x^2) + (y^2))
  ifelse(dist > 10, 0, 
         ifelse(dist > 5, 1,
                ifelse(dist > 1, 5, 10)))
}
score(0, 0)
score(-3.6, 3.6)


## Raindrops ====
raindrops <- function(number) {
  ifelse( number == 1, as.character(number), 
          ifelse( (number %% 3 == 0 & number %% 5 == 0 & number %% 7 == 0), "PlingPlangPlong", 
                  ifelse((number %% 3 == 0 & number %% 5 == 0), "PlingPlang", 
                         ifelse( (number %% 3 == 0 & number %% 7 == 0 ), "PlingPlong", 
                                 ifelse( (number %% 5 == 0 & number %% 7 == 0), "PlangPlong", 
                                         ifelse(number %% 3 == 0, "Pling", 
                                                ifelse(number %% 5 == 0, "Plang",
                                                       ifelse(number %% 7 == 0, "Plong", 
                                                              as.character(number)))))))))
}
raindrops(1)
raindrops(21)
raindrops(35) # PlangPlong
raindrops(105) # PlingPlangPlong

## Hamming =====
# This is a stub function to take two strings
# and calculate the hamming distance
hamming <- function(strand1, strand2) {
  if( nchar(strand1) != nchar(strand2)){
    stop("different length!")}
  else(
    sum(unlist(lapply(strsplit(strand1, NULL), rev)) != unlist(lapply(strsplit(strand2, NULL), rev))))
}
s1 <- "GATACA"; s2 <- "GCATAA"
hamming(s1, s2)

s1 <- "" ;s2 <- ""
hamming(s1, s2)

s1 <- "ATA"; s2 <- "AGTG"
hamming(s1, s2) # halted