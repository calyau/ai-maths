---
# === CORE IDENTIFICATION ===
concept: Faithfulness of Intuitionistic First Order Logic
slug: faithfulness-of-intuitionistic-logic

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
section: "4.6"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "completeness of intuitionistic first order predicate logic"
  - "Theorem 4.6.1"
  - "faithfulness"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normalization-theorem
  - normal-term-structure
  - translation-of-first-order-predicate-logic
extends:
  - normalization-theorem
related:
  - type
  - proposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

The fragment of intuitionistic first order predicate logic determined by implication and universal quantification is faithful (complete) relative to the theory of types: a closed first order formula C has a closed proof-term of type C* in the theory of types if and only if C is provable in intuitionistic first order predicate logic.

# Core Definition

Theorem 4.6.1: "Let C be a closed first order formula. Then there is a closed term of type C* in the theory of types if and only if C is provable in intuitionistic first order predicate logic." (Section 4.6)

The formula C is restricted to containing no logical constants other than implication (superset) and universal quantification (forall). The translation C* maps these to function types and Pi types respectively, as defined in Section 3.1.2.1.

Martin-Lof notes: "Kreisel 1970 has suggested to call this property *faithfulness* rather than completeness since it is quite different from the property that classical first order predicate logic enjoys by virtue of Godel's completeness theorem."

# Prerequisites

- **normalization-theorem**: The necessity direction depends on normalization.
- **normal-term-structure**: The proof analyzes the structure of normal proof-terms.
- **translation-of-first-order-predicate-logic**: The translation C |-> C* from first order formulas to types.

# Key Properties

1. **Sufficiency** (soundness direction): Established in Section 3.1.2.2. Every derivation c of C in intuitionistic logic translates to a term c* of type C*.
2. **Necessity** (faithfulness direction): A consequence of normalization. If there is a closed term of type C*, normalize it, then use Lemmas 4.6.2 and 4.6.3 to extract a derivation of C.
3. The restriction to the implication-forall fragment is essential. The result concerns the fragment without disjunction or existential quantification.
4. The type theory is set up with: a type constant I* for individuals, type constants P* for predicates, and object constants f* for function symbols. No other object constants are introduced.

# Construction / Recognition

## The Faithfulness Argument (Necessity):
1. Given a closed term t of type C*, normalize it to a normal term t'.
2. By Lemma 4.6.3, t' (a normal term of type C*) translates back to a derivation of C in intuitionistic first order logic.
3. Lemma 4.6.3 works by induction on the construction of t':
   - If t' = (lambda x*)b*[x*] and C* = (Pi x* in I*)B*[x*]: this corresponds to universal introduction.
   - If t' = (lambda x*)b*[x*] and C* = A* -> B*: this corresponds to implication introduction (modus ponens discharge).
   - If t' has elimination form: it must be y*(a_1*,...,a_n*) where y* is a variable of type B* for some formula B, and the a_i* translate to individual terms or derivations.

## Supporting Lemma 4.6.2:
A normal term of type I* (individual type) whose free variables are of type I* or of type A* (for first order formulas A) must be the translation of an individual term in first order logic.

# Context & Application

This result shows that the theory of types is a conservative extension of intuitionistic first order predicate logic (for the implication-forall fragment). The type theory does not prove any new first order theorems beyond what intuitionistic logic already proves.

The term "faithfulness" (Kreisel's terminology) distinguishes this from Godel's completeness theorem for classical logic. Godel completeness is a model-theoretic result (provable iff true in all models). Faithfulness is a proof-theoretic result (provable in the type theory iff provable in the logic).

# Examples

- The formula (forall x)(P(x) superset P(x)) is provable in intuitionistic logic (by the identity derivation). Correspondingly, (lambda x*)(lambda y*)y* is a closed term of type (Pi x* in I*)(P*(x*) -> P*(x*)).
- Conversely, if we find a closed term of type (Pi x* in I*)(P*(x*) -> P*(x*)), normalizing it and applying Lemma 4.6.3 recovers a derivation in intuitionistic logic.

# Relationships

## Builds Upon
- normalization-theorem, normal-term-structure: The necessity direction requires analyzing normal terms.
- translation-of-first-order-predicate-logic: The translation C |-> C* that mediates between the two systems.

## Related
- type, proposition: The propositions-as-types correspondence underlies the entire result.

# Common Errors

- **Error**: Thinking the result applies to full intuitionistic logic including disjunction and existential quantification.
  **Correction**: The theorem as stated applies only to the implication-forall fragment. Extension to the full logic would require additional argument (and the canonical forms for sum types would need to be brought in).

# Common Confusions

- **Confusion**: Conflating faithfulness with Godel completeness.
  **Clarification**: Godel completeness says: provable iff true in all models. Faithfulness says: provable in the logic iff provable in the type theory. These are fundamentally different properties. Martin-Lof and Kreisel deliberately use the term "faithfulness" to avoid this confusion.

- **Confusion**: Thinking this means the type theory adds no expressive power.
  **Clarification**: The type theory is strictly more expressive than first order logic (it has dependent types, natural numbers, universes, etc.). The faithfulness result only says it is conservative over the first order fragment -- it does not prove new first order theorems.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.6: Completeness of intuitionistic first order predicate logic. Theorem 4.6.1, Lemmas 4.6.2 and 4.6.3.

# Verification Notes

Confidence: high. Theorem 4.6.1 is explicitly stated and proved in Section 4.6 with supporting lemmas.
