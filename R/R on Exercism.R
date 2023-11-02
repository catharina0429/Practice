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
