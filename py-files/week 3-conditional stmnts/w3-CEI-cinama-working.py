
mov_g_rated="movie-1- the revenge - g rated"
mov_15_rated="movie-2 - the sequel - 15s rated"
mov_18_rated="movie-3 - the return - 18s rated"

cust_age=int(input("What is your age? "))

if cust_age < 12:
    print(" The following movies are available for you" + " "
          + "\n" + (mov_g_rated) )
elif cust_age >=12<=17:
    print(" The following movies are available for you" + " " +
          "\n" + (mov_g_rated) +
            "\n" + (mov_15_rated))
else:
    print(" The following movies are available for you" + " " +
      "\n" + (mov_g_rated)
        + "\n" + (mov_15_rated)
            + "\n" + (mov_18_rated))