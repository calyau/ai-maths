# Domain Taxonomy for "An Intuitionistic Theory of Types"

## Categories
- foundations: Basic notions (objects, types, propositions, proofs, Curry-Howard)
- type-formers: Type forming operations (Pi, Sigma, +, N_n, N, V)
- formal-system: Formal rules of the theory (type/term formation, variables, constants)
- reduction-theory: Contraction, reduction, conversion, Church-Rosser property
- translations: Embeddings of other formal theories into the theory of types
- normalization: Normalization theorem, computability method, consequences

## Tiers
- foundational: Basic concepts from Chapter 1 that require no prerequisites within this source
- intermediate: Formal system rules (Chapter 2), translations (Chapter 3)
- advanced: Normalization theorem and consequences (Chapter 4), Girard's paradox

## Notation Conventions

### Type Membership
- a in A: "a is an object of type A" or "a is a proof of proposition A"

### Type Formers
- (Pi x in A)B(x): Cartesian product / dependent function type
- (Sigma x in A)B(x): Disjoint union / dependent pair type
- A -> B: Non-dependent function type (special case of Pi)
- A x B: Cartesian product of two types (special case of Sigma)
- A + B: Disjoint union of two types
- N_n: Finite type with n elements
- N: Natural numbers
- V: Universe of small types

### Logical Connectives (as types)
- A supset B: Implication (represented by A -> B)
- A & B: Conjunction (represented by A x B)
- A v B: Disjunction (represented by A + B)
- (forall x in A)B(x): Universal quantification (represented by Pi type)
- (exists x in A)B(x): Existential quantification (represented by Sigma type)
- bottom (N_0): Falsehood
- top (N_1): Truth

### Term Formers
- (lambda x)b[x]: Lambda abstraction
- b(a): Application
- (a,b): Pairing
- E(c,d): Sigma elimination
- p(c), q(c): Left/right projections
- i(a), j(b): Canonical injections
- D(c,d,e): Definition by cases
- R_n(c,c_1,...,c_n): Finite type elimination
- R(c,d,e): Primitive recursion
- s(a): Successor
