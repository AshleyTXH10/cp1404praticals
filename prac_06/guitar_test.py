from prac_06.guitar import Guitar

g1 = Guitar("Xoc SDC electric guitar", 2013, 16500)
print(g1)
print(Guitar.get_age(g1))
print(Guitar.is_vintage(g1))