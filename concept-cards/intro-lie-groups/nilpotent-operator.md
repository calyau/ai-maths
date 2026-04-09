---
# === CORE IDENTIFICATION ===
concept: Nilpotent Operator
slug: nilpotent-operator

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - jordan-decomposition
  - semisimple-operator
  - generalized-eigenspace
contrasts_with:
  - semisimple-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a nilpotent operator?"
---

# Quick Definition
An operator $A: V \to V$ is nilpotent if $A^n = 0$ for some positive integer $n$. Equivalently, the only eigenvalue of $A$ is zero.

# Core Definition
(Kirillov, p. 120): An operator $A: V \to V$ is called *nilpotent* if $A^n = 0$ for sufficiently large $n$.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. All eigenvalues are zero
2. Sum of two commuting nilpotent operators is nilpotent (Lemma B.1(1))
3. In a suitable basis, $A$ is strictly upper-triangular
4. $\mathrm{ad}\, A$ is nilpotent when $A$ is strictly upper-triangular in some basis (Exercise B.1)
5. The minimal $n$ with $A^n = 0$ satisfies $n \leq \dim V$

# Context & Application
Nilpotent operators form one component of the Jordan decomposition. In Lie theory, nilpotent elements play a central role: the nil-positive and nil-negative subalgebras consist of elements that act nilpotently.

# Examples
**Example** (p. 120): A strictly upper-triangular matrix is nilpotent.

# Relationships
## Enables
- **Jordan decomposition** -- the nilpotent part $A_n$
- **Generalized eigenspace** -- defined via nilpotence of $A - \lambda I$

## Contrasts With
- **Semisimple operator** -- diagonalizable; nilpotent has only zero eigenvalues

# Source Reference
Appendix B: Jordan Decomposition, p. 120.

# Verification Notes
- Definition source: Direct from p. 120
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
