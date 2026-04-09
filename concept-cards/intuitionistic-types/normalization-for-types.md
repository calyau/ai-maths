---
# === CORE IDENTIFICATION ===
concept: Normalization for Types
slug: normalization-for-types

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
section: "4.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "type normalization"
  - "Corollary 4.2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normalization-theorem
  - type
extends:
  - normalization-theorem
related:
  - decidability-of-definitional-equality
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Every type in the theory reduces to a normal type. This is a direct corollary of the normalization theorem.

# Core Definition

Martin-Lof states: "Every type reduces to a normal type." (Section 4.2)

The proof: "Every type is built up by means of the operations Pi, Sigma, and + from V, small types and atomic types of the form P(a_1,...,a_n). A small type, being a term of type V, is normalizable according to the normalization theorem, and so is a type of the form P(a_1,...,a_n) since a_1,...,a_n are all terms. Hence every type is normalizable."

# Prerequisites

- **normalization-theorem**: The main result from which this corollary follows.
- **type**: The objects being normalized.

# Key Properties

1. Types are built from: V (universe), small types (terms of type V), and atomic types P(a_1,...,a_n).
2. Small types normalize because they are terms of type V.
3. Atomic types P(a_1,...,a_n) normalize because their arguments a_1,...,a_n are terms.
4. Compound types (Pi, Sigma, +) normalize because their components normalize.

# Construction / Recognition

## To Normalize a Type:
1. Normalize all term-level subexpressions within the type (using the normalization theorem for terms).
2. The result is a normal type.

# Context & Application

Type normalization is a necessary prerequisite for the decidability of definitional equality (Section 4.3). To decide whether two types are definitionally equal, we normalize both and check syntactic identity.

# Examples

- The type (Pi x in N)(N -> N) is already in normal form (no redexes in its components).
- If f is a closed term of type V -> V, then f(N) is a type that may not be normal. The normalization theorem guarantees f(N) reduces to a normal type.
- The type (Sigma x in ((lambda y)N)(0)) N contains a redex in its first component. Normalizing yields (Sigma x in N) N.

# Relationships

## Builds Upon
- normalization-theorem: The corollary is a direct consequence.

## Enables
- decidability-of-definitional-equality: Requires normalizing types before comparing.

# Common Errors

- **Error**: Thinking type normalization requires a separate proof.
  **Correction**: It follows directly from term normalization, since types are either built from terms (small types, atomic types) or composed from normalizable parts (Pi, Sigma, +).

# Common Confusions

- **Confusion**: Conflating "normal type" with "canonical type."
  **Clarification**: A normal type is one containing no redexes in any of its subexpressions. A canonical type (in the sense of Section 4.4) is a closed normal type of type V that has introduction form.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.2: Corollary.

# Verification Notes

Confidence: high. Explicitly stated as Corollary 4.2 with a brief complete proof.
