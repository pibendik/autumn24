# Make a program that uses rdflib 
# The program takes as an argument the input filename and the output filename:
# For now, it will take the ./simpsons.ttl file as input, and produce an output file "output.ttl"
# It should be run like this: 
# python3 Simpsons.py oblig/2/simpsons.ttl output.ttl

# 1. Importing the necessary libraries
# First, read the input file and create a rdﬂib Graph from it. 
# After parsing the input ﬁle to a graph you can iterate through graph.namespaces() 
# to get access to (preﬁx, namespace) tuples. You need to store the preﬁxes as variables with 
# “preﬁx = Namespace(namespace)” then bind them to the graph with “graph.bind("preﬁx", preﬁx)” 
# before you can use them when adding triples to the graph. See the EX example in the lecture slides.

# 2. adding information:
# then add the following information about Maggie, Mona, Abraham and
# Herb, whose identiﬁers are respectively sim:Maggie, sim:Mona, sim:Abraham and sim:Herb,
# to the model read from the input ﬁle. You will need to use the class foaf:Person, the predicates
# rdf:type, foaf:age, foaf:name, fam:hasSpouse and fam:hasFather, and the standard xsd
# datatypes.1 You shall assume that the preﬁxes sim and fam are deﬁned in the model that
# your program has read in the section above, so do not hardcode these namespaces in your
# program, but get them from the model you have created. (Hint: Model is a subinterface of
# PrefixMapping.)
# Add the following information to the model using rdflib methods:
#   • Maggie is a person, whose name is "Maggie Simpson" and age is 1. The datatype of the age value is xsd:int.
#   • Mona is a person, whose name is "Mona Simpson" and age is 70. The datatype of the age value is xsd:int.
#   • Abraham is a person, whose name is "Abraham Simpson" and age is 78. The datatype of the age value is xsd:int.
#   • Abraham is the spouse of Mona, and Mona is the spouse of Abraham.
#   • Herb is a person.
#   • Herb has a father (but we do not know who it is, i.e., use a blank node.).

# 3. Locate, read and write information:For each person in the model, i.e., for every resource of type foaf:Person, add the following
# information according to the person’s age:
#   • if age < 2 year, then add a triple stating that the person is of type fam:Infant,
#   • if age < 18 year, then add a triple stating that the person is of type fam:Minor,
#   • if age > 70 year, then add a triple stating that the person is of type fam:Old.
# Example: If the input model contains the triples
# sim:Someone rdf:type foaf:Person ;
#   foaf:age "75"^^xsd:int .
# then your program shall add the triple
# sim:Someone rdf:type fam:Old .
# to the model.

# 4. Write to file