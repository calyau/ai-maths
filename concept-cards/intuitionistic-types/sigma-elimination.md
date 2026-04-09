---
# === CORE IDENTIFICATION ===
concept: Sigma Elimination (E Operator and Projections)
slug: sigma-elimination

# === CLASSIFICATION ===
category: type-formers
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Informal Explanations of the Basic Concepts"
chapter_number: 1
pdf_page: 0
section: "1.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "E operator"
  - "Sigma elimination rule"
  - "dependent elimination of pairs"
  - "left and right projection"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sigma-type
  - pairing
  - pi-type
extends: []
related:
  - sigma-elimination
  - application
contrasts_with:
  - application

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I eliminate a pair (Sigma elimination / projections)?"
---

# Quick Definition

Sigma elimination provides two ways to use objects of Sigma type: the general E operator E(c, d) which applies a two-argument function d to the components of a pair c, and the derived left and right projections p(c) and q(c) which extract individual components.

# Core Definition

**E operator**: Martin-Lof writes: "Let C be a function which to an arbitrary object of type (Sigma x in A)B(x) assigns a type. Given a function d of type (Pi x in A)(Pi y in B(x))C((x,y)) we may then introduce a function of type (Pi z in (Sigma x in A)B(x))C(z) whose value for the argument c will be denoted E(c,d) by the schema E((a,b),d) = d(a,b)." (Section 1.4)

**Projections**: "we can introduce the left and right projections p and q of types (Sigma x in A)B(x) -> A and (Pi z in (Sigma x in A)B(x))B(p(z)), respectively, by putting p((a,b)) = a, q((a,b)) = b." (Section 1.4)

# Prerequisites

- **sigma-type**: The E operator and projections operate on objects of Sigma type.
- **pairing**: The computation rules are defined in terms of pairs.
- **pi-type**: The E operator and projections are themselves functions of Pi type.

# Key Properties

1. E(c, d) is the general (dependent) elimination form for Sigma types.
2. The computation rule is E((a,b), d) = d(a, b).
3. The E operator allows the result type C(z) to depend on z.
4. Left projection p extracts the first component: p((a,b)) = a.
5. Right projection q extracts the second component: q((a,b)) = b.
6. The type of q is dependent: (Pi z in (Sigma x in A)B(x))B(p(z)), because the type of the second component depends on the first.
7. The projections p and q are derivable from the E operator as special cases.

# Construction / Recognition

## To Construct/Create:
1. **E operator**: Given c of type (Sigma x in A)B(x) and d of type (Pi x in A)(Pi y in B(x))C((x,y)), form E(c,d) of type C(c).
2. **Left projection**: Apply p to c, yielding p(c) of type A.
3. **Right projection**: Apply q to c, yielding q(c) of type B(p(c)).

## To Identify/Recognize:
1. E(c, d) notation for general elimination.
2. p(c) and q(c) for projections.
3. The defining equations involve pattern-matching on pairs.

# Context & Application

Sigma elimination is the means of using (deconstructing) objects of Sigma type, just as application is the means of using objects of Pi type. The E operator is the fully general form that supports dependent elimination (the result type can mention the pair being eliminated). The projections p and q are simpler but sufficient for many purposes.

# Examples

From Section 1.4: E((a,b), d) = d(a,b). If c = (a,b) is a real number (a Cauchy sequence paired with its convergence proof), then E(c, d) applies d to the sequence and its proof.

From Section 1.4: p((a,b)) = a and q((a,b)) = b. For a real number (a, b), p extracts the Cauchy sequence and q extracts the convergence proof.

# Relationships

## Builds Upon
- sigma-type: Sigma elimination operates on Sigma types.
- pairing: The computation rules are defined in terms of pairs.
- pi-type: The eliminator d and the projections are functions of Pi type.

## Enables
- Any use of Sigma-typed data requires elimination.

## Related
- left-and-right-projection: Projections are special cases of E.

## Contrasts With
- application: Application eliminates Pi types; E and projections eliminate Sigma types.

# Common Errors

- **Error**: Forgetting that q has a dependent type: q(c) has type B(p(c)), not just B.
  **Correction**: The type of the right projection depends on the left projection. Only in the non-dependent case (A x B) does q have the simple type A x B -> B.

# Common Confusions

- **Confusion**: Thinking p and q are the only way to eliminate Sigma types.
  **Clarification**: The E operator is the general elimination form. Projections are derived special cases. The E operator is needed when the result type depends on the entire pair, not just one component.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.4: Disjoint union of a family of types.

# Verification Notes

Confidence: high. Both the E operator and projections are explicitly defined in Section 1.4 with schemas and typing.
