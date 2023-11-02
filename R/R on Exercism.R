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
leap(1990)
leap(2000)
leap(1996)
leap(1997)
