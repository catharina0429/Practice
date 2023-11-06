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
