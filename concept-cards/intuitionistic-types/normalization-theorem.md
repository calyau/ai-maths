---
# === CORE IDENTIFICATION ===
concept: Normalization Theorem
slug: normalization-theorem

# === CLASSIFICATION ===
category: normalization
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "The Normalization Theorem and Its Consequences"
chapter_number: 4
pdf_page: 34
section: "4.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "strong normalization"
  - "normalization property"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-form
  - reduction
  - church-rosser-property
  - computability-predicate
extends: []
related:
  - taits-method-of-computability
  - normalization-for-types
  - decidability-of-definitional-equality
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I normalize a term?"
  - "What must I know before understanding the normalization theorem?"
---

# Quick Definition

Every term in the intuitionistic theory of types reduces to a normal term -- a term containing no redexes.

# Core Definition

Martin-Lof states: "Every term reduces to a normal term." (Section 4.1)

The proof proceeds by showing, for every closed term a of type A, that the computability predicate phi_A is defined and that phi_A(a) holds. Since phi_A(a) implies normalizability (Lemma 4.1.2, third property), every term is normalizable.

The reduction from open to closed terms is handled by substituting constants: if a[x_1,...,x_n] depends on variables x_1,...,x_n of types A_1,...,A_n[x_1,...,x_{n-1}], we introduce constants a_1,...,a_n of the corresponding closed types and substitute, obtaining a closed term that "behaves just like a[x_1,...,x_n] from the point of view of normalization."

# Prerequisites

- **normal-form**: The target of normalization -- a term with no redexes.
- **reduction**: The process of contracting redexes to reach a normal form.
- **church-rosser-property**: Guarantees that the normal form, if it exists, is unique (up to bound variable renaming).
- **computability-predicate**: The proof tool (phi_A) used to establish that all terms are normalizable.

# Key Properties

1. Every term (open or closed) reduces to a normal term.
2. Combined with Church-Rosser, this implies every term has a unique normal form.
3. The proof proceeds by simultaneous induction on the construction of types and terms, reflecting the fact that types and terms are generated simultaneously in this theory.
4. The proof requires two lemmas: Lemma 4.1.2 (three properties of phi_A) and Lemma 4.1.3 (phi_A is invariant under conversion).

# Construction / Recognition

## To Normalize a Term:
1. Locate a redex in the term (a subterm where an elimination rule is applied directly to an introduction form).
2. Perform the contraction (substitute according to the reduction rule).
3. Repeat until no redexes remain.
4. The normalization theorem guarantees this process terminates.

## To Verify Normalization Applies:
1. Confirm the term is well-typed in the theory.
2. The theorem then guarantees a normal form exists, reachable by any reduction strategy.

# Context & Application

The normalization theorem is the central result of the paper. It is the foundation for all the corollaries in Chapter 4: decidability of definitional equality (4.3), the canonical forms of normal terms (4.4), mechanical computability of number theoretic functions (4.5), and completeness of intuitionistic first order predicate logic (4.6).

The key technical difficulty, distinguishing this proof from Tait's original, is that types and terms are generated simultaneously. This means one cannot first define computability for all types and then prove all terms computable -- both must be done in a single simultaneous induction.

# Examples

Given a closed term b(a) where b = (lambda x)d[x], this is a redex. Normalization proceeds by contracting it to d[a]. If d[a] contains further redexes, continue contracting until a normal form is reached. The theorem guarantees this process terminates for any well-typed term.

For a term of type N like R(s(0), d, (lambda x)(lambda y)e[x,y]), normalization would first contract the recursion on s(0) to e[0, R(0, d, (lambda x)(lambda y)e[x,y])], then contract R(0,...) to d, and continue until no redexes remain.

# Relationships

## Builds Upon
- normal-form, reduction, church-rosser-property: The conceptual framework for the theorem.
- computability-predicate: The proof method.

## Enables
- decidability-of-definitional-equality: Normalize both sides and compare.
- normal-term-structure: Determines what normal terms look like.
- mechanical-computability: Functions can be computed by normalizing.

## Related
- taits-method-of-computability: The proof technique used, extended to handle simultaneous type/term generation.

# Common Errors

- **Error**: Assuming the normalization proof is a simple induction on term structure.
  **Correction**: The proof requires simultaneous induction on both type and term construction because types and terms are generated together. The definition of phi_A and the proof that phi_A(a) holds cannot be separated.

- **Error**: Thinking normalization gives a reduction strategy.
  **Correction**: The theorem is existential -- it guarantees a normal form exists. Any reduction strategy reaches it (by Church-Rosser), but the theorem itself does not prescribe a particular strategy.

# Common Confusions

- **Confusion**: Conflating "normalizable" with "strongly normalizing."
  **Clarification**: Martin-Lof proves that every term reduces to a normal term (weak normalization). Strong normalization (every reduction sequence terminates) would require additional argument, though it also holds.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.1: Normalization theorem.

# Verification Notes

Confidence: high. The theorem is explicitly stated as the main result of Section 4.1 with a complete proof spanning 4.1.1 through 4.1.4.14.
