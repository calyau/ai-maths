---
# === CORE IDENTIFICATION ===
concept: Semisimple Operator
slug: semisimple-operator

# === CLASSIFICATION ===
category: lie-algebras
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix B - Jordan Decomposition"
chapter_number: null
pdf_page: 120
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "diagonalizable operator"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - jordan-decomposition
  - nilpotent-operator
contrasts_with:
  - nilpotent-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a semisimple operator?"
  - "What is the relationship between semisimple and diagonalizable?"
---

# Quick Definition
An operator $A: V \to V$ on a finite-dimensional complex vector space is semisimple if every $A$-invariant subspace has an $A$-invariant complement. Over $\mathbb{C}$, this is equivalent to being diagonalizable.

# Core Definition
(Kirillov, p. 120): An operator $A: V \to V$ is called *semisimple* if any $A$-invariant subspace has an $A$-invariant complement: if $W \subset V$, $AW \subset W$, then there exists $W' \subset V$ such that $V = W \oplus W'$, $AW' \subset W'$. For operators on a finite-dimensional complex vector space, this is equivalent to requiring that $A$ be diagonalizable.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Equivalent to diagonalizable over $\mathbb{C}$ (p. 120)
2. Sum of two commuting semisimple operators is semisimple (Lemma B.1(1))
3. Restriction of a semisimple operator to an invariant subspace is semisimple (Lemma B.1(2))
4. The quotient action on $V/W$ is also semisimple (Lemma B.1(2))
5. $A$ is semisimple iff there exists a polynomial $p$ without multiple roots such that $p(A) = 0$

# Construction / Recognition
## To check if $A$ is semisimple
1. Compute the minimal polynomial of $A$
2. $A$ is semisimple iff the minimal polynomial has no repeated roots
3. Equivalently, $A$ is diagonalizable: check if there is a basis of eigenvectors

# Context & Application
The notion of semisimple operator is foundational for Jordan decomposition and hence for the structure theory of Lie algebras. In Section 6.6, the Jordan decomposition is used to analyze the adjoint representation, leading to the Cartan subalgebra and root decomposition.

# Examples
**Example** (p. 120): A diagonal matrix is semisimple. A matrix with distinct eigenvalues is semisimple.

# Relationships
## Enables
- **Jordan decomposition** -- decomposes any operator into semisimple + nilpotent parts

## Contrasts With
- **Nilpotent operator** -- nilpotent operators have all eigenvalues zero; semisimple operators are diagonalizable

# Common Confusions
- **Confusion**: Thinking "semisimple operator" means the same as "semisimple Lie algebra element"
  **Clarification**: For a semisimple Lie algebra, an element is called semisimple if its adjoint action is a semisimple operator; the two notions are related but at different levels

# Source Reference
Appendix B: Jordan Decomposition, p. 120.

# Verification Notes
- Definition source: Direct from p. 120
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
