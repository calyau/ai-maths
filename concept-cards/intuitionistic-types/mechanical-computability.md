---
# === CORE IDENTIFICATION ===
concept: Mechanical Computability of Type-Theoretic Functions
slug: mechanical-computability

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
section: "4.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Corollary 4.5"
  - "computability of number theoretic functions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normalization-theorem
  - normal-term-structure
  - natural-numbers
extends:
  - normalization-theorem
related:
  - decidability-of-definitional-equality
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Every number theoretic function expressible in the theory of types is mechanically computable: given a numeral m, the application f(m) normalizes to a numeral n, and normalization is a purely mechanical process.

# Core Definition

Martin-Lof states: "A number theoretic function which can be constructed in the theory of types is mechanically computable." (Section 4.5)

The argument: A number theoretic function is represented by a closed term f of type N -> N (without object constants). Given a numeral m, the term f(m) is a closed term of type N. By the canonical forms result (Section 4.4), f(m) reduces to a numeral n = s(s(...s(0)...)). Martin-Lof concludes: "It only remains to remark that the normal form of a term can be found in a purely mechanical way, that is, by manipulating symbol strings according to rules which refer solely to their syntactical structure and not to their meaning."

Martin-Lof notes that "the fact that there is a not necessarily mechanical procedure for computing every function in the present theory of types does not require any proof at all for us, intelligent beings, who can understand the meaning of the types and the terms." The non-trivial content is that the computation can be done mechanically (by a machine).

# Prerequisites

- **normalization-theorem**: Guarantees that f(m) has a normal form.
- **normal-term-structure**: Guarantees that the normal form of a closed term of type N is a numeral.
- **natural-numbers**: The type N and its numerals.

# Key Properties

1. The result applies to any closed term f of type N -> N without object constants.
2. The computation is purely syntactic -- no understanding of meaning is required.
3. The result extends to real numbers: "having formalized the construction of the real numbers (for example, as Cauchy sequences of rationals) in the theory of types, we can prove as a corollary to the normalization theorem that every individual real number which we construct in the formal theory can be computed by a machine with an arbitrary degree of approximation."
4. Martin-Lof sees this as showing that "formalization taken together with the ensuing proof theoretical analysis effectuates the computerization of abstract intuitionistic mathematics that above all Bishop 1967 and 1970 has asked for."

# Construction / Recognition

## To Mechanically Compute f(m):
1. Represent the function as a closed term f of type N -> N.
2. Apply f to the numeral m, forming the term f(m).
3. Normalize f(m) by repeatedly contracting redexes.
4. The result is a numeral n = s(s(...s(0)...)), which is the value f(m).

## Why This Is Non-Trivial:
- The theory of types can express functions defined by higher-order recursion, dependent types, etc.
- It is not obvious a priori that such functions are mechanically computable.
- The normalization theorem provides the missing piece: the normalization process is itself mechanical.

# Context & Application

This corollary connects the theory of types to computability theory and constructive mathematics. It shows that Bishop's program of "computerizing" intuitionistic mathematics is achievable in principle through formalization in type theory combined with normalization.

Martin-Lof adds a caveat: "What is doubtful at present is not whether computerization is possible in principle, because we already know that, but rather whether these proof theoretical computation procedures are at all useful in practice. So far, they do not seem to have found a single significant application."

# Examples

- The identity function (lambda x)x of type N -> N: applying it to s(s(0)) yields ((lambda x)x)(s(s(0))), which contracts to s(s(0)). The result is the numeral 2.
- The successor function (lambda x)s(x): applying it to s(0) yields s(s(0)).
- A more complex function defined by primitive recursion R(m, d, (lambda x)(lambda y)e[x,y]) normalizes to a numeral by repeatedly unfolding the recursion.

# Relationships

## Builds Upon
- normalization-theorem: Guarantees termination of the computation.
- normal-term-structure: Guarantees the result is a numeral.

## Related
- decidability-of-definitional-equality: Another algorithmic consequence of normalization.

# Common Errors

- **Error**: Thinking this result means all functions in the theory are primitive recursive.
  **Correction**: The theory of types can express functions far beyond the primitive recursive ones (it has dependent types, the universe, etc.). The point is that whatever functions are expressible, they are all mechanically computable via normalization.

# Common Confusions

- **Confusion**: Thinking mechanical computability was already obvious.
  **Clarification**: For an "intelligent being" who understands the meaning, computability is clear. The non-trivial fact is that the computation can be carried out by purely syntactic manipulation -- by a machine with no understanding of meaning.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.5: Corollary.

# Verification Notes

Confidence: high. Explicitly stated as Corollary 4.5 with a clear argument.
