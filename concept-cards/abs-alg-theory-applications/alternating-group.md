---
# === CORE IDENTIFICATION ===
concept: Alternating Group
slug: alternating-group

# === CLASSIFICATION ===
category: permutation-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Permutation Groups"
chapter_number: 5
pdf_page: 77
section: "The Alternating Groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$A_n$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetric-group
  - even-permutation
extends: []
related:
  - permutation-group
  - lagranges-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the alternating group?"
  - "How many elements does $A_n$ have?"
---

# Quick Definition

The alternating group $A_n$ is the subgroup of $S_n$ consisting of all even permutations. It has order $n!/2$ for $n \geq 2$.

# Core Definition

"One of the most important subgroups of $S_n$ is the set of all even permutations, $A_n$. The group $A_n$ is called the *alternating group on $n$ letters*" (Judson, p. 77). It is proved to be a subgroup in Theorem 5.16.

# Prerequisites

- **Symmetric Group** — $A_n$ is a subgroup of $S_n$
- **Even Permutation** — Elements of $A_n$ are exactly the even permutations

# Key Properties

1. $|A_n| = n!/2$ for $n \geq 2$ (Proposition 5.17)
2. $A_n$ is a subgroup of $S_n$ (Theorem 5.16)
3. $A_n$ is nonabelian for $n \geq 4$
4. $A_n$ has index 2 in $S_n$
5. $A_4$ has no subgroup of order 6 (the converse of Lagrange's theorem fails)

# Construction / Recognition

## To Construct $A_n$:
1. List all permutations in $S_n$
2. For each, decompose into transpositions
3. Keep only those requiring an even number of transpositions

## To Recognize:
1. Verify the group is a subgroup of $S_n$
2. Verify it contains exactly the even permutations

# Context & Application

The alternating groups are among the most important examples in group theory. $A_5$ is the smallest non-abelian simple group, and this fact is central to proving the unsolvability of the quintic by radicals.

# Examples

**Example 1** (p. 78): $A_4$ has 12 elements: $(1)$, $(12)(34)$, $(13)(24)$, $(14)(23)$, $(123)$, $(132)$, $(124)$, $(142)$, $(134)$, $(143)$, $(234)$, $(243)$.

# Relationships

## Builds Upon
- **Symmetric Group** — $A_n \leq S_n$
- **Even Permutation** — $A_n$ consists of even permutations

## Enables
- **Lagrange's Theorem** — $A_4$ provides a counterexample to the converse

## Related
- **Permutation Group** — $A_n$ is a specific permutation group

# Common Errors

- **Error**: Assuming $A_n$ contains elements of every order dividing $|A_n|$
  **Correction**: $A_4$ has order 12 but no subgroup of order 6

# Common Confusions

- **Confusion**: Thinking $A_n$ is always abelian because of the name "alternating"
  **Clarification**: $A_n$ is nonabelian for $n \geq 4$

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, "The Alternating Groups," Theorem 5.16, Proposition 5.17, pages 77-78.

# Verification Notes

- Definition source: Direct from p. 77
- Confidence rationale: Explicit definition and theorems
- Uncertainties: None
- Cross-reference status: Verified
