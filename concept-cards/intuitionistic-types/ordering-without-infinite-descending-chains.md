---
# === CORE IDENTIFICATION ===
concept: Ordering Without Infinite Descending Chains
slug: ordering-without-infinite-descending-chains

# === CLASSIFICATION ===
category: paradoxes
subcategory: technical apparatus
tier: advanced

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Löf"
chapter: "Informal Explanations of the Basic Concepts"
chapter_number: 1
pdf_page: null
section: "1.9. Girard's paradox"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "wellfounded ordering"
  - "well-ordering (constructive)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - proposition
  - natural-numbers
  - pi-type
  - sigma-type
  - function-type
  - empty-type
related:
  - girards-paradox
  - universe
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding Girard's paradox?"
---

# Quick Definition
An ordering without infinite descending chains is a type A together with a binary relation < on A that is transitive and admits no infinite descending sequence. This is the technical device used in Martin-Lof's presentation of Girard's paradox.

# Core Definition
Martin-Lof defines: "an ordering without infinite descending chains ... to be a type A together with a binary relation < on A such that the propositions P(A, <) = (Pi x in A)(Pi y in A)(x < y -> y < z -> x < z) and Q(A, <) = (Pi f in N -> A)((Pi n in N)(f(n+1) < f(n)) -> bottom), which express that < is transitive and free from infinite descending chains, both hold." (Section 1.9)

He notes: "an ordering without descending chains is necessarily irreflexive, because, if a < a, then ... < a < ... < a < a is an infinite descending chain and we get a contradiction." (Section 1.9)

# Prerequisites
- **Type**: A is a type.
- **Proposition**: P and Q are propositions (types representing logical statements).
- **Natural numbers**: Used in Q to formalize "infinite sequence" (f in N -> A).
- **Pi type**: Used to quantify over elements and sequences.
- **Sigma type**: Used to package orderings with their proofs.
- **Function type**: The relation < is of type A -> A -> V; sequences are N -> A.
- **Empty type**: bottom (N_0) appears in Q -- an infinite descending chain leads to falsehood.

# Key Properties
1. Transitivity: P(A, <) states that < is transitive.
2. No infinite descending chains: Q(A, <) states that for any sequence f: N -> A, if f(n+1) < f(n) for all n, then bottom (contradiction).
3. Irreflexivity follows: if a < a, one can construct a constant infinite descending chain.
4. The type U of all such orderings is: (Sigma A in V)(Sigma < in A -> A -> V)(P(A,<) x Q(A,<)).
5. Girard uses "torsion free orderings" instead; Martin-Lof's formulation is a modification.

# Construction / Recognition
## To Construct/Create:
1. Choose a type A and a relation < on A (of type A -> A -> V).
2. Prove P(A, <): transitivity.
3. Prove Q(A, <): no infinite descending chain.
4. Package as (A, <, p, q) in U.

## To Identify/Recognize:
1. A type with a binary relation satisfying transitivity and the absence of infinite descending sequences.
2. In the source, formalized using Pi types, function types, and bottom.

# Context & Application
This notion is the key technical ingredient in Girard's paradox. The type U of all orderings without infinite descending chains, equipped with a natural ordering <_U (defined by order-preserving embeddings with dominating elements), is itself an ordering without infinite descending chains. Under the assumption V in V, this leads to U being an element of itself and ultimately to a contradiction via self-comparison.

# Examples
From Section 1.9: The ordering <_U on U is defined by (A, <_A) <_U (B, <_B) iff there exists an order-preserving f: A -> B and a b in B dominating the range of f. Martin-Lof proves <_U is transitive (by composing maps) and free from infinite descending chains (by transferring a descending chain in U to a descending chain in A_0).

# Relationships
## Builds Upon
- All basic type formers are used in the formalization.
## Enables
- **girards-paradox**: This is the device that makes the paradox work.
## Related
- **universe**: U in V is the critical assumption that leads to contradiction.

# Common Errors
- **Error**: Confusing this with classical well-ordering.
  **Correction**: Martin-Lof's formulation uses "no infinite descending chain" rather than "every non-empty subset has a least element." These are equivalent classically but not constructively. The chain condition is the constructively appropriate formulation.

# Common Confusions
- **Confusion**: Thinking the ordering <_U is itself problematic.
  **Clarification**: <_U is perfectly well-defined and well-behaved. The problem arises only from the assumption V in V, which allows U itself to be an object of V and hence an element of U.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.9.

# Verification Notes
Extracted from Section 1.9. Formal definitions P and Q quoted from source. High confidence.
