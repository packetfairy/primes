# primes

I started reading The Curious Incient of the Dog in the Night-Time today.

It includes the following quote:

"Prime numbers are what is left when you have taken all the patterns away.
 I think prime numbers are like life. They are very logical but you could
 never work out the rules, even if you spent all your time thinking about
 them."

I found that really beautiful and kinda moving, and so prime numbers were on
my mind tonight when I was otherwise bored and had free time on my hands. So
I did this.

It does not propose to search for a pattern.. only determines the set. I'm
sure others have done this, and I suspect far more gracefully than I have.
But whatever. It was just supposed to be fun.

As it is currently written, these are the approximate runtimes on my
Macbook Pro, utilizing only a single 2.7GHz i7 CPU:

| *range*        | *runtime*                                       |
| -------:       | ---------:                                      |
| 1 - 100        | 0.001384 seconds                                |
| 1 - 1,000      | 0.003717 seconds                                |
| 1 - 10,000     | 0.123570 seconds                                |
| 1 - 100,000    | 4.932996 seconds                                |
| 1 - 1,000,000  | 363.863991 seconds (~6 minutes)                 |
| 1 - 10,000,000 | 21143.8235 seconds (~352.4 minutes; ~5.9 hours) |

I'm thinking this might be a nice opportunity for me to learn about
threading/parallelization. Maybe for v2. But I've had enough fun for
one night.
