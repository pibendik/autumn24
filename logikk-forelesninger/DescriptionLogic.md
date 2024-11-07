# Everything which is "blah", must also be "blah"

... this is GCI (general concept inclusion)

We have restrictions on the first-order-logic, and then we sort of end up with a "fragment", which it is called in logics.

Description logics is all about

1. concepts,
1. individuals,
1. roles

In Description logics (one is called ALC, which is the one we looked at), the syntax is a bit strange, using symbols like:

| Symbol | Description                                          | Example    | Reads                         |
| ------ | ---------------------------------------------------- | ---------- | ----------------------------- |
| ⊤      | Special concept with every individual as an instance | ⊤          | top                           |
| ⊥      | Empty concept                                        | ⊥          | bottom                        |
| ⊓      | Intersection or conjunction of concepts              | C ⊓ D      | C and D                       |
| ⊔      | Union or disjunction of concepts                     | C ⊔ D      | C or D                        |
| ¬      | Negation or complement of concepts                   | ¬C         | not C                         |
| ∀      | Universal restriction                                | ∀R.C       | all R-successors are in C     |
| ∃      | Existential restriction                              | ∃R.C       | an R-successor exists in C    |
| ⊑      | Concept inclusion                                    | C ⊑ D      | all C are D                   |
| ≡      | Concept equivalence                                  | C ≡ D      | C is equivalent to D          |
| =˙     | Concept definition                                   | C =˙ D     | C is defined to be equal to D |
| :      | Concept assertion                                    | a : C      | a is a C                      |
| :      | Role assertion                                       | (a, b) : R | a is R-related to b           |

## TBox and ABox

A general concept inclusion (GCI) has the form C ⊑ D where C and D are concepts. Write C ≡ D when C ⊑ D and D ⊑ C. TBox is a finite set of the GCI

ABox is a finite set of assertions

#### TBox Examples

| Symbol | Description       | Example                              | Reads                                        |
| ------ | ----------------- | ------------------------------------ | -------------------------------------------- |
| ⊑      | Concept inclusion | Diabetes ⊑ ChronicDisease            | All Diabetes are Chronic Diseases            |
| ⊑      | Concept inclusion | Hypertension ⊑ CardiovascularDisease | All Hypertension are Cardiovascular Diseases |
| ⊑      | Concept inclusion | HeartAttack ⊑ EmergencyCondition     | All Heart Attacks are Emergency Conditions   |
| ⊑      | Concept inclusion | Stroke ⊑ NeurologicalCondition       | All Strokes are Neurological Conditions      |
| ⊑      | Concept inclusion | Cancer ⊑ SeriousIllness              | All Cancers are Serious Illnesses            |
| ⊑      | Concept inclusion | Flu ⊑ InfectiousDisease              | All Flu cases are Infectious Diseases        |

#### ABox Examples

| Symbol | Description       | Example             | Reads                    |
| ------ | ----------------- | ------------------- | ------------------------ |
| :      | Concept assertion | John : Diabetes     | John has Diabetes        |
| :      | Concept assertion | Mary : Hypertension | Mary has Hypertension    |
| :      | Concept assertion | Alice : HeartAttack | Alice had a Heart Attack |
| :      | Concept assertion | Bob : Stroke        | Bob had a Stroke         |
| :      | Concept assertion | Carol : Cancer      | Carol has Cancer         |
| :      | Concept assertion | Dave : Flu          | Dave has the Flu         |

together they make up a "Knowlege Base"

... in sequent calculus for ALC subsumtion (empty TBox)

## Modal Logic K (the most basic one)

... is essentially ALC concepts with a single role R
<>A -> ∃R.A
[]A -> ∀R.A

### soundness and completeness of the calculus for ALC

#### with empty TBox (polynomial time)

we can do the same as for Modal Logic K when proving soundness and completeness.
We will then have to make two minor changes, that don't affect much: something about the rules for the "for all" and "exists" rules, and one more thing, regarding the roles, I think...

### with TBox (exponential time)

several steps here... I think we have to "compile" a concept. A complicated something... like... the goal is to put it in the rules for things like the "for all -right rule". However, now we have a problem!!
We can now have infinite branches.

#### cycle detection

... However, the infinite branches are repetitive! So, we can recognize repetition, and terminate what would otherwise be looping forever. When we stop something that would otherwise expand forever, and know that they will never be closed. We call this "cycle detection".
Now we have to introduce a new object, and say that the concept must hold in the new object.

#### ...

We preserve soundness and completeness, and after adding cycle detection, we regain termination. The calculus will always terminate.

### semantics

You could translate from ALC into first-order logic. Always.
So we could find the semantic value of something from description logic this way.

## validity and unsatisfiability

in first order logic, we can check one with the negation of the other
we can NOT do this in ALC, because doing that negation could take us outside of the domain of ALC! mind blown!

Concept satisfiability with restraint that a TBox: ...

## further

we have actual usefull stuff in description logics.
It's actually succesfull out in the world.
Because it can take >100 000 concepts, and still terminate calculus fast.
