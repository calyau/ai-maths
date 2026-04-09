---
# === CORE IDENTIFICATION ===
concept: Existential Quantification (as Sigma Type)
slug: existential-quantification

# === CLASSIFICATION ===
category: foundations
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
  - "there exists"
  - "(exists x in A)B(x)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sigma-type
  - proposition
  - propositions-as-types
  - pairing
extends: []
related:
  - conjunction
  - universal-quantification
  - such-that-type
contrasts_with:
  - universal-quantification

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does existential quantification relate to the Sigma type?"
---

# Quick Definition

Existential quantification (exists x in A)B(x) is represented by the Sigma type (Sigma x in A)B(x); a proof is a pair (a, b) consisting of a witness a in A and a proof b of B(a).

# Core Definition

Martin-Lof writes: "When B(a) represents a proposition for every object a of type A, (Sigma x in A)B(x) represents the *existential* proposition (exists x in A)B(x) which we prove by exhibiting a pair (a,b) where a is an object of type A and b a proof of the proposition B(a)." (Section 1.4)

# Prerequisites

- **sigma-type**: Existential quantification is the logical reading of the Sigma type.
- **proposition**: B(a) must represent a proposition for each a in A.
- **propositions-as-types**: The identification of propositions with types underlies this correspondence.
- **pairing**: A proof of an existential is a pair.

# Key Properties

1. (exists x in A)B(x) is represented by (Sigma x in A)B(x).
2. A proof is a dependent pair: a witness a and a proof b of B(a).
3. The proof is constructive: one must actually exhibit the witness, not merely show existence indirectly.
4. This is the dependent generalization of conjunction (which is the special case where B does not depend on x).

# Construction / Recognition

## To Construct/Create:
1. Find a witness a of type A.
2. Construct a proof b of B(a).
3. Form the pair (a, b), which is a proof of (exists x in A)B(x).

## To Identify/Recognize:
1. An existentially quantified proposition (exists x in A)B(x) corresponds to a Sigma type.
2. Proofs are always pairs (witness, evidence).

# Context & Application

The representation of existential quantification as the Sigma type is a key instance of propositions-as-types. The intuitionistic requirement that existence proofs be constructive (providing an actual witness) is naturally captured by the pairing construction. Martin-Lof notes that the possibility of strengthening the usual existential elimination rule "seems first to have been indicated by Howard 1969" (Frontmatter).

# Examples

From Section 1.4: A proof of (exists x in A)B(x) is a pair (a, b) where a in A is the witness and b in B(a) is the proof that the witness satisfies the property.

From Section 1.4: The type of real numbers uses existential/Sigma structure: a real number is a pair of a Cauchy sequence and a proof of convergence.

# Relationships

## Builds Upon
- sigma-type: Existential quantification is the logical reading of the Sigma type.
- pairing: Proofs of existentials are pairs.

## Enables
- Constructive existence proofs within the type-theoretic framework.

## Related
- conjunction: Conjunction A & B is the non-dependent special case.
- such-that-type: The "such that" reading of Sigma types is closely related.

## Contrasts With
- universal-quantification: Existential (Sigma / pairs / "there exists") vs. universal (Pi / functions / "for all").

# Common Errors

- **Error**: Attempting a non-constructive existence proof (e.g., proof by contradiction without producing a witness).
  **Correction**: In the intuitionistic/type-theoretic setting, a proof of (exists x in A)B(x) must exhibit an actual pair (a, b).

# Common Confusions

- **Confusion**: Thinking existential quantification and conjunction are the same.
  **Clarification**: Conjunction A & B (represented by A x B) is the non-dependent special case where B does not depend on x. The full existential (exists x in A)B(x) allows B(x) to vary with x.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.4: Disjoint union of a family of types.

# Verification Notes

Confidence: high. The correspondence is explicitly stated in Section 1.4 with a direct quotation.
